#!/usr/bin/env python3
"""Valida os requisitos do desafio DIO: estrutura, 3-5 fontes, seções do README, prompts."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

RAIZ = Path(__file__).resolve().parent.parent
OBRIGATORIOS = ["README.md", "LICENSE", "sources/fontes.yaml", "prompts/biblioteca.yaml",
                "docs/miniguia.md", "docs/glossario.md", "docs/engenharia-de-prompts.md", "docs/troubleshooting.md"]
SECOES = ["Contexto e Objetivos", "Curadoria de Fontes", "Engenharia de Prompts", "Miniguia de Estudo"]


def main() -> int:
    erros = [f"arquivo ausente: {f}" for f in OBRIGATORIOS if not (RAIZ / f).exists()]
    fontes = yaml.safe_load((RAIZ / "sources/fontes.yaml").read_text(encoding="utf-8"))["fontes"]
    if not 3 <= len(fontes) <= 5:
        erros.append(f"o desafio pede 3 a 5 fontes; encontradas {len(fontes)}")
    erros += [f"fonte {f.get('id')}: URL deve ser https" for f in fontes if not str(f.get("url", "")).startswith("https://")]
    readme = (RAIZ / "README.md").read_text(encoding="utf-8") if (RAIZ / "README.md").exists() else ""
    erros += [f"README sem seção: {s}" for s in SECOES if s not in readme]
    sys.path.insert(0, str(RAIZ / "tools"))
    import prompt_lib
    erros += prompt_lib.validar(prompt_lib.carregar())
    print("\n".join(f"✗ {e}" for e in erros) if erros else "✓ Repositório válido para entrega")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
