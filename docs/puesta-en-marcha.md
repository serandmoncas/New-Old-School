# Puesta en marcha del repositorio

Pasos de una sola vez para la coordinación. Marca cada uno al terminarlo.

## 1. Crear la casa

- [x] Repositorio público: https://github.com/serandmoncas/New-Old-School
- [x] Contenido subido a `main`.
- [x] Marcadores reemplazados por `@serandmoncas` (CODEOWNERS, equipo, Discussions).

## 2. Sumar colaboradores

El repo vive en una cuenta personal, que no tiene equipos.

- [ ] Invitar a cada persona en **Settings → Collaborators** con permiso Write.
- [ ] Agregar su usuario en `docs/equipo.md` y en la línea de su carpeta en `.github/CODEOWNERS`.
- [ ] Opcional, si el grupo crece: crear una organización gratuita, transferir el repo (**Settings → Danger Zone → Transfer**) y usar equipos (`curadores-dinero`, `curadores-co`, `revisores`, `desarrollo`).

## 3. Proteger `main` (Settings → Branches → Add rule)

- [ ] Requerir Pull Request antes de hacer merge.
- [ ] Requerir 1 aprobación y **aprobación de Code Owners**.
- [ ] Descartar aprobaciones viejas cuando hay commits nuevos.
- [ ] Requerir que pase el check **Validar currículo**.
- [ ] Requerir que la rama esté al día antes del merge.
- [ ] No permitir push directo, tampoco a administradores.

## 4. Herramientas de coordinación

- [ ] Etiquetas: `python scripts/configurar_github.py --repo serandmoncas/New-Old-School`
- [ ] Activar **Discussions** con categorías: Anuncios, Propuestas, Preguntas, Equipo, Sincronización.
- [ ] Crear un **Project** (tablero) con columnas: Disponible · En curso · En revisión · Necesita experto · Hecho.
- [ ] Crear los Issues de la Fase 0 y Fase 1 desde `docs/roadmap.md`.
- [ ] Crear un Issue "Tarea de contenido" por cada nodo de referencia: `presupuesto`, `interes-compuesto`, `estafas-y-piramides`.

## 5. Invitar al equipo inicial

- [ ] Compartir el enlace al README y pedir que lean `docs/vision.md` y `CONTRIBUTING.md`.
- [ ] Agendar la primera sincronización semanal.
