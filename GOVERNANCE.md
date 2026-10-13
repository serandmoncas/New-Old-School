# Gobernanza

Cómo se organiza y decide New Old School mientras el proyecto es pequeño. Este documento se revisará cuando la comunidad supere ~30 colaboradores activos.

## Roles

| Rol | Responsabilidad | Permisos en GitHub |
| --- | --- | --- |
| **Coordinación** | Visión, prioridades, desbloquear, convocar la sincronización semanal | Admin |
| **Curador de módulo** | Mantiene el grafo de su módulo (`_modulo.yaml`), crea Issues de nodos, cuida la coherencia | Maintain sobre su carpeta (vía CODEOWNERS) |
| **Curador local** | Mantiene la adaptación de un país (`locales/<pais>/`) | Maintain sobre su carpeta |
| **Revisor** | Revisa PRs de contenido con las rúbricas | Write |
| **Revisor experto** | Aprueba contenido de riesgo (salud, electricidad, legal) | Write, etiqueta `necesita-experto` |
| **Colaborador** | Toma Issues y entrega contenido o código | Fork o Write |
| **Desarrollador** | Construye la plataforma | Write sobre `plataforma/` |

Una persona puede tener varios roles. La lista actual está en [`docs/equipo.md`](docs/equipo.md).

## Cómo se decide

| Tipo de decisión | Quién decide | Cómo |
| --- | --- | --- |
| Contenido de un nodo | Revisores del PR | Aprobación en el PR |
| Grafo de un módulo | Curador del módulo | PR propio, abierto 48 h a comentarios |
| Estructura, esquemas, herramientas, licencias | Coordinación + curadores | Propuesta en Discussions → consenso razonable → ADR en `docs/decisiones/` |
| Nuevo módulo o país | Coordinación | Propuesta en Discussions |

**Consenso razonable**: se publica la propuesta, se espera al menos 72 horas, se atienden objeciones. Si no hay acuerdo, decide la coordinación y lo deja escrito con sus razones.

## Registro de decisiones (ADR)

Toda decisión que afecte a más de una carpeta se registra en `docs/decisiones/NNNN-titulo.md` usando la plantilla `docs/plantillas/decision.md`. Una decisión no se borra: se reemplaza con otra que la cite.

## Contenido controvertido

Temas con desacuerdo legítimo (política, religión, economía) se presentan mostrando las posiciones principales con sus mejores argumentos y la evidencia disponible. No se toma partido. Si hay disputa, el curador abre una Discussion y, si hace falta, un panel de tres revisores decide.

## Sumarse a un rol

Cualquiera puede pedir un rol en Discussions, categoría "Equipo". Criterio: haber contribuido con calidad en al menos 3 PRs del área.
