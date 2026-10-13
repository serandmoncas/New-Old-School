# Kit · Explicar un concepto

**Produce**: la historia del nodo en formato Curioso (*El gancho*, *La idea*, *La evidencia*, *¿Y a mí qué?*, *La puerta abierta*) y el *Puente académico*.
**Rúbrica**: "Explicación de un concepto" en `docs/rubricas.md`.

## Prompt

```text
Actúas como divulgador y docente de secundaria para New Old School.
Ya leíste AGENTS.md y el archivo del nodo que te pasé.

Escribe SOLO estas secciones del nodo, en Markdown y en español neutro:
## El gancho (≈ 30 s)
## La idea (≈ 90 s)
## La evidencia (≈ 60 s)
## ¿Y a mí qué? (≈ 60 s)
## La puerta abierta (≈ 30 s)
## Puente académico

Condiciones:
- Las cinco primeras secciones forman una historia que se puede contar en
  voz alta en máximo 5 minutos (unas 650 palabras en total). Cuenta, no dictes.
- Una sola idea. Si necesitas explicar tres términos antes de llegar a lo
  curioso, recorta.
- Empieza directo en el gancho, sin introducción: una situación, una persona
  o un dato sorprendente.
- Concreto antes que completo: un ejemplo que se pueda imaginar o tocar vale
  más que tres conceptos.
- Público: estudiantes de 12 a 15 años, muchos sin apoyo en casa. Frases cortas.
  Explica toda palabra técnica.
- El ejemplo de "¿Y a mí qué?" debe funcionar en una ciudad y en una zona rural.
- En "La evidencia", di cómo lo sabemos y separa lo comprobado de lo que se dice.
- En "La puerta abierta", deja una pregunta para conversar y nombra el nodo siguiente.
- Usa los prerrequisitos del encabezado como lo que el estudiante ya sabe.
- En "Puente académico", conecta con los conceptos listados en `conecta_con`
  y muestra en 3 a 5 líneas cómo ese concepto explica la situación práctica.
- Si el nodo es de alcance "nucleo", NO menciones leyes, entidades, monedas
  ni montos de un país específico.
- No inventes datos. Si necesitas una cifra real, escribe
  <!-- VERIFICAR: qué hay que confirmar -->.
- No des consejos personalizados; enseña a entender y decidir.

Al final, fuera de las secciones, lista en 3 viñetas lo que un revisor
humano debería verificar.
```

## Antes de entregar

- [ ] Lo leí completo y lo entiendo.
- [ ] Verifiqué cada cálculo y cada afirmación factual.
- [ ] Cumple la rúbrica con al menos 80 %.
- [ ] Agregué mi entrada en `procedencia`.
