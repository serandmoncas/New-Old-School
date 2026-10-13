---
id: dinero.seguros
titulo: Seguros
modulo: dinero
alcance: nucleo
pais: null
nodo_base: null
nivel: 2
prerrequisitos: [dinero.presupuesto]
conecta_con: [matematicas.probabilidad, pensar.decidir-con-riesgo]
estado: en-revision
responsable: serandmoncas
revisores: []
revision_experta: false
procedencia:
- {autor: claude, modelo: claude-opus-5-5, fecha: '2026-10-13', nota: primera versión}
recursos:
- {titulo: Ley de los grandes números, url: 'https://es.wikipedia.org/wiki/Ley_de_los_grandes_n%C3%BAmeros', licencia: CC BY-SA 4.0}
- {titulo: Lloyd's de Londres, url: 'https://en.wikipedia.org/wiki/Lloyd%27s_of_London', licencia: CC BY-SA 4.0}
actualizado: '2026-10-13'
---

# Seguros

<!--
Primer nodo de la ruta Protegerse. Núcleo: no se recomiendan aseguradoras ni pólizas concretas.
Los seguros obligatorios de cada país (por ejemplo, para vehículos) y los programas públicos
de seguro agrícola van en una adaptación local. Moneda genérica ("pesos").
-->

## El gancho (≈ 30 s)

En una vereda hay cien familias, y cada una tiene una vaca que vale 2.000.000 de pesos. Cada año, en promedio, se muere una vaca. Nadie sabe de quién será.

Para la familia que la pierde, es una tragedia. Para las demás, nada.

Un día deciden algo: cada familia pone 20.000 pesos al año en un fondo común. Con eso, quien pierda su vaca recibe otra. Nadie vuelve a perderlo todo.

Sin saberlo, acaban de inventar el **seguro**.

## La idea (≈ 90 s)

Un **seguro** es un trato: pagas una cantidad pequeña y segura (la **prima**) para protegerte de una pérdida grande e incierta. Funciona porque muchas personas juntan su riesgo: casi todas pagan y pocas cobran.

Las palabras que debes conocer:

- **Cobertura:** qué protege el seguro y hasta cuánto.
- **Deducible:** la parte de la pérdida que pagas tú antes de que pague el seguro.
- **Exclusiones:** lo que el seguro **no** cubre. Están en la letra pequeña y son las que más sorpresas dan.
- **Siniestro:** el evento que activa el seguro (el robo, el accidente, la sequía).

¿Cuándo vale la pena? La regla es sencilla: **asegura lo que no podrías pagar si se pierde**. Una casa, la salud, lo que te da de comer, una deuda que quedaría pendiente. Lo pequeño (unos audífonos, un celular barato) es mejor cubrirlo con tu fondo de emergencias.

Y una verdad incómoda: en promedio, las aseguradoras cobran más de lo que pagan; así ganan. Comprar un seguro no es "ganar plata". Es pagar para que una mala suerte no te arruine.

## La evidencia (≈ 60 s)

**Está comprobado** que el seguro funciona por una ley matemática: la **ley de los grandes números**. Nadie sabe qué vaca se va a morir, pero con muchas vacas se puede predecir con bastante precisión **cuántas** se mueren en total. Por eso la aseguradora puede calcular la prima.

**También hay evidencia** de que el seguro cambia decisiones. En un experimento en Ghana, publicado en 2014, los agricultores que recibieron un seguro contra la falta de lluvia invirtieron más en sus cultivos. Sin el miedo a perderlo todo, se arriesgaron a producir más.

**Lo que se dice, pero no es tan simple**: "pagué el seguro y no me pasó nada: perdí la plata". No la perdiste: compraste tranquilidad durante ese tiempo, como la familia que puso 20.000 y no perdió su vaca. Y lo contrario: "todo hay que asegurarlo". Muchos seguros pequeños, como algunas garantías extendidas, cuestan más de lo que en promedio devuelven.

## ¿Y a mí qué? (≈ 60 s)

En la ciudad, Juan todavía debe la moto con la que trabaja. Si se la roban, pierde su ingreso y sigue debiendo. Ese es justo el tipo de pérdida que no podría pagar: un seguro contra robo tiene sentido, aunque cueste. En cambio, cuando la tienda le ofrece una "garantía extendida" para unos audífonos, la rechaza: si se dañan, los repone con su ahorro.

En el campo, existe un tipo de seguro pensado para los agricultores: el **seguro paramétrico**. No hace falta que un inspector visite la finca. Si una estación del clima mide que llovió menos de cierta cantidad, el seguro paga automáticamente. Es rápido y barato, aunque tiene un riesgo: puede que en la estación llueva bien y en tu finca no.

Antes de existir los seguros, las comunidades ya se protegían entre sí: con colectas, con trabajo compartido, con fondos de vecinos. El seguro moderno es esa misma idea, con matemáticas.

## La puerta abierta (≈ 30 s)

Para conversar: **¿cómo se ayuda tu comunidad cuando a una familia le pasa una desgracia?** ¿En qué se parece eso a un seguro, y en qué no?

El siguiente nodo es **Estafas y pirámides**: cuando alguien te promete protección o ganancias que son demasiado buenas para ser verdad.

---

## Puente académico

Para decidir si un seguro conviene se usa la **probabilidad**. La **pérdida esperada** es la probabilidad de que pase algo multiplicada por lo que perderías. Si un riesgo tiene 2 % de probabilidad y te costaría 6.000.000, la pérdida esperada es 120.000 al año. Casi siempre la prima es mayor que la pérdida esperada. Aun así, el seguro puede ser una buena decisión, porque **no es lo mismo perder 120.000 seguros que arriesgarte a perder 6.000.000 de golpe**. Esa diferencia entre el promedio y el peor caso es lo que se aprende en decidir con riesgo.

Un poco de historia: a finales del siglo XVII, en Londres, los comerciantes y dueños de barcos se reunían en el café de Edward Lloyd. Allí se repartían el riesgo de los viajes por mar: si un barco se hundía, la pérdida la cubrían entre muchos. De ese café nació una de las instituciones de seguros más conocidas del mundo, que todavía lleva su nombre.

## Ejercicios

1. **(Resuelto)** Cien familias tienen una vaca de 2.000.000 cada una, y en promedio muere una vaca al año. ¿Cuánto debe aportar cada familia para reponerla? Si además hay que pagar a una persona que administre el fondo (un 20 % adicional), ¿cuánto aporta cada una?
    - 2.000.000 ÷ 100 = **20.000** por familia.
    - Con 20 % de administración: 20.000 × 1,20 = **24.000**.
2. **(Resuelto)** La moto de Juan vale 6.000.000. La probabilidad de robo en un año es del 2 %. El seguro cuesta 300.000 al año y tiene un deducible del 10 %. ¿Cuál es la pérdida esperada sin seguro? Si se la roban, ¿cuánto paga el seguro? ¿Le conviene?
    - Pérdida esperada: 0,02 × 6.000.000 = **120.000** al año.
    - Si se la roban, el seguro paga 6.000.000 − 10 % = **5.400.000**.
    - La prima (300.000) es mayor que la pérdida esperada, pero Juan **no podría pagar** una pérdida de 6.000.000 y además seguir debiendo la moto. **Le conviene.**
3. Un carro asegurado tiene un daño de 800.000 y el deducible es de 300.000. ¿Cuánto paga el seguro y cuánto paga el dueño?
4. Un celular de 1.000.000 tiene una garantía extendida de un año que cuesta 150.000. La probabilidad de que falle ese año es del 5 % y repararlo costaría 400.000. ¿Cuál es el costo esperado de la falla? ¿Conviene la garantía?
5. ¿Cuáles de estos riesgos asegurarías y cuáles cubrirías con tu fondo de emergencias? Justifica: (a) que se queme la casa; (b) que se dañen unos audífonos; (c) una enfermedad grave; (d) que se pierda un paraguas; (e) que muera quien mantiene a la familia.
6. Un seguro paramétrico paga 1.000.000 si en la temporada llueve menos de cierta cantidad. Eso pasa, en promedio, 1 de cada 20 años. ¿Cuál es el pago esperado por año? Si la prima es de 60.000, ¿es razonable? ¿Qué riesgo tiene para el agricultor?
7. Lee esta exclusión: *"No se cubren daños causados por inundaciones en zonas declaradas de alto riesgo."* Si tu casa está cerca de un río, ¿qué deberías preguntar antes de comprar el seguro?
8. Compara la solidaridad de una comunidad (una colecta cuando alguien tiene una desgracia) con un seguro formal. Escribe dos ventajas de cada uno.

<details>
<summary>Soluciones</summary>

3. El seguro paga 800.000 − 300.000 = **500.000**; el dueño paga los **300.000** del deducible.
4. Costo esperado: 0,05 × 400.000 = **20.000**. La garantía cuesta 150.000: **no conviene** en promedio. Es mejor cubrir ese riesgo con el fondo de emergencias.
5. Asegurar: (a) la casa, (c) la salud y (e) la vida de quien mantiene a la familia, porque son pérdidas que no se podrían pagar. Fondo de emergencias: (b) los audífonos y (d) el paraguas, porque son pérdidas pequeñas.
6. Pago esperado: 1.000.000 ÷ 20 = **50.000** por año. Una prima de 60.000 es razonable (un poco mayor que el pago esperado, como casi todos los seguros). El riesgo para el agricultor es que la estación mida suficiente lluvia mientras en su finca hay sequía: se queda sin pago aunque pierda la cosecha.
7. Preguntas posibles: ¿mi zona está declarada de alto riesgo? ¿Quién lo determina y dónde lo consulto? ¿Hay otra póliza que sí cubra inundaciones? ¿Qué otras exclusiones tiene?
8. Comunidad: es cercana y flexible, y no cobra para ganar. Seguro formal: paga aunque la comunidad no tenga dinero ese año, y el monto es conocido y está garantizado por contrato. (Otras respuestas son válidas si están justificadas.)

</details>

## Caso práctico (evidencia de dominio)

**El mapa de riesgos de un hogar (simulación).**

1. Imagina un hogar (inventado o el de un personaje del módulo, como Juan o Doña Marta) y haz una lista de **seis riesgos** que podría enfrentar.
2. Para cada uno estima: ¿qué tan probable es? (alto, medio, bajo) y ¿cuánto costaría si pasara? (alto, medio, bajo).
3. Decide para cada riesgo: **asegurar**, **cubrir con ahorro**, **prevenir** (reducir la probabilidad) o **aceptar**.
4. Para uno de los riesgos que decidiste asegurar, investiga una póliza real: prima, cobertura, deducible y al menos dos exclusiones.

**Entrega:** la tabla de riesgos con tus decisiones y la ficha de la póliza investigada, con su fuente. *No se compra ningún seguro.*

**Se evalúa así:**

- Hay seis riesgos con probabilidad y costo estimados.
- Las decisiones siguen la regla: asegurar lo que no se podría pagar.
- La póliza investigada es real y la ficha incluye exclusiones.
- Hay al menos una medida de prevención, no solo de seguro.

## Errores comunes

- **No leer las exclusiones.** Es donde están las sorpresas.
- **Asegurar lo pequeño y dejar sin asegurar lo grande.**
- **Creer que el seguro es plata perdida** si no pasa nada.
- **Olvidar el deducible** al calcular cuánto te van a pagar.
- **Comprar seguros "de paquete"** con un crédito o un producto sin saber qué cubren ni cuánto cuestan.
- **Dejar de pagar la prima** y perder la cobertura justo cuando más se necesita.

## Para el docente ancla

- **Tiempo:** una sesión de 45 a 60 minutos y una semana para el mapa de riesgos.
- **Cómo abrir:** cuenta la historia de las cien vacas, o juégala: cada estudiante recibe un papel, uno de ellos está marcado como "pérdida", y el grupo decide si arma un fondo común antes de revelar a quién le tocó.
- **Para conversar:** ¿por qué hay gente que nunca compra seguros? ¿Qué formas tiene tu comunidad de protegerse?
- **Cuidado:** no recomiendes aseguradoras ni pólizas. Algunos estudiantes pueden haber vivido pérdidas recientes (enfermedades, desastres): trata los ejemplos con delicadeza.
- **Adaptación local:** los seguros obligatorios del país, los programas públicos de seguro agrícola y dónde reclamar si una aseguradora no paga van en el nodo local.
- **Siguiente nodo:** Estafas y pirámides.
