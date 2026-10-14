# New Old School

**Un colegio virtual open source que enseña primero lo que casi ningún colegio enseña y la vida práctica exige.**

Lo viejo —los saberes que antes se aprendían en casa o en el oficio— traído con lo nuevo: IA, comunidad abierta y acceso global. Empezamos por lo práctico (dinero, derechos, salud, autonomía, pensamiento crítico) y lo usamos como puerta de entrada a lo académico: el interés compuesto lleva a las funciones exponenciales, cocinar a la química, la electricidad de la casa a la física.

> Estado: **Fase 0 · Definición**. Módulo inicial: **Dinero**.

---

## Empieza aquí (10 minutos)

| Si eres… | Lee esto primero |
| --- | --- |
| Nuevo en el proyecto | [`docs/origen.md`](docs/origen.md) → [`docs/vision.md`](docs/vision.md) → [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Quien va a crear o revisar contenido | [`curriculo/README.md`](curriculo/README.md) → [`docs/rubricas.md`](docs/rubricas.md) |
| Quien va a usar su IA para aportar | [`docs/kits-de-tarea/`](docs/kits-de-tarea/) → [`AGENTS.md`](AGENTS.md) |
| Quien va a programar la plataforma | [`plataforma/README.md`](plataforma/README.md) |
| Quien quiere saber quién hace qué | [`docs/equipo.md`](docs/equipo.md) y el tablero de Issues |

## Cómo no pisarnos las mangueras (resumen)

1. **Nada se trabaja sin un Issue asignado.** Si no hay Issue, créalo; si está asignado a otra persona, coordina en el Issue.
2. **Un Issue = una rama = un Pull Request pequeño.** Un nodo del currículo por PR.
3. **Cada archivo de contenido dice quién lo tiene** (`responsable` y `estado` en su encabezado).
4. **Nadie hace merge de su propio PR.** CODEOWNERS asigna revisores por área.
5. **Las decisiones que afectan a todos se registran** en [`docs/decisiones/`](docs/decisiones/).

Detalles en [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Mapa del repositorio

```
new-old-school/
├── README.md                 ← estás aquí
├── AGENTS.md / CLAUDE.md     ← contexto para la IA de cada colaborador
├── CONTRIBUTING.md           ← cómo colaborar sin conflictos
├── GOVERNANCE.md             ← roles y cómo se decide
├── CODE_OF_CONDUCT.md
├── LICENSE                   ← código: MIT
├── LICENSE-CONTENT.md        ← contenido: CC BY-SA 4.0
├── docs/
│   ├── puesta-en-marcha.md   ← pasos de una vez para configurar GitHub
│   ├── origen.md             ← de dónde salió el proyecto y las ideas que lo orientan
│   ├── vision.md             ← qué es, principios, marco de referencia
│   ├── marco-curricular.md   ← núcleo académico y los frentes de saberes de vida
│   ├── glosario.md           ← vocabulario común (léelo, evita malentendidos)
│   ├── equipo.md             ← roles y quién es dueño de qué
│   ├── roadmap.md            ← fases y estado
│   ├── rubricas.md           ← criterios de calidad por tipo de contenido
│   ├── kits-de-tarea/        ← prompts + rúbrica + formato para aportar con IA
│   ├── decisiones/           ← registro de decisiones (ADR)
│   └── plantillas/           ← plantillas de nodo, de libro y de decisión
├── curriculo/
│   ├── README.md             ← cómo está organizado el currículo
│   └── dinero/               ← primer módulo
│       ├── _modulo.yaml      ← el grafo del módulo (nodos y prerrequisitos)
│       ├── nucleo/           ← contenido universal
│       └── locales/co/       ← adaptación a Colombia
├── biblioteca/               ← libros, sus temas y cómo se cruzan entre sí y con los nodos
├── plataforma/               ← código de la plataforma (Fase 2)
├── scripts/                  ← validador del grafo y generador de nodos
└── .github/                  ← plantillas de Issues/PR, CODEOWNERS, CI
```

## Comandos útiles

```bash
pip install pyyaml
python scripts/validar_curriculo.py          # revisa encabezados, ids, prerrequisitos y ciclos
python scripts/validar_curriculo.py --grafo  # imprime el grafo en Mermaid
python scripts/nuevo_nodo.py dinero <slug> "Título del nodo"   # crea un nodo desde la plantilla
python scripts/biblioteca.py --indice        # valida la biblioteca y actualiza su índice
```

## Licencias

- Código: [MIT](LICENSE).
- Contenido educativo (todo lo que está en `curriculo/` y `docs/`): [Creative Commons BY-SA 4.0](LICENSE-CONTENT.md).
