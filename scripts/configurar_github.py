#!/usr/bin/env python3
"""Crea en GitHub las etiquetas de `.github/labels.yml` (requiere `gh` autenticado).

Uso:
    python scripts/configurar_github.py --repo <organizacion>/new-old-school
"""

from __future__ import annotations

import argparse
import subprocess

import yaml

from _comun import RAIZ


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--repo", required=True)
    a = p.parse_args()

    etiquetas = yaml.safe_load((RAIZ / ".github" / "labels.yml").read_text(encoding="utf-8"))
    for e in etiquetas:
        subprocess.run(
            ["gh", "label", "create", e["name"], "--repo", a.repo, "--color", e["color"],
             "--description", e["description"], "--force"],
            check=True,
        )
        print(f"ok  {e['name']}")


if __name__ == "__main__":
    main()
