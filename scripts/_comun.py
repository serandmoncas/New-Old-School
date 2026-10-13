"""Utilidades compartidas por los scripts del currículo."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

RAIZ = Path(__file__).resolve().parent.parent
CURRICULO = RAIZ / "curriculo"
PLANTILLA_NODO = RAIZ / "docs" / "plantillas" / "nodo.md"

ESTADOS = ("pendiente", "en-progreso", "en-revision", "aprobado", "retirado")
ALCANCES = ("nucleo", "local")

# Orden fijo de las claves del encabezado: diffs pequeños y legibles.
ORDEN_CAMPOS = (
    "id",
    "titulo",
    "modulo",
    "alcance",
    "pais",
    "nodo_base",
    "nivel",
    "prerrequisitos",
    "conecta_con",
    "estado",
    "responsable",
    "revisores",
    "revision_experta",
    "procedencia",
    "recursos",
    "actualizado",
)


def separar_encabezado(texto: str) -> tuple[dict[str, Any], str]:
    """Devuelve (encabezado YAML, cuerpo) de un archivo Markdown con front matter."""
    if not texto.startswith("---"):
        raise ValueError("el archivo no empieza con un encabezado YAML (---)")
    partes = texto.split("---", 2)
    if len(partes) < 3:
        raise ValueError("el encabezado YAML no está cerrado con ---")
    datos = yaml.safe_load(partes[1]) or {}
    if not isinstance(datos, dict):
        raise ValueError("el encabezado YAML no es un diccionario")
    return datos, partes[2].lstrip("\n")


def escribir_encabezado(datos: dict[str, Any], cuerpo: str) -> str:
    ordenado = {k: datos.get(k) for k in ORDEN_CAMPOS}
    yaml_txt = yaml.safe_dump(
        ordenado, sort_keys=False, allow_unicode=True, default_flow_style=None, width=100
    )
    return f"---\n{yaml_txt}---\n\n{cuerpo}"


def cargar_modulo(carpeta: Path) -> dict[str, Any]:
    with (carpeta / "_modulo.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def modulos() -> list[Path]:
    return sorted(p for p in CURRICULO.iterdir() if (p / "_modulo.yaml").exists())
