"""Sonidos de las clases, sintetizados en local (no gasta créditos): marimba suave en do mayor, sin samples ni licencias.

    python musica.py   # escribe _audio/sonidos/{entrada,cortina,evidencia,cierre}.wav

entrada: el motivo, corto, tras el aviso de IA · cortina: el motivo entre secciones · evidencia: dos campanas antes
del testigo · cierre: el motivo completo que resuelve en un acorde.
"""
import wave
from pathlib import Path

import numpy as np

SR = 44100
SALIDA = Path(__file__).resolve().parent / "_audio" / "sonidos"
NOTAS = {"C4": 261.63, "E4": 329.63, "G4": 392.00, "A4": 440.00, "C5": 523.25, "D5": 587.33, "E5": 659.25,
         "G5": 783.99, "A5": 880.00, "C6": 1046.50, "D6": 1174.66, "C3": 130.81, "G3": 196.00, "F3": 174.61}


def marimba(f, dur=1.2, vel=1.0):
    t = np.arange(int(SR * dur)) / SR
    # parciales de una barra de marimba (1 : 3,9 : 9,2), los agudos mueren rápido
    s = (np.sin(2 * np.pi * f * t) * np.exp(-t * 3.0)
         + 0.25 * np.sin(2 * np.pi * f * 3.9 * t) * np.exp(-t * 12)
         + 0.08 * np.sin(2 * np.pi * f * 9.2 * t) * np.exp(-t * 30))
    ataque = np.minimum(1, t / 0.004)
    return vel * s * ataque


def campana(f, dur=2.0, vel=1.0):
    t = np.arange(int(SR * dur)) / SR
    s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * d)
            for r, a, d in [(1, 1, 1.6), (2.76, 0.35, 3), (5.4, 0.15, 6), (8.93, 0.06, 9)])
    return vel * s * np.minimum(1, t / 0.002)


def pista(eventos, dur):
    """eventos: (segundo, señal)."""
    out = np.zeros(int(SR * dur))
    for seg, s in eventos:
        i = int(seg * SR)
        n = min(len(s), len(out) - i)
        out[i:i + n] += s[:n]
    return out


def sala(x, mezcla=0.18):
    """Reverberación sencilla: cuatro ecos en peine, sin metales."""
    y = x.copy()
    for ms, g in [(37, 0.5), (53, 0.45), (71, 0.4), (97, 0.35)]:
        d = int(SR * ms / 1000)
        eco = np.zeros_like(x)
        for k in range(1, 8):
            if k * d >= len(x):
                break
            eco[k * d:] += x[:len(x) - k * d] * g ** k
        y += mezcla * eco / 4
    return y


def motivo(t0=0.0, paso=0.25):
    """C5 E5 G5 A5 G5 ... E5 D5 C5: alegre y curioso, en corcheas a 120 bpm."""
    frase = [("C5", 0), ("E5", 1), ("G5", 2), ("A5", 3), ("G5", 4), ("E5", 6), ("D5", 7), ("C5", 8)]
    ev = [(t0 + i * paso, marimba(NOTAS[n], vel=0.9 if i in (0, 8) else 0.7)) for n, i in frase]
    ev += [(t0, marimba(NOTAS["C3"], 2.0, 0.5)), (t0 + 4 * paso, marimba(NOTAS["F3"], 2.0, 0.4)),
           (t0 + 8 * paso, marimba(NOTAS["C3"], 2.5, 0.5))]
    return ev


def normalizar(x, pico_db=-6.0):
    x = x * np.minimum(1, np.arange(len(x)) / (SR * 0.01))      # sin clic al entrar
    cola = int(SR * 0.4)
    x[-cola:] *= np.linspace(1, 0, cola)                          # ni al salir
    return x / np.max(np.abs(x)) * 10 ** (pico_db / 20)


def guardar(nombre, x):
    SALIDA.mkdir(parents=True, exist_ok=True)
    datos = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(SALIDA / f"{nombre}.wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(datos.tobytes())
    print(f"{nombre}.wav: {len(x) / SR:.1f} s")


def main() -> None:
    guardar("entrada", normalizar(sala(pista(motivo(), 4.0))))
    guardar("cortina", normalizar(sala(pista(motivo(paso=0.22), 3.6)), -8))
    guardar("evidencia", normalizar(sala(pista([(0, campana(NOTAS["G5"])), (0.18, campana(NOTAS["D6"], vel=0.8))], 2.2)), -10))
    acorde = [(2.25 + k * 0.06, marimba(NOTAS[n], 3.5, 0.55)) for k, n in enumerate(["C4", "E4", "G4", "C5", "E5"])]
    guardar("cierre", normalizar(sala(pista(motivo() + [(2.25, marimba(NOTAS["C6"], 3.5, 0.5))] + acorde, 6.0))))


if __name__ == "__main__":
    main()
