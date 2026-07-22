# Refinar Prosa Canonical Skill Source Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Formalizar `skills/refinar-prosa/` como única fonte comportamental do Prosa Viva, impor divulgação progressiva verificável e preparar os planos #5–#10 para referências localizadas em `pt-BR`.

**Architecture:** O manifesto continua descobrindo a skill por `./skills/`, e nenhuma cópia de `SKILL.md` será criada na raiz. Um validador Python imporá fonte única, orçamentos de linhas, links diretos e ausência de referências vazias; as referências serão criadas e ligadas somente pelas issues que entregarem conteúdo real.

**Tech Stack:** Markdown, YAML, JSON, Python 3 standard library, `rg`, `npx skills`, validador de Agent Skills e validador de plugins Codex.

## Global Constraints

- `skills/refinar-prosa/SKILL.md` é a única entrada comportamental.
- Não criar `SKILL.md` na raiz, cópia de compatibilidade ou conteúdo gerado duplicado.
- O manifesto mantém `"skills": "./skills/"`.
- `agents/openai.yaml` contém somente apresentação e política de invocação.
- Referências de catálogo usam `skills/refinar-prosa/references/pt-BR/`.
- `skills/refinar-prosa/references/preservacao-autoral.md` permanece fora do namespace de idioma.
- Toda referência existente deve ser ligada diretamente pelo `SKILL.md`.
- Não criar referências vazias ou placeholders para antecipar as issues #5–#10.
- Referências não podem exigir leitura encadeada de outra referência.
- `SKILL.md` terá no máximo 250 linhas físicas.
- Cada referência terá no máximo 400 linhas físicas.
- As seis referências terão no máximo 2.000 linhas físicas no total.
- `agents/openai.yaml` terá no máximo 40 linhas físicas.
- A instalação isolada deve descobrir `skills/refinar-prosa/` sem segunda cópia.
- Não criar marketplace, cachebuster, MCP, app, hook ou asset nesta issue.
- Não alterar versão, identificador ou metadados do manifesto.
- Não deixar marcadores incompletos nem metadados específicos do Claude.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `skills/refinar-prosa/SKILL.md` | Declarar a fonte única e a política de divulgação progressiva. |
| `README.md` | Registrar a arquitetura pública, os dois caminhos de distribuição e os orçamentos. |
| `scripts/validate_skill_architecture.py` | Validar fonte única, caminhos, links e limites sem dependências externas. |
| `docs/superpowers/specs/2026-07-22-refinar-prosa-*-patterns-*-design.md` | Usar os caminhos finais `references/pt-BR/`. |
| `docs/superpowers/plans/2026-07-22-refinar-prosa-*-patterns-*.md` | Criar, ligar e validar as referências nos caminhos finais. |

---

### Task 1: Declarar a fonte canônica e adicionar validação durável

**Files:**
- Create: `scripts/validate_skill_architecture.py`
- Modify: `skills/refinar-prosa/SKILL.md`
- Modify: `README.md`
- Test: `scripts/validate_skill_architecture.py`

**Interfaces:**
- Consumes: `.codex-plugin/plugin.json`, o `SKILL.md` atual e qualquer referência que venha a existir sob `skills/refinar-prosa/references/`.
- Produces: comando `python3 scripts/validate_skill_architecture.py`, com exit code `0` para arquitetura válida e mensagens de erro específicas para cada invariante.

- [ ] **Step 1: Executar a verificação negativa da decisão ainda não registrada**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
missing = []
for item in ["## Fonte canônica e divulgação progressiva", "references/pt-BR/"]:
    if item not in skill:
        missing.append(f"SKILL.md: {item}")
for item in ["## Arquitetura da skill", "250 linhas", "2.000 linhas"]:
    if item not in readme:
        missing.append(f"README.md: {item}")
print("\n".join(missing))
raise SystemExit(not missing)
PY
```

Expected: exit code `1` e pelo menos uma linha para `SKILL.md` e uma para
`README.md`.

- [ ] **Step 2: Criar o validador arquitetural**

Use `apply_patch` para criar `scripts/validate_skill_architecture.py` com este
conteúdo:

```python
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
```

- [ ] **Step 3: Confirmar que o validador não exige placeholders**

Run:

```bash
python3 scripts/validate_skill_architecture.py
```

Expected: exit code `0` neste estado inicial, porque ainda não existem
referências e a decisão textual é validada no Step 1. Este passo comprova que o
validador não exige placeholders.

- [ ] **Step 4: Adicionar a decisão ao `SKILL.md`**

Use `apply_patch` para inserir depois da introdução:

```markdown
## Fonte canônica e divulgação progressiva

Este arquivo e suas referências sob `skills/refinar-prosa/` são a única fonte
do comportamento. Não procure nem mantenha outro `SKILL.md` na raiz.

As referências gerais vivem em `references/`, e os grupos editoriais desta
versão vivem em `references/pt-BR/`. Carregue somente referências ligadas
diretamente por este arquivo e relevantes aos sinais encontrados. Não dependa de
encadeamento entre referências nem crie arquivos vazios para grupos ainda não
implementados.
```

- [ ] **Step 5: Adicionar a arquitetura ao README**

Use `apply_patch` para inserir antes de `## Como funcionará`:

```markdown
## Arquitetura da skill

O comportamento possui uma única fonte canônica:
`skills/refinar-prosa/SKILL.md`. O plugin encontra essa pasta pelo campo
`"skills": "./skills/"`, e a instalação isolada usa o mesmo diretório. Não há
`SKILL.md` duplicado na raiz.

O arquivo principal contém contrato, modos, auditoria e roteamento. Regras
detalhadas são carregadas sob demanda: preservação autoral fica em
`references/preservacao-autoral.md`, enquanto o catálogo desta versão fica em
`references/pt-BR/`. Cada referência é ligada diretamente pelo `SKILL.md` quando
seu conteúdo passa a existir.

Os limites de manutenção são 250 linhas para o `SKILL.md`, 400 linhas para cada
referência, 2.000 linhas para o conjunto das referências e 40 linhas para
`agents/openai.yaml`. O comando `python3 scripts/validate_skill_architecture.py`
verifica esses invariantes.
```

- [ ] **Step 6: Validar a decisão e a arquitetura**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

skill = Path("skills/refinar-prosa/SKILL.md").read_text()
readme = Path("README.md").read_text()
for item in ["## Fonte canônica e divulgação progressiva", "references/pt-BR/", "Não procure nem mantenha outro `SKILL.md`"]:
    assert item in skill, item
for item in ["## Arquitetura da skill", "250 linhas", "400 linhas", "2.000 linhas", "40 linhas"]:
    assert item in readme, item
print("canonical architecture documentation: ok")
PY
python3 scripts/validate_skill_architecture.py
```

Expected: duas linhas, `canonical architecture documentation: ok` e
`canonical skill architecture: ok`, com exit code `0`.

- [ ] **Step 7: Commitar a fonte canônica e o validador**

```bash
git add skills/refinar-prosa/SKILL.md README.md scripts/validate_skill_architecture.py
git commit -m "feat: enforce canonical skill architecture"
```

### Task 2: Migrar os designs e planos do catálogo para `references/pt-BR/`

**Files:**
- Modify: `docs/superpowers/specs/2026-07-22-refinar-prosa-content-patterns-1-6-design.md`
- Modify: `docs/superpowers/plans/2026-07-22-refinar-prosa-content-patterns-1-6.md`
- Modify: `docs/superpowers/specs/2026-07-22-refinar-prosa-language-patterns-7-13-design.md`
- Modify: `docs/superpowers/plans/2026-07-22-refinar-prosa-language-patterns-7-13.md`
- Modify: `docs/superpowers/specs/2026-07-22-refinar-prosa-formatting-patterns-14-19-design.md`
- Modify: `docs/superpowers/plans/2026-07-22-refinar-prosa-formatting-patterns-14-19.md`
- Modify: `docs/superpowers/specs/2026-07-22-refinar-prosa-communication-patterns-20-25-design.md`
- Modify: `docs/superpowers/plans/2026-07-22-refinar-prosa-communication-patterns-20-25.md`
- Modify: `docs/superpowers/specs/2026-07-22-refinar-prosa-advanced-style-patterns-26-33-design.md`
- Modify: `docs/superpowers/plans/2026-07-22-refinar-prosa-advanced-style-patterns-26-33.md`
- Test: the same ten files

**Interfaces:**
- Consumes: final path convention from Task 1.
- Produces: executable plans that create and link references only under `references/pt-BR/`.

- [ ] **Step 1: Demonstrar os caminhos antigos ainda presentes**

Run:

```bash
rg -l 'references/(conteudo|linguagem|formatacao|comunicacao|estilo-avancado)\.md' \
  docs/superpowers/specs/2026-07-22-refinar-prosa-{content-patterns-1-6,language-patterns-7-13,formatting-patterns-14-19,communication-patterns-20-25,advanced-style-patterns-26-33}-design.md \
  docs/superpowers/plans/2026-07-22-refinar-prosa-{content-patterns-1-6,language-patterns-7-13,formatting-patterns-14-19,communication-patterns-20-25,advanced-style-patterns-26-33}.md
```

Expected: exit code `0` e os dez arquivos listados.

- [ ] **Step 2: Executar a substituição mecânica dos cinco caminhos**

Run:

```bash
sed -i \
  -e 's#references/conteudo\.md#references/pt-BR/conteudo.md#g' \
  -e 's#references/linguagem\.md#references/pt-BR/linguagem.md#g' \
  -e 's#references/formatacao\.md#references/pt-BR/formatacao.md#g' \
  -e 's#references/comunicacao\.md#references/pt-BR/comunicacao.md#g' \
  -e 's#references/estilo-avancado\.md#references/pt-BR/estilo-avancado.md#g' \
  docs/superpowers/specs/2026-07-22-refinar-prosa-{content-patterns-1-6,language-patterns-7-13,formatting-patterns-14-19,communication-patterns-20-25,advanced-style-patterns-26-33}-design.md \
  docs/superpowers/plans/2026-07-22-refinar-prosa-{content-patterns-1-6,language-patterns-7-13,formatting-patterns-14-19,communication-patterns-20-25,advanced-style-patterns-26-33}.md
```

Expected: exit code `0`. Este é um rewrite mecânico de caminhos; não alterar
outro conteúdo dos documentos.

- [ ] **Step 3: Confirmar ausência dos caminhos antigos e cobertura dos novos**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

pairs = {
    "content-patterns-1-6": "conteudo.md",
    "language-patterns-7-13": "linguagem.md",
    "formatting-patterns-14-19": "formatacao.md",
    "communication-patterns-20-25": "comunicacao.md",
    "advanced-style-patterns-26-33": "estilo-avancado.md",
}
for stem, filename in pairs.items():
    paths = [
        Path(f"docs/superpowers/specs/2026-07-22-refinar-prosa-{stem}-design.md"),
        Path(f"docs/superpowers/plans/2026-07-22-refinar-prosa-{stem}.md"),
    ]
    old = f"references/{filename}"
    new = f"references/pt-BR/{filename}"
    for path in paths:
        text = path.read_text()
        assert old not in text, (path, old)
        assert new in text, (path, new)
print("catalog paths: 10/10 ok")
PY
```

Expected: exit code `0` e saída `catalog paths: 10/10 ok`.

- [ ] **Step 4: Confirmar que preservação autoral continua no núcleo**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

paths = [
    Path("docs/superpowers/specs/2026-07-22-refinar-prosa-authorial-preservation-design.md"),
    Path("docs/superpowers/plans/2026-07-22-refinar-prosa-authorial-preservation.md"),
]
for path in paths:
    text = path.read_text()
    assert "references/preservacao-autoral.md" in text, path
    assert "references/pt-BR/preservacao-autoral.md" not in text, path
print("core preservation path: ok")
PY
```

Expected: exit code `0` e saída `core preservation path: ok`.

- [ ] **Step 5: Commitar a migração documental**

```bash
git add docs/superpowers/specs docs/superpowers/plans
git commit -m "docs: namespace pt-BR references"
```

### Task 3: Verificar descoberta da skill independente

**Files:**
- Modify: `README.md`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `README.md`

**Interfaces:**
- Consumes: estrutura canônica da Task 1.
- Produces: evidência de que a raiz descobre `refinar-prosa` sem instalar uma cópia alternativa.

- [ ] **Step 1: Listar skills descobertas pelo instalador**

Run:

```bash
npx skills add . --list
```

Expected: exit code `0` e saída contendo `refinar-prosa`. O comando não deve
criar `SKILL.md` na raiz nem modificar arquivos versionados. Se a ferramenta não
estiver disponível ou não aceitar `--list`, registrar a incompatibilidade da
versão e interromper esta task; não criar uma cópia como contorno.

- [ ] **Step 2: Confirmar que a listagem não alterou o repositório**

Run:

```bash
test ! -e SKILL.md
git status --short
```

Expected: `test` com exit code `0`; status contendo somente alterações já
esperadas da implementação, sem arquivos gerados pelo `npx skills`.

- [ ] **Step 3: Registrar no README o comando verificado**

Use `apply_patch` para acrescentar ao final de `## Arquitetura da skill`:

````markdown
Durante o desenvolvimento, confirme que a instalação independente encontra a
fonte canônica sem instalar nada:

```bash
npx skills add . --list
```

A saída deve incluir `refinar-prosa`. A instalação e a remoção propriamente
ditas serão documentadas depois do teste completo da #21.
````

- [ ] **Step 4: Validar a documentação da descoberta**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path("README.md").read_text()
assert "npx skills add . --list" in text
assert "A saída deve incluir `refinar-prosa`" in text
assert "#21" in text
print("standalone discovery documentation: ok")
PY
```

Expected: exit code `0` e saída `standalone discovery documentation: ok`.

- [ ] **Step 5: Commitar a descoberta independente verificada**

```bash
git add README.md
git commit -m "docs: verify standalone skill discovery"
```

### Task 4: Executar validação integrada da #17

**Files:**
- Test: `.codex-plugin/plugin.json`
- Test: `skills/refinar-prosa/SKILL.md`
- Test: `skills/refinar-prosa/agents/openai.yaml`
- Test: `scripts/validate_skill_architecture.py`
- Test: `README.md`
- Test: `docs/superpowers/specs/*.md`
- Test: `docs/superpowers/plans/*.md`

**Interfaces:**
- Consumes: Tasks 1–3.
- Produces: evidência de fonte única, descoberta nos dois fluxos e pacote válido.

- [ ] **Step 1: Executar o validador arquitetural**

Run:

```bash
python3 scripts/validate_skill_architecture.py
```

Expected: exit code `0` e saída `canonical skill architecture: ok`.

- [ ] **Step 2: Executar os validadores da skill e do plugin**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: ambos com exit code `0` e mensagens de validação bem-sucedida.

- [ ] **Step 3: Auditar fonte única, orçamentos e ausência de placeholders**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

root = Path(".")
skills = sorted(root.glob("skills/**/SKILL.md"))
assert skills == [Path("skills/refinar-prosa/SKILL.md")], skills
assert not Path("SKILL.md").exists()
assert len(Path("skills/refinar-prosa/SKILL.md").read_text().splitlines()) <= 250
assert len(Path("skills/refinar-prosa/agents/openai.yaml").read_text().splitlines()) <= 40
assert not list(Path("skills/refinar-prosa").rglob("*.empty"))
print("single source and budgets: ok")
PY
rg -n -i 'claude|\.claude-plugin|marketplace\.json|placeholder|\[preencher\]' .codex-plugin skills scripts README.md
```

Expected: Python com exit code `0` e saída `single source and budgets: ok`;
`rg` com exit code `1` e nenhuma saída.

- [ ] **Step 4: Verificar diff e estado do repositório**

Run:

```bash
git diff --check
git status --short --branch
```

Expected: `git diff --check` sem saída; branch correta e nenhum arquivo
inesperado ou alteração não commitada.

- [ ] **Step 5: Não criar commit vazio**

Se os passos anteriores não exigirem correção, não criar commit. Se houver uma
correção estritamente limitada aos arquivos desta issue, aplicá-la com
`apply_patch`, repetir todos os passos da Task 4 e então executar:

```bash
git add .codex-plugin/plugin.json skills/refinar-prosa README.md scripts/validate_skill_architecture.py docs/superpowers/specs docs/superpowers/plans
git commit -m "fix: validate canonical skill architecture"
```
