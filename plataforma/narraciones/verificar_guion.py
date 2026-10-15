"""Chequeo automático de un guion contra su nodo (REGLA-NODO-GUION.md, sección 7). No gasta créditos.

    python plataforma/narraciones/verificar_guion.py plataforma/narraciones/guiones/presupuesto-guion.md curriculo/dinero/nucleo/presupuesto.md

Sale con código 1 si algo falla.
"""
import re
import sys
from pathlib import Path

PAPELES = {"ANCLA", "PREGUNTA", "TESTIGO"}
RANGO = (3000, 4500)
VAL = {w: i for i, w in enumerate(
    "cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince dieciséis "
    "diecisiete dieciocho diecinueve veinte veintiuno veintidós veintitrés veinticuatro veinticinco "
    "veintiséis veintisiete veintiocho veintinueve".split())}
VAL.update(dict(un=1, una=1, dieciseis=16, veintidos=22, veintitres=23, veintiseis=26, treinta=30,
                cuarenta=40, cincuenta=50, sesenta=60, setenta=70, ochenta=80, noventa=90, cien=100,
                ciento=100, doscientos=200, trescientos=300, cuatrocientos=400, quinientos=500,
                seiscientos=600, setecientos=700, ochocientos=800, novecientos=900))
for w in list(VAL):
    if w.endswith("ientos"):
        VAL[w[:-2] + "as"] = VAL[w]


def numeros(texto: str) -> set[int]:
    """Todos los números de un texto, escritos en dígitos o en palabras."""
    salida, total, actual, en_num = set(), 0, 0, False
    toks = re.findall(r"\d[\d.]*|[a-záéíóúñ]+|\S", texto.lower())
    for i, t in enumerate(toks):
        if t[0].isdigit():
            salida.add(int(t.strip(".").replace(".", "")))
            continue
        if t in ("ciento", "cien") and i and toks[i - 1] == "por":  # «por ciento» no es un número
            continue
        if t in VAL:
            actual += VAL[t]; en_num = True
        elif t == "mil":
            total += (actual or 1) * 1000; actual = 0; en_num = True
        elif t in ("millón", "millones"):
            total = (total + (actual or 1)) * 10**6; actual = 0; en_num = True
        elif t == "y" and en_num and i + 1 < len(toks) and toks[i + 1] in VAL and actual % 10 == 0 and actual >= 30:
            continue
        else:
            if en_num:
                salida.add(total + actual)
            total, actual, en_num = 0, 0, False
    if en_num:
        salida.add(total + actual)
    return salida


def curioso(nodo: str) -> str:
    """Cuerpo del nodo sin frontmatter y hasta antes del puente académico."""
    cuerpo = nodo.split("\n---\n", 1)[1] if nodo.startswith("---") else nodo
    cuerpo = re.sub(r"\(≈ \d+ s\)", "", cuerpo)  # los tiempos de los títulos no son datos
    return re.split(r"^## Puente académico", cuerpo, flags=re.M)[0]


def nombres(texto: str) -> set[str]:
    """Palabras con mayúscula que no abren frase."""
    salida = set()
    for m in re.finditer(r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+", texto):
        antes = texto[:m.start()].rstrip(" ¿¡«" + chr(34))
        if antes and not antes.endswith((".", "?", "!", ":", "…", chr(10))):
            salida.add(m.group())
    return salida


def main(ruta_guion: str, ruta_nodo: str) -> int:
    guion = Path(ruta_guion).read_text(encoding="utf-8")
    nodo = curioso(Path(ruta_nodo).read_text(encoding="utf-8"))
    sin_coment = re.sub(r"<!--.*?-->", "", guion, flags=re.S)
    fallas, rol, seccion, narrado = [], None, 0, []
    for linea in sin_coment.splitlines():
        s = linea.strip()
        if s == "---":
            seccion += 1; continue
        if not s or s.startswith(("#", "[")):
            continue
        m = re.match(r"([A-ZÁÉÍÓÚÑ]+):\s*(.*)", s)
        if m:
            rol, s = m.group(1), m.group(2)
            if rol not in PAPELES:
                fallas.append(f"papel desconocido: {rol}")
        if rol == "TESTIGO" and seccion != 2:
            fallas.append(f"TESTIGO fuera de la evidencia (sección {seccion + 1}): {s[:50]}")
        narrado.append(s)
    texto = "\n".join(narrado)
    en_nodo = numeros(nodo)
    for n in sorted(numeros(texto) - en_nodo):
        if n > 1:
            fallas.append(f"número que no está en el nodo: {n}")
    for w in sorted(nombres(texto)):
        if w not in nodo:
            fallas.append(f"nombre propio que no está en el nodo: {w}")
    car = len(texto)
    if not RANGO[0] <= car <= RANGO[1]:
        fallas.append(f"{car} caracteres narrados, fuera de {RANGO}")
    print(f"{ruta_guion}: {car} caracteres narrados, {seccion + 1} secciones")
    for f in fallas:
        print("  FALLA", f)
    print("  OK" if not fallas else f"  {len(fallas)} fallas")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
