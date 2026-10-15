"""Narra un guion de tres papeles (ANCLA, PREGUNTA, TESTIGO) con las voces elegidas en VOCES.md.

Formato del guion (REGLA-NODO-GUION.md): «ROL: texto»; un párrafo sin rol sigue siendo del último que habló;
[cues] suenan el .wav que nombran (de musica.py); comentarios <!-- --> y títulos no se narran; «---» separa
secciones (pausa larga). Cada clase empieza con el aviso de IA y la música de entrada.

Cada parlamento se pide una sola vez a ElevenLabs: el MP3 queda en _cache/<hash>.mp3 y se reutiliza mientras no
cambien voz, modelo, ajustes ni texto (remezclar no gasta). Luego ffmpeg los une con silencios, nivela el volumen de
cada parlamento y escribe _audio/<nodo>.mp3 a 192 kbps.

    python musica.py                                        # una vez: los sonidos, en local
    python narrar.py guiones/presupuesto-guion.md --seco    # cuenta caracteres y lo ya cacheado, no gasta
    python narrar.py guiones/presupuesto-guion.md           # gasta créditos solo por lo no cacheado

Necesita ffmpeg en el PATH y la variable de entorno ELEVENLABS_API_KEY (nunca en el repo).
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CACHE = AQUI / "_cache"
SALIDA = AQUI / "_audio"
SONIDOS = SALIDA / "sonidos"  # de musica.py; un cue [MÚSICA: cortina] o [SONIDO evidencia] suena el .wav que nombra
API = "https://api.elevenlabs.io/v1"
MODELO = "eleven_v4"
FORMATO = "mp3_44100_192"
AJUSTES = {"stability": 0.55, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 0.92}
VOCES = {  # VOCES.md, sección Elegidas (Diego, 13-oct)
    "ANCLA": "ECOET12tGKHdXyB0CfqU",  # David
    "PREGUNTA": "scn1gPWkdVd8FhODJoei",  # María
    "TESTIGO": "SmgKjOvC1aIujLWcMzqq",  # Alisson
}
VOLUMEN = -22.0  # dB de volumen medio por parlamento
PAUSA = {"parrafo": 0.35, "turno": 0.55, "seccion": 1.4, "sonido": 0.5}  # segundos de silencio antes de cada pieza
MUSICA_DB = -3.0  # la música, un poco por debajo de las voces
AVISO = (
    "ANCLA",
    "Las voces de esta clase fueron creadas con inteligencia artificial. "
    "El guion se escribió con ayuda de inteligencia artificial y lo revisó una persona.",
)  # política de uso de ElevenLabs §10; la segunda frase solo vale si hubo revisión humana

Parte = tuple[str, str, float]  # (rol, texto, pausa previa); el rol "SONIDO" lleva en texto el nombre del .wav


def leer_guion(ruta: str) -> list[Parte]:
    """Parlamentos del guion, precedidos por el aviso de IA y la entrada musical."""
    texto = re.sub(r"<!--.*?-->", "", Path(ruta).read_text(encoding="utf-8"), flags=re.S)
    partes: list[Parte] = [(*AVISO, 0.0), ("SONIDO", "entrada", 0.6)]
    rol, pausa = None, "sonido"
    for parrafo in re.split(r"\n\s*\n", texto):
        p = " ".join(parrafo.split())
        if not p or p.startswith("#"):
            continue
        if p == "---":
            pausa = pausa or "seccion"
            continue
        if p.startswith("[") and p.endswith("]"):
            nombre = next((f.stem for f in SONIDOS.glob("*.wav") if f.stem in p.lower()), None)
            if nombre is None:
                raise SystemExit(f"Cue sin sonido en {SONIDOS}: {p} (¿corrió musica.py?)")
            partes.append(("SONIDO", nombre, PAUSA["sonido"] if pausa == "sonido" else 0.8))
            rol, pausa = None, "sonido"
            continue
        m = re.match(r"^([A-ZÁÉÍÓÚÑ]+):\s*(.+)$", p)
        if m and m.group(1) in VOCES:
            nuevo, p = m.group(1), m.group(2)
        elif m:
            raise SystemExit(f"Rol desconocido: {m.group(1)}")
        else:
            nuevo = rol
        if nuevo is None:
            raise SystemExit(f"Párrafo sin rol al inicio: {p[:60]}")
        if pausa is None:
            pausa = "parrafo" if nuevo == rol else "turno"
        partes.append((nuevo, p, PAUSA[pausa]))
        rol, pausa = nuevo, None
    return partes


def clave(rol: str, texto: str) -> str:
    datos = json.dumps([VOCES[rol], MODELO, FORMATO, AJUSTES, texto], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(datos.encode()).hexdigest()[:16]


def pedir_voz(voz: str, texto: str, api_key: str) -> bytes:
    body = json.dumps({"text": texto, "model_id": MODELO, "voice_settings": AJUSTES}).encode()
    req = urllib.request.Request(f"{API}/text-to-speech/{voz}?output_format={FORMATO}", data=body, method="POST",
                                 headers={"xi-api-key": api_key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs {e.code}: {e.read().decode(errors='replace')[:300]}") from e


def sintetizar(rol: str, texto: str, api_key: str) -> Path:
    if rol == "SONIDO":
        return SONIDOS / f"{texto}.wav"
    ruta = CACHE / f"{clave(rol, texto)}.mp3"
    if not ruta.exists():
        ruta.write_bytes(pedir_voz(VOCES[rol], texto, api_key))
    return ruta


def volumen_medio(ruta: Path) -> float:
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(ruta), "-af", "volumedetect", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return float(re.search(r"mean_volume: (-?[\d.]+) dB", out).group(1))


def unir(rutas_y_pausas: list[tuple[Path, float]], salida: Path) -> None:
    """Une los MP3 con silencios entre ellos, cada parlamento llevado al mismo volumen medio
    (las voces no salen parejas: Alisson ~4 dB por encima, medido 13-oct), en una sola codificación a 192 kbps."""
    entradas, filtros, etiquetas = [], [], []
    for i, (ruta, pausa) in enumerate(rutas_y_pausas):
        entradas += ["-i", str(ruta)]
        ganancia = MUSICA_DB if ruta.suffix == ".wav" else VOLUMEN - volumen_medio(ruta)
        filtros.append(f"[{i}:a]aresample=44100,aformat=channel_layouts=mono,volume={ganancia:.1f}dB,"
                       f"adelay={int(pausa * 1000)}[a{i}]")
        etiquetas.append(f"[a{i}]")
    filtros.append(f"{''.join(etiquetas)}concat=n={len(etiquetas)}:v=0:a=1,"
                   "alimiter=limit=0.89:level=false,apad=pad_dur=1.5[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros),
                    "-map", "[out]", "-b:a", "192k", str(salida)], check=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("guion")
    ap.add_argument("--seco", action="store_true", help="no pide nada a ElevenLabs")
    args = ap.parse_args()
    partes = leer_guion(args.guion)
    CACHE.mkdir(parents=True, exist_ok=True)
    voces = [(r, t) for r, t, _ in partes if r != "SONIDO"]
    nuevos = [(r, t) for r, t in voces if not (CACHE / f"{clave(r, t)}.mp3").exists()]
    for rol in VOCES:
        print(f"{rol}: {sum(1 for r, _ in voces if r == rol)} parlamentos")
    print(f"{len(partes)} piezas, {sum(len(t) for _, t in voces)} car.; "
          f"por pedir: {len(nuevos)} ({sum(len(t) for _, t in nuevos)} car.)")
    if args.seco:
        for rol, texto, pausa in partes:
            print(f"  {pausa:4.2f}s {rol:8} {texto[:70]}")
        return 0
    api_key = os.environ.get("ELEVENLABS_API_KEY", "")
    if nuevos and not api_key:
        raise SystemExit("Falta ELEVENLABS_API_KEY en el entorno.")
    rutas = []
    for i, (rol, texto, pausa) in enumerate(partes, 1):
        rutas.append((sintetizar(rol, texto, api_key), pausa))
        print(f"  {i}/{len(partes)} {rol}")
    SALIDA.mkdir(exist_ok=True)
    salida = SALIDA / (Path(args.guion).stem.replace("-guion", "") + ".mp3")
    unir(rutas, salida)
    print(f"Listo: {salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
