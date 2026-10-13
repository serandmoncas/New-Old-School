#!/usr/bin/env python3
"""Crea un nodo del currículo a partir de la plantilla.

Ejemplos:
    python scripts/nuevo_nodo.py dinero presupuesto "Presupuesto"
    python scripts/nuevo_nodo.py dinero impuestos-basicos "Impuestos básicos en Colombia" --pais co
    python scripts/nuevo_nodo.py dinero --desde-grafo      # crea los nodos del núcleo que falten

Si el nodo ya está en `_modulo.yaml`, toma de allí el nivel, los prerrequisitos y los puentes.
Nunca sobrescribe un archivo existente.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys

from _comun import CURRICULO, PLANTILLA_NODO, cargar_modulo, escribir_encabezado, separar_encabezado

SLUG_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

CUERPO_LOCAL = """# {titulo}

> Adaptación local. Complementa el nodo del núcleo: [{nucleo}]({nucleo}). No repitas su explicación.
> Kit: `docs/kits-de-tarea/adaptar-local.md`. Todo dato legal, tributario o de cifras lleva fuente y fecha.

## Cómo funciona aquí

Leyes, entidades y reglas vigentes, explicadas para un estudiante.

## Ejemplo con datos locales

Un caso con moneda, montos y situaciones del país.

## Entidades y recursos oficiales

- Entidad o recurso — enlace — fecha de consulta.

## Ejercicios con contexto local

1. …

<details>
<summary>Soluciones</summary>

1. …

</details>
"""


def crear(modulo: str, slug: str, titulo: str | None, pais: str | None) -> bool:
    carpeta = CURRICULO / modulo
    if not (carpeta / "_modulo.yaml").exists():
        sys.exit(f"No existe el módulo '{modulo}' (falta curriculo/{modulo}/_modulo.yaml).")
    if not SLUG_VALIDO.match(slug):
        sys.exit(f"Slug inválido '{slug}': usa minúsculas, números y guiones.")

    grafo = cargar_modulo(carpeta)
    id_nodo = f"{modulo}.{slug}"
    en_grafo = next((n for n in grafo.get("nodos", []) if n["id"] == id_nodo), None)

    if pais:
        destino = carpeta / "locales" / pais / f"{slug}.md"
        if not (carpeta / "nucleo" / f"{slug}.md").exists():
            sys.exit(f"Primero debe existir el nodo del núcleo: curriculo/{modulo}/nucleo/{slug}.md")
    else:
        destino = carpeta / "nucleo" / f"{slug}.md"
        if en_grafo is None:
            print(
                f"Aviso: '{id_nodo}' no está en _modulo.yaml. Propón el nodo al curador en un Issue.",
                file=sys.stderr,
            )

    if destino.exists():
        print(f"Ya existe, no se toca: {destino.relative_to(CURRICULO.parent)}")
        return False

    titulo = titulo or (en_grafo or {}).get("titulo") or slug.replace("-", " ").capitalize()
    if pais:
        titulo = titulo if f"({pais.upper()})" in titulo else f"{titulo} ({pais.upper()})"
        cuerpo = CUERPO_LOCAL.format(titulo=titulo, nucleo=f"../../nucleo/{slug}.md")
    else:
        _, cuerpo = separar_encabezado(PLANTILLA_NODO.read_text(encoding="utf-8"))
        cuerpo = cuerpo.replace("# Título del nodo", f"# {titulo}", 1)

    requiere_experto = id_nodo in grafo.get("requieren_local", []) and bool(pais)
    datos = {
        "id": id_nodo,
        "titulo": titulo,
        "modulo": modulo,
        "alcance": "local" if pais else "nucleo",
        "pais": pais,
        "nodo_base": id_nodo if pais else None,
        "nivel": (en_grafo or {}).get("nivel", 1),
        "prerrequisitos": [] if pais else list((en_grafo or {}).get("prerrequisitos", [])),
        "conecta_con": [] if pais else list((en_grafo or {}).get("conecta_con", [])),
        "estado": "pendiente",
        "responsable": None,
        "revisores": [],
        "revision_experta": requiere_experto,
        "procedencia": [],
        "recursos": [],
        "actualizado": dt.date.today().isoformat(),
    }

    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(escribir_encabezado(datos, cuerpo), encoding="utf-8")
    print(f"Creado: {destino.relative_to(CURRICULO.parent)}")
    return True


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("modulo")
    p.add_argument("slug", nargs="?")
    p.add_argument("titulo", nargs="?")
    p.add_argument("--pais", help="código ISO del país en minúscula, p. ej. co")
    p.add_argument("--desde-grafo", action="store_true", help="crea todos los nodos del núcleo que falten")
    a = p.parse_args()

    if a.desde_grafo:
        grafo = cargar_modulo(CURRICULO / a.modulo)
        creados = sum(
            crear(a.modulo, n["id"].split(".", 1)[1], n.get("titulo"), None) for n in grafo.get("nodos", [])
        )
        print(f"{creados} nodo(s) nuevo(s).")
        return
    if not a.slug:
        p.error("falta el slug del nodo")
    crear(a.modulo, a.slug, a.titulo, a.pais)


if __name__ == "__main__":
    main()
