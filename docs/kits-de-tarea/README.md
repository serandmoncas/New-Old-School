# Kits de tarea

Un kit es todo lo que necesitas para aportar con **tu propia IA**: el contexto, el prompt, la rúbrica y el formato de entrega.

## Cómo usar un kit

1. Toma un Issue de tipo "Tarea de contenido" y asígnatelo (ver `CONTRIBUTING.md`).
2. Abre el kit que indica el Issue.
3. En tu chat de IA pega, en este orden:
    - el contenido de `AGENTS.md`,
    - el archivo del nodo (`curriculo/.../<slug>.md`),
    - el prompt del kit.
4. **Lee y corrige el resultado.** Verifica cálculos y datos. Marca con `<!-- VERIFICAR: ... -->` lo que no puedas confirmar.
5. Revisa contra la rúbrica del kit.
6. Pega el resultado en el archivo, agrega tu entrada en `procedencia` y abre el PR.

## Kits disponibles

| Kit | Para qué | Rúbrica |
| --- | --- | --- |
| [`explicar-concepto.md`](explicar-concepto.md) | Escribir la explicación, ejemplo y puente académico de un nodo | Explicación |
| [`generar-ejercicios.md`](generar-ejercicios.md) | Crear ejercicios con soluciones y errores comunes | Ejercicios |
| [`revisar-nodo.md`](revisar-nodo.md) | Revisar críticamente un nodo existente antes de aprobarlo | Todas |
| [`adaptar-local.md`](adaptar-local.md) | Crear la versión local de un nodo del núcleo | Adaptación local |

¿Propones un kit nuevo? Abre una Discussion en "Propuestas" con un ejemplo de uso.
