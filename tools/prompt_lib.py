#!/usr/bin/env python3
"""CLI da biblioteca de prompts: list | show | render | validate.

Exemplos:
  python tools/prompt_lib.py list
  python tools/prompt_lib.py render resumo-estruturado --var tema="RAG" --var nivel="iniciante"
  python tools/prompt_lib.py validate
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
import yaml

ARQ = Path(__file__).resolve().parent.parent / "prompts" / "biblioteca.yaml"
CAMPOS = {"id", "objetivo", "variaveis", "template"}


def carregar() -> list[dict]:
    return yaml.safe_load(ARQ.read_text(encoding="utf-8"))["prompts"]


def validar(prompts: list[dict]) -> list[str]:
    erros, vistos = [], set()
    for p in prompts:
        falta = CAMPOS - p.keys()
        if falta:
            erros.append(f"{p.get('id', '?')}: campos ausentes {sorted(falta)}")
            continue
        if p["id"] in vistos:
            erros.append(f"{p['id']}: id duplicado")
        vistos.add(p["id"])
        usadas = set(re.findall(r"\{(\w+)\}", p["template"]))
        if usadas != set(p["variaveis"]):
            erros.append(f"{p['id']}: variáveis declaradas {sorted(p['variaveis'])} != usadas {sorted(usadas)}")
    return erros


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("validate")
    s = sub.add_parser("show")
    s.add_argument("id")
    r = sub.add_parser("render")
    r.add_argument("id")
    r.add_argument("--var", action="append", default=[])
    a = ap.parse_args()
    ps = carregar()
    idx = {p["id"]: p for p in ps}

    if a.cmd == "list":
        for p in ps:
            print(f"{p['id']:<22} {p['objetivo']}  vars={p['variaveis']}")
    elif a.cmd == "validate":
        e = validar(ps)
        print("\n".join(e) if e else f"OK: {len(ps)} prompts válidos")
        return 1 if e else 0
    elif a.cmd == "show":
        print(idx[a.id]["template"])
    elif a.cmd == "render":
        p = idx[a.id]
        vals = dict(v.split("=", 1) for v in a.var)
        faltam = set(p["variaveis"]) - vals.keys()
        if faltam:
            print(f"Faltam variáveis: {sorted(faltam)}", file=sys.stderr)
            return 2
        print(p["template"].format(**vals))
    return 0


if __name__ == "__main__":
    sys.exit(main())
