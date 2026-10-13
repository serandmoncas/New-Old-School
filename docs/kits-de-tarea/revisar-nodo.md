# Kit · Revisar un nodo

**Produce**: una revisión estructurada para pegar como comentario en el PR.
**Rúbricas**: todas las que apliquen en `docs/rubricas.md`.

La IA ayuda a encontrar problemas; **la aprobación es siempre humana**.

## Prompt

```text
Actúas como revisor crítico y exigente para New Old School.
Ya leíste AGENTS.md, docs/rubricas.md y el nodo que te pasé.

1. Califica el nodo con las rúbricas que apliquen (0, 1 o 2 por criterio),
   en una tabla: criterio | puntaje | motivo concreto.
2. Lista los errores factuales o de cálculo que encuentres, citando la línea.
3. Lista lo que no puedes verificar y habría que confirmar con una fuente.
4. Señala si algo del núcleo debería ir en una adaptación local.
5. Señala si el tema requiere revisión experta y no está marcado.
6. Propón máximo 5 mejoras concretas, ordenadas por impacto.

Sé directo. No elogies sin motivo. Si todo está bien, dilo en una línea.
```

## Antes de aprobar el PR

- [ ] Leí el nodo entero yo mismo, no solo la revisión de la IA.
- [ ] Confirmé los errores que la IA señaló (puede equivocarse).
- [ ] Si `revision_experta: true`, etiqueté `necesita-experto` en vez de aprobar solo.
- [ ] Mi usuario quedó en `revisores` del encabezado.
