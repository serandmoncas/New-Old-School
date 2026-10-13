# 0005 · Clases narradas con un motor de tres voces

- **Estado**: propuesta
- **Fecha**: 2026-10-13
- **Decide**: Coordinación
- **Discusión**: Issue #26

## Contexto

Muchos estudiantes leen poco o con dificultad, estudian desde un celular básico y casi no tienen acompañamiento en casa. Una clase que se puede escuchar llega a más gente, y un MP3 se puede descargar una vez y oír sin conexión. Desde el comienzo, en `docs/origen.md`, se habló de varios «Profesores» por clase.

Un voluntario (Diego Robledo) armó un prototipo en `plataforma/narraciones/` y lo probó con dos nodos de Dinero:

- Un guion para tres papeles por cada nodo: ancla, la que pregunta y testigo. Se escribe con una regla escrita y un chequeo automático que no deja agregar datos que no estén en el nodo.
- Voces colombianas de ElevenLabs.
- Música sintetizada en local.

Los dos audios se escucharon y se aprobaron. Pero quedan restricciones abiertas.

- **Licencia.** La política de uso de ElevenLabs (versión del 9-oct-2026) prohíbe redistribuir el audio con términos más permisivos que los propios (§12), lo que choca con CC BY-SA (ADR 0001). También prohíbe los productos dirigidos a menores de 18 sin aprobación escrita (§1).
- **Costo.** Cada clase cuesta unos 2.000 créditos de una cuenta de pago, y hoy los pone un voluntario. Esto va en la línea de la ADR 0004.
- **Dependencias.** ffmpeg y numpy, más una API de pago.

## Opciones consideradas

1. **Adoptar el motor tal como está (ElevenLabs).** Suena bien, ya se escuchó y funciona. En contra: no se puede publicar el audio hasta tener permiso escrito de ElevenLabs, y cuesta dinero en cada clase.
2. **El mismo motor con un TTS abierto local.** Se cambia solo la función que pide la voz y lo demás sigue igual. Así desaparecen los dos bloqueos, no hay costo por clase y funciona sin conexión. En contra: todavía no se midió cómo suena, y probablemente suene peor.
3. **No narrar por ahora.** No cuesta nada. En contra: se pierde el formato oral, justo para quienes más lo necesitan.

## Decisión

Propuesta, que Coordinación debe decidir:

- Que entre a `plataforma/narraciones/` como **herramienta experimental**: la regla nodo→guion, el chequeo y el motor.
- Que los guiones se versionen en el repo con licencia CC BY-SA, porque son una derivación de los nodos.
- Que **no se publique ningún audio** mientras no se resuelva la licencia por alguna de estas vías: (a) permiso escrito de ElevenLabs para publicar con CC BY-SA y para un público menor de 18 años; (b) otra licencia solo para el audio; o (c) un TTS abierto, la opción 2.

## Consecuencias

- Cualquier voluntario puede preparar y revisar guiones sin gastar nada. Narrar exige una cuenta de pago y la clave en el entorno; nunca se sube al repo.
- Cada guion pasa por el chequeo automático y por una revisión humana con nombre y fecha antes de narrarse. El aviso de IA va al comienzo de cada clase.
- Hay que decidir quién le escribe a ElevenLabs para pedir los permisos, o si se prueba la opción 2 y se compara a ciegas con el audio actual.
- Hay que decidir los nombres propios de los tres Profesores. Son parte de la identidad del proyecto.
- Si el dueño de una voz de la Voice Library la retira (con 730 días de aviso), ese papel vuelve a casting y hay que renarrar las clases.
