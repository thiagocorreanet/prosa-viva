#!/usr/bin/env python3
"""Validate the canonical Refinar Prosa skill layout."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "refinar-prosa"
SKILL = SKILL_DIR / "SKILL.md"
AGENT = SKILL_DIR / "agents" / "openai.yaml"
REFERENCES = SKILL_DIR / "references"
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"

ALLOWED_REFERENCES = {
    "references/preservacao-autoral.md",
    "references/pt-BR/conteudo.md",
    "references/pt-BR/linguagem.md",
    "references/pt-BR/formatacao.md",
    "references/pt-BR/comunicacao.md",
    "references/pt-BR/estilo-avancado.md",
}


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    if not SKILL.is_file():
        fail(f"missing canonical skill: {SKILL.relative_to(ROOT)}")

    product_skills = sorted(ROOT.glob("skills/**/SKILL.md"))
    if product_skills != [SKILL]:
        names = [str(path.relative_to(ROOT)) for path in product_skills]
        fail(f"expected one product SKILL.md, found: {names}")
    if (ROOT / "SKILL.md").exists():
        fail("root SKILL.md is forbidden")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("skills") != "./skills/":
        fail('plugin manifest must keep "skills": "./skills/"')

    if line_count(SKILL) > 250:
        fail(f"SKILL.md exceeds 250 lines: {line_count(SKILL)}")
    if line_count(AGENT) > 40:
        fail(f"agents/openai.yaml exceeds 40 lines: {line_count(AGENT)}")

    skill_text = SKILL.read_text(encoding="utf-8")
    linked = set(
        re.findall(r"\[[^\]]+\]\((references/[^)]+\.md)\)", skill_text)
    )
    existing_paths = sorted(REFERENCES.rglob("*.md")) if REFERENCES.exists() else []
    existing = {
        path.relative_to(SKILL_DIR).as_posix() for path in existing_paths
    }

    unexpected = existing - ALLOWED_REFERENCES
    if unexpected:
        fail(f"unexpected reference paths: {sorted(unexpected)}")
    broken = linked - existing
    if broken:
        fail(f"broken reference links: {sorted(broken)}")
    unlinked = existing - linked
    if unlinked:
        fail(f"existing references not linked by SKILL.md: {sorted(unlinked)}")

    total_reference_lines = 0
    for path in existing_paths:
        count = line_count(path)
        relative = path.relative_to(ROOT)
        if count == 0:
            fail(f"empty reference is forbidden: {relative}")
        if count > 400:
            fail(f"reference exceeds 400 lines: {relative} ({count})")
        total_reference_lines += count
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)", text):
            clean_target = target.split("#", 1)[0]
            if "://" in clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            if REFERENCES.resolve() in resolved.parents and resolved != path.resolve():
                fail(f"chained reference requirement in {relative}: {target}")
    if total_reference_lines > 2000:
        fail(f"references exceed 2,000 total lines: {total_reference_lines}")

    print("canonical skill architecture: ok")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as error:
        print(f"canonical skill architecture: {error}", file=sys.stderr)
        raise SystemExit(1)
