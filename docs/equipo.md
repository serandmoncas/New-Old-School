# Equipo y responsabilidades

Quién es dueño de qué. **Mantener esta tabla al día es la forma más simple de no pisarnos.** Cualquier cambio de rol va en un PR revisado por la coordinación.

## Roles actuales

| Persona | Usuario GitHub | Roles | Áreas que cuida | Contacto preferido |
| --- | --- | --- | --- | --- |
| Sergio Monsalve | `@serandmoncas` | Coordinación, curador de Dinero, plataforma | Todo el repo (temporal) | Discussions |
| _(por asignar)_ | | Curador local Colombia | `curriculo/*/locales/co/` | |
| _(por asignar)_ | | Revisor | `curriculo/dinero/` | |
| _(por asignar)_ | | Revisor experto legal/tributario | Nodos con `revision_experta: true` | |
| _(por asignar)_ | | Desarrollo | `plataforma/` | |

Al confirmar los usuarios de GitHub, actualizar también `.github/CODEOWNERS`.

## Quién trabaja en qué ahora

No se mantiene aquí: la fuente de verdad es el **tablero de Issues** (GitHub Projects) y el campo `responsable` del encabezado de cada nodo. Para verlo desde la terminal:

```bash
python scripts/validar_curriculo.py --estado
```

## Sincronización semanal

- Duración: 30 minutos.
- Agenda fija: (1) qué se cerró, (2) qué está bloqueado, (3) qué Issues se reparten esta semana, (4) decisiones pendientes.
- El resumen se publica en Discussions, categoría "Sincronización".
