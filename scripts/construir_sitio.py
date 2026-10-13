#!/usr/bin/env python3
"""Construye el sitio estático de New Old School a partir de curriculo/.

Uso:
    python scripts/construir_sitio.py            # genera _sitio/
    python scripts/construir_sitio.py --salida X # otra carpeta

No necesita servidor: todos los enlaces son relativos, así funciona igual en
GitHub Pages (https://<usuario>.github.io/New-Old-School/) y abriendo los
archivos en el computador.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path
from typing import Any

import markdown

from _comun import CURRICULO, RAIZ, cargar_modulo, modulos, separar_encabezado

REPO = "https://github.com/serandmoncas/New-Old-School"
ESTILOS = RAIZ / "sitio" / "estilos.css"

ESTADO_TEXTO = {
    "pendiente": "Por escribir",
    "en-progreso": "En escritura",
    "en-revision": "En revisión",
    "aprobado": "Aprobado",
    "retirado": "Retirado",
}
ESTADO_NOTA = {
    "pendiente": "Este nodo todavía no está escrito. Puedes tomarlo: busca su Issue en GitHub.",
    "en-progreso": "Alguien lo está escribiendo. Puede cambiar mucho.",
    "en-revision": "Borrador completo. Todavía no lo aprueba una persona revisora: úsalo con criterio y avísanos si ves un error.",
    "aprobado": "Revisado y aprobado por el equipo.",
    "retirado": "Este nodo ya no se usa.",
}
PAISES = {"co": "Colombia"}
NIVELES = {1: "Nivel 1, para empezar", 2: "Nivel 2, intermedio", 3: "Nivel 3, avanzado"}

MD_EXT = ["tables", "sane_lists", "smarty"]
MD_CONF = {"smarty": {"smart_quotes": False}}


# ---------------------------------------------------------------- utilidades

def md(texto: str) -> str:
    """Markdown a HTML, renderizando también el contenido de <details>."""
    def detalles(m: re.Match[str]) -> str:
        resumen, dentro = m.group(1), m.group(2)
        return (f'<details><summary>{resumen}</summary>\n'
                f'{markdown.markdown(dentro, extensions=MD_EXT, extension_configs=MD_CONF)}\n</details>')
    texto = re.sub(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>", detalles, texto, flags=re.S)
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)  # notas internas fuera del sitio
    return markdown.markdown(texto, extensions=MD_EXT, extension_configs=MD_CONF)


def slug_de(id_nodo: str) -> str:
    return id_nodo.split(".", 1)[1]


def secciones(cuerpo: str) -> tuple[str, list[tuple[str, str]], list[tuple[str, str]]]:
    """Separa (título, secciones de la historia, secciones de profundización)."""
    cuerpo = re.sub(r"<!--.*?-->", "", cuerpo, flags=re.S)
    titulo = ""
    m = re.match(r"\s*# (.+)\n", cuerpo)
    if m:
        titulo, cuerpo = m.group(1).strip(), cuerpo[m.end():]
    historia_txt, _, resto_txt = cuerpo.partition("\n---\n")

    def partir(txt: str) -> list[tuple[str, str]]:
        partes = re.split(r"^## (.+)$", txt, flags=re.M)
        intro = partes[0].strip()
        salida = [("", intro)] if intro else []
        for i in range(1, len(partes), 2):
            salida.append((partes[i].strip(), partes[i + 1].strip()))
        return salida

    return titulo, partir(historia_txt), partir(resto_txt)


def pagina(titulo: str, cuerpo: str, raiz: str, descripcion: str = "") -> str:
    desc = html.escape(descripcion or "New Old School: lo que casi no se enseña y la vida práctica exige.")
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{raiz}estilos.css">
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>
<header class="barra">
  <a class="marca" href="{raiz}index.html">New Old School</a>
  <nav><a href="{raiz}dinero/index.html">Dinero</a><a href="{REPO}">Colaborar</a></nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <p>Contenido abierto bajo licencia CC BY-SA 4.0. Lo escribimos entre muchas personas, con ayuda de IA, y lo revisan personas.</p>
  <ul class="pie-enlaces"><li><a href="{REPO}">Repositorio en GitHub</a></li><li><a href="{REPO}/issues/new/choose">Reportar un error</a></li></ul>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- lectura

def leer_nodos(carpeta: Path) -> tuple[dict[str, Any], dict[str, dict], dict[str, dict[str, dict]]]:
    grafo = cargar_modulo(carpeta)
    nucleo: dict[str, dict] = {}
    for f in sorted((carpeta / "nucleo").glob("*.md")):
        datos, cuerpo = separar_encabezado(f.read_text(encoding="utf-8"))
        nucleo[datos["id"]] = {"datos": datos, "cuerpo": cuerpo, "archivo": f}
    locales: dict[str, dict[str, dict]] = {}
    for f in sorted((carpeta / "locales").glob("*/*.md")):
        datos, cuerpo = separar_encabezado(f.read_text(encoding="utf-8"))
        locales.setdefault(datos["nodo_base"], {})[datos["pais"]] = {"datos": datos, "cuerpo": cuerpo, "archivo": f}
    return grafo, nucleo, locales


# ---------------------------------------------------------------- piezas

def sello(estado: str) -> str:
    return f'<span class="sello sello-{estado}">{ESTADO_TEXTO.get(estado, estado)}</span>'


def mapa_rutas(grafo: dict, nucleo: dict, raiz_mod: str) -> str:
    titulos = {n["id"]: n["titulo"] for n in grafo["nodos"]}
    filas = []
    for i, ruta in enumerate(grafo.get("rutas", [])):
        paradas = []
        for nid in ruta["nodos"]:
            estado = nucleo.get(nid, {}).get("datos", {}).get("estado", "pendiente")
            paradas.append(
                f'<li class="parada parada-{estado}"><a href="{raiz_mod}{slug_de(nid)}/index.html">'
                f'<span class="punto" aria-hidden="true"></span>'
                f'<span class="texto"><span class="nombre">{html.escape(titulos.get(nid, nid))}</span>'
                f'<span class="lectores">{ESTADO_TEXTO.get(estado, estado)}</span></span></a></li>'
            )
        filas.append(
            f'<section class="ruta ruta-{i % 5}" aria-label="Ruta {html.escape(ruta["nombre"])}">'
            f'<h3 class="ruta-nombre">{html.escape(ruta["nombre"])}</h3>'
            f'<ol class="paradas">{"".join(paradas)}</ol></section>'
        )
    return f'<div class="mapa">{"".join(filas)}</div>'


def ruta_de(grafo: dict, nid: str) -> tuple[int, str, int, list[str]] | None:
    for i, ruta in enumerate(grafo.get("rutas", [])):
        if nid in ruta["nodos"]:
            return i, ruta["nombre"], ruta["nodos"].index(nid), ruta["nodos"]
    return None


def recursos_html(datos: dict) -> str:
    recs = datos.get("recursos") or []
    if not recs:
        return ""
    items = "".join(
        f'<li><a href="{html.escape(r["url"])}">{html.escape(str(r["titulo"]))}</a></li>' for r in recs
    )
    return f'<section class="fuentes"><h2>Fuentes y para leer más</h2><ul>{items}</ul></section>'


# ---------------------------------------------------------------- páginas

def pagina_nodo(grafo: dict, nodo: dict, locales: dict[str, dict], raiz: str, raiz_mod: str,
                local: str | None = None) -> str:
    datos, cuerpo = nodo["datos"], nodo["cuerpo"]
    estado = datos.get("estado", "pendiente")
    nid = datos["nodo_base"] if local else datos["id"]
    titulo, historia, profundizar = secciones(cuerpo)
    titulo = datos.get("titulo") or titulo
    archivo_rel = nodo["archivo"].relative_to(RAIZ).as_posix()

    # Encabezado
    ubic = ruta_de(grafo, nid)
    migas = f'<a href="{raiz_mod}index.html">Dinero</a>'
    if ubic:
        migas += f' / <span>Ruta {html.escape(ubic[1])}</span>'
    meta = [NIVELES.get(datos.get("nivel"), ""), sello(estado)]
    otras = ""
    if local:
        otras = (f'<p class="aviso-local">Versión para {PAISES.get(local, local)}. Complementa el nodo general '
                 f'<a href="../index.html">{html.escape(nodo.get("titulo_base", ""))}</a> con leyes, cifras y entidades del país.</p>')
    elif locales:
        enlaces = " ".join(
            f'<a class="boton-pais" href="{p}/index.html">Versión para {PAISES.get(p, p)}</a>' for p in sorted(locales)
        )
        otras = f'<p class="paises">{enlaces}</p>'

    cab = (f'<header class="nodo-cab"><p class="migas">{migas}</p>'
           f'<h1>{html.escape(titulo)}</h1>'
           f'<p class="meta">{" ".join(m for m in meta if m)}</p>'
           f'<p class="nota-estado">{ESTADO_NOTA.get(estado, "")}</p>{otras}</header>')

    if estado == "pendiente":
        cuerpo_html = (f'<section class="vacio"><p>Este nodo está en el mapa, pero nadie lo ha escrito todavía.</p>'
                       f'<p><a class="boton" href="{REPO}/issues?q=is%3Aissue+is%3Aopen+{slug_de(nid)}">Ver el Issue para tomarlo</a></p></section>')
        return pagina(f"{titulo} · New Old School", f'<div class="hoja">{cab}{cuerpo_html}</div>', raiz)

    # Historia (Formato Curioso): secciones con su tiempo en el margen
    bloques = []
    for nombre, contenido in historia:
        if not nombre:
            if local:
                contenido = "\n".join(l for l in contenido.splitlines()
                                      if "Adaptación local" not in l and "Kit:" not in l)
            if contenido.strip():
                bloques.append(f'<div class="intro">{md(contenido)}</div>')
            continue
        m = re.match(r"(.*?)\s*\((≈[^)]*)\)\s*$", nombre)
        titulo_sec, tiempo = (m.group(1), m.group(2)) if m else (nombre, "")
        clase = "puerta" if titulo_sec.lower().startswith("la puerta") else ""
        bloques.append(
            f'<section class="tramo {clase}"><p class="tiempo">{html.escape(tiempo)}</p>'
            f'<h2>{html.escape(titulo_sec)}</h2>{md(contenido)}</section>'
        )
    historia_html = f'<article class="cuaderno">{"".join(bloques)}</article>'

    # Profundizar: plegable
    prof = []
    for nombre, contenido in profundizar:
        if not nombre:
            continue
        abierto = " open" if nombre.lower().startswith("puente") else ""
        prof.append(f'<details class="bloque"{abierto}><summary><h2>{html.escape(nombre)}</h2></summary>'
                    f'<div class="bloque-cuerpo">{md(contenido)}</div></details>')
    prof_html = f'<section class="profundizar"><h2 class="sub">Para clase y para profundizar</h2>{"".join(prof)}</section>' if prof else ""

    # Siguiente en la ruta
    sig = ""
    if ubic and not local:
        i, nombre_ruta, pos, ids = ubic
        if pos + 1 < len(ids):
            nxt = ids[pos + 1]
            t = next((n["titulo"] for n in grafo["nodos"] if n["id"] == nxt), nxt)
            sig = (f'<nav class="siguiente ruta-{i % 5}"><span>Sigue en la ruta {html.escape(nombre_ruta)}</span>'
                   f'<a href="{raiz_mod}{slug_de(nxt)}/index.html">{html.escape(t)}</a></nav>')

    acciones = (f'<ul class="acciones"><li><a href="{REPO}/edit/main/{archivo_rel}">Sugerir un cambio</a></li>'
                f'<li><a href="{REPO}/issues/new?template=3-error-contenido.yml">Reportar un error</a></li>'
                f'<li><a href="{REPO}/blob/main/{archivo_rel}">Ver el archivo en GitHub</a></li></ul>')

    cuerpo_html = historia_html + prof_html + recursos_html(datos) + sig + acciones
    return pagina(f"{titulo} · New Old School", f'<div class="hoja">{cab}{cuerpo_html}</div>', raiz,
                  descripcion=f"{titulo}: nodo del módulo Dinero de New Old School.")


def pagina_modulo(grafo: dict, nucleo: dict, locales: dict) -> str:
    total = len(grafo["nodos"])
    escritos = sum(1 for n in nucleo.values() if n["datos"].get("estado") not in ("pendiente", None))
    aprobados = sum(1 for n in nucleo.values() if n["datos"].get("estado") == "aprobado")
    n_loc = sum(1 for por_pais in locales.values() for d in por_pais.values() if d["datos"].get("estado") != "pendiente")
    cuerpo = f"""
<section class="portada">
  <p class="migas"><a href="../index.html">Módulos</a></p>
  <h1>{html.escape(grafo["titulo"])}</h1>
  <p class="pregunta"><mark>{html.escape(grafo.get("gran_pregunta", ""))}</mark></p>
  <p class="lead">{html.escape(" ".join(grafo.get("descripcion", "").split()))}</p>
  <p class="cuenta">{escritos} de {total} temas escritos, {aprobados} aprobados, {n_loc} adaptados a Colombia.</p>
</section>
<section class="rutas">
  <h2>Elige una ruta</h2>
  <p class="ayuda">Cada línea es una ruta y se recorre en orden. Cada parada es un tema de unos cinco minutos de lectura, con ejercicios y un caso práctico. Si es tu primera vez, empieza por Base.</p>
  {mapa_rutas(grafo, nucleo, "")}
  <ul class="leyenda">
    <li><span class="punto p-en-revision"></span> En revisión: borrador completo</li>
    <li><span class="punto p-aprobado"></span> Aprobado</li>
    <li><span class="punto p-pendiente"></span> Por escribir: puedes tomarlo</li>
  </ul>
</section>
"""
    return pagina("Dinero · New Old School", cuerpo, "../",
                  descripcion=grafo.get("gran_pregunta", ""))


def pagina_inicio(mods: list[dict]) -> str:
    tarjetas = "".join(
        f'<li><a href="{m["modulo"]}/index.html"><strong>{html.escape(m["titulo"])}</strong>'
        f'<span>{html.escape(m.get("gran_pregunta", ""))}</span></a></li>' for m in mods
    )
    cuerpo = f"""
<section class="inicio">
  <h1>Lo que casi no se enseña<br>y la vida te va a pedir.</h1>
  <p class="lead">New Old School es un colegio virtual abierto y gratuito. Empezamos por los saberes prácticos que antes se aprendían en casa o en el oficio, y desde ahí llegamos a las matemáticas, las ciencias y la historia.</p>
  <p class="lead">Cada tema se lee en unos cinco minutos, como una historia, y trae ejercicios, un caso práctico y una guía para el docente.</p>
</section>
<section class="modulos">
  <h2>Módulos</h2>
  <ul class="lista-modulos">{tarjetas}
    <li class="proximo"><strong>Próximamente</strong><span>Derechos, salud, autonomía, pensamiento crítico y más. Ayúdanos a escribirlos.</span></li>
  </ul>
</section>
<section class="colaborar">
  <h2>Hecho entre muchos</h2>
  <p>Cualquier persona puede escribir, revisar o adaptar un tema a su país. Usamos IA para escribir borradores, y personas para revisarlos. Todo queda en <a href="{REPO}">GitHub</a>, con licencia abierta.</p>
</section>
"""
    return pagina("New Old School", cuerpo, "")


# ---------------------------------------------------------------- principal

def construir(salida: Path) -> int:
    if salida.exists():
        shutil.rmtree(salida)
    salida.mkdir(parents=True)
    shutil.copy(ESTILOS, salida / "estilos.css")
    (salida / ".nojekyll").write_text("")
    mods, paginas = [], 0
    for carpeta in modulos():
        grafo, nucleo, locales = leer_nodos(carpeta)
        mods.append(grafo)
        dmod = salida / grafo["modulo"]
        dmod.mkdir()
        (dmod / "index.html").write_text(pagina_modulo(grafo, nucleo, locales), encoding="utf-8")
        paginas += 1
        for nid, nodo in nucleo.items():
            dnodo = dmod / slug_de(nid)
            dnodo.mkdir()
            loc = {p: d for p, d in locales.get(nid, {}).items() if d["datos"].get("estado") != "pendiente"}
            (dnodo / "index.html").write_text(pagina_nodo(grafo, nodo, loc, "../../", "../"), encoding="utf-8")
            paginas += 1
            for pais, lnodo in loc.items():
                lnodo["titulo_base"] = nodo["datos"]["titulo"]
                (dnodo / pais).mkdir()
                (dnodo / pais / "index.html").write_text(
                    pagina_nodo(grafo, lnodo, {}, "../../../", "../../", local=pais), encoding="utf-8")
                paginas += 1
    (salida / "index.html").write_text(pagina_inicio(mods), encoding="utf-8")
    return paginas + 1


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--salida", default=str(RAIZ / "_sitio"))
    args = p.parse_args()
    n = construir(Path(args.salida))
    print(f"Sitio generado: {n} páginas en {args.salida}")


if __name__ == "__main__":
    main()
