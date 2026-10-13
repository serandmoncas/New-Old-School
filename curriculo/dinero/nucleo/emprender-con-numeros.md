---
id: dinero.emprender-con-numeros
titulo: Emprender con números
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 3
prerrequisitos: [dinero.trabajo-independiente, dinero.costo-real-de-un-credito]
conecta_con: [matematicas.funciones-lineales, matematicas.estadistica-descriptiva]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión; punto de equilibrio y escenarios verificados con script}
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: 'verificación de evidencias con fuentes primarias (Issue #10); correcciones de precisión'}
recursos:
- {titulo: Punto de equilibrio, url: 'https://es.wikipedia.org/wiki/Punto_de_equilibrio_(econom%C3%ADa)', licencia: CC BY-SA 4.0}
- {titulo: Richard Cantillon y el concepto de emprendedor, url: 'https://en.wikipedia.org/wiki/Richard_Cantillon', licencia: CC BY-SA 4.0}
- {titulo: 'BLS: supervivencia de establecimientos nacidos en 2013', url: 'https://www.bls.gov/opub/ted/2024/34-7-percent-of-business-establishments-born-in-2013-were-still-operating-in-2023.htm', licencia: referencia}
- {titulo: 'The top reasons startups fail (CB Insights, 2026)', url: 'https://www.cbinsights.com/research/report/startup-failure-reasons-top/', licencia: referencia}
- {titulo: 'Cantillon, Essai sur la nature du commerce en général (Econlib)', url: 'https://www.econlib.org/library/NPDBooks/Cantillon/cntNT8.html', licencia: referencia}
actualizado: '2026-10-13'
---

# Emprender con números

<!--
Último nodo del módulo Dinero. Moneda genérica ("pesos"), cifras redondas.
Los requisitos para formalizar un negocio en cada país van en una adaptación local.
Tono: animar a emprender con los ojos abiertos, no desanimar.
-->

## El gancho (≈ 30 s)

Luz vende empanadas en la esquina del colegio. Vende 100 al día, a 2.500 pesos cada una: entran **250.000 pesos diarios**. "¡Qué buen negocio!", le dicen los vecinos.

Luz saca la cuenta completa. Cada empanada le cuesta 1.200 en ingredientes. Paga 400.000 al mes por el puesto y 200.000 por el gas. Trabaja diez horas diarias. Al final, por cada hora de trabajo gana cerca de 10.700 pesos: un poco más que un empleo, pero sin salud, pensión ni vacaciones.

No es un mal negocio. Pero no es lo que parecía. **Las ventas no son la ganancia.** Esa diferencia decide qué emprendimientos sobreviven.

## La idea (≈ 90 s)

Para saber si un negocio funciona, necesitas cuatro números:

1. **Precio:** cuánto cobras por cada unidad.
2. **Costo variable:** lo que te cuesta producir cada unidad (ingredientes, empaque). Sube si vendes más.
3. **Costos fijos:** lo que pagas cada mes aunque no vendas nada (arriendo, servicios, cuotas de un crédito).
4. **Margen:** precio menos costo variable. Es lo que cada venta aporta para pagar los fijos y, después, para ganar.

Con eso calculas el número más importante de un negocio: el **punto de equilibrio**, cuántas unidades tienes que vender para no perder ni ganar.

> **Punto de equilibrio = costos fijos ÷ margen por unidad**

Luz necesita vender 600.000 ÷ 1.300 ≈ 462 empanadas al mes, unas 18 al día, solo para cubrir sus costos. Todo lo que venda por encima es ganancia.

Dos consejos más. Cuida el **flujo de caja**: puedes tener un negocio rentable y quebrar porque te pagan tarde y no tienes con qué comprar los ingredientes. Y **prueba antes de invertir**: vende un poco, en pequeño, para saber si de verdad hay clientes, antes de endeudarte.

## La evidencia (≈ 60 s)

**Es un dato**: muchos negocios nuevos cierran pronto. En Estados Unidos, por ejemplo, alrededor de uno de cada cinco cierra en su primer año y cerca de la mitad no llega a los cinco años. En muchos países de América Latina la proporción es parecida o mayor.

**Se ha estudiado por qué**. En análisis de cientos de *startups* (empresas nuevas con inversionistas) que cerraron, las razones más comunes fueron quedarse sin dinero y vender algo que el mercado no necesitaba lo suficiente. Quedarse sin dinero suele ser el final de la historia: muchas veces el problema empezó antes, al no conocer bien a sus clientes ni sus números.

**Lo que se dice, pero no es tan simple**: "si vendes mucho, ganas mucho". Si el margen es pequeño o los costos fijos son altos, puedes vender mucho y perder. Y otro mito: "emprender es solo para quien tiene plata". Muchos negocios empiezan en pequeño, probando con poco, y crecen con lo que van ganando.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, Luz prueba subir el precio a 3.000. Vende menos, 80 al día, pero su margen sube a 1.800 por empanada. Hace la cuenta: gana más que antes, vendiendo menos y trabajando menos. Sin números, nunca se habría atrevido.

En el campo, Doña Marta piensa en vender huevos a una tienda del pueblo que paga a los 30 días. Las ventas suben, pero el concentrado lo tiene que pagar de contado cada semana. Si no planea su flujo de caja, se queda sin plata para alimentar a las gallinas justo cuando el negocio va mejor. Decide pedir que le paguen la mitad por adelantado.

Emprender no es tener una buena idea. Es tener una buena idea **con números que cierran**.

## La puerta abierta (≈ 30 s)

Para conversar: **¿qué negocio de tu barrio o vereda te parece que funciona bien? ¿Por qué crees que funciona?** Si pudieras preguntarle a su dueño un solo número, ¿cuál sería?

Con este nodo termina el módulo **Dinero**. Lo que sigue es usarlo: tu propio presupuesto, tu propia meta y, quizás, tu propio negocio.

---

## Puente académico

La ganancia de un negocio es una **función lineal** de las unidades vendidas:

> **Ganancia = margen × unidades − costos fijos**

Su gráfica es una recta que empieza en negativo (si no vendes nada, pierdes los costos fijos) y cruza el cero justo en el **punto de equilibrio**. Y para entender las ventas de cada día, que suben y bajan, se usa la **estadística descriptiva**: promedio, mínimo, máximo, y qué tanto varían.

Un poco de historia: uno de los primeros en usar la palabra **emprendedor** en economía fue **Richard Cantillon**, un banquero que escribió hacia 1730 un ensayo sobre el comercio, publicado en 1755. Para él, el emprendedor era quien compra a un precio cierto para vender a un precio incierto: alguien que asume el riesgo. Casi tres siglos después, la definición sigue siendo buena.

## Ejercicios

1. **(Resuelto)** Luz vende empanadas a 2.500, cada una le cuesta 1.200 en ingredientes, y sus costos fijos son 600.000 al mes. ¿Cuál es su margen por empanada y su punto de equilibrio? Si trabaja 26 días al mes, ¿cuántas empanadas diarias son?
    - Margen: 2.500 − 1.200 = **1.300**.
    - Punto de equilibrio: 600.000 ÷ 1.300 ≈ 461,5 → **462 empanadas al mes**.
    - Por día: 462 ÷ 26 ≈ **18 empanadas**.
2. **(Resuelto)** Si Luz vende 100 empanadas al día durante 26 días y trabaja 10 horas diarias, ¿cuánto gana al mes y por hora?
    - Unidades: 100 × 26 = 2.600.
    - Ganancia: 2.600 × 1.300 − 600.000 = **2.780.000** al mes.
    - Horas: 10 × 26 = 260 → 2.780.000 ÷ 260 ≈ **10.692 por hora**.
3. Luz sube el precio a 3.000 y vende 80 al día durante 26 días. Calcula su nuevo margen y su ganancia mensual. ¿Le convino el cambio?
4. Calcula el margen como porcentaje del precio en los dos casos (2.500 y 3.000). ¿Qué te dice ese porcentaje?
5. Doña Marta vende 2.000.000 en huevos al mes a una tienda que paga a 30 días, pero paga 500.000 cada semana de concentrado. Explica qué problema de flujo de caja puede tener en su primer mes y propón dos soluciones.
6. Pedro tiene 5.000.000 ahorrados y quiere comprar un horno para vender pan. Propón una forma de **probar** si hay clientes antes de comprar el horno.
7. Un negocio tiene costos fijos de 1.200.000 al mes y un margen de 4.000 por unidad. ¿Cuál es el punto de equilibrio? Si su capacidad máxima es de 250 unidades al mes, ¿es viable? ¿Qué podría cambiar?
8. Diseña la tabla de números básicos de un negocio que te gustaría tener: precio, costo variable, margen, costos fijos, punto de equilibrio y una meta de ventas. Explica de dónde sacaste cada número.

<details>
<summary>Soluciones</summary>

3. Margen: 3.000 − 1.200 = **1.800**. Unidades: 80 × 26 = 2.080. Ganancia: 2.080 × 1.800 − 600.000 = **3.144.000**. Le convino: gana 364.000 más que antes (2.780.000), vendiendo menos.
4. Con 2.500: 1.300 ÷ 2.500 = **52 %**. Con 3.000: 1.800 ÷ 3.000 = **60 %**. Un margen mayor significa que cada venta aporta más para cubrir los costos fijos; pequeños cambios de precio pueden mover mucho la ganancia.
5. En el primer mes paga unos 2.000.000 de concentrado (4 semanas × 500.000) antes de recibir el pago de la tienda: puede quedarse sin efectivo aunque el negocio sea rentable. Soluciones: pedir un anticipo a la tienda, negociar pago a 15 días, tener un colchón para el primer mes, o vender una parte de contado a otros clientes.
6. Ejemplos: hornear en pequeño con un horno prestado o alquilado y vender a vecinos durante unas semanas; tomar pedidos por adelantado; preguntar a tiendas si comprarían y a qué precio. La idea es comprobar que hay demanda **antes** de invertir los 5.000.000.
7. Punto de equilibrio: 1.200.000 ÷ 4.000 = **300 unidades** al mes. Con capacidad de 250 **no es viable**: aunque venda todo lo que puede producir, pierde. Puede subir el precio, bajar el costo variable, reducir costos fijos o aumentar la capacidad.
8. Respuesta abierta. Se evalúa que el margen y el punto de equilibrio estén bien calculados y que cada número tenga una fuente razonable (precios averiguados, cotizaciones, preguntas a negocios similares).

</details>

## Caso práctico (evidencia de dominio)

**Los números de un negocio real.**

1. Elige un negocio pequeño de tu barrio o vereda (una tienda, un puesto de comida, un taller) cuyo dueño acepte conversar contigo. Si no es posible, elige un negocio que te gustaría crear.
2. Con preguntas sencillas (sin pedir datos que el dueño no quiera dar), estima: precio de un producto típico, su costo variable, los costos fijos del mes y cuántas unidades vende.
3. Calcula el margen, el punto de equilibrio y una ganancia aproximada.
4. Propón **una mejora** al negocio basada en los números y explica cómo la probarías en pequeño.

**Entrega:** la tabla con los números (indicando cuáles son estimados), los cálculos y tu propuesta. No publiques información privada del negocio sin permiso.

**Se evalúa así:**

- Los cuatro números básicos están identificados o estimados con un criterio claro.
- El margen y el punto de equilibrio están bien calculados.
- La propuesta se apoya en los números.
- Incluye una forma concreta de probar la mejora antes de invertir.

## Errores comunes

- **Confundir ventas con ganancia.**
- **No contar tu propio tiempo.** Si no te pagas, el negocio parece mejor de lo que es.
- **Olvidar los costos fijos** cuando no vendes.
- **Invertir todo antes de probar** que hay clientes.
- **Ignorar el flujo de caja.** Vender a crédito sin tener con qué producir mientras te pagan.
- **Mezclar la plata del negocio con la de la casa.** Así nunca sabes si el negocio gana o pierde.

## Para el docente ancla

- **Tiempo:** dos sesiones de 45 a 60 minutos y dos semanas para el caso práctico.
- **Cómo abrir:** pregunta "¿cuánto gana Luz si vende 250.000 al día?" y deja que respondan antes de sacar la cuenta completa.
- **Para conversar:** ¿qué negocios de la comunidad han durado muchos años y por qué? ¿Qué se necesita, además de números, para emprender?
- **Cuidado:** muchos estudiantes vienen de familias con negocios pequeños o informales. Usa este nodo para valorar ese saber y darle herramientas, no para juzgarlo.
- **Adaptación local:** los requisitos para formalizar un negocio, los programas de apoyo a emprendedores y las opciones de crédito para pequeñas empresas van en el nodo local.
- **Cierre del módulo:** es un buen momento para un proyecto integrador que use varios nodos: el presupuesto, la meta de ahorro, el costo de un crédito y los números de un negocio.
