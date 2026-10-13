#!/usr/bin/env python3
"""Valida el currículo: encabezados, ids, prerrequisitos, ciclos y coherencia con el grafo.

Uso:
    python scripts/validar_curriculo.py           # valida; sale con código 1 si hay errores
    python scripts/validar_curriculo.py --estado  # tabla de quién tiene qué
    python scripts/validar_curriculo.py --grafo   # diagrama Mermaid de cada módulo
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from _comun import ALCANCES, CURRICULO, ESTADOS, ORDEN_CAMPOS, RAIZ, cargar_modulo, modulos, separar_encabezado

ID_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+(-[a-z0-9]+)*$")
FECHA_VALIDA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Informe:
    def __init__(self) -> None:
        self.errores: list[str] = []
        self.avisos: list[str] = []

    def error(self, donde: str, msg: str) -> None:
        self.errores.append(f"ERROR  {donde}: {msg}")

    def aviso(self, donde: str, msg: str) -> None:
        self.avisos.append(f"aviso  {donde}: {msg}")


def rel(p: Path) -> str:
    return str(p.relative_to(RAIZ))


def buscar_ciclo(nodos: dict[str, list[str]]) -> list[str] | None:
    blanco, gris, negro = 0, 1, 2
    color = {n: blanco for n in nodos}
    pila: list[str] = []

    def visitar(n: str) -> list[str] | None:
        color[n] = gris
        pila.append(n)
        for m in nodos.get(n, []):
            if m not in color:
                continue
            if color[m] == gris:
                return pila[pila.index(m):] + [m]
            if color[m] == blanco and (c := visitar(m)):
                return c
        pila.pop()
        color[n] = negro
        return None

    for n in nodos:
        if color[n] == blanco and (c := visitar(n)):
            return c
    return None


def validar_grafo(carpeta: Path, grafo: dict[str, Any], inf: Informe) -> dict[str, dict[str, Any]]:
    donde = rel(carpeta / "_modulo.yaml")
    modulo = carpeta.name
    if grafo.get("modulo") != modulo:
        inf.error(donde, f"'modulo' debe ser '{modulo}'")
    por_id: dict[str, dict[str, Any]] = {}
    for n in grafo.get("nodos", []):
        nid = n.get("id", "")
        if not ID_VALIDO.match(nid) or not nid.startswith(f"{modulo}."):
            inf.error(donde, f"id inválido '{nid}' (formato {modulo}.slug-en-minusculas)")
        if nid in por_id:
            inf.error(donde, f"id duplicado '{nid}'")
        por_id[nid] = n
    for nid, n in por_id.items():
        for pre in n.get("prerrequisitos", []):
            if pre not in por_id:
                inf.error(donde, f"'{nid}' tiene un prerrequisito que no existe: '{pre}'")
    ciclo = buscar_ciclo({k: v.get("prerrequisitos", []) for k, v in por_id.items()})
    if ciclo:
        inf.error(donde, "ciclo de prerrequisitos: " + " → ".join(ciclo))
    for lista in ("requieren_local", "referencia"):
        for nid in grafo.get(lista, []):
            if nid not in por_id:
                inf.error(donde, f"'{lista}' menciona un nodo que no existe: '{nid}'")
    return por_id


def validar_nodo(
    archivo: Path, carpeta: Path, por_id: dict[str, dict[str, Any]], modulos_existentes: set[str], inf: Informe
) -> dict[str, Any] | None:
    donde = rel(archivo)
    try:
        d, cuerpo = separar_encabezado(archivo.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        inf.error(donde, str(e))
        return None

    faltan = [c for c in ORDEN_CAMPOS if c not in d]
    if faltan:
        inf.error(donde, "faltan campos: " + ", ".join(faltan))
    sobran = [c for c in d if c not in ORDEN_CAMPOS]
    if sobran:
        inf.error(donde, "campos no permitidos (ver plantilla): " + ", ".join(sobran))

    modulo, slug = carpeta.name, archivo.stem
    id_esperado = f"{modulo}.{slug}"
    if d.get("id") != id_esperado:
        inf.error(donde, f"id '{d.get('id')}' debe ser '{id_esperado}' (coincidir con la ruta)")
    if d.get("modulo") != modulo:
        inf.error(donde, f"'modulo' debe ser '{modulo}'")
    if d.get("estado") not in ESTADOS:
        inf.error(donde, f"estado '{d.get('estado')}' no válido; usa uno de {', '.join(ESTADOS)}")
    if d.get("alcance") not in ALCANCES:
        inf.error(donde, f"alcance '{d.get('alcance')}' no válido; usa nucleo o local")
    if d.get("nivel") not in (1, 2, 3):
        inf.error(donde, "nivel debe ser 1, 2 o 3")
    if not FECHA_VALIDA.match(str(d.get("actualizado", ""))):
        inf.error(donde, "'actualizado' debe ser una fecha AAAA-MM-DD")
    for campo in ("prerrequisitos", "conecta_con", "revisores", "procedencia", "recursos"):
        if not isinstance(d.get(campo, []), list):
            inf.error(donde, f"'{campo}' debe ser una lista")

    estado = d.get("estado")
    if estado in ("en-progreso", "en-revision") and not d.get("responsable"):
        inf.error(donde, f"estado '{estado}' necesita un 'responsable'")
    if estado == "aprobado":
        if not d.get("revisores"):
            inf.error(donde, "un nodo aprobado necesita al menos un usuario en 'revisores'")
        if d.get("responsable") and d.get("responsable") in (d.get("revisores") or []):
            inf.error(donde, "quien es responsable no puede ser su propio revisor")
        if not d.get("procedencia"):
            inf.error(donde, "un nodo aprobado necesita 'procedencia'")
        if "VERIFICAR" in cuerpo:
            inf.error(donde, "un nodo aprobado no puede tener marcas VERIFICAR pendientes")

    en_local = archivo.parent.parent.name == "locales"
    if en_local:
        pais = archivo.parent.name
        if d.get("alcance") != "local" or d.get("pais") != pais:
            inf.error(donde, f"un archivo en locales/{pais}/ necesita alcance: local y pais: {pais}")
        if d.get("nodo_base") != id_esperado:
            inf.error(donde, f"'nodo_base' debe ser '{id_esperado}'")
        if not (carpeta / "nucleo" / archivo.name).exists():
            inf.error(donde, "no existe el nodo del núcleo que adapta")
    else:
        if d.get("alcance") != "nucleo" or d.get("pais") or d.get("nodo_base"):
            inf.error(donde, "un archivo en nucleo/ necesita alcance: nucleo, pais: null y nodo_base: null")
        nodo_grafo = por_id.get(id_esperado)
        if nodo_grafo is None:
            inf.error(donde, "el nodo no está en _modulo.yaml; propónlo al curador del módulo")
        else:
            if sorted(d.get("prerrequisitos") or []) != sorted(nodo_grafo.get("prerrequisitos", [])):
                inf.error(donde, "los prerrequisitos no coinciden con _modulo.yaml")
            if d.get("nivel") != nodo_grafo.get("nivel"):
                inf.aviso(donde, "el nivel no coincide con _modulo.yaml")
        for c in d.get("conecta_con") or []:
            if c.split(".", 1)[0] not in modulos_existentes:
                inf.aviso(donde, f"puente hacia un módulo que aún no existe: {c}")
    return d


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--estado", action="store_true", help="muestra quién tiene cada nodo")
    p.add_argument("--grafo", action="store_true", help="imprime el grafo en Mermaid")
    p.add_argument("--silencioso", action="store_true", help="oculta los avisos")
    a = p.parse_args()

    inf = Informe()
    carpetas = modulos()
    existentes = {c.name for c in carpetas}
    filas: list[tuple[str, str, str, str]] = []

    for carpeta in carpetas:
        grafo = cargar_modulo(carpeta)
        por_id = validar_grafo(carpeta, grafo, inf)

        if a.grafo:
            print(f"\n### {grafo.get('titulo', carpeta.name)}\n\n```mermaid\nflowchart TD")
            for nid, n in por_id.items():
                print(f'  {nid.replace(".", "_").replace("-", "_")}["{n.get("titulo", nid)}"]')
            for nid, n in por_id.items():
                for pre in n.get("prerrequisitos", []):
                    print(f'  {pre.replace(".", "_").replace("-", "_")} --> {nid.replace(".", "_").replace("-", "_")}')
            print("```")

        archivos = sorted((carpeta / "nucleo").glob("*.md")) + sorted((carpeta / "locales").glob("*/*.md"))
        vistos = set()
        for archivo in archivos:
            d = validar_nodo(archivo, carpeta, por_id, existentes, inf)
            if d is None:
                continue
            if d.get("alcance") == "nucleo":
                vistos.add(d.get("id"))
            filas.append((
                str(d.get("id")) + (f" [{d.get('pais')}]" if d.get("pais") else ""),
                str(d.get("estado")),
                str(d.get("responsable") or "—"),
                "sí" if d.get("revision_experta") else "",
            ))
        for nid in por_id:
            if nid not in vistos:
                inf.aviso(rel(carpeta / "_modulo.yaml"), f"'{nid}' aún no tiene archivo en nucleo/")

    if a.estado:
        print(f"\n{'Nodo':<48} {'Estado':<12} {'Responsable':<20} Experto")
        print("-" * 92)
        for f in filas:
            print(f"{f[0]:<48} {f[1]:<12} {f[2]:<20} {f[3]}")
        print()

    if not a.silencioso:
        for m in inf.avisos:
            print(m)
    for m in inf.errores:
        print(m)
    print(f"\n{len(inf.errores)} error(es), {len(inf.avisos)} aviso(s).")
    sys.exit(1 if inf.errores else 0)


if __name__ == "__main__":
    main()
