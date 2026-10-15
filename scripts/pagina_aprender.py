#!/usr/bin/env python3
"""Genera la página pública "Libros para aprender a aprender" a partir de las fichas de la biblioteca.

Uso:
    python scripts/pagina_aprender.py                      # escribe _sitio/aprender-a-aprender.html
    python scripts/pagina_aprender.py --idioma en          # versión en inglés: _sitio/learning-to-learn.html
    python scripts/pagina_aprender.py --salida otra.html   # en otro lugar
    python scripts/pagina_aprender.py --sitio --salida ../sergiomonsalve.com/public/aprender-a-aprender.html
                                                           # documento completo para un sitio propio

Lee las fichas de biblioteca/, los veredictos, rutas y preguntas de biblioteca/_pagina-aprender.yaml
(y su traducción en _pagina-aprender.en.yaml), los textos de la interfaz de
scripts/plantillas/pagina_aprender.textos.yaml y la plantilla scripts/plantillas/pagina_aprender.html.
La versión en inglés traduce todo menos el texto completo de las fichas: cada libro enlaza a su ficha en español.
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
DATOS = {"es": BIBLIOTECA / "_pagina-aprender.yaml", "en": BIBLIOTECA / "_pagina-aprender.en.yaml"}
PLANTILLAS = RAIZ / "scripts" / "plantillas"
PLANTILLA = PLANTILLAS / "pagina_aprender.html"
TEXTOS = PLANTILLAS / "pagina_aprender.textos.yaml"
SALIDA = {"es": RAIZ / "_sitio" / "aprender-a-aprender.html", "en": RAIZ / "_sitio" / "learning-to-learn.html"}
PAGINA_ES = "aprender-a-aprender.html"
VEREDICTOS = ("solido", "matices", "promete", "filosofia")
SECCIONES = ("cinco-minutos", "que-funciona", "ponte-a-prueba", "repaso", "veredictos", "linea", "mapa", "fichas")


def cargar_fichas() -> dict[str, tuple[dict[str, Any], str]]:
    fichas = {}
    for archivo in sorted(BIBLIOTECA.glob("*.md")):
        if archivo.name != "README.md" and not archivo.name.startswith("_"):
            fichas[archivo.stem] = separar_encabezado(archivo.read_text(encoding="utf-8"))
    return fichas


def aristas_de(cfg: dict[str, Any], fichas: dict) -> list[dict[str, Any]]:
    """Cada cruce aparece una vez; si toca un libro de otro tema, ese libro va como segundo extremo."""
    en_pagina = {s for g in cfg["grupos"] for s in g["libros"]}
    aristas = []
    for s, (d, _) in fichas.items():
        for c in d.get("cruza_con") or []:
            a, b = s, c["libro"]
            if a in en_pagina or b in en_pagina:
                if a not in en_pagina:
                    a, b = b, a
                aristas.append({"a": a, "b": b, "por": c["por"], "fuera": b not in en_pagina})
    return aristas


def validar(cfg: dict[str, Any], fichas: dict, en: dict[str, Any] | None) -> list[str]:
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
    for i, q in enumerate(cfg.get("preguntas") or [], 1):
        if q.get("es") not in ("mito", "evidencia"):
            errores.append(f"pregunta {i}: 'es' debe ser mito o evidencia")
        if not all(q.get(k) for k in ("frase", "explica", "cita", "doi")):
            errores.append(f"pregunta {i}: necesita frase, explica, cita y doi")
    if en is not None:  # la traducción debe cubrir todo lo que aparece en la página
        if len(en.get("preguntas") or []) != len(cfg.get("preguntas") or []):
            errores.append("en: no tiene las mismas preguntas que la versión en español")
        if len(en["grupos"]) != len(cfg["grupos"]) or len(en["rutas"]) != len(cfg["rutas"]):
            errores.append("en: no tiene los mismos grupos y rutas que la versión en español")
        for s in slugs:
            if s not in en.get("veredictos", {}):
                errores.append(f"en: falta el veredicto de '{s}'")
        for a in aristas_de(cfg, fichas):
            for s in (a["a"], a["b"]):
                if s not in en.get("titulos", {}):
                    errores.append(f"en: falta el título de '{s}'")
            if f'{a["a"]}|{a["b"]}' not in en.get("cruces", {}):
                errores.append(f'en: falta el cruce {a["a"]}|{a["b"]}')
    return sorted(set(errores))


def traducir(cfg: dict[str, Any], en: dict[str, Any]) -> dict[str, Any]:
    """Combina la estructura en español con los textos en inglés (citas y DOI quedan del español)."""
    t = json.loads(json.dumps(cfg))
    t["etiquetas"] = en["etiquetas"]
    for g, ge in zip(t["grupos"], en["grupos"]):
        g.update(ge)
    for r, re_ in zip(t["rutas"], en["rutas"]):
        r.update(re_)
    for s, v in en["veredictos"].items():
        t["veredictos"][s].update(v)
    for q, qe in zip(t["preguntas"], en["preguntas"]):
        q.update(qe)
    t["titulos"] = en["titulos"]
    t["cruces"] = en["cruces"]
    return t


def ficha_html(slug: str, fichas: dict, cfg: dict, tx: dict, titulo, en_pagina: set, ficha_es: str | None) -> str:
    d, cuerpo = fichas[slug]
    v = cfg["veredictos"][slug]
    traducida = ficha_es is not None
    cruces = []
    for c in d.get("cruza_con") or []:
        otro = c["libro"]
        por = cfg["cruces"].get(f"{slug}|{otro}", cfg["cruces"].get(f"{otro}|{slug}", c["por"])) if traducida else c["por"]
        nombre = html.escape(titulo(otro))
        cruces.append((f'<li><a href="#{otro}">{nombre}</a> · ' if otro in en_pagina else f"<li><em>{nombre}</em> · ") + f"{html.escape(por)}</li>")
    bloque_cruces = f"<div class='cruces'><p class='rotulo'>{tx['se_cruza']}</p><ul>{''.join(cruces)}</ul></div>" if cruces else ""
    original = f'<p class="original">{html.escape(str(d["titulo_original"]))}</p>' if d.get("titulo_original") and not traducida else ""
    if traducida:
        fuente = (
            f'<p class="tenue" style="font-size:1rem">{html.escape(v["cita"])} · '
            f'<a href="https://doi.org/{v["doi"]}" target="_blank" rel="noopener">doi.org/{html.escape(v["doi"])}</a></p>'
            if v.get("doi") else ""
        )
        detalle = (
            f'<div class="cuerpo"><p><b>{html.escape(tx["la_promesa"])}</b> {html.escape(v["promesa"])}.</p><p>{html.escape(v["juicio"])}</p>{fuente}'
            f'<p><a href="{html.escape(ficha_es)}#{slug}" hreflang="es">{html.escape(tx["leer_ficha"])}</a></p></div>'
        )
        temas = ""
    else:
        cuerpo = re.sub(r"\s*<!--.*?-->", "", cuerpo, flags=re.S)
        cuerpo = re.sub(r"^# .*\n", "", cuerpo.strip(), count=1)
        h = markdown.markdown(cuerpo, extensions=["tables"])
        h = h.replace("<table>", '<div class="tabla"><table>').replace("</table>", "</table></div>")
        h = h.replace("<a href=", '<a target="_blank" rel="noopener" href=')
        detalle = f'<details class="cuerpo"><summary>{tx["leer_ficha"]}</summary>{h}</details>'
        temas = f'<div><dt>{tx["temas"]}</dt><dd>' + " ".join(f'<span class="tema">{html.escape(t)}</span>' for t in d.get("temas") or []) + "</dd></div>"
    cota = html.escape(str(d["publicado"]) if traducida else f'{d["tipo"]} · {d["publicado"]}')  # el tipo es un término del repo, en español
    return f"""
<article class="ficha" id="{slug}">
  <header class="tarjeta">
    <div class="sello"><span class="cota">{cota}</span><span class="chip v-{v["veredicto"]}">{cfg["etiquetas"][v["veredicto"]]}</span></div>
    <h3>{html.escape(titulo(slug))}</h3>
    {original}
    <dl><div><dt>{tx["autor"]}</dt><dd>{html.escape(d["autor"])}</dd></div>{temas}</dl>
    {bloque_cruces}
  </header>
  {detalle}
</article>"""


def construir(cfg: dict[str, Any], fichas: dict, tx: dict[str, Any], idioma: str, ficha_es: str | None) -> tuple[str, int, int]:
    traducida = idioma != "es"

    def titulo(s: str) -> str:
        return cfg["titulos"].get(s, fichas[s][0]["titulo"]) if traducida else fichas[s][0]["titulo"]

    slugs = [s for g in cfg["grupos"] for s in g["libros"]]
    en_pagina = set(slugs)
    grupo_de = {s: i for i, g in enumerate(cfg["grupos"]) for s in g["libros"]}

    libros = []
    for s in slugs:
        d, _ = fichas[s]
        v = cfg["veredictos"][s]
        libros.append({
            "id": s, "titulo": titulo(s), "autor": d["autor"], "anio": str(d["publicado"]), "grupo": grupo_de[s],
            "veredicto": v["veredicto"], "frase": v["promesa"], "juicio": v["juicio"], "cita": v.get("cita"), "doi": v.get("doi"),
        })
    aristas = aristas_de(cfg, fichas)
    for a in aristas:
        if traducida:
            a["por"] = cfg["cruces"][f'{a["a"]}|{a["b"]}']
        a["titulo_b"] = titulo(a["b"])

    secciones = "".join(
        f'<section class="grupo"><div class="grupo-cab"><h2>{html.escape(g["nombre"])}</h2><p>{html.escape(g["sub"])}</p></div>'
        + "".join(ficha_html(s, fichas, cfg, tx, titulo, en_pagina, ficha_es if traducida else None) for s in g["libros"])
        + "</section>"
        for g in cfg["grupos"]
    )
    rutas = "".join(
        f'<div class="ruta"><h3>{html.escape(r["nombre"])}</h3><p>{html.escape(r["texto"])}</p><ol>'
        + "".join(f'<li><a href="#{s}">{html.escape(titulo(s))}</a></li>' for s in r["libros"])
        + "</ol></div>"
        for r in cfg["rutas"]
    )
    leyenda = "".join(
        f'<span><span class="chip v-{k}">{html.escape(cfg["etiquetas"][k])}</span> {html.escape(tx["leyenda"][k])}</span>' for k in VEREDICTOS
    )
    nav = "".join(f'<a href="#{s}">{html.escape(n)}</a>' for s, n in zip(SECCIONES, tx["nav"]))

    def seguro(o: Any) -> str:  # JSON dentro de <script>: que ningún texto cierre la etiqueta
        return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

    datos_js = seguro({
        "libros": libros, "aristas": aristas, "grupos": [g["nombre"] for g in cfg["grupos"]],
        "etiquetas": cfg["etiquetas"], "preguntas": cfg.get("preguntas") or [],
    })

    pagina = PLANTILLA.read_text(encoding="utf-8")
    pagina = re.sub(r"\{\{t\.(\w+)\}\}", lambda m: html.escape(str(tx[m.group(1)]).replace("{n}", str(len(slugs)))), pagina)
    pagina = (
        pagina.replace("{{FICHAS}}", secciones).replace("{{RUTAS}}", rutas).replace("{{LEYENDA}}", leyenda)
        .replace("{{NAV}}", nav).replace("{{DATOS}}", datos_js).replace("{{UI}}", seguro(tx))
    )
    resto = re.search(r"\{\{[A-Za-z_.]+\}\}", pagina)
    if resto:
        raise ValueError(f"quedó un marcador sin reemplazar en la plantilla: {resto.group(0)}")
    return pagina, len(slugs), len(aristas)


def documento_completo(pagina: str, tx: dict[str, Any], volver: str, otro: tuple[str, str] | None) -> str:
    """Envuelve la página (pensada para un visor que pone el esqueleto) en un HTML completo."""
    corte = pagina.index('<div class="marco">')
    cabeza, cuerpo = pagina[:corte], pagina[corte:]
    extra = f'<a href="{html.escape(volver)}">← {html.escape(volver.split("//")[-1].strip("/"))}</a>'
    if otro:
        extra += f'<a href="{html.escape(otro[0])}" hreflang="{"en" if tx["lang"] == "es" else "es"}">{html.escape(otro[1])}</a>'
    cuerpo = re.sub(r'(<nav aria-label="[^"]*">)', lambda m: m.group(1) + extra, cuerpo, count=1)
    meta = (
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<meta name="description" content="{html.escape(tx["descripcion"])}">\n'
        f'<meta property="og:title" content="{html.escape(tx["titulo"])}">\n'
        f'<meta property="og:description" content="{html.escape(tx["descripcion"])}">\n'
        '<meta property="og:type" content="website">\n'
        "<style>body { margin: 0; } [hidden] { display: none !important; }</style>\n"
    )
    return f'<!doctype html>\n<html lang="{tx["lang"]}">\n<head>\n{cabeza}{meta}</head>\n<body>\n{cuerpo}</body>\n</html>\n'


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--idioma", choices=("es", "en"), default="es")
    p.add_argument("--salida", type=Path, help="archivo HTML de salida (por defecto, en _sitio/)")
    p.add_argument("--sitio", action="store_true", help="documento HTML completo, para publicarlo en un sitio propio")
    p.add_argument("--volver", default="https://sergiomonsalve.com", help="con --sitio: enlace de regreso en la barra")
    p.add_argument("--otro-idioma", help="con --sitio: URL de la misma página en el otro idioma")
    p.add_argument("--ficha-es", default=PAGINA_ES, help="en inglés: página en español donde están las fichas completas")
    a = p.parse_args()

    cfg = yaml.safe_load(DATOS["es"].read_text(encoding="utf-8"))
    en = yaml.safe_load(DATOS["en"].read_text(encoding="utf-8")) if a.idioma == "en" else None
    fichas = cargar_fichas()
    errores = validar(cfg, fichas, en)
    for e in errores:
        print(f"ERROR  {e}")
    if errores:
        sys.exit(1)

    tx = yaml.safe_load(TEXTOS.read_text(encoding="utf-8"))[a.idioma]
    datos = traducir(cfg, en) if en else cfg
    pagina, n_libros, n_cruces = construir(datos, fichas, tx, a.idioma, a.ficha_es)
    if a.sitio:
        otro = (a.otro_idioma, "English" if a.idioma == "es" else "Español") if a.otro_idioma else None
        pagina = documento_completo(pagina, tx, a.volver, otro)
    salida = a.salida or SALIDA[a.idioma]
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(pagina, encoding="utf-8")
    print(f"{salida}: {n_libros} libros, {n_cruces} cruces ({a.idioma}).")


if __name__ == "__main__":
    main()
