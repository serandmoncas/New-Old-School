# Reloj de Curioso

Página para presentar y observar una charla en **Formato Curioso** (máximo 300 segundos). Es un solo archivo HTML, sin instalación: [`reloj-curioso.html`](reloj-curioso.html). Descárgalo y ábrelo en cualquier navegador, también en el celular.

## Tres pestañas

- **Presentar.** Regla de 300 s dividida en los cinco bloques (gancho, idea, evidencia, ¿y a mí qué?, puerta abierta), contador del bloque y guion en letra grande. El contador se pone ámbar en los últimos 10 s y rojo si te pasas. Al terminar muestra el tiempo objetivo contra el real de cada bloque.
- **Observar.** La hoja del observador de la [guía de la Ruta Base](../curioso-ruta-base.md) como formulario. Si el reloj se usó en el mismo dispositivo, el botón *Llevar a la hoja del observador* llena los tiempos solo.
- **Registro.** Compara las sesiones guardadas: tiempo medio, cuántas pasaron de 300 s, cuánta conversación abrieron y la claridad promedio, por guion.

## Guiones

Trae cargadas las pruebas 1 y 3 de [*El lobo estepario*](../curioso-lobo-estepario.md). En **Mi guion** puedes pegar cualquier otro: cada bloque empieza con una línea que comienza con `#`, su nombre y, si quieres, sus segundos entre paréntesis, por ejemplo `# Gancho (30)`. Lo que pegues se guarda solo en ese navegador.

Atajos: `Espacio` inicia o pausa, `→` pasa al siguiente bloque, `←` vuelve al anterior.

## Dónde quedan los registros

Este archivo, abierto desde el repo o desde tu computador, **no guarda las hojas en ningún servidor**: el botón las copia como texto para pegarlas en la conversación *Piloto Curioso · octubre 2026* de GitHub Discussions, como pide la guía. La versión publicada que usa el equipo del piloto sí guarda el registro compartido.

No escribas nombres ni historias personales de los asistentes sin su permiso.

## Si cambias los guiones

Los guiones están dentro del HTML, en la constante `GUIONES`. Si editas un guion en su `.md`, actualiza también esa constante para que el reloj muestre la misma versión.
