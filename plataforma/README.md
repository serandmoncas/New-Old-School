# Plataforma

Código de la plataforma de New Old School. **Aún no hay código**: se empieza en la Fase 2 (ver `docs/roadmap.md`). Antes de escribirlo, abre Issues con la plantilla "Tarea de plataforma".

## Qué hace

1. **Grafo de conocimiento**: lee `curriculo/` (Git es la fuente de verdad) y lo indexa.
2. **Motor de tareas**: detecta huecos en los nodos, genera tareas con su kit, gestiona entregas, revisiones y reputación.
3. **Entrega a estudiantes**: app web progresiva offline y exportación a Kolibri.

## Estructura prevista

```
plataforma/
├── backend/     FastAPI · Python 3.11+ · ruff
├── frontend/    Next.js · TypeScript estricto · PWA
└── infra/       Docker Compose para desarrollo local
```

## Stack y decisiones

| Pieza | Elección | Estado |
| --- | --- | --- |
| Backend | FastAPI | propuesta |
| Frontend | Next.js | propuesta |
| Base de datos | Postgres + pgvector | propuesta |
| Contenido | Markdown + YAML en este repo | aceptada (ADR 0002) |
| Cola de tareas | Sobre Postgres al inicio | propuesta |

Cada elección "propuesta" se confirma con un ADR antes de escribir código.

## Modelo de datos inicial

`Concepto`, `Relación`, `Artefacto`, `Tarea`, `Entrega`, `Revisión`, `Voluntario`, `Hilo`, `Localización`. Ver `docs/vision.md` para el flujo del motor de tareas.

## Reglas

- Ningún secreto en el repositorio: usa `.env` (ignorado) y documenta las variables en `.env.example`.
- Datos de estudiantes menores: mínimos, nunca en logs, nunca enviados a servicios de IA de terceros.
- Un PR por tarea; tests para la lógica del motor de tareas.
