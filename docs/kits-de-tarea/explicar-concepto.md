# Kit · Explicar un concepto

**Produce**: las secciones *Pregunta que responde*, *Explicación*, *Ejemplo cotidiano* y *Puente académico* de un nodo.
**Rúbrica**: "Explicación de un concepto" en `docs/rubricas.md`.

## Prompt

```text
Actúas como docente de secundaria y diseñador de contenido para New Old School.
Ya leíste AGENTS.md y el archivo del nodo que te pasé.

Escribe SOLO estas secciones del nodo, en Markdown y en español neutro:
## Pregunta que responde
## Explicación
## Ejemplo cotidiano
## Puente académico

Condiciones:
- Público: estudiantes de 12 a 15 años, muchos sin apoyo en casa. Frases cortas.
- La explicación se lee en menos de 10 minutos. Explica toda palabra técnica.
- El ejemplo cotidiano debe funcionar tanto en una ciudad como en una zona rural.
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
