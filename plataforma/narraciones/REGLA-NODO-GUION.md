# Regla: de nodo a guion para el oído

Versión 1 (2026-10-13). Sale de cómo se escribió el guion de Presupuesto (aprobado por Diego) y se
probó con Necesidad o deseo: el guion salió a la primera, pasó el chequeo y Diego aprobó el audio. Si una corrección humana se repite, se vuelve regla aquí.

## 1. Fuente única

- La fuente es **un** nodo del currículo, en un commit dado. El encabezado del guion cita ruta,
  commit, estado y responsable del nodo.
- No se agrega ningún dato: toda cifra, nombre, fecha, estudio o afirmación sale del nodo.
- Sí se puede agregar lo que no afirma nada: conectores («Te presento a…», «Llamo a un testigo»),
  reacciones de PREGUNTA («Suena duro», «¿Dos días nada más?») y preguntas retóricas.
- Si el nodo no nombra a los autores de un estudio, el guion tampoco.

## 2. Qué entra

- Entran las cinco secciones Curioso, en su orden: **gancho, idea, evidencia, ¿y a mí qué?,
  puerta abierta**.
- Quedan fuera (son para leer): puente académico, ejercicios, caso práctico, errores comunes,
  nota al docente, soluciones.
- Se conserva el **tono** que el comentario del nodo declare (p. ej. «desear no es malo»).

## 3. Los tres papeles

| Papel | Hace | No hace |
| --- | --- | --- |
| ANCLA | Lleva el hilo, define, presenta personajes y casos, cierra cada sección. | Leer la evidencia de estudios. |
| PREGUNTA | Dice las dudas reales del estudiante, incluidas las **equivocadas** que el nodo corrige (registro ≠ presupuesto; «desear está mal»). Calcula en voz alta antes que el ANCLA cuando la cuenta es fácil. | Afirmar datos nuevos o dar la respuesta del nodo. |
| TESTIGO | Lee la sección de evidencia: estudios, fechas, lo comprobado y lo que no es tan seguro. Habla en tercera persona. | Poner frases en boca de investigadores; aparecer fuera de la evidencia. |

- Cada sección tiene al menos una intervención de PREGUNTA; ningún parlamento del ANCLA pasa de
  unas seis frases sin interrupción.
- La distinción del nodo entre «está comprobado» y «se dice, pero no es tan seguro» se conserva
  palabra por palabra en sentido.

## 4. Escrito para el oído

- Cifras, años y porcentajes en palabras («dos mil diecisiete», «cincuenta por ciento»).
- Frases que se dicen en una respiración; puntos suspensivos para la pausa antes del remate.
- Se abre con una prueba o pregunta directa al oyente, en segunda persona («tú»).
- Las listas del nodo se reparten en turnos: PREGUNTA pide el siguiente punto.
- Cada sección cierra con una frase corta repetible tomada del nodo («gota a gota»; «con plan y
  sin culpa»).
- La puerta abierta deja la pregunta para conversar y nombra la próxima clase con la frase del nodo.

## 5. Formato para el motor (narrar.py)

- `ROL: texto`; un párrafo sin rol sigue siendo del último que habló.
- `---` entre secciones (pausa larga).
- Cues: `[MÚSICA: cortina]` tras el gancho, `[SONIDO evidencia]` antes de la primera intervención
  del TESTIGO, `[MÚSICA: cierre]` al final. La entrada y el aviso de IA los pone el motor.
- Tras cada sección, un comentario `<!-- … -->` que lista sus cifras y fuentes en dígitos, para la
  revisión humana. Los comentarios no se narran.

## 6. Duración y costo

- Meta: 4 a 5 minutos; entre 3.000 y 4.500 caracteres narrados (`narrar.py --seco` los cuenta sin
  gastar). Con eleven_v4, unos 0,44 créditos por carácter: ~2.000 por clase.

## 7. Control

1. `python plataforma/narraciones/verificar_guion.py <guion> <nodo>` (automático, no gasta):
   - todo número dicho en el guion (en palabras o dígitos, mayor que uno) aparece en las secciones
     Curioso del nodo;
   - todo nombre propio a mitad de frase aparece en el nodo (parcial: no ve los que abren frase);
   - solo hay papeles ANCLA, PREGUNTA, TESTIGO; el TESTIGO solo en la sección de evidencia;
   - caracteres narrados dentro del rango.
2. Revisión humana entera del guion, leído en voz alta o escuchado en seco, antes de gastar
   créditos. El encabezado dice «falta revisión humana» hasta que alguien lo apruebe con nombre y fecha.
3. Escucha del MP3 terminado (audífono y parlante de celular).
