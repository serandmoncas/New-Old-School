# Biblia de voces · los Profesores de New Old School (v1, 2026-10-13)

Hay tres papeles, uno por función en la clase y no por materia. Las descripciones de abajo son las que se escribieron para Voice Design; las voces elegidas al final salieron de la Voice Library (ver «Elegidas»). Se buscaron voces cercanas, de 25 a 30 años, con acento colombiano neutro, que den ganas de preguntarles algo. El reparto lo aprobó Diego el 13-oct: un hombre de ancla y dos mujeres.

Voice Design sigue mejor las descripciones en inglés y, si no se le da un acento explícito, se va al castellano de España. En la primera tanda (13-oct) «latino neutro» no bastó: siete de nueve sonaron peninsulares. Desde la segunda: acento colombiano neutro de Bogotá, nombrado al principio y con el seseo explicado. Por eso el acento va escrito en cada descripción (lo aprendimos con TalkToMe, en `voice/cli.py`). No se nombra a ninguna persona real: la política de ElevenLabs prohíbe imitar voces reales, así que se describe el estilo.

---

## ANCLA · el profesor que guía (hombre, ~28)

**Quién es:** el que lleva la clase. Tiene la curiosidad alegre de un gran profesor de física: le asombran las ideas y el asombro se le contagia a quien escucha. Explica con cosas de la casa, ríe bajito cuando algo lo sorprende y habla con el estudiante de igual a igual, nunca desde arriba.

**Descripción para Voice Design:**

> Native Colombian Spanish speaker with a neutral, educated Colombian accent from Bogotá. Clear seseo: c and z always sound like s, never the Castilian th sound; absolutely no Spain accent. A Colombian man in his late twenties. Warm, mid-range voice with a little natural texture. A curious, playful teacher who is genuinely delighted by ideas: his enthusiasm is contagious, he chuckles softly when something surprises him, speeds up a little when excited and slows down to make a point land. He explains with everyday examples and talks with the listener as an equal, never lecturing or talking down. Friendly, approachable and conversational, close to the microphone. Studio-quality recording.

**Texto de prueba** (sale del guion de Presupuesto):

> Mira esto. Un paquete de galletas cuesta dos mil quinientos pesos. No parece nada, ¿verdad? Pero si lo compras veinte días al mes, son cincuenta mil pesos. Y en un año... seiscientos mil. ¡Eso es un celular! La plata rara vez se va de golpe. Se va gota a gota. Por eso existe el presupuesto: un plan para tu dinero, antes de gastarlo. Tú decides a dónde va cada peso.

---

## PREGUNTA · la que pregunta (mujer, ~25)

**Quién es:** la amiga lista o la hermana mayor que pregunta lo que el estudiante no se atreve a preguntar. Es espontánea, un poco escéptica («¿y eso a mí qué?») y nunca tonta. Reacciona de verdad: se sorprende, duda, se ríe. No se hace pasar por niña. Lo que modela es preguntar sin vergüenza.

**Descripción para Voice Design:**

> Native Colombian Spanish speaker with a neutral, educated Colombian accent from Bogotá. Clear seseo: c and z always sound like s, never the Castilian th sound; absolutely no Spain accent. A Colombian woman about twenty-five years old. Clear, bright, mid-to-high voice. Spontaneous, quick-witted and a little skeptical: she asks the questions a teenager would not dare to ask, with honest curiosity and light humor, never naive. Relaxed and natural, like a smart older sister, with genuine reactions: surprise, doubt, a small laugh. Friendly, expressive and conversational. Studio-quality recording.

**Texto de prueba** (las líneas del guion, con algún enlace entre ellas):

> ¿Cada peso? ... No. Ni la mitad. Espera, espera... ¿seiscientos mil? ¿En galletas? No puede ser. Bueno, pero entonces, ¿por qué no ahorro lo que me sobre al final del mes? ... Ya, ya sé lo que vas a decir. Otra pregunta: ella tiene plata todos los meses. ¿Y si la plata no llega cada mes? Creo que ya sé cuál es mi gasto hormiga.

---

## TESTIGO · la que trae el dato (mujer, ~30)

**Quién es:** la que trae la evidencia y la historia. Cuenta los hechos con calma y precisión, con un toque de narradora, como quien comparte algo notable. Es más pausada que el ancla, para que el oído la distinga, pero igual de cálida: nunca fría ni solemne.

**Descripción para Voice Design:**

> Native Colombian Spanish speaker with a neutral, educated Colombian accent from Bogotá. Clear seseo: c and z always sound like s, never the Castilian th sound; absolutely no Spain accent. A Colombian woman about thirty years old. Calm, warm, mid-low voice with clear, precise diction. She brings the evidence: a composed storyteller who presents facts and history with quiet confidence and a touch of intrigue, as if sharing something remarkable. Measured, unhurried pacing, noticeably calmer than an energetic teacher, yet warm and approachable, never cold or formal. Studio-quality recording.

**Texto de prueba** (del guion, sin cambios):

> El economista Richard Thaler, Premio Nobel de Economía en dos mil diecisiete, estudió lo que se llama contabilidad mental. En la cabeza separamos el dinero en cajones, y lo tratamos distinto según el cajón. La plata extra, un regalo o un premio, se gasta más fácil que la que costó ganar. Otros estudios encontraron algo parecido con las monedas sueltas: se gastan más fácil que un billete grande.

---

## Elegidas

| Papel | Voz | voice_id | Origen | Decidió |
|---|---|---|---|---|
| ANCLA | David - Friendly Male (joven, Cali) | `ECOET12tGKHdXyB0CfqU` | Voice Library, clon profesional; aviso de retiro 730 días | Diego, 13-oct, tras oírla leer el texto de prueba |
| PREGUNTA | Maria - Confident and Clear (joven, colombiana) | `scn1gPWkdVd8FhODJoei` | Voice Library, clon profesional; aviso de retiro 730 días | Diego, 13-oct, la oyó en la web de ElevenLabs; luego narró las dos clases |
| TESTIGO | Alisson - Tender and Mellow (mediana edad, colombiana) | `SmgKjOvC1aIujLWcMzqq` | Voice Library, clon profesional; aviso de retiro 730 días | Diego, 13-oct, tras oírla leer el texto de prueba |

Ajustes con los que se oyó: `eleven_v4`, stability 0,55, similarity 0,8, style 0,2, speaker boost, speed 0,92, MP3 192 kbps. Se usa por API con su voice_id, sin agregarla a la cuenta.

Reparto completo: un hombre y dos mujeres, como se aprobó. Las candidatas de Voice Design quedan descartadas (ver «Cómo se eligieron»).

## Cómo se eligieron (13-oct)

1. **Voice Design** (`eleven_ttv_v3`): dos tandas de tres llamadas, una por papel, con las descripciones de arriba. Se renombraron las muestras al azar y Diego las escuchó a ciegas en audífono y en el parlante del celular, con cinco criterios: cercanía, acento, claridad, papel y contraste. Resultado: aunque se pidió acento latino, y en la segunda tanda colombiano con seseo, catorce de dieciocho muestras sonaron a España, y ningún ANCLA sirvió. Cada tanda costó unos 1.100 créditos. **Lección:** Voice Design tiende al castellano de España.
2. **Voice Library**: se probaron voces colombianas leyendo los textos de prueba por API, con su `voice_id` y sin agregarlas a la cuenta. Diego eligió las tres de la tabla.

Las voces de la Voice Library son clones profesionales de personas reales. Su dueño puede retirarlas con el aviso indicado en la tabla, de 730 días para las tres. Si una se retira, se repite el casting de ese papel y se renarran las clases.

## Aviso de IA (al inicio de cada clase)

> Las voces de esta clase fueron creadas con inteligencia artificial. El guion se escribió con ayuda de inteligencia artificial y lo revisó una persona.

Va en `narrar.py` (AVISO) y lo lee el ANCLA. Lo exige la política de uso de ElevenLabs (§10). La segunda frase solo vale si de verdad hubo revisión humana del guion.

## Pendiente

- Nombres propios de los profesores: son parte de la identidad del proyecto y se deciden con Sergio.
- Leer el Voice Library Addendum de ElevenLabs. Todavía no se verificó: ver `LICENCIA-AUDIO.md`.
