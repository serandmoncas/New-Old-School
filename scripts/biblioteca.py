#!/usr/bin/env python3
"""Valida la biblioteca y genera su índice: libros, temas y cruces.

Uso:
    python scripts/biblioteca.py              # valida; sale con código 1 si hay errores
    python scripts/biblioteca.py --indice     # además reescribe el índice en biblioteca/README.md
    python scripts/biblioteca.py --comprobar  # falla si el índice del README está desactualizado (CI)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

from _comun import RAIZ, cargar_modulo, modulos, separar_encabezado

BIBLIOTECA = RAIZ / "biblioteca"
INDICE = BIBLIOTECA / "README.md"
INICIO, FIN = "<!-- indice:inicio -->", "<!-- indice:fin -->"

CAMPOS = (
    "id",
    "titulo",
    "titulo_original",
    "autor",
    "publicado",
    "tipo",
    "acceso",
    "texto_libre",
    "temas",
    "cruza_con",
    "nodos",
    "estado",
    "procedencia",
    "actualizado",
)
TIPOS = ("novela", "cuento", "fabula", "poema", "teatro", "ensayo", "tratado", "divulgacion", "historia")
ACCESOS = ("dominio-publico", "con-derechos")
ESTADOS = ("propuesta", "aceptado", "retirado")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def rel(p: Path) -> str:
    return str(p.relative_to(RAIZ))


def ids_del_curriculo() -> set[str]:
    return {n["id"] for c in modulos() for n in cargar_modulo(c).get("nodos", [])}


def cargar_libros(errores: list[str]) -> dict[str, dict[str, Any]]:
    libros: dict[str, dict[str, Any]] = {}
    for archivo in sorted(BIBLIOTECA.glob("*.md")):
        if archivo.name == "README.md" or archivo.name.startswith("_"):
            continue
        try:
            d, _ = separar_encabezado(archivo.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errores.append(f"ERROR  {rel(archivo)}: {e}")
            continue
        d["_archivo"] = archivo
        libros[archivo.stem] = d
    return libros


def validar(libros: dict[str, dict[str, Any]], temas: dict[str, str], nodos: set[str], errores: list[str]) -> None:
    pares: dict[frozenset[str], str] = {}
    for slug, d in libros.items():
        donde = rel(d["_archivo"])

        def error(msg: str) -> None:
            errores.append(f"ERROR  {donde}: {msg}")

        faltan = [c for c in CAMPOS if c not in d]
        sobran = [c for c in d if c not in CAMPOS and c != "_archivo"]
        if faltan:
            error("faltan campos: " + ", ".join(faltan))
        if sobran:
            error("campos no permitidos (ver docs/plantillas/libro.md): " + ", ".join(sobran))
        if not SLUG.match(slug) or d.get("id") != slug:
            error(f"id '{d.get('id')}' debe ser '{slug}' (el nombre del archivo, en minúsculas y con guiones)")
        if d.get("tipo") not in TIPOS:
            error(f"tipo '{d.get('tipo')}' no válido; usa uno de {', '.join(TIPOS)}")
        if d.get("acceso") not in ACCESOS:
            error(f"acceso '{d.get('acceso')}' no válido; usa {' o '.join(ACCESOS)}")
        if d.get("acceso") == "con-derechos" and d.get("texto_libre"):
            error("un libro con derechos no puede enlazar un 'texto_libre'")
        if d.get("estado") not in ESTADOS:
            error(f"estado '{d.get('estado')}' no válido; usa uno de {', '.join(ESTADOS)}")
        if not FECHA.match(str(d.get("actualizado", ""))):
            error("'actualizado' debe ser una fecha AAAA-MM-DD")
        if not d.get("temas"):
            error("necesita al menos un tema")
        for t in d.get("temas") or []:
            if t not in temas:
                error(f"el tema '{t}' no está en biblioteca/_temas.yaml")
        for n in d.get("nodos") or []:
            if n not in nodos:
                error(f"el nodo '{n}' no existe en ningún _modulo.yaml")
        for c in d.get("cruza_con") or []:
            otro = c.get("libro") if isinstance(c, dict) else None
            if not otro or not c.get("por"):
                error("cada cruce necesita 'libro' y 'por' (por qué se cruzan)")
                continue
            if otro == slug:
                error("un libro no se cruza consigo mismo")
            elif otro not in libros:
                error(f"cruce con un libro que no está en la biblioteca: '{otro}'")
            par = frozenset((slug, otro))
            if par in pares:
                error(f"el cruce con '{otro}' ya está declarado en {pares[par]}; decláralo en un solo lado")
            pares[par] = donde


def cruces(libros: dict[str, dict[str, Any]]) -> list[tuple[str, str, str]]:
    return [
        (slug, c["libro"], c["por"])
        for slug, d in libros.items()
        for c in d.get("cruza_con") or []
        if isinstance(c, dict) and c.get("libro") in libros
    ]


def generar_indice(libros: dict[str, dict[str, Any]], temas: dict[str, str]) -> str:
    def enlace(slug: str) -> str:
        return f"[*{libros[slug]['titulo']}*]({slug}.md)"

    orden = sorted(libros, key=lambda s: libros[s]["titulo"])
    lineas = ["### Libros", "", "| Libro | Autor | Publicado | Temas | Nodos | Estado |", "| --- | --- | --- | --- | --- | --- |"]
    for s in orden:
        d = libros[s]
        nodos = ", ".join(f"`{n}`" for n in d.get("nodos") or []) or "—"
        libre = " 📖" if d.get("texto_libre") else ""
        lineas.append(
            f"| {enlace(s)}{libre} | {d['autor']} | {d['publicado']} | {', '.join(d.get('temas') or [])} "
            f"| {nodos} | {d['estado']} |"
        )

    lineas += ["", "📖 = texto completo libre y legal (dominio público).", "", "### Cruces", ""]
    lineas += ["| Libro | Se cruza con | Por qué |", "| --- | --- | --- |"]
    for a, b, por in sorted(cruces(libros), key=lambda x: (libros[x[0]]["titulo"], libros[x[1]]["titulo"])):
        lineas.append(f"| {enlace(a)} | {enlace(b)} | {por} |")

    lineas += ["", "### Por tema", "", "Dos libros que comparten tema son un cruce posible aunque nadie lo haya escrito aún.", ""]
    for t, descripcion in temas.items():
        con = [s for s in orden if t in (libros[s].get("temas") or [])]
        if con:
            lineas.append(f"- **{t}** ({descripcion}): " + ", ".join(enlace(s) for s in con))

    lineas += ["", "### Mapa", "", "```mermaid", "flowchart LR"]
    for s in orden:
        lineas.append(f'  {s.replace("-", "_")}["{libros[s]["titulo"]}"]')
    for a, b, _ in cruces(libros):
        lineas.append(f'  {a.replace("-", "_")} --- {b.replace("-", "_")}')
    lineas.append("```")
    return "\n".join(lineas)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--indice", action="store_true", help="reescribe el índice de biblioteca/README.md")
    p.add_argument("--comprobar", action="store_true", help="falla si el índice está desactualizado")
    a = p.parse_args()

    errores: list[str] = []
    temas = yaml.safe_load((BIBLIOTECA / "_temas.yaml").read_text(encoding="utf-8")) or {}
    libros = cargar_libros(errores)
    validar(libros, temas, ids_del_curriculo(), errores)

    if not errores and (a.indice or a.comprobar):
        texto = INDICE.read_text(encoding="utf-8")
        antes, resto = texto.split(INICIO, 1)
        despues = resto.split(FIN, 1)[1]
        nuevo = f"{antes}{INICIO}\n<!-- Generado por scripts/biblioteca.py --indice. No editar a mano. -->\n\n{generar_indice(libros, temas)}\n\n{FIN}{despues}"
        if a.indice:
            INDICE.write_text(nuevo, encoding="utf-8")
        elif nuevo != texto:
            errores.append("ERROR  biblioteca/README.md: el índice está desactualizado; corre scripts/biblioteca.py --indice")

    for m in errores:
        print(m)
    print(f"\n{len(libros)} libro(s), {len(cruces(libros))} cruce(s), {len(errores)} error(es).")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
