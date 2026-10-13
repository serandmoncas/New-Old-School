# Contexto para asistentes de IA

Este archivo es el contexto compartido que cualquier asistente de IA (Claude, ChatGPT, Gemini, Copilot, agentes de código) debe leer antes de ayudar en este repositorio. Si eres colaborador humano, pásale este archivo a tu IA al empezar una sesión.

## Qué es el proyecto

New Old School es un colegio virtual open source. Enseña primero saberes prácticos que casi no se enseñan (dinero, derechos, salud, autonomía, pensamiento crítico) y los conecta con los conceptos académicos que los sostienen. El contenido lo construyen voluntarios con ayuda de su propia IA y lo validan docentes. Debe poder llegar a estudiantes sin internet.

Lee `docs/vision.md` y `docs/glosario.md` antes de proponer cambios de fondo.

## Público

- Estudiantes de ≈ 11 a 16 años (básica secundaria), también adultos que nunca aprendieron estos temas.
- Muchos con celular básico, poca conectividad y poco acompañamiento en casa.
- Idioma base: español claro y neutro. Adaptaciones locales en `curriculo/<modulo>/locales/<pais>/`.

## Reglas para el contenido que generes

1. **Respeta el formato.** Todo nodo usa la plantilla `docs/plantillas/nodo.md`, con el encabezado YAML completo. No inventes campos nuevos.
2. **No cambies `id`, `responsable` ni `estado` de un nodo** salvo que la persona te lo pida explícitamente.
3. **Lenguaje para un estudiante de 12 años**: frases cortas, ejemplos cotidianos, cero jerga sin explicar.
4. **Núcleo vs. local.** En `nucleo/` va solo lo universal (conceptos). Leyes, impuestos, entidades, montos y trámites de un país van en `locales/<pais>/`.
5. **No inventes datos.** Cifras, tasas, leyes o nombres de entidades: si no tienes una fuente verificable, deja `<!-- VERIFICAR: ... -->` en el texto para que un humano lo revise.
6. **Seguridad primero.** Salud, primeros auxilios, medicamentos y electricidad siempre llevan `revision_experta: true` y nunca se marcan como aprobados por la IA.
7. **Nada de consejos financieros personalizados.** Se enseñan conceptos y cómo decidir, no qué comprar o invertir.
8. **Pluralidad.** Evita ejemplos que solo funcionen en un país rico o en una ciudad grande.
9. **Cita fuentes** abiertas cuando aportes recursos (`recursos:` en el encabezado).
10. **Indica tu participación.** En `procedencia:` registra el modelo usado (por ejemplo `claude-opus-5-5`, `gpt-…`) y que hubo revisión humana.

## Reglas para el código

- Stack previsto: Next.js (frontend y PWA), FastAPI (backend), Postgres + pgvector. Ver `plataforma/README.md`.
- Python 3.11+, tipado, `ruff` para formato. TypeScript estricto en el frontend.
- No agregues dependencias pesadas sin una decisión registrada en `docs/decisiones/`.
- Cambios pequeños y enfocados; una tarea por PR.

## Antes de terminar una tarea

- Ejecuta `python scripts/validar_curriculo.py` si tocaste `curriculo/`.
- Resume en el PR qué cambió y qué quedó pendiente de verificar.
- No hagas cambios fuera del alcance del Issue en el que estás trabajando.

## Dónde preguntar

Dudas de contenido: en el Issue del nodo. Dudas de dirección del proyecto: en Discussions, categoría "Propuestas". Decisiones tomadas: `docs/decisiones/`.
