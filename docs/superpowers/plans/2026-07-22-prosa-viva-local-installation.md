# Prosa Viva Local Installation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Entregar e provar um fluxo reproduzível para instalar, atualizar, reinstalar e remover localmente o plugin Prosa Viva sem alterar a versão canônica do repositório.

**Architecture:** O checkout continua sendo a fonte canônica com SemVer limpa. Um script Python copia apenas a allowlist distribuível para `~/plugins/prosa-viva`; em seguida, os helpers oficiais do `plugin-creator` aplicam o cachebuster na cópia e leem o nome do marketplace pessoal antes de chamar a CLI pública do Codex.

**Tech Stack:** Python 3 (biblioteca padrão e `unittest`), JSON, Codex CLI, helpers oficiais `plugin-creator`, Markdown.

## Global Constraints

- O identificador do plugin é exatamente `prosa-viva`.
- A origem canônica mantém `0.1.0`; cachebusters existem apenas no staging.
- O staging padrão é `~/plugins/prosa-viva` e contém somente `.codex-plugin/`, `skills/`, `README.md` e `LICENSE` quando existir.
- O marketplace pessoal é `~/.agents/plugins/marketplace.json`; seu campo `name` é lido, nunca presumido.
- Não editar manualmente `~/.codex/config.toml`, caches do Codex ou o marketplace durante atualizações.
- Não adicionar MCP, app, hooks, assets vazios nem metadados do Claude.
- Uma conversa nova é obrigatória após reinstalar mudanças de skill ou manifesto.

---

### Task 1: Ferramenta segura de staging

**Files:**
- Create: `tests/test_stage_local_plugin.py`
- Create: `scripts/stage_local_plugin.py`

**Interfaces:**
- Consumes: raiz do checkout contendo `.codex-plugin/plugin.json` com `name: prosa-viva`.
- Produces: `stage_plugin(source: Path, destination: Path) -> tuple[str, ...]` e CLI com `--source` e `--destination`.

- [ ] **Step 1: Escrever testes que definem allowlist e validações**

Criar testes `unittest` que montam um repositório temporário, importam `stage_plugin`, verificam a cópia de `.codex-plugin`, `skills`, `README.md` e `LICENSE`, recusam nome de plugin divergente, recusam destino igual à origem e confirmam que arquivos antigos somem após nova sincronização.

- [ ] **Step 2: Executar os testes e observar a falha esperada**

Run: `python3 -m unittest tests/test_stage_local_plugin.py -v`

Expected: `ModuleNotFoundError` para `scripts.stage_local_plugin`.

- [ ] **Step 3: Implementar a cópia transacional**

Implementar `stage_plugin` com `pathlib`, `json`, `tempfile`, `shutil.copytree`, `Path.replace` e backup vizinho. Validar que fonte e destino são distintos, que o manifesto é um objeto com `name == "prosa-viva"`, que `.codex-plugin` e `skills` existem e que destino não é `/` nem o diretório home. Copiar somente a allowlist para um temporário, renomear o staging anterior para backup, instalar a nova cópia e restaurar o backup se a troca falhar.

- [ ] **Step 4: Executar a suíte e validar a CLI em diretório temporário**

Run: `python3 -m unittest tests/test_stage_local_plugin.py -v`

Expected: todos os casos com `OK`.

Run: `python3 scripts/stage_local_plugin.py --destination /tmp/prosa-viva-stage-test/prosa-viva`

Expected: lista de arquivos copiados sem `.git`, `docs` ou `evals`.

- [ ] **Step 5: Commitar a ferramenta testada**

```bash
git add scripts/stage_local_plugin.py tests/test_stage_local_plugin.py
git commit -m "feat: add safe local plugin staging"
```

### Task 2: Documentação do ciclo local

**Files:**
- Modify: `README.md`
- Test: `tests/test_local_installation_docs.py`

**Interfaces:**
- Consumes: `scripts/stage_local_plugin.py` e comandos públicos `codex plugin add|list|remove`.
- Produces: instruções separadas de instalação inicial, atualização/reinstalação, remoção e instalação somente como skill.

- [ ] **Step 1: Escrever teste documental**

Criar um teste `unittest` que leia `README.md` e exija os títulos `Instalação local como plugin`, `Atualização e reinstalação`, `Remoção` e `Instalação somente como skill`, além dos comandos `stage_local_plugin.py`, `update_plugin_cachebuster.py`, `read_marketplace_name.py`, `codex plugin add`, `codex plugin list`, `codex plugin remove` e `npx skills add`.

- [ ] **Step 2: Executar o teste e observar a falha esperada**

Run: `python3 -m unittest tests/test_local_installation_docs.py -v`

Expected: falha porque o README ainda descreve a instalação como futura.

- [ ] **Step 3: Substituir a seção de instalação**

Documentar que os helpers citados pertencem à skill de sistema `$plugin-creator`; usar os comandos exatos do script do projeto e da CLI; explicar staging, cachebuster, leitura do marketplace, nova conversa, reinício do desktop somente após mudança de fonte e a diferença da instalação independente da skill.

- [ ] **Step 4: Executar os testes documentais e de staging**

Run: `python3 -m unittest discover -s tests -v`

Expected: todos os casos com `OK`.

- [ ] **Step 5: Commitar a documentação**

```bash
git add README.md tests/test_local_installation_docs.py
git commit -m "docs: document local plugin lifecycle"
```

### Task 3: Prova do ciclo real no Codex

**Files:**
- Modify outside repository: `/home/thiago-botelho/plugins/prosa-viva/.codex-plugin/plugin.json`
- Verify outside repository: `/home/thiago-botelho/.agents/plugins/marketplace.json`

**Interfaces:**
- Consumes: staging gerado nas Tasks 1–2 e marketplace pessoal existente.
- Produces: plugin `prosa-viva@personal` instalado com um único cachebuster e removível pela CLI pública.

- [ ] **Step 1: Validar checkout e gerar staging**

```bash
python3 scripts/validate_skill_architecture.py
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
python3 scripts/stage_local_plugin.py
```

Expected: três validadores aprovam e o staging contém somente a allowlist.

- [ ] **Step 2: Aplicar cachebuster apenas no staging**

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py /home/thiago-botelho/plugins/prosa-viva --cachebuster local-20260722-issue21
```

Expected: staging usa `0.1.0+codex.local-20260722-issue21` e checkout continua em `0.1.0`.

- [ ] **Step 3: Ler o marketplace e instalar**

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/read_marketplace_name.py
codex plugin add prosa-viva@personal --json
codex plugin list --json
```

Expected: nome lido `personal`; listagem mostra `prosa-viva@personal` instalado com a versão cachebustada.

- [ ] **Step 4: Provar remoção e reinstalação pública**

```bash
codex plugin remove prosa-viva@personal --json
codex plugin list --json
codex plugin add prosa-viva@personal --json
codex plugin list --json
```

Expected: a primeira listagem não inclui o plugin instalado; a segunda volta a incluí-lo sem alterar a entrada do marketplace.

- [ ] **Step 5: Executar verificação integrada e conferir o diff**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_skill_architecture.py
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
npx skills add . --list
git diff --check
git status --short
```

Expected: testes e validadores aprovam, `refinar-prosa` é descoberto, não há erro de whitespace e a versão versionada permanece `0.1.0`.

- [ ] **Step 6: Commitar o plano e enviar a conclusão**

```bash
git add docs/superpowers/plans/2026-07-22-prosa-viva-local-installation.md
git commit -m "docs: plan local plugin lifecycle"
git push origin main
gh issue close 21 --comment "Implementado e validado o ciclo local de instalação, atualização, reinstalação e remoção do plugin."
```
