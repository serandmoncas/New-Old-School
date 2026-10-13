# Puesta en marcha del repositorio

Pasos de una sola vez para la coordinación. Marca cada uno al terminarlo.

## 1. Crear la casa

- [ ] Crear la organización en GitHub (sugerido: `new-old-school`).
- [ ] Crear el repositorio `new-old-school` dentro de la organización, público, **sin** README (ya lo tenemos).
- [ ] Subir este contenido:

```bash
cd new-old-school
git remote add origin https://github.com/<organizacion>/new-old-school.git
git push -u origin main
```

## 2. Reemplazar marcadores

- [ ] `@SERGIO` en `.github/CODEOWNERS` → tu usuario real.
- [ ] `@<usuario>` en `docs/equipo.md`.
- [ ] La URL de Discussions en `.github/ISSUE_TEMPLATE/config.yml` si la organización no se llama `new-old-school`.

## 3. Equipos (Settings → Teams de la organización)

- [ ] `curadores-dinero`, `curadores-co`, `revisores`, `desarrollo`.
- [ ] Dar a cada equipo permiso **Write** sobre el repositorio.

## 4. Proteger `main` (Settings → Branches → Add rule)

- [ ] Requerir Pull Request antes de hacer merge.
- [ ] Requerir 1 aprobación y **aprobación de Code Owners**.
- [ ] Descartar aprobaciones viejas cuando hay commits nuevos.
- [ ] Requerir que pase el check **Validar currículo**.
- [ ] Requerir que la rama esté al día antes del merge.
- [ ] No permitir push directo, tampoco a administradores.

## 5. Herramientas de coordinación

- [ ] Etiquetas: `python scripts/configurar_github.py --repo <organizacion>/new-old-school`
- [ ] Activar **Discussions** con categorías: Anuncios, Propuestas, Preguntas, Equipo, Sincronización.
- [ ] Crear un **Project** (tablero) con columnas: Disponible · En curso · En revisión · Necesita experto · Hecho.
- [ ] Crear los Issues de la Fase 0 y Fase 1 desde `docs/roadmap.md`.
- [ ] Crear un Issue "Tarea de contenido" por cada nodo de referencia: `presupuesto`, `interes-compuesto`, `estafas-y-piramides`.

## 6. Invitar al equipo inicial

- [ ] Compartir el enlace al README y pedir que lean `docs/vision.md` y `CONTRIBUTING.md`.
- [ ] Agendar la primera sincronización semanal.
