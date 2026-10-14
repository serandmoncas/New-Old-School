---
id: dinero.interes-compuesto
titulo: Interés compuesto
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 2
prerrequisitos: [dinero.interes-simple]
conecta_con: [matematicas.funciones-exponenciales, matematicas.potencias]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-14', nota: 'primera versión, nodo de referencia; evidencias verificadas en las fuentes; aprobada por serandmoncas para revisión'}
recursos:
- {titulo: Interés compuesto, url: 'https://es.wikipedia.org/wiki/Inter%C3%A9s_compuesto', licencia: CC BY-SA 4.0}
- {titulo: Wheat and chessboard problem, url: 'https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem', licencia: CC BY-SA 4.0}
- {titulo: Número e, url: 'https://es.wikipedia.org/wiki/N%C3%BAmero_e', licencia: CC BY-SA 4.0}
- {titulo: 'The Economic Importance of Financial Literacy (Lusardi y Mitchell, 2014)', url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5450829/', licencia: referencia}
- {titulo: 'Quote Investigator: Compound Interest Is Man''s Greatest Invention', url: 'https://quoteinvestigator.com/2011/10/31/compound-interest/', licencia: referencia}
actualizado: '2026-10-14'
---

# Interés compuesto

<!--
Nodo de referencia de la ruta Crecer. Moneda genérica ("pesos") y cifras redondas: es contenido del núcleo.
Las tasas (10 %, 6 %, 5 %) son para practicar, no promesas de rentabilidad ni recomendaciones.
Viene de Interés simple, que anuncia que "la gráfica se curvará": aquí se curva.
No repite lo que ya usan nodos vecinos: el sesgo exponencial (Costo real de un crédito),
Don Jairo con interés compuesto (Costo real de un crédito), la tarjeta de Mariana (Tarjetas de crédito).
Usa la regla del 70, igual que Inflación.
-->

## El gancho (≈ 30 s)

Cuenta una leyenda que el inventor del ajedrez le mostró el juego a un rey, y el rey, feliz, le ofreció lo que quisiera. El inventor pidió arroz: un grano en la primera casilla del tablero, dos en la segunda, cuatro en la tercera, y así, el doble en cada casilla.

El rey se rió: "¿Solo eso?". Pero en la casilla 21 ya iban más de un millón de granos. Y en la casilla 64, la última, harían falta más de nueve trillones. No hay tanto arroz en ningún reino.

Lo que pasó en ese tablero le pasa a tu dinero. A veces a tu favor y a veces en tu contra.

## La idea (≈ 90 s)

En el **interés simple**, el interés se calcula siempre sobre la plata del comienzo. En el **interés compuesto**, el interés de cada periodo **se suma** a lo que tienes, y el periodo siguiente se cobra o se paga interés **sobre todo**, incluido el interés anterior. Es **interés sobre interés**.

Mira la diferencia con 1.000.000 de pesos al 10 % anual:

- **Simple**: ganas 100.000 cada año, siempre lo mismo. En 3 años tienes 1.300.000.
- **Compuesto**: el primer año ganas 100.000 y tienes 1.100.000. El segundo ganas el 10 % de 1.100.000, que son 110.000, y tienes 1.210.000. El tercero ganas 121.000 y tienes **1.331.000**.

La diferencia parece pequeña, pero en 10 años, con interés simple tienes 2.000.000; con compuesto, **2.593.742**. En 20 años: 3.000.000 contra **6.727.500**.

Por eso el ingrediente más poderoso del interés compuesto no es la tasa: es el **tiempo**.

Un truco de memoria es la **regla del 70**: lo que crece *x* % por periodo se duplica en unos **70 ÷ *x*** periodos. Al 10 % anual, en unos 7 años.

Y funciona igual con las deudas. Si no pagas, los intereses se suman a lo que debes, y la deuda crece como el arroz del tablero.

## La evidencia (≈ 60 s)

**Lo comprobado**: la cuenta. No es una opinión: es aritmética, y puedes hacerla tú.

**También está comprobado** que a mucha gente le cuesta. Las economistas Annamaria Lusardi y Olivia Mitchell reunieron encuestas de muchos países que hacían la misma pregunta: "Si tienes 100 en una cuenta al 2 % anual y dejas crecer el dinero, después de 5 años, ¿tienes más de 102, exactamente 102 o menos de 102?". En los Países Bajos acertaron más de 8 de cada 10 adultos; en Estados Unidos, cerca de 2 de cada 3; en Rumania, solo 4 de cada 10. La respuesta es "más de 102": al primer año ya tienes 102, y después sigue creciendo. <!-- Verificado 2026-10-14 en Lusardi y Mitchell (2014), versión abierta en PMC: pregunta textual; tabla 2, pregunta de interés, correctas: Países Bajos 84,8 %, EE. UU. 64,9 %, Rumania 41,3 %. -->

**Lo que se dice, pero no es tan seguro**: que Albert Einstein llamó al interés compuesto "el mayor invento de la humanidad". Nadie ha encontrado una prueba de que lo dijera. La atribución más antigua que se conoce es de 1976, veintiún años después de su muerte. <!-- Verificado 2026-10-14 en Quote Investigator (2011): "QI has not located any significant evidence that Einstein made this comment"; primera atribución a Einstein, Wall Street Journal, 1976; murió en 1955. Cubre la variante "greatest invention", no "octava maravilla". -->

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, Sofía guarda 500.000 pesos a los 15 años en una cuenta que paga 6 % al año, y no los toca. Su primo guarda lo mismo, pero empieza a los 25. A los 35 años, el primo tiene 895.424. Sofía tiene **1.603.568**. Pusieron lo mismo; la de Sofía tuvo diez años más para crecer.

En el campo, Doña Rosa pide 200.000 pesos al 5 % mensual y no logra pagar. Cada mes los intereses se suman a la deuda. Al año debe 359.171. Al segundo año, **645.020**. El primer año la deuda creció 159.171; el segundo, 285.849. La bola de nieve rueda más rápido cuanto más grande es.

La misma fuerza que hace crecer el ahorro de Sofía hace crecer la deuda de Doña Rosa. La pregunta es de qué lado del tablero estás.

## La puerta abierta (≈ 30 s)

Para conversar: **si el tiempo es el ingrediente más poderoso, ¿qué cosa pequeña podrías empezar hoy para que crezca durante años?** No tiene que ser dinero.

Los siguientes nodos son **Deuda buena y deuda mala**, para cuando la bola de nieve rueda en tu contra, e **Invertir, lo básico**, para cuando rueda a tu favor.

---

## Puente académico

El interés compuesto es una **función exponencial**. Si llamas *M* al dinero después de *t* periodos, con capital *C* y tasa *r*:

> **M(t) = C × (1 + r)ᵗ**

El exponente *t* dice cuántas veces se multiplica por (1 + r). Por eso necesitas las **potencias**: 1,1³ = 1,1 × 1,1 × 1,1 = 1,331. Con 1.000.000 al 10 % durante 3 años: 1.000.000 × 1,331 = 1.331.000.

En el interés simple, la gráfica es una **recta**: sube lo mismo cada periodo. En el compuesto es una **curva** que se empina cada vez más, porque cada periodo sube un porcentaje de algo más grande. El tablero de ajedrez es la misma función con *r* = 100 %: en la casilla *n* hay 2ⁿ⁻¹ granos.

La leyenda del ajedrez es solo eso: la versión escrita más antigua que se conoce es de 1256. Lo real es la cuenta del tablero.

Un poco de historia: en 1683, el matemático suizo **Jacob Bernoulli** se preguntó qué pasaría si el interés se sumara cada mes, cada día, cada segundo. Descubrió que hay un límite: con 100 % al año, sumado sin parar, 1 peso se vuelve unos 2,718 pesos y nunca más. Ese número se llama ***e*** y hoy aparece en toda la ciencia, desde las poblaciones de bacterias hasta la física.

## Ejercicios

1. **(Resuelto)** Guardas 1.000.000 al 10 % anual de interés compuesto. ¿Cuánto tienes después de 3 años? Compáralo con interés simple.
    - Año 1: 1.000.000 × 1,10 = 1.100.000.
    - Año 2: 1.100.000 × 1,10 = 1.210.000.
    - Año 3: 1.210.000 × 1,10 = **1.331.000**.
    - Con interés simple: 1.000.000 + 100.000 × 3 = 1.300.000.
    - Diferencia: **31.000**. Es el interés que ganaron los intereses.
2. **(Resuelto)** Con la regla del 70, ¿en cuánto tiempo se duplica algo que crece 7 % al año? Compruébalo con la calculadora.
    - 70 ÷ 7 = **unos 10 años**.
    - Comprobación: 1,07¹⁰ ≈ 1,967. Casi el doble: la regla es una aproximación, no una cuenta exacta.
3. Una deuda de 200.000 pesos cobra 5 % mensual compuesto y no se paga nada. ¿Cuánto se debe después de 3 meses? Hazlo mes por mes.
4. Guardas 500.000 al 10 % anual durante 2 años. ¿Cuánto tienes con interés simple y cuánto con compuesto? ¿De dónde sale la diferencia?
5. Con la regla del 70: ¿en cuántos años se duplica algo que crece 2 % al año? ¿Y algo que crece 14 %?
6. Mira la deuda de Doña Rosa: el primer año creció 159.171 y el segundo, 285.849. Explica con tus palabras por qué creció más el segundo año, si la tasa fue la misma.
7. Responde la pregunta de Lusardi y Mitchell y justifica: si tienes 100 en una cuenta al 2 % anual compuesto, después de 5 años, ¿tienes más de 102, exactamente 102 o menos de 102? Calcula el valor exacto.
8. En el tablero de ajedrez, ¿cuántos granos hay en la casilla 11? ¿En qué casilla se pasa por primera vez del millón?
9. Haz una tabla de 100.000 pesos al 20 % anual (una tasa alta, solo para practicar) desde el año 0 hasta el año 5, con interés compuesto y con interés simple. Dibuja las dos gráficas en el mismo plano. ¿Qué forma tiene cada una?

<details>
<summary>Soluciones</summary>

3. Mes 1: 200.000 × 1,05 = 210.000. Mes 2: 210.000 × 1,05 = 220.500. Mes 3: 220.500 × 1,05 = **231.525**.
4. Simple: 500.000 + 50.000 × 2 = **600.000**. Compuesto: 500.000 × 1,1² = **605.000**. La diferencia, **5.000**, es el 10 % de los 50.000 de interés del primer año, que en el compuesto también ganaron interés el segundo año.
5. Al 2 %: 70 ÷ 2 = **35 años**. Al 14 %: 70 ÷ 14 = **5 años**. (Comprobación: 1,02³⁵ ≈ 2,00 y 1,14⁵ ≈ 1,93.)
6. Porque el 5 % del segundo año se calcula sobre una deuda más grande: ya incluye los intereses del primer año. La tasa es la misma, pero se aplica sobre más.
7. **Más de 102.** Al primer año ya hay 102, y cada año se suma más. Con interés simple serían 100 + 2 × 5 = 110; con compuesto, 100 × 1,02⁵ ≈ **110,41**. Quien responde "exactamente 102" está pensando en un solo año.
8. En la casilla *n* hay 2ⁿ⁻¹ granos. Casilla 11: 2¹⁰ = **1.024**. La casilla 20 tiene 524.288 y la 21 tiene 1.048.576: se pasa del millón en la **casilla 21**.
9. Compuesto: 100.000; 120.000; 144.000; 172.800; 207.360; **248.832**. Simple: 100.000; 120.000; 140.000; 160.000; 180.000; **200.000**. La del simple es una **recta**; la del compuesto, una **curva** que se separa cada vez más hacia arriba.

</details>

## Caso práctico (evidencia de dominio)

**La bola de nieve en números.**

1. Busca **una tasa real**: la de una cuenta de ahorros, una cooperativa, un crédito de una tienda o una tarjeta. Puede ser de un anuncio o de lo que te cuente un adulto de confianza. Anota la tasa y su periodo (mensual o anual).
2. Con esa tasa, haz una tabla de **10 periodos** para 100.000 pesos, con interés compuesto y con interés simple. Puedes usar calculadora, hoja de cálculo o hacerlo a mano.
3. Dibuja las dos gráficas en el mismo plano.
4. Escribe en 3 o 4 frases: ¿esa tasa trabaja a tu favor o en tu contra? ¿Qué pasaría si el tiempo fuera el doble?

**Entrega:** la tasa y su origen, la tabla, la gráfica y tu conclusión. No incluyas datos personales de nadie.

**Se evalúa así:**

- La tasa es real, su origen está identificado y se usa en el periodo correcto.
- La tabla del compuesto multiplica sobre el saldo anterior (no suma siempre lo mismo).
- La gráfica muestra la recta y la curva, bien rotuladas.
- La conclusión explica el papel del tiempo con un dato de la propia tabla.

## Errores comunes

- **Pensar en línea recta.** "10 % al año por 10 años es 100 %". Con interés compuesto es mucho más: 159 %.
- **Calcular siempre sobre el capital inicial.** En el compuesto, cada periodo se calcula sobre el saldo del periodo anterior.
- **Creer que solo sirve para ahorrar.** Las deudas que no se pagan crecen igual, y casi siempre a tasas más altas.
- **Fijarse solo en la tasa.** Una tasa pequeña durante mucho tiempo puede pesar más que una grande durante poco.
- **Creer en rentabilidades compuestas altísimas.** "Gana 10 % mensual" suena bien, pero compuesto es más del 200 % al año. Cuando alguien promete eso sin riesgo, casi seguro es una estafa (ver Estafas y pirámides).

## Para el docente ancla

- **Tiempo:** una sesión de 45 a 60 minutos y una semana para el caso práctico.
- **Cómo abrir:** cuenta la leyenda del ajedrez y pregunta, antes de hacer cuentas, cuántos granos creen que hay en la última casilla. Si hay tiempo, que llenen las primeras casillas con granos, fríjoles o tapas hasta que no alcance.
- **Para conversar:** ¿por qué es tan difícil imaginar el crecimiento compuesto? ¿Dónde más aparece algo que crece así (una noticia que se comparte, una plaga, un rumor)?
- **Cuidado:** este nodo no recomienda dónde ahorrar ni en qué invertir. Las tasas son para practicar. Puede haber familias del grupo con deudas que crecen; habla de cómo funcionan las deudas, nunca de las personas que las tienen.
- **Siguientes nodos:** Deuda buena y deuda mala, e Invertir, lo básico.
