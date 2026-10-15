#!/usr/bin/env python3
"""Genera la página pública "Libros para aprender a aprender" a partir de las fichas de la biblioteca.

Uso:
    python scripts/pagina_aprender.py                      # escribe _sitio/aprender-a-aprender.html
    python scripts/pagina_aprender.py --salida otra.html   # en otro lugar

Lee las fichas de biblioteca/, los veredictos y las rutas de biblioteca/_pagina-aprender.yaml
y la plantilla de scripts/plantillas/pagina_aprender.html. La página es un solo archivo HTML
sin dependencias, listo para abrir en el navegador o publicar.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

import markdown
import yaml

from _comun import RAIZ, separar_encabezado

BIBLIOTECA = RAIZ / "biblioteca"
DATOS = BIBLIOTECA / "_pagina-aprender.yaml"
PLANTILLA = RAIZ / "scripts" / "plantillas" / "pagina_aprender.html"
SALIDA = RAIZ / "_sitio" / "aprender-a-aprender.html"
VEREDICTOS = ("solido", "matices", "promete", "filosofia")


def cargar_fichas() -> dict[str, tuple[dict[str, Any], str]]:
    fichas = {}
    for archivo in sorted(BIBLIOTECA.glob("*.md")):
        if archivo.name != "README.md" and not archivo.name.startswith("_"):
            fichas[archivo.stem] = separar_encabezado(archivo.read_text(encoding="utf-8"))
    return fichas


def validar(cfg: dict[str, Any], fichas: dict) -> list[str]:
    errores = []
    slugs = [s for g in cfg["grupos"] for s in g["libros"]]
    for s in slugs + [s for r in cfg["rutas"] for s in r["libros"]]:
        if s not in fichas:
            errores.append(f"'{s}' no tiene ficha en biblioteca/")
    for s in slugs:
        v = cfg["veredictos"].get(s)
        if not v:
            errores.append(f"'{s}' no tiene veredicto")
        elif v["veredicto"] not in VEREDICTOS:
            errores.append(f"'{s}': veredicto '{v['veredicto']}' no válido; usa uno de {', '.join(VEREDICTOS)}")
        elif bool(v.get("cita")) != bool(v.get("doi")):
            errores.append(f"'{s}': la cita y el doi van juntos")
    return errores


def ficha_html(slug: str, fichas: dict, titulos: dict, en_pagina: set, cfg: dict) -> str:
    d, cuerpo = fichas[slug]
    cuerpo = re.sub(r"\s*<!--.*?-->", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r"^# .*\n", "", cuerpo.strip(), count=1)
    h = markdown.markdown(cuerpo, extensions=["tables"])
    h = h.replace("<table>", '<div class="tabla"><table>').replace("</table>", "</table></div>")
    h = h.replace("<a href=", '<a target="_blank" rel="noopener" href=')
    v = cfg["veredictos"][slug]["veredicto"]
    temas = " ".join(f'<span class="tema">{html.escape(t)}</span>' for t in d.get("temas") or [])
    cruces = "".join(
        (
            f'<li><a href="#{c["libro"]}">{html.escape(titulos[c["libro"]])}</a> · '
            if c["libro"] in en_pagina
            else f'<li><em>{html.escape(titulos.get(c["libro"], c["libro"]))}</em> · '
        )
        + f'{html.escape(c["por"])}</li>'
        for c in d.get("cruza_con") or []
    )
    original = f'<p class="original">{html.escape(str(d["titulo_original"]))}</p>' if d.get("titulo_original") else ""
    bloque_cruces = f"<div class='cruces'><p class='rotulo'>Se cruza con</p><ul>{cruces}</ul></div>" if cruces else ""
    return f"""
<article class="ficha" id="{slug}">
  <header class="tarjeta">
    <div class="sello"><span class="cota">{d["tipo"]} · {html.escape(str(d["publicado"]))}</span><span class="chip v-{v}">{cfg["etiquetas"][v]}</span></div>
    <h3>{html.escape(d["titulo"])}</h3>
    {original}
    <dl><div><dt>Autor</dt><dd>{html.escape(d["autor"])}</dd></div><div><dt>Temas</dt><dd>{temas}</dd></div></dl>
    {bloque_cruces}
  </header>
  <details class="cuerpo"><summary>Leer la ficha completa</summary>{h}</details>
</article>"""


def construir(cfg: dict[str, Any], fichas: dict) -> tuple[str, int, int]:
    titulos = {s: d["titulo"] for s, (d, _) in fichas.items()}
    slugs = [s for g in cfg["grupos"] for s in g["libros"]]
    en_pagina = set(slugs)
    grupo_de = {s: i for i, g in enumerate(cfg["grupos"]) for s in g["libros"]}

    libros = []
    for s in slugs:
        d, _ = fichas[s]
        v = cfg["veredictos"][s]
        libros.append({
            "id": s, "titulo": d["titulo"], "autor": d["autor"], "anio": str(d["publicado"]), "grupo": grupo_de[s],
            "veredicto": v["veredicto"], "frase": v["promesa"], "juicio": v["juicio"], "cita": v.get("cita"), "doi": v.get("doi"),
        })

    # Cada cruce aparece una vez; si toca un libro de otro tema, ese libro va como segundo extremo.
    aristas = []
    for s, (d, _) in fichas.items():
        for c in d.get("cruza_con") or []:
            a, b = s, c["libro"]
            if a in en_pagina or b in en_pagina:
                if a not in en_pagina:
                    a, b = b, a
                aristas.append({"a": a, "b": b, "por": c["por"], "fuera": b not in en_pagina, "titulo_b": titulos.get(b, b)})

    secciones = "".join(
        f'<section class="grupo"><div class="grupo-cab"><h2>{html.escape(g["nombre"])}</h2><p>{html.escape(g["sub"])}</p></div>'
        + "".join(ficha_html(s, fichas, titulos, en_pagina, cfg) for s in g["libros"])
        + "</section>"
        for g in cfg["grupos"]
    )
    rutas = "".join(
        f'<div class="ruta"><h3>{html.escape(r["nombre"])}</h3><p>{html.escape(r["texto"])}</p><ol>'
        + "".join(f'<li><a href="#{s}">{html.escape(titulos[s])}</a></li>' for s in r["libros"])
        + "</ol></div>"
        for r in cfg["rutas"]
    )
    datos_js = json.dumps(
        {"libros": libros, "aristas": aristas, "grupos": [g["nombre"] for g in cfg["grupos"]], "etiquetas": cfg["etiquetas"]},
        ensure_ascii=False,
    ).replace("</", "<\\/")
    pagina = (
        PLANTILLA.read_text(encoding="utf-8")
        .replace("{{FICHAS}}", secciones)
        .replace("{{RUTAS}}", rutas)
        .replace("{{DATOS}}", datos_js)
        .replace("{{TOTAL}}", str(len(slugs)))
    )
    return pagina, len(slugs), len(aristas)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--salida", type=Path, default=SALIDA, help="archivo HTML de salida")
    a = p.parse_args()

    cfg = yaml.safe_load(DATOS.read_text(encoding="utf-8"))
    fichas = cargar_fichas()
    errores = validar(cfg, fichas)
    for e in errores:
        print(f"ERROR  {DATOS.relative_to(RAIZ)}: {e}")
    if errores:
        sys.exit(1)

    pagina, n_libros, n_cruces = construir(cfg, fichas)
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(pagina, encoding="utf-8")
    print(f"{a.salida}: {n_libros} libros, {n_cruces} cruces.")


if __name__ == "__main__":
    main()
