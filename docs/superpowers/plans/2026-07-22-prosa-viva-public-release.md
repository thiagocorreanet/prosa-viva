# Prosa Viva Public Release Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar o Prosa Viva v0.1.0 como plugin Codex instalável pelo GitHub, com licença MIT, marketplace Git, validação contínua e GitHub Release automatizada.

**Architecture:** O repositório funciona simultaneamente como fonte do plugin e marketplace de um item. O marketplace aponta por `source: url` para a raiz da tag imutável `v0.1.0`; um validador Python aplica a mesma política localmente e nos workflows de CI e release.

**Tech Stack:** Python 3.12 e `unittest`, JSON, GitHub Actions, GitHub CLI, Codex CLI.

## Global Constraints

- Plugin, marketplace e pasta usam o identificador exato `prosa-viva`.
- A primeira versão pública e sua tag são `0.1.0` e `v0.1.0`.
- Builds públicos não aceitam sufixo `+codex.*`.
- A licença é MIT, copyright 2026 Thiago Corrêa.
- A fonte pública é `https://github.com/thiagocorreanet/prosa-viva.git` fixada em `v0.1.0`.
- Não adicionar MCP, app, hooks, assets vazios ou manifestos do Claude.
- `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` corresponde a v7.0.1.
- `actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97` corresponde a v7.0.0.
- Não criar a tag até o workflow de validação de `main` passar.

---

### Task 1: Validador testável de release

**Files:**
- Create: `tests/test_validate_release.py`
- Create: `scripts/validate_release.py`

**Interfaces:**
- Consumes: `validate_release(root: Path, tag: str | None = None) -> tuple[str, ...]`.
- Produces: CLI `python3 scripts/validate_release.py [--tag v0.1.0] [--root PATH]` com exit 0 para pacote válido e mensagem única em stderr para pacote inválido.

- [ ] **Step 1: Escrever fixtures e testes que definem a política**

Criar `ReleaseValidationTests` com um `setUp` que gera `prosa-viva/` temporário contendo manifesto `0.1.0`, marketplace remoto `v0.1.0`, licença MIT, README, `skills/refinar-prosa/SKILL.md`, `agents/openai.yaml` e `docs/releases/v0.1.0.md`.

Os testes devem chamar a API real e cobrir estes resultados:

```python
self.assertIn("release=v0.1.0", validate_release(self.root, "v0.1.0"))
with self.assertRaisesRegex(ValueError, "tag"):
    validate_release(self.root, "v0.1.1")
with self.assertRaisesRegex(ValueError, "cachebuster"):
    validate_release(self.root_with_version("0.1.0+codex.local-test"))
with self.assertRaisesRegex(ValueError, "marketplace"):
    validate_release(self.root_with_marketplace_ref("v0.1.1"))
with self.assertRaisesRegex(ValueError, "LICENSE"):
    validate_release(self.root_without("LICENSE"))
with self.assertRaisesRegex(ValueError, "Claude"):
    validate_release(self.root_with_file(".claude-plugin/plugin.json", "{}"))
with self.assertRaisesRegex(ValueError, "placeholder"):
    validate_release(self.root_with_file("README.md", "[TODO: release]"))
```

- [ ] **Step 2: Executar a suíte e observar a ausência do módulo**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_validate_release.py -v`

Expected: FAIL com `ModuleNotFoundError: No module named 'scripts.validate_release'`.

- [ ] **Step 3: Implementar o validador mínimo**

Implementar:

```python
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?$")
PLUGIN_NAME = "prosa-viva"
REPOSITORY_URL = "https://github.com/thiagocorreanet/prosa-viva"
SOURCE_URL = REPOSITORY_URL + ".git"
REQUIRED_FILES = (
    "LICENSE",
    "README.md",
    "skills/refinar-prosa/SKILL.md",
    "skills/refinar-prosa/agents/openai.yaml",
)
```

Criar helpers `load_object(path: Path) -> dict[str, object]`,
`require_string(payload: dict[str, object], field: str, source: Path) -> str`,
`resolve_declared_path(root: Path, value: str) -> Path` e
`scan_forbidden_content(root: Path) -> None`. A função `validate_release` deve
usar esses helpers para validar tipos antes de acessar campos, resolver caminhos
relativos contra `root`, recusar caminhos fora da raiz, exigir os metadados e
políticas da especificação e retornar `("plugin=prosa-viva",
"version=0.1.0", "release=v0.1.0")` no caso válido. A CLI captura exceções,
imprime a mensagem em stderr e termina com status 1.

- [ ] **Step 4: Executar testes e validar regressão**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_validate_release.py -v`

Expected: todos os casos com `OK`.

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`

Expected: suíte completa com `OK`.

- [ ] **Step 5: Commitar o validador**

```bash
git add scripts/validate_release.py tests/test_validate_release.py
git commit -m "feat: validate public plugin releases"
```

### Task 2: Pacote público, licença e documentação

**Files:**
- Create: `.agents/plugins/marketplace.json`
- Create: `LICENSE`
- Create: `docs/releases/v0.1.0.md`
- Modify: `.codex-plugin/plugin.json`
- Modify: `README.md`
- Modify: `tests/test_local_installation_docs.py`

**Interfaces:**
- Consumes: política de `scripts/validate_release.py`.
- Produces: marketplace instalável `prosa-viva`, pacote MIT e instruções públicas completas.

- [ ] **Step 1: Estender os testes documentais primeiro**

Exigir no README os comandos:

```text
codex plugin marketplace add thiagocorreanet/prosa-viva
codex plugin add prosa-viva@prosa-viva
codex plugin marketplace upgrade prosa-viva
codex plugin remove prosa-viva@prosa-viva
```

Exigir também `v0.1.0`, `MIT`, `npx skills add thiagocorreanet/prosa-viva` e uma
seção separada `## Desenvolvimento local`.

- [ ] **Step 2: Executar o teste e observar a falha documental**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_local_installation_docs.py -v`

Expected: FAIL porque a instalação pública e a release ainda não constam no README.

- [ ] **Step 3: Criar os metadados públicos**

Criar `.agents/plugins/marketplace.json` com esta forma:

```json
{
  "name": "prosa-viva",
  "interface": { "displayName": "Prosa Viva" },
  "plugins": [
    {
      "name": "prosa-viva",
      "source": {
        "source": "url",
        "url": "https://github.com/thiagocorreanet/prosa-viva.git",
        "ref": "v0.1.0"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Adicionar o texto padrão da licença MIT com `Copyright (c) 2026 Thiago Corrêa`.
No manifesto, manter `version: 0.1.0` e trocar somente `author.name` para
`Thiago Corrêa`.

- [ ] **Step 4: Escrever notas e reorganizar o README**

Criar `docs/releases/v0.1.0.md` com capacidades, instalação plugin/skill,
limitações pt-BR, ausência de promessas sobre detectores ou autoria humana e
link para issues. No README, tornar a instalação Git o fluxo principal e mover
staging/cachebuster para `## Desenvolvimento local`.

- [ ] **Step 5: Executar validações do pacote público**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`

Run: `python3 scripts/validate_release.py`

Run: `python3 scripts/validate_release.py --tag v0.1.0`

Expected: testes com `OK`; ambos os comandos imprimem `release=v0.1.0`.

- [ ] **Step 6: Commitar pacote e documentação**

```bash
git add .agents/plugins/marketplace.json LICENSE docs/releases/v0.1.0.md .codex-plugin/plugin.json README.md tests/test_local_installation_docs.py
git commit -m "feat: prepare prosa viva v0.1.0"
```

### Task 3: GitHub Actions de validação e publicação

**Files:**
- Create: `tests/test_release_workflows.py`
- Create: `.github/workflows/validate.yml`
- Create: `.github/workflows/release.yml`

**Interfaces:**
- Consumes: `scripts/validate_release.py` e `docs/releases/<tag>.md`.
- Produces: CI read-only para `main`/PR e release automática para tags SemVer.

- [ ] **Step 1: Escrever testes estruturais dos workflows**

Os testes devem ler os YAMLs como texto e exigir:

```python
self.assertIn("pull_request:", validate_workflow)
self.assertIn("branches: [main]", validate_workflow)
self.assertIn("contents: read", validate_workflow)
self.assertNotIn("contents: write", validate_workflow)
self.assertIn("tags:", release_workflow)
self.assertIn("'v*.*.*'", release_workflow)
self.assertIn("contents: write", release_workflow)
self.assertIn("gh release create", release_workflow)
self.assertIn("--verify-tag", release_workflow)
self.assertIn("git archive", release_workflow)
self.assertIn("sha256sum", release_workflow)
```

Ambos devem conter os dois SHAs oficiais definidos nas restrições globais e
nenhum `uses:` adicional.

- [ ] **Step 2: Executar o teste e observar a ausência dos workflows**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_release_workflows.py -v`

Expected: ERROR por ausência de `.github/workflows/validate.yml`.

- [ ] **Step 3: Criar `validate.yml`**

Configurar `push` para `[main]`, `pull_request`, `permissions: contents: read`,
Ubuntu latest, checkout/setup-python fixados por SHA, Python `3.12` e estes
comandos:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skill_architecture.py
python3 scripts/validate_release.py
```

- [ ] **Step 4: Criar `release.yml`**

Configurar tag `'v*.*.*'`, permissão de job `contents: write`, os mesmos testes
e `python3 scripts/validate_release.py --tag "$GITHUB_REF_NAME"`. Empacotar com:

```bash
git archive --format=zip --prefix=prosa-viva/ \
  --output="prosa-viva-${GITHUB_REF_NAME}.zip" HEAD \
  .codex-plugin skills README.md LICENSE
sha256sum "prosa-viva-${GITHUB_REF_NAME}.zip" \
  > "prosa-viva-${GITHUB_REF_NAME}.zip.sha256"
```

Publicar com:

```bash
gh release create "$GITHUB_REF_NAME" \
  --verify-tag \
  --title "Prosa Viva ${GITHUB_REF_NAME}" \
  --notes-file "docs/releases/${GITHUB_REF_NAME}.md" \
  "prosa-viva-${GITHUB_REF_NAME}.zip" \
  "prosa-viva-${GITHUB_REF_NAME}.zip.sha256"
```

- [ ] **Step 5: Executar suíte e simular o asset local**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`

Run: `python3 scripts/validate_release.py --tag v0.1.0`

Run: `git archive --format=zip --prefix=prosa-viva/ --output=/tmp/prosa-viva-v0.1.0.zip HEAD .codex-plugin skills README.md LICENSE`

Run: `unzip -Z1 /tmp/prosa-viva-v0.1.0.zip`

Expected: somente a allowlist sob `prosa-viva/`.

- [ ] **Step 6: Commitar os workflows**

```bash
git add .github/workflows/validate.yml .github/workflows/release.yml tests/test_release_workflows.py
git commit -m "ci: automate plugin validation and releases"
```

### Task 4: Publicar e provar a instalação Git

**Files:**
- Create: tag Git `v0.1.0`.
- Create externally: GitHub Release `v0.1.0` e assets.
- Update externally: marketplace/config/cache do Codex pelos comandos públicos.

**Interfaces:**
- Consumes: commit validado de `main` e workflows da Task 3.
- Produces: release pública instalável e issue #16 concluída.

- [ ] **Step 1: Executar verificação local final**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/validate_skill_architecture.py
python3 scripts/validate_release.py --tag v0.1.0
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
git diff --check
git status --short --branch
```

Expected: tudo aprovado, árvore limpa e `main` à frente apenas pelos commits da release.

- [ ] **Step 2: Enviar `main` e aguardar CI**

```bash
git push origin main
gh run list --workflow validate.yml --branch main --limit 1
PROSA_VIVA_VALIDATE_RUN_ID="$(gh run list --workflow validate.yml --branch main --limit 1 --json databaseId --jq '.[0].databaseId')"
gh run watch "${PROSA_VIVA_VALIDATE_RUN_ID}" --exit-status
```

Expected: workflow `validate` concluído com `success` no commit atual.

- [ ] **Step 3: Criar e enviar tag anotada**

```bash
git tag -a v0.1.0 -m "Prosa Viva v0.1.0"
git push origin v0.1.0
```

Expected: tag aponta exatamente para o HEAD validado.

- [ ] **Step 4: Aguardar e verificar a GitHub Release**

```bash
gh run list --workflow release.yml --branch v0.1.0 --limit 1
PROSA_VIVA_RELEASE_RUN_ID="$(gh run list --workflow release.yml --branch v0.1.0 --limit 1 --json databaseId --jq '.[0].databaseId')"
gh run watch "${PROSA_VIVA_RELEASE_RUN_ID}" --exit-status
gh release view v0.1.0 --json tagName,name,isDraft,isPrerelease,assets,url
```

Expected: release não draft, não prerelease, com ZIP e `.sha256`.

- [ ] **Step 5: Testar instalação pública real**

```bash
codex plugin remove prosa-viva@personal --json
codex plugin marketplace add thiagocorreanet/prosa-viva --json
codex plugin add prosa-viva@prosa-viva --json
codex plugin list --marketplace prosa-viva --json
```

Expected: plugin instalado do marketplace Git na versão `0.1.0`.

- [ ] **Step 6: Testar em sessão nova**

Run: `codex exec --ephemeral --sandbox read-only --color never 'Use $refinar-prosa em modo embutido para revisar: Em um cenário corporativo cada vez mais dinâmico, registrar decisões de maneira eficaz desempenha um papel fundamental.'`

Expected: a sessão lê `skills/refinar-prosa/SKILL.md` do cache
`prosa-viva/prosa-viva/0.1.0` e devolve somente a revisão.

- [ ] **Step 7: Fechar a issue e confirmar estado final**

```bash
gh issue close 16 --comment "Publicada a v0.1.0 com licença MIT, marketplace Git, CI, release automatizada e instalação pública validada em sessão nova."
git status --short --branch
```

Expected: issue #16 fechada e `main` sincronizada com `origin/main`.
