# Motor de narraciones

Convierte un nodo del currículo en una **clase de audio** de unos cinco minutos. Tres voces se reparten la clase: el **ancla** lleva el hilo, **la que pregunta** pone las dudas del estudiante y **la testigo** trae la evidencia. Lleva música y empieza con un aviso de IA. Es una propuesta: ver la [decisión 0005](../../docs/decisiones/0005-motor-de-narraciones.md).

**Estado:** prototipo que funciona de punta a punta, probado con dos nodos de Dinero: Presupuesto y ¿Necesidad o deseo?. Los audios **no se publican** hasta resolver la licencia (ver [`LICENCIA-AUDIO.md`](LICENCIA-AUDIO.md)).

## Cómo se hace una clase

```
nodo ──(regla, a mano con IA)──► guion ──verificar_guion.py──► revisión humana ──narrar.py──► MP3 ──► escucha
```

1. **Guion.** Se escribe con [`REGLA-NODO-GUION.md`](REGLA-NODO-GUION.md), con la IA de cada quien. Una clase sale de un nodo y no agrega datos. Va en `guiones/<nodo>-guion.md`.
2. **Chequeo automático.** No gasta nada.
   ```bash
   python plataforma/narraciones/verificar_guion.py plataforma/narraciones/guiones/necesidad-o-deseo-guion.md curriculo/dinero/nucleo/necesidad-o-deseo.md
   ```
   Falla si el guion trae un número o un nombre propio que no está en el nodo, un papel desconocido o la testigo fuera de la evidencia, o si se sale del largo.
3. **Revisión humana completa** del guion, antes de gastar créditos. Quien aprueba pone su nombre y la fecha en el encabezado del guion.
4. **Narración.** Hay que hacerlo desde esta carpeta.
   ```bash
   pip install numpy
   python musica.py                                   # una vez: sonidos sintetizados en local, sin licencias
   python narrar.py guiones/<nodo>-guion.md --seco    # cuenta caracteres, no gasta
   python narrar.py guiones/<nodo>-guion.md           # pide a ElevenLabs solo lo que no está en caché
   ```
   Necesita `ffmpeg` y la variable de entorno `ELEVENLABS_API_KEY`. Escribe `_audio/<nodo>.mp3` (192 kbps). Cada parlamento queda en `_cache/`: volver a mezclar no gasta créditos, y cambiar una frase solo cuesta esa frase. Ninguna de las dos carpetas se sube al repo.
5. **Escucha** con audífono y en el parlante de un celular. Si algo falla una y otra vez, la corrección pasa a ser regla.

## Archivos

| Archivo | Qué es |
| --- | --- |
| `REGLA-NODO-GUION.md` | Cómo un nodo se vuelve guion: fuente única, qué entra, qué hace cada papel, escritura para el oído, formato, duración, control. |
| `verificar_guion.py` | El chequeo automático de la regla. |
| `narrar.py` | Guion → voces (con caché) → volumen parejo → música → MP3. |
| `musica.py` | Marimba y campanas sintetizadas: entrada, cortina, evidencia, cierre. |
| `VOCES.md` | Quién es cada papel, cómo se eligieron las voces, cuáles son y con qué ajustes. |
| `LICENCIA-AUDIO.md` | Por qué todavía no se puede publicar el audio y las salidas posibles. |
| `guiones/` | Guiones aprobados: Presupuesto y ¿Necesidad o deseo?. |

## Costos medidos (13-oct-2026)

- Voz: ElevenLabs `eleven_v4` cuesta unos 0,44 créditos por carácter narrado. Una clase de 4.000 caracteres sale en **unos 1.500 a 2.000 créditos**. Lo de hoy se pagó con la cuenta de un voluntario.
- Música: gratis, sale de `musica.py`.
- Duración: Presupuesto, 5 min 16 s; ¿Necesidad o deseo?, 5 min 12 s.
