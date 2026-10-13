# Kit · Adaptar un nodo a un país

**Produce**: un nodo local en `curriculo/<modulo>/locales/<pais>/<slug>.md` que complementa al nodo del núcleo.
**Rúbrica**: "Adaptación local" en `docs/rubricas.md`.

## Antes de empezar

Crea el archivo con:

```bash
python scripts/nuevo_nodo.py <modulo> <slug> "Título" --pais <codigo>
```

Así queda enlazado al nodo del núcleo (`nodo_base`).

## Prompt

```text
Actúas como docente de secundaria en <PAÍS> y diseñador de contenido para
New Old School. Ya leíste AGENTS.md y el nodo del núcleo que te pasé.

Escribe la adaptación local para <PAÍS>. No repitas la explicación del núcleo:
compleméntala. Secciones, en Markdown:
## Cómo funciona en <PAÍS>
## Ejemplo con datos de <PAÍS>
## Entidades y recursos oficiales
## Ejercicios con contexto local (3 a 5, con soluciones en <details>)

Condiciones:
- Usa vocabulario y moneda del país.
- Toda ley, entidad, tasa, monto o trámite debe ir con su fuente oficial.
  Si no tienes certeza de que esté vigente, escribe
  <!-- VERIFICAR: dato, fuente sugerida, fecha -->.
- No des asesoría tributaria, legal ni financiera personalizada.
```

## Antes de entregar

- [ ] Verifiqué cada dato con una fuente oficial y anoté la fecha de consulta en `recursos`.
- [ ] Si toca impuestos, seguridad social o temas legales, `revision_experta: true`.
- [ ] Agregué mi entrada en `procedencia`.
