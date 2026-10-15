#!/usr/bin/env python3
"""Genera las páginas públicas de la biblioteca por tema ("aprender a aprender", "dinero") a partir de las fichas.

Uso:
    python scripts/pagina_aprender.py                      # escribe _sitio/aprender-a-aprender.html
    python scripts/pagina_aprender.py --idioma en          # versión en inglés: _sitio/learning-to-learn.html
    python scripts/pagina_aprender.py --pagina dinero      # libros del módulo Dinero: _sitio/libros-del-dinero.html
    python scripts/pagina_aprender.py --salida otra.html   # en otro lugar
    python scripts/pagina_aprender.py --sitio --salida ../sergiomonsalve.com/public/aprender-a-aprender.html
                                                           # documento completo para un sitio propio
    python scripts/pagina_aprender.py --publicar ../sergiomonsalve.com/public
                                                           # todas las páginas e idiomas, enlazadas entre sí

Lee las fichas de biblioteca/, los veredictos, rutas y preguntas de biblioteca/_pagina-<pagina>.yaml
(y su traducción en _pagina-<pagina>.en.yaml), los textos de la interfaz de
scripts/plantillas/pagina_aprender.textos.yaml (con los cambios de pagina_<pagina>.textos.yaml, si existe)
y la plantilla scripts/plantillas/pagina_aprender.html. Cada página elige sus secciones; las demás quedan ocultas.
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
PLANTILLAS = RAIZ / "scripts" / "plantillas"
PLANTILLA = PLANTILLAS / "pagina_aprender.html"
TEXTOS = PLANTILLAS / "pagina_aprender.textos.yaml"
ARCHIVOS = {  # nombre del archivo publicado, por página e idioma
    "aprender": {"es": "aprender-a-aprender.html", "en": "learning-to-learn.html"},
    "dinero": {"es": "libros-del-dinero.html", "en": "books-on-money.html"},
}
VEREDICTOS = ("solido", "matices", "promete", "filosofia", "literatura")
SECCIONES = ("cinco-minutos", "que-funciona", "ponte-a-prueba", "repaso", "veredictos", "nodos", "linea", "mapa", "fichas")


def datos_de(pagina: str, idioma: str) -> Path:
    return BIBLIOTECA / (f"_pagina-{pagina}.yaml" if idioma == "es" else f"_pagina-{pagina}.{idioma}.yaml")


def textos_de(pagina: str, idioma: str) -> dict[str, Any]:
    """Textos base de la interfaz, con los cambios propios de la página encima."""
    tx = yaml.safe_load(TEXTOS.read_text(encoding="utf-8"))[idioma]
    propios = PLANTILLAS / f"pagina_{pagina}.textos.yaml"
    if propios.exists():
        tx.update(yaml.safe_load(propios.read_text(encoding="utf-8")).get(idioma) or {})
    return tx


ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}


def anio_de(publicado: str) -> tuple[int, str | None]:
    """Año para ordenar la línea de tiempo y, si no es un año exacto, la etiqueta del siglo.

    '1849-1850' → 1849; 'hacia 1596-1598' → 1596; 's. VIII a. C. (según la tradición)' → (-750, 's. VIII a. C.').
    """
    m = re.search(r"\d{4}", publicado)
    if m:
        return int(m.group(0)), None
    m = re.search(r"s\.\s*([IVXLC]+)\s*a\.\s*C\.", publicado)
    if not m:
        raise ValueError(f"no se entiende la fecha de publicación '{publicado}'")
    total, previo = 0, 0
    for letra in reversed(m.group(1)):
        v = ROMANOS[letra]
        total, previo = (total - v, previo) if v < previo else (total + v, v)
    return -(total * 100 - 50), m.group(0)


def nodos_del_modulo(modulo: str) -> list[dict[str, Any]]:
    from _comun import CURRICULO, cargar_modulo
    return cargar_modulo(CURRICULO / modulo).get("nodos", [])


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
        if cfg.get("modulo"):
            for n in nodos_del_modulo(cfg["modulo"]):
                if n["id"] not in en.get("nodos_titulos", {}):
                    errores.append(f'en: falta el título del nodo {n["id"]}')
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
    t["nodos_titulos"] = en.get("nodos_titulos", {})
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
    nodos = ""
    if d.get("nodos") and cfg.get("_nodo_titulo"):
        nodos = f'<div><dt>{tx["nodos"]}</dt><dd>' + ", ".join(html.escape(cfg["_nodo_titulo"](n)) for n in d["nodos"]) + "</dd></div>"
    cota = html.escape(str(d["publicado"]) if traducida else f'{d["tipo"]} · {d["publicado"]}')  # el tipo es un término del repo, en español
    return f"""
<article class="ficha" id="{slug}">
  <header class="tarjeta">
    <div class="sello"><span class="cota">{cota}</span><span class="chip v-{v["veredicto"]}">{cfg["etiquetas"][v["veredicto"]]}</span></div>
    <h3>{html.escape(titulo(slug))}</h3>
    {original}
    <dl><div><dt>{tx["autor"]}</dt><dd>{html.escape(d["autor"])}</dd></div>{temas}{nodos}</dl>
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
    pagina_oculta: list[str] = []
    if cfg.get("modulo"):
        titulos_nodo = {n["id"]: n["titulo"] for n in nodos_del_modulo(cfg["modulo"])}
        cfg["_nodo_titulo"] = lambda i: (cfg.get("nodos_titulos") or {}).get(i, titulos_nodo.get(i, i)) if traducida else titulos_nodo.get(i, i)
    grupo_de = {s: i for i, g in enumerate(cfg["grupos"]) for s in g["libros"]}

    libros = []
    for s in slugs:
        d, _ = fichas[s]
        v = cfg["veredictos"][s]
        libros.append({
            "id": s, "titulo": titulo(s), "autor": d["autor"], "anio": str(d["publicado"]), "grupo": grupo_de[s],
            "orden": anio_de(str(d["publicado"]))[0], "siglo": anio_de(str(d["publicado"]))[1],
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
    presentes = [k for k in VEREDICTOS if any(cfg["veredictos"][s]["veredicto"] == k for s in slugs)]
    leyenda = "".join(
        f'<span><span class="chip v-{k}">{html.escape(cfg["etiquetas"][k])}</span> {html.escape(tx["leyenda"].get(k, ""))}</span>' for k in presentes
    )
    activas = cfg.get("secciones") or [s for s in SECCIONES if s != "nodos"]
    nav = "".join(f'<a href="#{s}">{html.escape(tx["nav"][s])}</a>' for s in SECCIONES if s in activas)

    # Qué leer para cada lección: los nodos del módulo, en su orden, con los libros que los iluminan
    lecciones = ""
    if cfg.get("modulo"):
        for n in nodos_del_modulo(cfg["modulo"]):
            con = [s for s in slugs if n["id"] in (fichas[s][0].get("nodos") or [])]
            enlaces = "".join(
                f'<a class="hito" href="#{s}" data-id="{s}"><i style="background:var(--v-{cfg["veredictos"][s]["veredicto"]})"></i>{html.escape(titulo(s))}</a>'
                for s in con
            ) or f'<span class="tenue">{html.escape(tx["sin_libros"])}</span>'
            lecciones += f'<div class="decada"><span class="nodo">{html.escape(cfg["_nodo_titulo"](n["id"]))}</span><div class="fila">{enlaces}</div></div>'
        lecciones = f'<div class="linea lecciones">{lecciones}</div>'


    def seguro(o: Any) -> str:  # JSON dentro de <script>: que ningún texto cierre la etiqueta
        return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

    for s in SECCIONES:  # las secciones que la página no usa quedan ocultas; el script de la página las ignora
        if s not in activas:
            pagina_oculta.append(s)
    datos_js = seguro({
        "libros": libros, "aristas": aristas, "grupos": [g["nombre"] for g in cfg["grupos"]],
        "etiquetas": cfg["etiquetas"], "preguntas": cfg.get("preguntas") or [],
    })

    pagina = PLANTILLA.read_text(encoding="utf-8")
    for s in pagina_oculta:
        pagina = pagina.replace(f'<section class="seccion" id="{s}">', f'<section class="seccion" id="{s}" hidden>', 1)
    if "cinco-minutos" not in activas:
        pagina = pagina.replace('<button class="boton lleno" id="presentar">', '<button class="boton lleno" id="presentar" hidden>', 1)
    pagina = re.sub(r"\{\{t\.(\w+)\}\}", lambda m: html.escape(str(tx[m.group(1)]).replace("{n}", str(len(slugs)))), pagina)
    pagina = (
        pagina.replace("{{FICHAS}}", secciones).replace("{{RUTAS}}", rutas).replace("{{LEYENDA}}", leyenda)
        .replace("{{NAV}}", nav).replace("{{DATOS}}", datos_js).replace("{{UI}}", seguro(tx)).replace("{{LECCIONES}}", lecciones)
    )
    resto = re.search(r"\{\{[A-Za-z_.]+\}\}", pagina)
    if resto:
        raise ValueError(f"quedó un marcador sin reemplazar en la plantilla: {resto.group(0)}")
    return pagina, len(slugs), len(aristas)


def documento_completo(pagina: str, tx: dict[str, Any], volver: str, otro: tuple[str, str] | None, enlaces: list[str]) -> str:
    """Envuelve la página (pensada para un visor que pone el esqueleto) en un HTML completo."""
    corte = pagina.index('<div class="marco">')
    cabeza, cuerpo = pagina[:corte], pagina[corte:]
    extra = f'<a href="{html.escape(volver)}">← {html.escape(volver.split("//")[-1].strip("/"))}</a>'
    if otro:
        extra += f'<a href="{html.escape(otro[0])}" hreflang="{"en" if tx["lang"] == "es" else "es"}">{html.escape(otro[1])}</a>'
    for e in enlaces:  # "url|texto": otras páginas de la biblioteca
        url, texto = e.split("|", 1)
        extra += f'<a href="{html.escape(url)}">{html.escape(texto)}</a>'
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


ENLACE_A = {"aprender": {"es": "Aprender a aprender", "en": "Learning to learn"}, "dinero": {"es": "Libros del dinero", "en": "Books on money"}}


def generar(pagina: str, idioma: str, ficha_es: str | None = None) -> tuple[str, dict[str, Any], int, int]:
    cfg = yaml.safe_load(datos_de(pagina, "es").read_text(encoding="utf-8"))
    en = yaml.safe_load(datos_de(pagina, "en").read_text(encoding="utf-8")) if idioma == "en" else None
    fichas = cargar_fichas()
    errores = validar(cfg, fichas, en)
    for e in errores:
        print(f"ERROR  {pagina} {idioma}: {e}")
    if errores:
        sys.exit(1)
    tx = textos_de(pagina, idioma)
    datos = traducir(cfg, en) if en else cfg
    html_, n_libros, n_cruces = construir(datos, fichas, tx, idioma, ficha_es or ARCHIVOS[pagina]["es"])
    return html_, tx, n_libros, n_cruces


def publicar(carpeta: Path, volver: str) -> None:
    """Todas las páginas en ambos idiomas, cada una con enlace a su otro idioma y a las demás páginas."""
    for pagina, archivos in ARCHIVOS.items():
        for idioma, nombre in archivos.items():
            otro = "en" if idioma == "es" else "es"
            html_, tx, n_libros, n_cruces = generar(pagina, idioma, "/" + archivos["es"])
            enlaces = [f"/{ARCHIVOS[p][idioma]}|{ENLACE_A[p][idioma]}" for p in ARCHIVOS if p != pagina]
            html_ = documento_completo(html_, tx, volver, ("/" + archivos[otro], "English" if idioma == "es" else "Español"), enlaces)
            (carpeta / nombre).write_text(html_, encoding="utf-8")
            print(f"{carpeta / nombre}: {n_libros} libros, {n_cruces} cruces.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--pagina", choices=tuple(ARCHIVOS), default="aprender")
    p.add_argument("--idioma", choices=("es", "en"), default="es")
    p.add_argument("--salida", type=Path, help="archivo HTML de salida (por defecto, en _sitio/)")
    p.add_argument("--sitio", action="store_true", help="documento HTML completo, para publicarlo en un sitio propio")
    p.add_argument("--volver", default="https://sergiomonsalve.com", help="con --sitio: enlace de regreso en la barra")
    p.add_argument("--otro-idioma", help="con --sitio: URL de la misma página en el otro idioma")
    p.add_argument("--enlace", action="append", default=[], help='con --sitio: otra página para la barra, como "url|texto"; se puede repetir')
    p.add_argument("--ficha-es", help="en inglés: página en español donde están las fichas completas")
    p.add_argument("--publicar", type=Path, help="genera todas las páginas e idiomas en esta carpeta, enlazadas entre sí")
    a = p.parse_args()

    if a.publicar:
        publicar(a.publicar, a.volver)
        return
    pagina, tx, n_libros, n_cruces = generar(a.pagina, a.idioma, a.ficha_es)
    if a.sitio:
        otro = (a.otro_idioma, "English" if a.idioma == "es" else "Español") if a.otro_idioma else None
        pagina = documento_completo(pagina, tx, a.volver, otro, a.enlace)
    salida = a.salida or RAIZ / "_sitio" / ARCHIVOS[a.pagina][a.idioma]
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(pagina, encoding="utf-8")
    print(f"{salida}: {n_libros} libros, {n_cruces} cruces ({a.pagina}, {a.idioma}).")


if __name__ == "__main__":
    main()
