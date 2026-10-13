---
id: dinero.historial-crediticio
titulo: Historial crediticio
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 2
prerrequisitos: [dinero.deuda-buena-y-mala]
conecta_con: [sociales.instituciones]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión; cuotas verificadas con script}
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: 'verificación de evidencias con fuentes primarias (Issue #10); correcciones de precisión'}
recursos:
- {titulo: Historial crediticio, url: 'https://en.wikipedia.org/wiki/Credit_history', licencia: CC BY-SA 4.0}
- {titulo: Grameen Bank y el microcrédito, url: 'https://es.wikipedia.org/wiki/Grameen_Bank', licencia: CC BY-SA 4.0}
- {titulo: 'FTC: estudio sobre errores en reportes de crédito (2013)', url: 'https://www.ftc.gov/news-events/news/press-releases/2013/02/ftc-study-five-percent-consumers-had-errors-their-credit-reports-could-result-less-favorable-terms', licencia: referencia}
- {titulo: 'Private Credit in 129 Countries (Djankov, McLiesh y Shleifer, 2007)', url: 'https://shleifer.scholars.harvard.edu/publications/private-credit-129-countries', licencia: referencia}
actualizado: '2026-10-13'
---

# Historial crediticio

<!--
Núcleo: no se nombran centrales de riesgo ni leyes. Cuáles existen en el país, cómo se consulta
el reporte gratis, cuánto dura un reporte negativo y la ley de protección de datos van en la
adaptación local (este nodo está en requieren_local). Moneda genérica ("pesos").
-->

## El gancho (≈ 30 s)

El banco no sabe quién eres. No conoce tu cara, ni tu familia, ni si eres buena persona.

Pero sabe si pagaste a tiempo la cuota del celular hace tres años. Y si te atrasaste con una tarjeta. Y cuánto debes hoy.

Dos hermanos piden el mismo préstamo de 5.000.000. A uno se lo aprueban al 1,5 % mensual. Al otro, al 2,3 %. En tres años, el segundo paga casi **900.000 pesos más**. La diferencia no está en cuánto ganan: está en su **historial**.

## La idea (≈ 90 s)

El **historial crediticio** es el registro de cómo has manejado tus deudas: si pagaste a tiempo, si te atrasaste, cuánto debes y desde cuándo tienes créditos. Lo guardan empresas especializadas, que en muchos países se llaman **centrales de riesgo** o burós de crédito, vigiladas por el Estado.

Con esa información, muchas entidades calculan un **puntaje**: un número que resume qué tan probable es que pagues. Ese número decide si te prestan, **a qué tasa**, y a veces influye en si te arriendan un apartamento.

Lo que **ayuda**:

- Pagar siempre a tiempo, aunque sea el valor exacto de la cuota.
- No usar todo el cupo: una guía común es no pasar del 30 % de lo disponible.
- Tener créditos antiguos bien manejados.

Lo que **perjudica**:

- Los atrasos (la **mora**), sobre todo los largos.
- Las deudas que llegan a cobro.
- Pedir muchos créditos al mismo tiempo.

Y un derecho importante: en muchos países puedes **consultar tu propio reporte gratis** y pedir que corrijan los errores.

## La evidencia (≈ 60 s)

**Está comprobado** que compartir información de crédito ayuda a que más gente acceda a préstamos. Estudios con datos de muchos países encontraron que donde existen sistemas de información crediticia, los bancos prestan más al sector privado, y eso incluye a pequeñas empresas.

**También está comprobado** que los reportes tienen errores con frecuencia. Un estudio oficial en Estados Unidos, de 2013, encontró que **uno de cada cinco** consumidores tenía al menos un error en alguno de sus reportes. Por eso revisarlo vale la pena.

**Lo que se dice, pero no es cierto**: "si consulto mi propio historial, me baja el puntaje". En general, consultarlo tú mismo no te afecta. Y otro mito: "lo mejor es nunca pedir crédito". Sin historial, para el banco eres un desconocido, y eso también puede cerrarte puertas.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, Mariana se atrasó dos veces con su tarjeta. Cuando quiso un crédito para una moto, se lo aprobaron, pero a una tasa más alta. Ahora paga siempre puntual y usa poco de su cupo: en uno o dos años su historial va a mejorar. Kevin, en cambio, nunca ha tenido crédito. Para empezar su historial puede usar un producto pequeño, como un crédito de bajo monto, y pagarlo puntual.

En el campo, muchas personas no tienen historial formal, aunque llevan años cumpliendo sus compromisos. Por eso existen formas distintas de prestar. En Bangladés, el **Grameen Bank** prestaba a grupos de vecinos que se respaldaban entre sí: la confianza del grupo reemplazaba el historial. Su fundador, Muhammad Yunus, y el propio banco recibieron el Premio Nobel de la Paz en 2006. Las cooperativas de muchas veredas funcionan con una lógica parecida: te conocen.

Tu historial es tu reputación con el dinero. Se construye despacio y se daña rápido.

## La puerta abierta (≈ 30 s)

Para conversar: **¿es justo que una deuda vieja te siga afectando años después? ¿Cuánto tiempo crees que debería durar un reporte negativo?**

Con este nodo termina la ruta Deber. La siguiente es **Protegerse**, que empieza con **Seguros**.

---

## Puente académico

Las centrales de riesgo son **instituciones**: empresas privadas que guardan datos personales bajo reglas del Estado. Eso abre preguntas de ciudadanía: ¿quién puede ver tus datos?, ¿cómo los corriges?, ¿cuánto tiempo pueden guardarlos? Muchos países tienen leyes de **protección de datos** que responden estas preguntas.

El puntaje, además, es un modelo estadístico: usa el pasado de muchas personas para estimar la **probabilidad** de que alguien pague. Como todo modelo, puede equivocarse con personas que no se parecen a las del pasado.

Un poco de historia: en 1841, en Nueva York, un comerciante llamado Lewis Tappan creó una agencia que reunía información sobre la confiabilidad de los comerciantes para otros comerciantes. De esa idea nacieron los burós de crédito modernos. Y en 1989 apareció en Estados Unidos uno de los primeros puntajes de crédito usados de forma masiva.

## Ejercicios

1. **(Resuelto)** Clasifica cada comportamiento: ¿ayuda o perjudica al historial? (a) pagar la cuota cinco días tarde; (b) usar el 20 % del cupo y pagarlo completo; (c) pedir créditos en cinco tiendas la misma semana; (d) consultar tu propio reporte; (e) dejar que una deuda llegue a cobro.
    - (a) **Perjudica**: es un atraso. (b) **Ayuda**. (c) **Perjudica**: muchas solicitudes juntas parecen necesidad urgente. (d) **No afecta** en general. (e) **Perjudica mucho**.
2. **(Resuelto)** Mariana tiene un cupo de 1.500.000 y debe 900.000. ¿Qué porcentaje del cupo usa? ¿Cuánto debería deber como máximo para estar en el 30 %?
    - 900.000 ÷ 1.500.000 = 0,60 → usa el **60 %**.
    - 30 % de 1.500.000 = **450.000** como máximo.
3. Dos personas piden 5.000.000 a 36 meses con cuota fija. Una tiene buen historial y le cobran 1,5 % mensual; la otra, 2,3 % mensual. Las cuotas resultan de 180.762 y 205.739. ¿Cuánto paga cada una en total? ¿Cuánto le cuesta el mal historial a la segunda?
4. Kevin tiene 19 años y nunca ha tenido crédito. Propón tres pasos para empezar a construir un buen historial sin endeudarse de más.
5. Te llega este mensaje: *"Borramos tu reporte negativo de las centrales de riesgo en 48 horas. Solo pagas 200.000."* ¿Por qué es probablemente una estafa? ¿Qué harías en cambio?
6. Una persona tiene dos tarjetas: una con cupo de 1.000.000 y deuda de 600.000; otra con cupo de 2.000.000 y deuda de 300.000. ¿Qué porcentaje usa en cada tarjeta y en total? ¿Qué le recomendarías?
7. Una cuota de 200.000 se paga 15 días tarde. La entidad cobra interés de mora del 3 % mensual sobre la cuota y un cargo de cobranza de 20.000. ¿Cuánto cuesta el atraso en dinero? ¿Qué otro costo tiene que no se ve en el recibo?
8. Debate: ¿debería un historial crediticio poder usarse para decidir si contratar a alguien en un trabajo? Escribe un argumento a favor y uno en contra.

<details>
<summary>Soluciones</summary>

3. Primera: 180.762 × 36 ≈ **6.507.431**. Segunda: 205.739 × 36 ≈ **7.406.602**. El mal historial le cuesta unos **899.000 pesos** (casi 25.000 más en cada cuota).
4. Ejemplos: abrir un producto pequeño (un crédito de bajo monto o una tarjeta con cupo bajo) solo si lo puede pagar; usar poco cupo y pagar siempre el total y a tiempo; pagar puntualmente servicios o planes a su nombre cuando la entidad los reporte; consultar su reporte una vez al año. Se evalúa que los pasos sean responsables y no impliquen endeudarse de más.
5. Nadie puede borrar un reporte verdadero a cambio de dinero: los reportes negativos se eliminan cuando se paga y pasa el tiempo que fija la ley, o cuando son errores. Pedir pago por adelantado y prometer rapidez son señales típicas de estafa. Lo correcto: consultar el reporte gratis en la central de riesgo, y si hay un error, reclamar directamente a la entidad o a la central.
6. Primera: 600.000 ÷ 1.000.000 = **60 %**. Segunda: 300.000 ÷ 2.000.000 = **15 %**. Total: 900.000 ÷ 3.000.000 = **30 %**. Recomendación: priorizar bajar la deuda de la primera tarjeta, que está muy cargada, y no aumentar el uso total.
7. Interés de mora: 200.000 × 0,03 × 0,5 = 3.000. Más el cargo de cobranza: **23.000** en total. El costo oculto es el **reporte de atraso** en el historial, que puede encarecer créditos futuros.
8. Respuesta abierta. Se evalúa que presente un argumento razonable a cada lado (por ejemplo: a favor, muestra responsabilidad con compromisos; en contra, castiga a quien tuvo una emergencia y puede impedir justo el trabajo que le permitiría pagar).

</details>

## Caso práctico (evidencia de dominio)

**Guía para cuidar tu reputación financiera.**

1. Investiga, en fuentes oficiales de tu país, **cómo se consulta gratis** el historial crediticio, **cuánto tiempo** dura un reporte negativo y **a dónde se reclama** un error. *No consultes el historial de nadie más.*
2. Con eso y lo aprendido, diseña una **guía de una página** para un joven que va a tener su primer crédito: qué hacer, qué evitar y qué derechos tiene.
3. Incluye una advertencia sobre estafas relacionadas con el historial.

**Entrega:** la guía (en papel o digital) con las fuentes citadas.

**Se evalúa así:**

- La información del país es correcta y tiene fuente oficial.
- La guía incluye al menos tres hábitos que ayudan y tres que perjudican.
- Menciona el derecho a consultar y corregir.
- Incluye la advertencia sobre estafas.

## Errores comunes

- **Pensar que un atraso pequeño no importa.** Queda registrado.
- **Usar todo el cupo** aunque se pague: muestra dependencia del crédito.
- **Pedir crédito en muchos lugares a la vez** "para ver cuál aprueban".
- **Nunca revisar el propio reporte.** Los errores son frecuentes.
- **Pagar a quien promete "limpiar" el historial.** Es casi siempre una estafa.
- **Creer que no tener historial es lo mismo que tener uno bueno.**

## Para el docente ancla

- **Tiempo:** una sesión de 45 a 60 minutos y una semana para la guía.
- **Cómo abrir:** cuenta la historia de los dos hermanos y pregunta qué creen que hizo la diferencia antes de revelar que fue el historial.
- **Para conversar:** ¿es justo calificar a las personas con un número? ¿Qué pasa con quien nunca ha tenido acceso al crédito?
- **Cuidado:** no pidas a nadie que consulte o comparta su historial ni el de su familia. Algunas familias pueden tener reportes negativos por emergencias: habla del sistema, no de las personas.
- **Adaptación local:** las centrales de riesgo del país, cómo se consulta el reporte gratis, cuánto dura un reporte negativo y la ley de protección de datos van en el nodo local.
- **Siguiente ruta:** Protegerse, empezando por Seguros.
