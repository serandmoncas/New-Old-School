# Currículo

El currículo es un **grafo de nodos** organizado por módulos. Git es la fuente de verdad (ver ADR 0002).

## Estructura

```
curriculo/
└── <modulo>/
    ├── _modulo.yaml        ← el grafo: lista de nodos, nivel y prerrequisitos
    ├── nucleo/<slug>.md    ← un archivo por nodo, contenido universal
    └── locales/<pais>/<slug>.md   ← adaptación a un país (opcional por nodo)
```

## Reglas

- **El `id` de un nodo es `<modulo>.<slug>`** y coincide con el nombre del archivo. No se cambia nunca; si un nodo se reemplaza, se marca `estado: retirado`.
- **`_modulo.yaml` lo mantiene el curador del módulo.** Para proponer un nodo nuevo o cambiar prerrequisitos, abre un Issue "Propuesta de nodo".
- **Un nodo local** usa el mismo slug que su nodo base, vive en `locales/<pais>/` y tiene `alcance: local`, `pais` y `nodo_base`.
- **`conecta_con`** puede apuntar a módulos académicos que aún no existen (`matematicas.*`, `quimica.*`). El validador lo permite con un aviso.
- El encabezado y el grafo deben coincidir: los prerrequisitos del archivo son los mismos de `_modulo.yaml`.

## Validar

```bash
python scripts/validar_curriculo.py            # errores bloquean el CI
python scripts/validar_curriculo.py --estado   # quién tiene qué
python scripts/validar_curriculo.py --grafo    # diagrama Mermaid del grafo
```

## Módulos

| Módulo | Estado | Curador |
| --- | --- | --- |
| [`dinero`](dinero/) | Grafo en borrador, nodos pendientes | Coordinación (temporal) |
