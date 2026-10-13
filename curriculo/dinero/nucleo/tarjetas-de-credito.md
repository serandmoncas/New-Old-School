---
id: dinero.tarjetas-de-credito
titulo: Tarjetas de crédito
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 2
prerrequisitos: [dinero.deuda-buena-y-mala]
conecta_con: [matematicas.funciones-exponenciales]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión; simulación de pago mínimo verificada con script}
recursos:
- {titulo: Tarjeta de crédito, url: 'https://es.wikipedia.org/wiki/Tarjeta_de_cr%C3%A9dito', licencia: CC BY-SA 4.0}
- {titulo: Historia de Diners Club, url: 'https://en.wikipedia.org/wiki/Diners_Club_International', licencia: CC BY-SA 4.0}
actualizado: '2026-10-13'
---

# Tarjetas de crédito

<!--
Núcleo: las reglas concretas (si las compras a una cuota cobran interés, la tasa máxima, el
pago mínimo exigido, la cuota de manejo) cambian por país y por entidad: van en una adaptación local.
Las cifras del gancho salen de una simulación con tasa de 2,5 % mensual compuesto y pago mínimo
del 5 % del saldo (mínimo 20.000). Moneda genérica ("pesos").
-->

## El gancho (≈ 30 s)

Mariana debe 1.000.000 de pesos en su tarjeta. El extracto le ofrece un alivio: "Pago mínimo: 51.250".

Si cada mes paga solo el mínimo, ¿cuánto tarda en salir de la deuda?

**Más de cinco años.** Y en total paga más de 1.700.000 pesos por un millón que gastó en un par de meses.

Si en cambio paga 100.000 fijos cada mes, termina en un año y paga unos 1.165.000. La misma deuda, la misma tarjeta. Lo único que cambió fue cuánto pagaba.

## La idea (≈ 90 s)

Una **tarjeta de crédito** es un préstamo que ya está aprobado y que usas cada vez que pagas con ella. El banco te da un **cupo**: el máximo que puedes deber.

Cada mes te llega un **extracto** con lo que gastaste, y tienes una **fecha límite de pago**. Ahí decides:

- **Pagar el total:** en muchos casos no pagas intereses por esas compras. Así, la tarjeta es solo un medio de pago.
- **Pagar el mínimo o una parte:** sobre lo que queda debiendo se cobra interés, y ese interés se suma a la deuda. El mes siguiente pagas interés sobre el interés: es **interés compuesto** trabajando en tu contra.

Otros costos que hay que conocer: la **cuota de manejo** (lo que cobran por tener la tarjeta), los **avances en efectivo** (sacar plata de un cajero con la tarjeta, que suele ser de lo más caro) y los **intereses de mora** si te atrasas.

La regla de oro: **usa la tarjeta solo para comprar lo que podrías pagar de contado, y paga el total cada mes.** Si no puedes, no es una tarjeta: es una deuda cara.

## La evidencia (≈ 60 s)

**Está comprobado** que el pago mínimo funciona como un ancla. En un experimento publicado en 2009, las personas a las que se les mostró el pago mínimo en el extracto decidieron pagar menos que las que no lo vieron. Ese número pequeño hace que la deuda parezca más manejable de lo que es.

Por eso algunos países obligan a los bancos a mostrar en el extracto **cuánto tardarías y cuánto pagarías** si solo abonas el mínimo. En Estados Unidos es obligatorio desde 2009.

**Se ha encontrado también** que pagar con tarjeta hace que gastemos más que pagando en efectivo, porque no sentimos que el dinero sale. Un estudio famoso encontró diferencias muy grandes; otros estudios encontraron efectos más pequeños. Lo seguro es que el dolor de pagar existe y la tarjeta lo suaviza.

**Lo que se dice, pero no es cierto**: "tener cupo es tener plata". El cupo es plata prestada.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, a muchos jóvenes les ofrecen su primera tarjeta con el primer trabajo. Mariana recibió una con cupo de 1.500.000 y la usó como si fuera un aumento de sueldo. En dos meses ya debía un millón. Ahora sabe que el mínimo es la puerta de una trampa, y paga 100.000 al mes hasta salir.

En el campo y en los barrios existe algo parecido: el **fiado** en la tienda. El tendero anota en una libreta lo que llevas y pagas a fin de mes. Muchas veces no cobra intereses, y eso es una gran ayuda de la comunidad. Pero las reglas son las mismas: si la cuenta crece más rápido de lo que pagas, te atrapa; y si solo puedes comprar donde te fían, quizás pagas precios más altos sin darte cuenta.

Bien usada, una tarjeta es cómoda y segura. Mal usada, es la deuda más cara de tu vida.

## La puerta abierta (≈ 30 s)

Para conversar: **¿por qué crees que los bancos regalan tarjetas a personas jóvenes?** ¿Quién gana cuando pagas solo el mínimo?

El siguiente nodo es **El costo real de un crédito**: cómo saber cuánto cuesta de verdad un préstamo, con todo incluido.

---

## Puente académico

Una deuda en la tarjeta sin pagos crece así: **saldo × (1 + r)ⁿ**, donde *r* es la tasa mensual y *n* los meses. Es una **función exponencial**. Con 2,5 % mensual, en 12 meses una deuda de 1.000.000 sin pagos llega a 1.344.889: un 34,5 % más, no un 30 %, porque cada mes el interés se calcula sobre una deuda más grande.

Y cuando pagas solo el mínimo, el saldo baja muy despacio: casi todo tu pago se va en intereses y apenas una parte pequeña reduce lo que debes.

Un poco de historia: en 1950, en Nueva York, nació el Diners Club, una de las primeras tarjetas que servía en muchos comercios distintos. La leyenda dice que su fundador la inventó después de una cena en la que olvidó la billetera; los historiadores creen que la historia fue adornada para la publicidad. Lo cierto es que en pocas décadas las tarjetas cambiaron la forma de comprar en todo el mundo.

## Ejercicios

1. **(Resuelto)** Mariana debe 1.000.000 con un interés del 2,5 % mensual. Al final del mes, ¿cuánto interés se suma? Si el pago mínimo es el 5 % del nuevo saldo, ¿cuánto paga y cuánto de eso realmente reduce la deuda?
    - Interés: 1.000.000 × 0,025 = **25.000**. Nuevo saldo: 1.025.000.
    - Pago mínimo: 1.025.000 × 0,05 = **51.250**.
    - De esos 51.250, 25.000 se fueron en intereses: solo **26.250** reducen la deuda.
2. **(Resuelto)** Con los datos anteriores, una simulación mes a mes da estos resultados. ¿Qué conclusiones sacas?

    | Forma de pagar | Meses hasta salir | Total pagado |
    | --- | --- | --- |
    | Solo el mínimo (5 % del saldo, mínimo 20.000) | 63 (más de 5 años) | ≈ 1.732.000 |
    | 50.000 fijos al mes | 29 | ≈ 1.404.000 |
    | 100.000 fijos al mes | 12 | ≈ 1.165.000 |

    - Pagando solo el mínimo, Mariana paga **más de 700.000 en intereses** y tarda más de cinco años.
    - Duplicar el pago de 50.000 a 100.000 reduce el tiempo **a menos de la mitad** y ahorra casi 240.000.
3. Si Mariana no pagara nada durante 12 meses, con 2,5 % mensual compuesto, ¿cuánto debería? ¿En qué porcentaje creció la deuda? ¿Por qué no es 30 %?
4. Una compra de 600.000 se difiere a 6 cuotas fijas, con 2,5 % mensual. La cuota resulta de 108.930. ¿Cuánto pagas en total? ¿Cuánto pagas de intereses?
5. Una tarjeta cobra 25.000 pesos de cuota de manejo al mes. ¿Cuánto cuesta al año solo tenerla? ¿Qué te dice eso sobre aceptar tarjetas "porque sí"?
6. La fecha de corte de una tarjeta es el día 15 y la fecha límite de pago, el día 30. Haces una compra el día 16. ¿En qué extracto aparece y aproximadamente cuántos días pasan hasta que debes pagarla? ¿Por qué este dato puede ser útil y peligroso a la vez?
7. Compara el fiado en la tienda con una tarjeta de crédito: escribe dos parecidos y dos diferencias.
8. Mariana gana 1.200.000 al mes, debe 900.000 en la tarjeta y puede destinar 300.000 al mes a pagarla. Propón un plan para salir de la deuda y explica qué haría con la tarjeta mientras tanto.

<details>
<summary>Soluciones</summary>

3. 1.000.000 × 1,025¹² ≈ **1.344.889**. Creció **34,5 %**, no 30 % (2,5 % × 12), porque es interés compuesto: cada mes el interés se calcula sobre un saldo que ya incluye los intereses anteriores.
4. Total: 108.930 × 6 = **653.580**. Intereses: 653.580 − 600.000 = **53.580**.
5. 25.000 × 12 = **300.000 al año**. Una tarjeta que no necesitas cuesta aunque no la uses.
6. Aparece en el extracto del **siguiente corte** (el día 15 del mes siguiente) y debe pagarse hacia el día 30 de ese mes: unos **45 días** después de la compra. Es útil porque da tiempo para pagar sin intereses si pagas el total; es peligroso porque hace que la compra parezca "gratis" por mucho tiempo y es fácil olvidar que se debe.
7. Parecidos: compras hoy y pagas después; si la deuda crece más rápido de lo que pagas, te atrapa. Diferencias: el fiado muchas veces no cobra intereses y depende de la confianza personal; la tarjeta cobra intereses y cuotas, pero sirve en muchos lugares y está regulada. (Otras respuestas son válidas si están justificadas.)
8. Un plan razonable: **dejar de usar la tarjeta** mientras paga; pagar **300.000 fijos al mes** (no el mínimo) hasta saldarla: con 2,5 % mensual, lo logra en **4 meses** (el último pago es pequeño); revisar el presupuesto para no volver a depender de ella; y, cuando esté en cero, usarla solo para compras que pueda pagar completas cada mes.

</details>

## Caso práctico (evidencia de dominio)

**Leer un extracto (simulación).**

1. Consigue un **extracto de tarjeta de ejemplo**: muchos bancos publican modelos en su página, o tu docente puede repartir uno. *No uses el extracto real de nadie.*
2. Encuentra y anota: cupo, saldo total, pago mínimo, fecha de corte, fecha límite de pago, tasa de interés, cuota de manejo y otros cargos.
3. Calcula cuánto interés se cobraría el próximo mes si solo se paga el mínimo.
4. Escribe una recomendación de tres líneas para la persona dueña de ese extracto.

**Entrega:** la tabla con los datos encontrados, tu cálculo y tu recomendación.

**Se evalúa así:**

- Se identifican correctamente al menos seis de los ocho datos.
- El cálculo del interés es correcto.
- La recomendación es concreta y usa lo aprendido (pago total, evitar avances, revisar cargos).

## Errores comunes

- **Pagar solo el mínimo.** Es la forma más cara de pagar.
- **Pensar que el cupo es plata propia.** Es un préstamo.
- **Sacar avances en efectivo.** Suelen tener las condiciones más caras.
- **Diferir compras pequeñas a muchas cuotas.** Pagas intereses por cosas que ya se acabaron.
- **Tener varias tarjetas "por si acaso".** Cada una puede cobrar cuota de manejo y tentar a gastar.
- **No leer el extracto.** Ahí aparecen cargos que no esperabas.

## Para el docente ancla

- **Tiempo:** una sesión de 60 minutos y una semana para leer el extracto de ejemplo.
- **Cómo abrir:** muestra la frase "Pago mínimo: 51.250" y pregunta cuánto tiempo creen que tarda en pagarse la deuda pagando eso. Deja que apuesten antes de revelar los cinco años.
- **Para conversar:** ¿por qué los bancos ganan más cuando pagamos poco? ¿El fiado de la tienda es bueno o malo para la comunidad?
- **Cuidado:** usa siempre extractos de ejemplo, nunca reales. No presentes las tarjetas como malas en sí: el problema es el uso, no la herramienta.
- **Adaptación local:** las reglas de intereses de cada país (por ejemplo, si las compras a una cuota cobran interés), la tasa máxima y cómo se calcula el pago mínimo van en el nodo local.
- **Siguiente nodo:** El costo real de un crédito.
