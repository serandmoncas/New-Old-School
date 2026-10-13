# 0004 · Se aporta con la IA de cada voluntario

- **Estado**: aceptada
- **Fecha**: 2026-10-12
- **Decide**: Coordinación

## Contexto

La idea original era aprovechar los "tokens sobrantes" de las suscripciones de IA de muchas personas, al estilo SETI@home.

## Opciones consideradas

1. **Agrupar suscripciones en la plataforma** — los límites de uso no son transferibles y compartir o automatizar cuentas de consumo suele ir contra los términos de los proveedores.
2. **Cada voluntario usa su propia IA en una tarea compartida** — legal, aprovecha lo que ya paga cada quien y suma revisión humana.
3. **Cómputo voluntario con modelos abiertos** — análogo real a SETI; útil para tareas por lotes más adelante.
4. **Créditos de API donados** — para tareas exigentes, vía becas o donaciones.

## Decisión

Para el MVP, solo la opción 2 (modo copiar y pegar con kits de tarea). Las opciones 3 y 4 quedan para fases posteriores.

## Consecuencias

- Toda entrega pasa por una persona que la revisa y responde por ella.
- Se registra el modelo usado en `procedencia`.
- La IA donada se usa para **producir contenido**, no para tutoría en vivo con estudiantes.
