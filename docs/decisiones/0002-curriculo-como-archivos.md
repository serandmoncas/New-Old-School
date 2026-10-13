# 0002 · El currículo vive como archivos Markdown + YAML en Git

- **Estado**: aceptada
- **Fecha**: 2026-10-12
- **Decide**: Coordinación

## Contexto

Necesitamos que muchas personas editen el currículo en paralelo, con historial, revisión y posibilidad de forks por país, antes de que exista la plataforma.

## Opciones consideradas

1. **Base de datos desde el inicio** — consultas ricas, pero exige construir la plataforma primero y pierde el historial público.
2. **Documentos compartidos (Google Docs, Notion)** — fácil de editar, pero sin revisión estructurada, sin forks y difícil de validar.
3. **Markdown + YAML en Git** — historial, revisión por PR, forks nativos, validable con scripts, legible sin herramientas.

## Decisión

Cada nodo es un archivo `.md` con encabezado YAML. El grafo de cada módulo vive en `_modulo.yaml`. La plataforma futura **lee** de este repositorio; Git es la fuente de verdad del contenido.

## Consecuencias

- Colaborar requiere un mínimo de GitHub; se documenta en `CONTRIBUTING.md` y se permitirá aportar por la plataforma después.
- El esquema del encabezado se valida en CI (`scripts/validar_curriculo.py`).
- Cambiar el esquema exige una nueva decisión y migrar todos los nodos.
