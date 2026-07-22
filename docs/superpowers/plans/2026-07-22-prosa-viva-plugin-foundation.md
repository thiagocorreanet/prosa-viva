# Prosa Viva Plugin Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar a fundação mínima instalável do Prosa Viva como plugin nativo do Codex, com uma skill pt-BR funcional e metadados válidos.

**Architecture:** A raiz do repositório será a raiz do plugin `prosa-viva`. O manifesto `.codex-plugin/plugin.json` apontará para `./skills/`, e `skills/refinar-prosa/SKILL.md` será a única fonte canônica do comportamento; `agents/openai.yaml` cuidará apenas da apresentação e da política de invocação no Codex.

**Tech Stack:** JSON, YAML, Markdown, Python 3, PyYAML, validadores locais de plugins Codex e Agent Skills.

## Global Constraints

- O nome da pasta raiz e o campo `name` do manifesto são `prosa-viva`.
- A versão inicial é exatamente `0.1.0`.
- A licença declarada é exatamente `MIT`.
- A autoria pública é `thiagocorreanet` e o repositório é `https://github.com/thiagocorreanet/prosa-viva`.
- `skills/refinar-prosa/` é a única fonte canônica; não criar `SKILL.md` na raiz.
- Português brasileiro é o único idioma oficialmente suportado em `0.1.0`.
- Criar somente `.codex-plugin/plugin.json`, `skills/refinar-prosa/SKILL.md` e `skills/refinar-prosa/agents/openai.yaml` como arquivos do produto.
- Não criar ou declarar MCP, apps, hooks, assets, marketplace, referências modulares, ícones, logos, screenshots ou cor de marca.
- Não criar manifestos ou metadados específicos do Claude.
- Não modificar `README.md`; sincronização documental, arquivo `LICENSE`, marketplace e teste em nova sessão permanecem em #16 e #21.
- Todos os caminhos do manifesto devem ser relativos à raiz do plugin e começar com `./`.
- Não deixar marcadores `[TODO: ...]`, `TBD` ou conteúdo vazio.

## File Structure

| Arquivo | Responsabilidade |
| --- | --- |
| `.codex-plugin/plugin.json` | Identidade, versão, autoria, descoberta da skill e apresentação do plugin. |
| `skills/refinar-prosa/SKILL.md` | Fonte canônica do contrato editorial mínimo e do comportamento pt-BR. |
| `skills/refinar-prosa/agents/openai.yaml` | Nome de apresentação, descrição curta, prompt inicial e invocação implícita. |

---

### Task 1: Criar a skill canônica e seus metadados de descoberta

**Files:**
- Create: `skills/refinar-prosa/SKILL.md`
- Create: `skills/refinar-prosa/agents/openai.yaml`

**Interfaces:**
- Consumes: texto ou arquivo solicitado pelo usuário e, opcionalmente, instruções de tom; não consome serviços, ferramentas ou referências externas.
- Produces: skill `refinar-prosa`, invocável como `$refinar-prosa`, com contrato editorial pt-BR e `policy.allow_implicit_invocation: true`.

- [ ] **Step 1: Executar a validação negativa antes de criar a skill**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: exit code `1` e saída `SKILL.md not found`.

- [ ] **Step 2: Criar o contrato editorial mínimo**

Use `apply_patch` para criar `skills/refinar-prosa/SKILL.md` com este conteúdo exato:

````markdown
---
name: refinar-prosa
description: "Use para revisar e reescrever prosa em português brasileiro, em texto colado ou arquivos, melhorando clareza e naturalidade sem alterar fatos, estrutura protegida ou voz."
---

# Refinar prosa

Revise somente a prosa em português brasileiro que o usuário colocar no escopo.
Melhore clareza, concisão, ritmo e naturalidade sem trocar o significado pela
forma.

## Fluxo

1. Confirme que há texto ou um arquivo legível para revisar.
2. Identifique se a prosa está em português brasileiro.
3. Preserve fatos, nomes, números, datas, citações, ressalvas e grau de certeza.
4. Preserve a voz, o registro e as escolhas incomuns que sejam intencionais.
5. Edite somente o necessário; mantenha o original quando não houver melhoria
   útil.
6. Compare a revisão com a fonte e remova qualquer informação acrescentada.
7. Entregue somente o texto revisado, salvo quando o usuário pedir explicações.

## Conteúdo protegido

Ao editar arquivos, preserve frontmatter, links, tabelas, blocos de código e
outros trechos não textuais. Não altere citações nem passagens em outro idioma.

Em documentos mistos, revise apenas a prosa em português brasileiro. Se o texto
estiver claramente em outro idioma, não o modifique; informe brevemente que esta
versão suporta somente pt-BR.

## Limites

- Não invente fatos, fontes, exemplos, experiências ou opiniões.
- Não transforme incerteza em certeza.
- Não prometa detecção de texto gerado por IA.
- Não apresente a revisão como verificação factual ou revisão técnica,
  jurídica ou acadêmica especializada.
- Se a entrada estiver ausente, o arquivo não puder ser lido ou as instruções
  impedirem uma revisão segura, explique o problema antes de editar.

## Exemplos de uso

```text
Use $refinar-prosa para revisar o texto abaixo sem alterar os fatos.

[texto em português brasileiro]
```

```text
Use $refinar-prosa para revisar docs/guia.md e preservar sua estrutura.
```
````

- [ ] **Step 3: Criar os metadados da skill para o Codex**

Use `apply_patch` para criar `skills/refinar-prosa/agents/openai.yaml` com este
conteúdo exato:

```yaml
interface:
  display_name: "Refinar Prosa"
  short_description: "Revise prosa em pt-BR sem perder fatos ou voz"
  default_prompt: "Use $refinar-prosa para revisar o texto abaixo em português brasileiro, preservando fatos, estrutura e voz."

policy:
  allow_implicit_invocation: true
```

- [ ] **Step 4: Validar o frontmatter e os metadados da skill**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: exit code `0` e saída `Skill is valid!`.

Run:

```bash
python3 -c 'from pathlib import Path; import yaml; p=yaml.safe_load(Path("skills/refinar-prosa/agents/openai.yaml").read_text()); i=p["interface"]; assert set(p)=={"interface","policy"}; assert i["display_name"]=="Refinar Prosa"; assert i["short_description"]=="Revise prosa em pt-BR sem perder fatos ou voz"; assert "$refinar-prosa" in i["default_prompt"]; assert p["policy"]["allow_implicit_invocation"] is True; print("openai.yaml valid")'
```

Expected: exit code `0` e saída `openai.yaml valid`.

- [ ] **Step 5: Revisar o escopo da skill**

Run:

```bash
find skills/refinar-prosa -type f -print
```

Expected exatamente estes caminhos, em qualquer ordem:

```text
skills/refinar-prosa/SKILL.md
skills/refinar-prosa/agents/openai.yaml
```

Run:

```bash
rg -n 'pt-BR|português brasileiro|\$refinar-prosa' skills/refinar-prosa
```

Expected: ocorrências em `SKILL.md` e `agents/openai.yaml`, comprovando escopo
linguístico e invocação explícita.

- [ ] **Step 6: Commitar a skill canônica**

```bash
git add skills/refinar-prosa/SKILL.md skills/refinar-prosa/agents/openai.yaml
git commit -m "feat: add refinar-prosa skill"
```

Expected: commit criado contendo somente os dois arquivos da skill.

---

### Task 2: Criar e validar o manifesto do plugin

**Files:**
- Create: `.codex-plugin/plugin.json`
- Test: `.codex-plugin/plugin.json`, `skills/refinar-prosa/SKILL.md`, `skills/refinar-prosa/agents/openai.yaml`

**Interfaces:**
- Consumes: a pasta real `./skills/` e a skill `refinar-prosa` produzida na Task 1.
- Produces: pacote `prosa-viva` versão `0.1.0`, aceito pelo contrato local de ingestão de plugins do Codex.

- [ ] **Step 1: Executar a validação negativa antes de criar o manifesto**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: exit code `1`, cabeçalho `Plugin validation failed:` e erro
`missing \`.codex-plugin/plugin.json\``.

- [ ] **Step 2: Criar o manifesto nativo do Codex**

Use `apply_patch` para criar `.codex-plugin/plugin.json` com este conteúdo exato:

```json
{
  "name": "prosa-viva",
  "version": "0.1.0",
  "description": "Revisa textos em português brasileiro com clareza, naturalidade e preservação factual.",
  "author": {
    "name": "thiagocorreanet",
    "url": "https://github.com/thiagocorreanet"
  },
  "homepage": "https://github.com/thiagocorreanet/prosa-viva",
  "repository": "https://github.com/thiagocorreanet/prosa-viva",
  "license": "MIT",
  "keywords": [
    "escrita",
    "revisão",
    "português",
    "pt-BR",
    "prosa"
  ],
  "skills": "./skills/",
  "interface": {
    "displayName": "Prosa Viva",
    "shortDescription": "Refina prosa em pt-BR sem perder fatos ou voz",
    "longDescription": "Revisa textos em português brasileiro para melhorar clareza, concisão, ritmo e naturalidade, preservando fatos, estrutura e voz.",
    "developerName": "thiagocorreanet",
    "category": "Productivity",
    "capabilities": [
      "Write"
    ],
    "websiteURL": "https://github.com/thiagocorreanet/prosa-viva",
    "defaultPrompt": [
      "Use $refinar-prosa para revisar este texto em pt-BR sem alterar os fatos.",
      "Use $refinar-prosa para revisar este arquivo e preservar sua estrutura."
    ]
  }
}
```

- [ ] **Step 3: Executar o validador completo do plugin**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: exit code `0` e saída iniciada por `Plugin validation passed:` seguida
do caminho absoluto da raiz do repositório.

- [ ] **Step 4: Verificar os contratos que o validador não restringe por valor**

Run:

```bash
python3 -c 'from pathlib import Path; import json; p=json.loads(Path(".codex-plugin/plugin.json").read_text()); i=p["interface"]; assert Path.cwd().name=="prosa-viva"; assert p["name"]=="prosa-viva"; assert "id" not in p; assert p["version"]=="0.1.0"; assert p["license"]=="MIT"; assert p["skills"]=="./skills/"; assert p["author"]=={"name":"thiagocorreanet","url":"https://github.com/thiagocorreanet"}; assert p["homepage"]==p["repository"]=="https://github.com/thiagocorreanet/prosa-viva"; assert p["keywords"]==["escrita","revisão","português","pt-BR","prosa"]; assert i["displayName"]=="Prosa Viva"; assert i["developerName"]=="thiagocorreanet"; assert i["category"]=="Productivity"; assert i["capabilities"]==["Write"]; assert len(i["defaultPrompt"])==2; assert all("$refinar-prosa" in x and len(x)<=128 for x in i["defaultPrompt"]); print("plugin contract valid")'
```

Expected: exit code `0` e saída `plugin contract valid`.

- [ ] **Step 5: Confirmar ausência de placeholders e componentes fora do escopo**

Run:

```bash
rg -n -i 'claude|\.claude-plugin|\[TODO:|TBD' .codex-plugin skills
```

Expected: exit code `1` e nenhuma saída.

Run:

```bash
rg -n '"(apps|mcpServers|hooks|composerIcon|logo|logoDark|screenshots|brandColor)"' .codex-plugin/plugin.json
```

Expected: exit code `1` e nenhuma saída.

Run separadamente; cada comando deve terminar com exit code `0`:

```bash
test ! -e .mcp.json
test ! -e .app.json
test ! -e .claude-plugin
test ! -e marketplace.json
test ! -e assets
test ! -e SKILL.md
```

- [ ] **Step 6: Executar a verificação final da entrega**

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/skill-creator/scripts/quick_validate.py skills/refinar-prosa
```

Expected: `Skill is valid!`.

Run:

```bash
python3 /home/thiago-botelho/.config/orca/codex-accounts/9ae230c7-073c-4dc6-85bc-436aca338b5d/home/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

Expected: `Plugin validation passed:` seguido do caminho absoluto do pacote.

Run:

```bash
git diff --check
```

Expected: exit code `0` e nenhuma saída.

Run:

```bash
git status --short
```

Expected antes do commit: somente `.codex-plugin/plugin.json` como arquivo novo;
os dois arquivos da skill já estão no commit da Task 1.

- [ ] **Step 7: Commitar o manifesto validado**

```bash
git add .codex-plugin/plugin.json
git commit -m "feat: add Codex plugin manifest"
```

Expected: commit criado contendo somente `.codex-plugin/plugin.json`.

- [ ] **Step 8: Confirmar o estado final do pacote**

Run:

```bash
git status --short --branch
```

Expected: árvore de trabalho limpa; a branch local estará à frente do remoto
pelos commits da especificação, do plano e da implementação.
