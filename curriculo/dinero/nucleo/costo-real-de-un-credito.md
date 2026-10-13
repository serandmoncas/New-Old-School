---
id: dinero.costo-real-de-un-credito
titulo: El costo real de un crédito
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 3
prerrequisitos: [dinero.tarjetas-de-credito]
conecta_con: [matematicas.sucesiones, matematicas.funciones-exponenciales]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión; cuotas, tasas efectivas y tasa implícita verificadas con script}
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: 'verificación de evidencias con fuentes primarias (Issue #10); correcciones de precisión'}
recursos:
- {titulo: Tasa anual equivalente, url: 'https://es.wikipedia.org/wiki/Tasa_anual_equivalente', licencia: CC BY-SA 4.0}
- {titulo: Liber Abaci de Fibonacci, url: 'https://es.wikipedia.org/wiki/Liber_abaci', licencia: CC BY-SA 4.0}
- {titulo: 'Exponential Growth Bias and Household Finance (Stango y Zinman, 2009)', url: 'https://doi.org/10.1111/j.1540-6261.2009.01518.x', licencia: referencia}
actualizado: '2026-10-13'
---

# El costo real de un crédito

<!--
Nodo técnico de nivel 3. Núcleo: explica tasa efectiva, cuota fija y costo total sin nombres
de entidades. El nombre de la tasa estándar de cada país (TEA, TAE, APR…), la tasa de usura y
los cargos obligatorios van en la adaptación local (este nodo está en requieren_local).
Cifras verificadas con script. Moneda genérica ("pesos").
-->

## El gancho (≈ 30 s)

Juan necesita 1.000.000 de pesos a un año y tiene dos ofertas.

La primera cobra **1,8 % mensual**. La segunda, **2,1 % mensual**. Elige la primera, claro: es más barata.

Pero la primera trae un "seguro obligatorio" de 15.000 pesos al mes. Juan hace la cuenta completa: con la primera paga en total **1.300.824**. Con la segunda, **1.141.695**.

La tasa más baja le salía casi 160.000 pesos más cara. La tasa es solo una parte del precio. Lo que importa es **cuánto pagas en total, con todo incluido**.

## La idea (≈ 90 s)

Para saber cuánto cuesta un crédito de verdad hay que mirar tres cosas.

**1. La tasa efectiva.** Si te cobran 2 % mensual, en un año no es 24 %. Como el interés se acumula sobre el interés, el costo anual es (1,02)¹² − 1 ≈ **26,8 %**. Esa es la **tasa efectiva anual**. Muchos países obligan a los bancos a informarla con un nombre estándar, para que se puedan comparar ofertas.

**2. La cuota fija y cómo se reparte.** En la mayoría de los créditos pagas la misma cuota cada mes. Al principio, casi todo se va en intereses y poco en reducir la deuda (el **abono a capital**). Al final es al revés. Por eso, si pagas antes, ahorras sobre todo los intereses que faltaban.

**3. Los costos extra.** Seguros, comisiones de estudio, cuota de manejo, papelería, penalidades por pagar antes o por atrasarte. Todo eso es parte del precio, aunque no aparezca en la tasa.

La pregunta definitiva siempre es la misma: **¿cuánto voy a pagar en total, y cuánto me prestaron de verdad?** La diferencia es el costo real.

## La evidencia (≈ 60 s)

**Está comprobado** que las personas subestimamos cómo crece algo con interés compuesto. Los economistas lo llaman **sesgo del crecimiento exponencial**: imaginamos que las cosas crecen en línea recta. Un estudio publicado en 2009 encontró que quienes más tienen este sesgo tienden a pedir más prestado y a ahorrar menos.

**También hay evidencia** de que la información clara ayuda, aunque el efecto es moderado. En 1968, Estados Unidos empezó a exigir que todo crédito informe una tasa anual que incluya los costos obligatorios, justamente para que la gente pueda comparar. Después, muchos países copiaron la idea. Pero la herramienta solo sirve si se usa.

**Lo que se dice, pero no es cierto**: "sin intereses" significa gratis. Muchas ofertas de "0 % de interés" esconden el costo en un precio más alto que el de contado. Y otra: "la tasa más baja es la mejor oferta". Como vio Juan, depende de los costos extra.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, una tienda ofrece un televisor "a 10 cuotas de 120.000, ¡0 % de interés!". En otra tienda, el mismo televisor cuesta 1.000.000 de contado. Pagar 1.200.000 en cuotas por algo que vale 1.000.000 equivale a un crédito de casi el **3,5 % mensual**, más del **50 % al año**. El "cero por ciento" estaba en el precio.

En el campo, muchos créditos agrícolas se pagan **de una sola vez al final**, cuando se vende la cosecha, en lugar de cuotas mensuales. Para un productor eso puede ser mucho mejor, aunque los intereses se acumulen. Elegir bien la **forma de pago** es tan importante como la tasa.

Quien pregunta "¿cuánto pago en total?" negocia mejor y se equivoca menos.

## La puerta abierta (≈ 30 s)

Para conversar: **¿has visto alguna oferta de "0 % de interés" o "cuotas cómodas"? ¿Dónde crees que estaba el costo?**

Los siguientes nodos son **Historial crediticio**, sobre cómo los bancos deciden si prestarte, y la ruta **Protegerse**.

---

## Puente académico

El saldo de un crédito mes a mes es una **sucesión**: cada término se calcula a partir del anterior (se le suma el interés y se le resta la cuota). La fórmula de la cuota fija sale de sumar una **serie geométrica**:

> **cuota = P × r ÷ (1 − (1 + r)⁻ⁿ)**

donde *P* es lo prestado, *r* la tasa mensual y *n* el número de cuotas. Y el paso de una tasa mensual a una anual, (1 + r)¹² − 1, es una **función exponencial**: por eso la diferencia entre 24 % y 26,8 % crece cuanto más alta es la tasa.

Un poco de historia: en 1202, el matemático italiano **Fibonacci** publicó el *Liber Abaci*, el libro que ayudó a llevar a Europa los números que usamos hoy (los "arábigos", que vienen de la India). Una buena parte del libro estaba dedicada a problemas de comerciantes: cambios de moneda, repartos de ganancias e intereses. Las matemáticas del crédito tienen más de 800 años.

## Ejercicios

1. **(Resuelto)** Un crédito cobra 2 % mensual. ¿Cuál es la tasa efectiva anual?
    - (1,02)¹² − 1 = 1,2682 − 1 = 0,2682 → **26,8 % anual**, no 24 %.
2. **(Resuelto)** Compara las ofertas de Juan por 1.000.000 a 12 meses: A, 1,8 % mensual más un seguro de 15.000 al mes; B, 2,1 % mensual sin seguro.
    - A: cuota del crédito ≈ 93.402 + seguro 15.000 = **108.402** al mes → total ≈ **1.300.824**.
    - B: cuota ≈ **95.141** al mes → total ≈ **1.141.695**.
    - **B es más barata** por unos 159.000, aunque su tasa es más alta.
3. Te prestan 1.000.000 al 2 % mensual a 12 meses con cuota fija. Usa la fórmula para calcular la cuota. ¿Cuánto pagas en total y cuánto en intereses?
4. Con el crédito del ejercicio 3, completa los tres primeros meses de la tabla de amortización: interés del mes, abono a capital y saldo.
5. El mismo 1.000.000 al 2 % mensual, pero a 24 meses. ¿Cuál es la cuota? ¿Cuánto pagas en total? Compara con el plazo de 12 meses: ¿qué ganas y qué pierdes con un plazo más largo?
6. Al crédito del ejercicio 3 le cobran una comisión de estudio de 50.000 al inicio. ¿Cuál es ahora el costo total del crédito (todo lo que pagas menos lo que te prestaron)?
7. Un productor pide 2.000.000 al 1,5 % mensual y lo paga de una sola vez al final de 6 meses, con interés compuesto. ¿Cuánto paga? Compáralo con el resultado de interés simple del nodo Interés simple (2.180.000).
8. Un televisor cuesta 1.000.000 de contado. Otra tienda lo vende en 10 cuotas de 120.000 "sin intereses". ¿Cuánto pagas en total? ¿Cuánto más que de contado? Con una calculadora financiera u hoja de cálculo (función TASA), encuentra la tasa mensual escondida.

<details>
<summary>Soluciones</summary>

3. cuota = 1.000.000 × 0,02 ÷ (1 − 1,02⁻¹²) ≈ **94.560**. Total: 94.560 × 12 ≈ **1.134.715**. Intereses: ≈ **134.715**.
4. Mes 1: interés 1.000.000 × 0,02 = 20.000; abono 94.560 − 20.000 = 74.560; saldo **925.440**. Mes 2: interés ≈ 18.509; abono ≈ 76.051; saldo ≈ **849.390**. Mes 3: interés ≈ 16.988; abono ≈ 77.572; saldo ≈ **771.818**. Cada mes el interés baja y el abono sube.
5. Cuota a 24 meses ≈ **52.871**; total ≈ **1.268.906**; intereses ≈ 268.906, el **doble** que a 12 meses. Ganas una cuota más baja (más fácil de pagar cada mes); pierdes porque pagas mucho más en total.
6. Pagas 1.134.715 + 50.000 = 1.184.715 por un préstamo de 1.000.000: costo total ≈ **184.715**.
7. 2.000.000 × 1,015⁶ ≈ **2.186.887**. Con interés simple eran 2.180.000: el compuesto cuesta unos **6.887** más. En plazos cortos la diferencia es pequeña; en plazos largos crece mucho.
8. Total: 120.000 × 10 = **1.200.000**, es decir **200.000 más** que de contado. La tasa escondida es de aproximadamente **3,46 % mensual**, que equivale a más del **50 % efectivo anual**. "Sin intereses" no significaba gratis.

</details>

## Caso práctico (evidencia de dominio)

**Comparador de créditos (simulación).**

1. Busca **dos o tres ofertas reales** para el mismo monto y plazo (por ejemplo, 1.000.000 a 12 meses): bancos, cooperativas, tiendas o aplicaciones. Usa sus simuladores públicos si los tienen.
2. Para cada una anota: tasa (y si es mensual o anual), tasa efectiva anual si la informan, cuota, seguros, comisiones y otros cargos.
3. Calcula para cada una el **total a pagar** y el **costo total** (total menos lo prestado).
4. Ordénalas de la más barata a la más cara y explica si el orden coincide con el de sus tasas.

**Entrega:** la tabla comparativa con fuentes, tus cálculos y tu conclusión. *No hay que pedir ningún crédito real ni dar datos personales en los simuladores.*

**Se evalúa así:**

- Las ofertas son reales, comparables (mismo monto y plazo) y con fuente.
- Se incluyen los costos extra, no solo la tasa.
- El total y el costo total están bien calculados.
- La conclusión explica por qué la más barata lo es.

## Errores comunes

- **Comparar tasas nominales** sin pasarlas a efectivas o sin mirar el periodo.
- **Ignorar los costos extra.** Seguros y comisiones pueden cambiar cuál crédito es más barato.
- **Elegir solo por la cuota más baja.** Un plazo más largo baja la cuota, pero sube el total.
- **Creer en el "0 % de interés"** sin comparar con el precio de contado.
- **No preguntar por el pago anticipado.** Algunos créditos penalizan pagar antes; otros permiten ahorrar intereses.
- **Firmar sin la tabla de amortización.** Pídela siempre: muestra cuánto pagas en cada cuota y cuánto debes después.

## Para el docente ancla

- **Tiempo:** dos sesiones de 45 a 60 minutos (es un nodo técnico) y una semana para el comparador.
- **Cómo abrir:** presenta las dos ofertas de Juan y pide que voten por la más barata antes de hacer la cuenta completa.
- **Para conversar:** ¿por qué las ofertas destacan la tasa o la cuota y no el total? ¿Qué debería informar obligatoriamente todo crédito?
- **Herramientas:** una hoja de cálculo con las funciones de pago y tasa (PAGO y TASA, o PMT y RATE) ahorra mucho trabajo; también sirve para construir la tabla de amortización entre todos.
- **Cuidado:** los simuladores de las entidades a veces piden datos personales. Indica que solo se usen los que no los piden, o que se use información de ejemplo.
- **Adaptación local:** el nombre y la definición de la tasa estándar del país, la tasa máxima legal y los seguros obligatorios van en el nodo local.
- **Siguiente nodo:** Historial crediticio.
