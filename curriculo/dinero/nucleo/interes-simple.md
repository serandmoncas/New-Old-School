---
id: dinero.interes-simple
titulo: Interés simple
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 2
prerrequisitos: [dinero.porcentajes-en-la-vida-real]
conecta_con: [matematicas.funciones-lineales]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión}
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: 'verificación de evidencias con fuentes primarias (Issue #10); correcciones de precisión'}
recursos:
- {titulo: Código de Hammurabi, url: 'https://es.wikipedia.org/wiki/C%C3%B3digo_de_Hammurabi', licencia: CC BY-SA 4.0}
- {titulo: Usura, url: 'https://es.wikipedia.org/wiki/Usura', licencia: CC BY-SA 4.0}
- {titulo: 'Information Disclosure, Cognitive Biases, and Payday Borrowing (Bertrand y Morse, 2011)', url: 'https://www.povertyactionlab.org/evaluation/information-disclosure-cognitive-biases-and-payday-borrowing-united-states', licencia: referencia}
actualizado: '2026-10-13'
---

# Interés simple

<!--
Moneda genérica ("pesos"), cifras redondas. Las tasas máximas legales (usura) y las entidades
que las fijan son de cada país: van en una adaptación local.
Tono: no se demoniza el crédito; se enseña a medir su costo.
-->

## El gancho (≈ 30 s)

Andrés necesita 100.000 pesos con urgencia. Un prestamista del barrio se los da sin papeles ni preguntas: solo tiene que devolver 6.000 pesos diarios durante 20 días.

Parece poco: 6.000 al día. Pero 6.000 × 20 = 120.000. Pagó 20.000 de más en menos de un mes. Si ese ritmo siguiera un año entero, el interés sería de **más del 300 %**.

Lo que parece barato cuando se dice "por día" puede ser carísimo cuando se mira completo. Hoy vas a aprender a mirarlo completo.

## La idea (≈ 90 s)

El **interés** es el precio de usar dinero ajeno. Si te prestan, pagas interés. Si tú prestas o guardas tu plata en una cuenta, te pagan interés.

Para calcularlo necesitas tres datos:

- **Capital (C):** cuánto te prestan o cuánto guardas.
- **Tasa (r):** qué porcentaje cobran o pagan **por cada periodo** (por mes, por año).
- **Tiempo (t):** cuántos periodos pasan.

En el **interés simple**, el interés se calcula siempre sobre el capital inicial:

> **Interés = C × r × t**

Si te prestan 500.000 al 2 % mensual durante 6 meses: 500.000 × 0,02 × 6 = 60.000 de interés. Devuelves 560.000.

La regla de oro: **compara tasas en el mismo periodo**. Un 2 % mensual parece menor que un 20 % anual, pero en un año el 2 % mensual da 24 %. Y pregunta siempre **cuánto vas a pagar en total**, en pesos, no solo la cuota.

## La evidencia (≈ 60 s)

**Es muy antiguo**: el Código de Hammurabi, escrito en Babilonia hace unos 3.700 años, ya ponía un límite a los intereses que se podían cobrar por préstamos de grano y de plata. Desde entonces, muchos países tienen una **tasa máxima legal**, y cobrar por encima de ella se llama **usura**.

**Está comprobado** que la forma de mostrar el costo cambia la decisión. En un estudio en Estados Unidos con préstamos de corto plazo, a algunos clientes les mostraron cuánto pagarían en dinero si mantenían el préstamo semanas o meses, en lugar de mostrarles solo la tasa. Esos clientes volvieron a pedir prestado cerca de un 11 % menos de veces, y pidieron casi una cuarta parte menos de dinero.

**Lo que se dice, pero no es tan simple**: "si la cuota es baja, el préstamo es barato". Una cuota baja durante mucho tiempo puede costar más que una alta durante poco. Y hay costos que no aparecen en la tasa: seguros, comisiones, papeleo.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, Andrés compara antes de pedir. El prestamista del barrio le cobra 20.000 por 100.000 en 20 días. Una cooperativa le presta al 2 % mensual: en un mes pagaría 2.000. Tarda más en conseguirlo, pero cuesta diez veces menos. Y no corre el riesgo de que lo presionen o lo amenacen si se atrasa, algo frecuente con los préstamos informales de cobro diario.

En el campo, Don Jairo pide 2.000.000 para la siembra, al 1,5 % mensual por 6 meses. El interés es 2.000.000 × 0,015 × 6 = 180.000. Si espera vender la cosecha en 3.000.000, después de pagar el préstamo le quedan 820.000. Aquí el crédito no es malo: le permite producir. La clave es saber cuánto cuesta **antes** de firmar.

## La puerta abierta (≈ 30 s)

Para conversar: **¿por qué una persona aceptaría un préstamo carísimo, sabiendo que lo es?** ¿Qué tendría que existir para que no le tocara?

El siguiente nodo es **Interés compuesto**: qué pasa cuando el interés empieza a ganar (o a cobrar) interés. Es la idea más poderosa de este módulo.

---

## Puente académico

El interés simple es una **función lineal**. Si llamas *M* al dinero total después de *t* periodos:

> **M(t) = C + C × r × t**

La gráfica es una **línea recta**: empieza en el capital *C* y sube siempre lo mismo en cada periodo. Esa subida constante es la **pendiente**, y vale *C × r*. Cuando veas Interés compuesto, la gráfica dejará de ser recta y se curvará hacia arriba: esa curva es la diferencia entre los dos tipos de interés.

Un poco de historia: la palabra **interés** viene del latín *interesse*, "estar entre". En la Edad Media se usaba para la compensación que se debía a alguien por el daño de no tener su dinero a tiempo. Durante siglos, muchas religiones prohibieron o limitaron cobrar intereses, y por eso hubo tantas formas de nombrarlos y disfrazarlos.

## Ejercicios

1. **(Resuelto)** Te prestan 500.000 pesos al 2 % mensual de interés simple durante 6 meses. ¿Cuánto pagas de interés y cuánto devuelves en total?
    - Interés: 500.000 × 0,02 × 6 = **60.000**
    - Total: 500.000 + 60.000 = **560.000**
2. **(Resuelto)** Un prestamista te da 100.000 y le devuelves 120.000 en 20 días. ¿Qué tasa cobra en esos 20 días? ¿Y por día? Si cobrara así todo un año de 365 días, ¿qué tasa simple sería?
    - Interés: 20.000 de 100.000 → **20 % en 20 días**.
    - Por día: 20 % ÷ 20 = **1 % diario**.
    - En un año: 1 % × 365 = **365 % anual**.
3. Guardas 1.000.000 de pesos en una cuenta que paga 4 % anual de interés simple. ¿Cuánto interés ganas en 3 años?
4. Una tienda ofrece crédito al 3 % mensual. ¿A qué tasa anual simple equivale?
5. Necesitas 1.000.000 por un año. Opción A: 2 % mensual. Opción B: 20 % anual. Ambas de interés simple. ¿Cuánto pagas de interés en cada una? ¿Cuál conviene?
6. Pediste 800.000 prestados y después de 5 meses devolviste 920.000. ¿Qué tasa mensual de interés simple te cobraron?
7. Don Jairo pide 2.000.000 al 1,5 % mensual por 6 meses. ¿Cuánto debe pagar en total? Si vende su cosecha en 3.000.000, ¿cuánto le queda después de pagar el préstamo?
8. Ahorras 200.000 al 5 % mensual de interés simple (una tasa alta, solo para practicar). Haz una tabla del dinero total en los meses 0, 1, 2, 3 y 4, y dibuja la gráfica. ¿Qué forma tiene? ¿Cuál es la pendiente?

<details>
<summary>Soluciones</summary>

3. 1.000.000 × 0,04 × 3 = **120.000**.
4. 3 % × 12 = **36 % anual**.
5. A: 1.000.000 × 0,02 × 12 = **240.000**. B: 1.000.000 × 0,20 × 1 = **200.000**. Conviene **B**, aunque "2 %" suene a menos que "20 %": hay que comparar en el mismo periodo.
6. Interés: 920.000 − 800.000 = 120.000. Tasa: 120.000 ÷ (800.000 × 5) = 0,03 → **3 % mensual**.
7. Interés: 2.000.000 × 0,015 × 6 = 180.000. Total a pagar: **2.180.000**. Le quedan 3.000.000 − 2.180.000 = **820.000**.
8. M(t) = 200.000 + 200.000 × 0,05 × t = 200.000 + 10.000 × t. Mes 0: 200.000; mes 1: 210.000; mes 2: 220.000; mes 3: 230.000; mes 4: **240.000**. Es una **línea recta** con pendiente de **10.000 pesos por mes**.

</details>

## Caso práctico (evidencia de dominio)

**Detective de préstamos.**

1. Encuentra **dos ofertas reales de crédito**: un anuncio de una tienda, una publicidad de un banco o cooperativa, un préstamo por aplicación, o pregunta a un adulto de confianza por una que conozca.
2. Para cada una, escribe: capital, tasa, periodo de la tasa, plazo y costos extra (si los dice).
3. Calcula con interés simple **cuánto se pagaría en total** por un mismo monto (por ejemplo, 500.000 pesos a 6 meses).
4. Escribe cuál elegirías y por qué, y qué información le faltaba al anuncio para decidir bien.

**Entrega:** la tabla con las dos ofertas, tus cálculos y tu conclusión. No incluyas datos personales de nadie.

**Se evalúa así:**

- Las ofertas son reales y su origen está identificado.
- Las tasas se comparan en el mismo periodo.
- El total a pagar está bien calculado.
- La conclusión menciona información que faltaba en la oferta.

*Nota: los créditos reales suelen usar interés compuesto y costos adicionales, así que el total verdadero puede ser mayor. Este cálculo es una primera aproximación.*

## Errores comunes

- **Comparar tasas de periodos distintos.** 2 % mensual no es menor que 20 % anual.
- **Mirar solo la cuota.** Lo que importa es cuánto pagas en total.
- **Olvidar los costos extra.** Seguros, comisiones y papeleo también son parte del precio.
- **Creer que todo crédito es malo.** Un préstamo para producir o para algo necesario puede valer la pena si su costo es razonable.
- **Confiar en préstamos "sin papeles"**. Lo fácil de conseguir suele ser lo más caro y lo más riesgoso.

## Para el docente ancla

- **Tiempo:** una sesión de 45 a 60 minutos y una semana para el detective de préstamos.
- **Cómo abrir:** presenta la oferta del prestamista ("solo 6.000 diarios") y pregunta si es barata o cara antes de hacer la cuenta.
- **Para conversar:** ¿por qué existen los préstamos informales de cobro diario? ¿Qué alternativas hay en la comunidad?
- **Cuidado:** puede haber familias del grupo que usan o han usado préstamos informales. Habla de los préstamos y sus costos, nunca de las personas que los toman. Si un estudiante cuenta una situación de amenaza o presión por deudas, remítelo a un adulto responsable o a la orientación escolar.
- **Adaptación local:** la tasa máxima legal (usura), quién la fija y a dónde denunciar préstamos abusivos van en el nodo local.
- **Siguiente nodo:** Interés compuesto.
