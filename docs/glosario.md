# Glosario

Vocabulario común del proyecto. Si una palabra se usa distinto en un PR o una discusión, se corrige aquí primero.

| Término | Significado en este proyecto |
| --- | --- |
| **Módulo** | Uno de los frentes del currículo (por ejemplo `dinero`). Es una carpeta en `curriculo/`. |
| **Nodo** | Un concepto enseñable en una o dos sesiones (por ejemplo "interés compuesto"). Es un archivo `.md` con encabezado YAML. |
| **Grafo** | Los nodos de un módulo y sus relaciones. Vive en `_modulo.yaml`. |
| **Prerrequisito** | Nodo que hay que dominar antes de otro. Arista dirigida del grafo. |
| **Puente académico** | Conexión de un nodo práctico con un concepto académico (campo `conecta_con`). |
| **Núcleo** | Contenido universal, válido en cualquier país (`nucleo/`). |
| **Local / fork local** | Adaptación de un nodo a un país (`locales/<pais>/`), con leyes, entidades, montos y ejemplos propios. |
| **Artefacto** | Una pieza de contenido dentro de un nodo: explicación, ejercicio, caso, evaluación. |
| **Hilo** | Recorrido curado a través de varios nodos, alrededor de una gran pregunta, con un proyecto integrador. |
| **Kit de tarea** | Paquete para aportar con IA: contexto, prompt, rúbrica y formato de entrega (`docs/kits-de-tarea/`). |
| **Tarea / microtarea** | Unidad de trabajo pequeña sobre un nodo. Se gestiona como Issue. |
| **Responsable** | La única persona a cargo de un nodo o Issue en un momento dado. |
| **Revisión de pares** | Revisión de un PR por otro colaborador usando las rúbricas. |
| **Revisión experta** | Aprobación obligatoria de un profesional para contenido de riesgo (salud, electricidad, legal). |
| **Procedencia** | Registro de quién escribió, con qué modelo de IA y quién revisó. |
| **Evidencia práctica** | Prueba de dominio basada en hacer algo real (un presupuesto, una reparación, un caso). |
| **Curador** | Persona que mantiene la coherencia de un módulo o de una adaptación local. |
| **Docente ancla** | Mentor que acompaña a un grupo de estudiantes durante un hilo. |
| **ADR** | Registro de decisión (*Architecture/Any Decision Record*) en `docs/decisiones/`. |
| **MVP** | Primera versión mínima: módulo Dinero, español + Colombia, tres tipos de tarea. |
