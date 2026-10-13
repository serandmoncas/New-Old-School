# Cómo colaborar

Gracias por sumarte. Este documento existe para una sola cosa: que muchas personas trabajen al mismo tiempo **sin pisarse las mangueras**.

## Las 7 reglas

1. **Todo trabajo empieza en un Issue.** Si no existe, créalo con la plantilla que corresponda. Si existe y está asignado a otra persona, no lo tomes: comenta y coordina.
2. **Pide el Issue antes de empezar.** Comenta `/tomo` (o "lo tomo") y espera a que un curador te lo asigne, o asígnatelo si tienes permisos. Un Issue tiene **una sola persona responsable**.
3. **Si en 7 días no hay avance, el Issue se libera.** Comenta si vas lento; nadie pierde nada por soltar una tarea.
4. **Una rama y un PR por Issue**, pequeño y enfocado. En contenido: **un nodo por PR**.
5. **El encabezado del archivo dice quién lo tiene.** Al tomar un nodo, cambia `estado: en-progreso` y `responsable: tu-usuario` en tu primer commit. Así cualquiera lo ve en el repo, no solo en GitHub.
6. **Nadie hace merge de su propio PR.** Se necesita al menos una aprobación de quien CODEOWNERS indique para esa carpeta.
7. **Lo que afecta a todos se decide en público.** Estructura, esquemas, licencias, herramientas: propuesta en Discussions → decisión registrada en `docs/decisiones/`.

## Flujo de trabajo

```
Issue (con plantilla) → asignación → rama → commits → PR (con plantilla)
   → validación automática → revisión de pares → (revisión experta si aplica) → merge
```

### Nombres de rama

| Tipo de trabajo | Formato | Ejemplo |
| --- | --- | --- |
| Contenido de un nodo | `contenido/<modulo>/<slug>` | `contenido/dinero/interes-compuesto` |
| Adaptación local | `local/<pais>/<modulo>/<slug>` | `local/co/dinero/impuestos-basicos` |
| Revisión | `revision/<modulo>/<slug>` | `revision/dinero/presupuesto` |
| Documentación | `docs/<tema>` | `docs/glosario-dinero` |
| Plataforma | `plataforma/<tema>` | `plataforma/modelo-de-datos` |

### Mensajes de commit

Formato corto: `tipo(área): qué cambió`. Tipos: `contenido`, `local`, `revision`, `docs`, `plataforma`, `ci`.

```
contenido(dinero/interes-compuesto): primera versión de explicación y 8 ejercicios
```

## Estados de un nodo

| Estado | Significa | Quién lo cambia |
| --- | --- | --- |
| `pendiente` | Nadie lo ha tomado | Curador al crear el nodo |
| `en-progreso` | Alguien lo está escribiendo | El responsable |
| `en-revision` | PR abierto esperando revisión | El responsable |
| `aprobado` | Pasó revisión de pares (y experta si aplica) | Un revisor al aprobar |
| `retirado` | Ya no se usa; queda por historial | Curador del área |

## Si vas a usar IA para aportar

- Usa un kit de `docs/kits-de-tarea/` y pásale a tu IA el archivo `AGENTS.md`.
- **Siempre revisas tú** antes de subir. Eres responsable de lo que entregas.
- Registra el modelo usado en el campo `procedencia` del nodo.
- No subas texto que no entiendas o no puedas defender.

## Cómo evitar conflictos de Git

- Haz `git pull --rebase` antes de empezar y antes de abrir el PR.
- No edites `_modulo.yaml` en el mismo PR que un nodo; los cambios al grafo van en su propio PR revisado por el curador del módulo.
- No reformatees archivos que no son parte de tu Issue.
- Si dos PRs chocan, gana el que se abrió primero; el otro hace rebase.

## Revisar el trabajo de otros

- Usa `docs/rubricas.md`. Comenta en línea, sé concreto y amable.
- "Aprobar" significa: lo leí entero, cumple la rúbrica, lo defendería ante un estudiante.
- Si un nodo requiere `revision_experta: true`, tu aprobación no basta: etiqueta `necesita-experto`.

## Primeros pasos técnicos

```bash
git clone https://github.com/<organizacion>/new-old-school.git
cd new-old-school
pip install pyyaml
python scripts/validar_curriculo.py
```

## Comunicación

- **Issues**: una tarea concreta.
- **Discussions**: ideas, propuestas y preguntas abiertas.
- **Sincronización semanal**: 30 minutos para ver el tablero, desbloquear y repartir Issues. El resumen se publica en Discussions.

Al participar aceptas el [Código de conducta](CODE_OF_CONDUCT.md).
