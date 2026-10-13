# Origen del proyecto

New Old School nació el 12 de octubre de 2026 en una sesión de trabajo entre Sergio Monsalve y Diego Fernando Robledo, como desprendimiento del grupo **Experiencias IA** y del espacio **Curioso**. Este documento recoge las ideas de esa sesión que orientan el proyecto, para que quien llegue después entienda el porqué de las decisiones.

## La pregunta de partida

¿Cuál es la diferencia entre un niño de un colegio privado de Medellín y uno de La Guajira que a veces no puede llegar a clase porque el río está crecido? El colegio da muchas cosas —convivencia, habilidades sociales— pero también **contexto y conocimiento**, y esa parte sí puede llegar por otros caminos. La IA hace factible algo que antes no lo era: producir, con voluntarios, contenido bien contado para cualquiera.

## Ideas que orientan el proyecto

### 1. Despertar curiosidad, no dictar clase

El problema ya no es el acceso al conocimiento, sino saber **qué** conocimiento importa para cada quien y **cómo** se cuenta. El objetivo de cada pieza es generar la emoción de querer saber más. Por eso los nodos siguen el formato de Curioso (ver abajo).

### 2. Narraciones, no "un señor hablando a cámara"

Producir cursos grabados cuesta mucho tiempo de filmación y edición. Con IA se puede producir **narración bien contada**: guion investigado y verificado, voces, ilustración tipo tablero, ejemplos. Diego ya viene construyendo un flujo de producción de narraciones con IA que sigue este ciclo:

```
investigación → validación por agentes "ciegos" → curaduría humana → guion
→ revisión del guion → narración por tomas → ensamble → revisión final
```

Es el mismo principio de calidad del motor de tareas de la plataforma: nada se publica sin verificación humana. La idea es convertirlo en un **motor de clases** reutilizable.

### 3. Transversalidad: el conocimiento conectado

La gran crítica al colegio tradicional: cada materia vive aislada. ¿Por qué se inventó el trinomio cuadrado perfecto, en qué época, qué problema resolvía y qué cambió después? Cada tema debería poder conectarse con su historia, su uso y otras áreas. Esto se traduce en los **hilos** y los **puentes académicos** del grafo.

### 4. Varios profesores para una misma clase

En una institución pagar a tres docentes por una clase es inviable; con IA y voluntarios no. Un tema puede contarse entre varios expertos (o varias "voces" con estilo propio, por ejemplo a la manera de un gran divulgador), siempre con un hilo planeado y un **docente ancla** para que no se vuelva un conversatorio. Ver `docs/vision.md`, modelo pedagógico.

### 5. Saberes de vida primero

La crítica más repetida al colegio: "¿y esto para qué me sirve?". Por eso el proyecto empieza por lo que casi nadie enseña: finanzas, primeros auxilios, derechos y trámites, salud mental, convivencia. La expresión **"saberes de vida"** resume bien esta línea. Como antecedente se mencionó la *Urbanidad de Carreño*: un texto sobre cómo convivir en sociedad que muchos recuerdan con cariño por cómo estaba contado.

### 6. Aprender haciendo

"Aprendo más haciendo que estudiando teoría." La experimentación es central: casos prácticos, evidencia de dominio y proyectos con cosas que se puedan tocar.

### 7. Usar los tokens para algo mejor

Hay una crítica creciente al gasto de energía de la IA en contenido trivial. La respuesta del proyecto: usar esa capacidad en una causa que importa —la educación básica— con un modelo de colaboración voluntaria al estilo de SETI@home o Wikipedia (ver ADR 0004).

## A quién le habla

La primera intuición fue la población rural sin acceso. La conclusión fue más amplia:

- **Personas curiosas** de cualquier edad, incluidas las rurales.
- **Docentes**, que pueden usar el contenido y la estructura como herramienta.
- **Autodidactas** que quieran cubrir lo que da el colegio. Meta medible propuesta: que alguien que estudie por su cuenta pueda presentar las **pruebas Saber** con buen resultado.

El canal principal serían las **redes sociales**, con colaboración entre creadores que se citan y se invitan entre sí, en lugar de competir.

## Cómo nos posicionamos

Si el proyecto funciona, el sistema tradicional podría verlo como amenaza. La postura del proyecto es la contraria: **ser aliado de los colegios**. Ofrecemos contenido y estructura abiertos; los colegios aportan lo que nosotros no podemos dar, el acompañamiento humano directo.

## Ideas para explorar después

- **Waldorf** y otras pedagogías alternativas como complemento a la tradicional.
- **Dinero como narrativa**: la historia del dinero, cómo funcionan las finanzas del mundo y sus alternativas, como un canal de contenido.
- **Contenido ramificable**: una pieza corta que genera reacciones, pedidos de ampliación y otras versiones.
- **Investigaciones colaterales**: ¿qué recuerda la gente del colegio y qué le sirvió de verdad?
- **Alianzas** con empresas y entidades públicas para pilotos.

## Documentos relacionados

[Visión](vision.md) · [Marco curricular](marco-curricular.md) · [Plantilla de nodo](plantillas/nodo.md) · [Decisiones](decisiones/)
