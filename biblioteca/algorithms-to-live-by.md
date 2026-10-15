---
id: algorithms-to-live-by
titulo: Algoritmos para la vida cotidiana
titulo_original: 'Algorithms to Live By: The Computer Science of Human Decisions'
autor: Brian Christian y Tom Griffiths
publicado: '2016'
tipo: divulgacion
acceso: con-derechos
texto_libre: null
temas: [decisiones, matematicas, memoria]
cruza_con:
- {libro: pensar-rapido-pensar-despacio, por: 'Kahneman muestra cuánto nos equivocamos; Christian y Griffiths, que muchas veces decidimos razonablemente bien con lo poco que sabemos.'}
- {libro: deep-work, por: 'Saltar de una tarea a otra tiene un costo: Newport lo llama residuo de atención; los informáticos, thrashing.'}
- {libro: moonwalking-with-einstein, por: 'Foer entrena la memoria para recordar más; Christian y Griffiths explican por qué olvidar también es útil.'}
nodos: []
estado: propuesta
procedencia:
- {autor: serandmoncas, modelo: claude-opus-5-5, fecha: 2026-10-14}
actualizado: 2026-10-14
---

# Algoritmos para la vida cotidiana

## De qué trata

Un escritor, Brian Christian, y un científico cognitivo de Princeton, Tom Griffiths, toman problemas que la informática ya resolvió para las computadoras y los aplican a decisiones de todos los días: cuándo dejar de buscar, cómo ordenar el escritorio, qué olvidar, cómo organizar las tareas. Lo publicó Henry Holt en 2016; en español lo publicó Teell en 2017 (*Algoritmos para la vida cotidiana: la ciencia de la informática aplicada a las decisiones humanas*, traducción de Isabel Moros y Cristina Alcoya).

## Resumen

Una introducción, once capítulos y una conclusión:

1. **Parada óptima: cuándo dejar de buscar.** Si hay que elegir entre opciones que llegan una por una y no se puede volver atrás (un apartamento, por ejemplo), conviene mirar el primer 37 % sin elegir y luego quedarse con la primera opción mejor que todas las anteriores.
2. **Explorar o explotar.** ¿Probar un restaurante nuevo o volver al de siempre? Depende de cuánto tiempo queda para disfrutar lo que se descubra.
3. **Ordenar.** Ordenar cuesta, y a veces es mejor no ordenar y simplemente buscar.
4. **La caché: olvídalo.** Guardar a mano lo que se usó hace poco. Por eso una pila de papeles con lo más reciente encima funciona mejor de lo que parece.
5. **Planificar: lo primero es lo primero.** Cómo ordenar las tareas, y el costo de cambiar de una a otra todo el tiempo.
6. **La regla de Bayes: predecir el futuro.** Cómo hacer buenas predicciones con poca información.
7. **Sobreajuste: cuándo pensar menos.** Por qué un plan demasiado detallado puede ser peor que uno sencillo.
8. **Relajación: déjalo pasar.** Resolver primero una versión más fácil del problema.
9. **Aleatoriedad: cuándo dejarlo al azar.**
10. **Redes: cómo nos conectamos.**
11. **Teoría de juegos: la mente de los otros.**
- **Conclusión: amabilidad computacional.** Hacerles fácil a los otros las decisiones; por ejemplo, proponer una hora concreta para verse en vez de decir "cuando quieras".

La tesis: **muchos problemas de la vida diaria tienen la misma forma que problemas que la informática ya estudió, y sus soluciones sirven para decidir mejor, o al menos con más calma.**

## Por qué está en la biblioteca

Es el puente más claro entre el pensamiento computacional y la vida cotidiana. Un estudiante de 13 años entiende qué es un algoritmo cuando lo usa para decidir algo suyo, como cuándo dejar de buscar o cómo organizar sus tareas.

## Análisis

**Lo que hace bien.**

- **Detrás de varias de sus ideas hay investigación seria:**
  - La memoria parece adaptada al mundo: la probabilidad de que necesitemos un recuerdo depende de cuántas veces y qué tan recientemente lo usamos, igual que en el entorno ([Anderson y Schooler, 1991](https://doi.org/10.1111/j.1467-9280.1991.tb00174.x)). Olvidar lo que no se usa no es una falla.
  - Cuando se le pide a la gente predecir cosas cotidianas, como cuánto vivirá alguien o cuánto recaudará una película, sus predicciones se acercan mucho a las que daría un cálculo estadístico óptimo ([Griffiths y Tenenbaum, 2006](https://doi.org/10.1111/j.1467-9280.2006.01780.x)). Griffiths es coautor del libro.
  - El índice de Gittins, con el que se resuelve el dilema de explorar o explotar en ciertos casos, salió de un artículo de estadística ([Gittins, 1979](https://doi.org/10.1111/j.2517-6161.1979.tb01068.x)).
- **Da una mirada amable sobre los errores.** A diferencia de los libros de sesgos, dice que muchas veces decidimos razonablemente bien dado lo difícil del problema.
- **Enseña conceptos de verdad:** búsqueda, ordenamiento, caché, probabilidad. No es solo una colección de trucos.

**Sus límites.**

- **La vida real casi nunca cumple las condiciones de los algoritmos.** La regla del 37 % supone que se sabe cuántas opciones habrá, que no se puede volver atrás y que la opción elegida siempre acepta. El libro trata algunas variantes, pero varios lectores críticos opinan que aplicarlo a decisiones como elegir pareja es forzado.
- **En los experimentos, la gente no sigue la regla.** Las personas tienden a detener la búsqueda antes de lo óptimo ([Seale y Rapoport, 2000](https://doi.org/10.1002/1099-0771(200010/12)13:4<391::AID-BDM359>3.0.CO;2-I)). Eso puede ser un error, o puede ser que buscar también cuesta.
- **Es denso en algunas partes** y supone algo de gusto por los números.
- **La traducción al español ha recibido quejas de lectores;** conviene revisarla antes de recomendarla a estudiantes.

**Para el colegio.** Es la mejor lectura de fondo para el frente de pensamiento computacional. Los capítulos 1, 3 y 4 se pueden convertir en actividades con cartas, filas y cajones. Se cruza con *Pensar rápido, pensar despacio* (dos miradas sobre cómo decidimos) y con *Enfócate* (el costo de saltar de tarea en tarea).

## Para leer en clase

El capítulo 1, sobre la parada óptima. Actividad: cada grupo baraja 20 cartas con números al azar, las voltea una por una y debe quedarse con una, sin poder volver atrás. Cada grupo prueba una estrategia distinta (mirar 2, 4, 7 o 10 cartas antes de elegir) durante 20 rondas, y el curso junta los resultados para ver cuál acierta más a menudo con la carta más alta. Pregunta para conversar: ¿en qué decisiones de tu vida no se puede volver atrás, y en cuáles sí?

## Con cuidado

- Los ejemplos de elegir pareja o casa son de adultos; con los estudiantes funcionan mejor ejemplos como escoger un puesto en la fila o un producto en la tienda.
- Tiene derechos de autor.
