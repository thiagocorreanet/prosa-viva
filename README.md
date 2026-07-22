<div align="center">

# Prosa Viva

### Escrita mais natural, sem trocar clareza por teatro.

Um plugin nativo para Codex que revisa textos em português, preserva o que o
autor quis dizer e devolve ritmo, precisão e voz à prosa.

[![Status: em planejamento](https://img.shields.io/badge/status-em%20planejamento-F5A623)](https://github.com/thiagocorreanet/prosa-viva/issues)
[![Plataforma: Codex](https://img.shields.io/badge/plataforma-Codex-111111)](https://developers.openai.com/codex/)
[![Idioma principal: pt-BR](https://img.shields.io/badge/idioma-pt--BR-009C3B)](https://github.com/thiagocorreanet/prosa-viva/issues/19)

[Visão](#visão) ·
[Como funcionará](#como-funcionará) ·
[Exemplo](#exemplo) ·
[Roadmap](#roadmap) ·
[Contribuir](#como-contribuir)

</div>

> [!IMPORTANT]
> O Prosa Viva está em fase de definição e ainda não possui uma versão
> instalável. Acompanhe a [épica do projeto](https://github.com/thiagocorreanet/prosa-viva/issues/1)
> ou as [releases](https://github.com/thiagocorreanet/prosa-viva/releases) para
> saber quando a primeira versão estiver disponível.

## Visão

Textos gerados ou excessivamente polidos por modelos de linguagem costumam
chegar ao mesmo lugar: frases corretas, organizadas e esquecíveis. Tudo parece
importante. Toda conclusão é otimista. Todo parágrafo anuncia o próximo.

O Prosa Viva será um editor de prosa para Codex. Seu trabalho não será
“disfarçar IA”, mas revisar textos com critérios editoriais claros:

- preservar fatos, nomes, números, datas, citações e ressalvas;
- remover fórmulas vazias sem apagar informações;
- adaptar o texto ao público, ao gênero e à voz do autor;
- reconhecer quando uma escolha incomum é estilo, não defeito;
- editar somente o necessário.

## Princípios

### O significado vem antes da forma

Parágrafos podem ser divididos, unidos ou reorganizados. O conteúdo factual não
pode desaparecer nem ser substituído por uma versão mais conveniente.

### Natural não significa casual

Um relatório técnico, uma política interna e um ensaio pessoal pedem vozes
diferentes. O Prosa Viva não transformará todo texto em conversa de internet.

### Nenhum detalhe será inventado

A reescrita não acrescentará experiências, fontes, datas, estatísticas,
opiniões ou exemplos concretos que não estejam na entrada.

### Contexto vale mais que listas de palavras

Um travessão, uma frase curta ou a palavra “fundamental” não provam nada
sozinhos. A revisão considerará conjuntos de sinais e respeitará escolhas
legítimas do autor.

### Texto bom também sabe parar

Se o original já estiver claro e natural, a melhor revisão pode ser não mudar
nada.

## Exemplo

**Antes**

> Em um cenário corporativo cada vez mais dinâmico, registrar decisões de
> maneira eficaz desempenha um papel fundamental para equipes distribuídas,
> garantindo alinhamento e evitando que as mesmas discussões sejam retomadas em
> reuniões futuras.

**Depois**

> Equipes distribuídas precisam registrar decisões com clareza. Sem esse
> registro, reuniões futuras retomam discussões já encerradas.

A segunda versão preserva as duas afirmações do original: o registro mantém a
equipe alinhada e evita repetir discussões. A mudança está na forma, não nos
fatos.

## Como funcionará

O projeto prevê três modos de uso.

### Texto colado

```text
Use $refinar-prosa para revisar o texto abaixo.
Mantenha o tom profissional e não altere nenhuma informação factual.

[texto]
```

O Codex devolverá o texto revisado. Explicações sobre as alterações serão
incluídas somente quando solicitadas.

### Edição de arquivo

```text
Use $refinar-prosa para revisar docs/guia.md.
Preserve frontmatter, links, tabelas e blocos de código.
```

Somente a prosa será editada. Estruturas protegidas permanecerão intactas.

### Calibração de voz

```text
Use $refinar-prosa.

Esta é uma amostra da minha escrita:
[amostra]

Agora revise este rascunho:
[rascunho]
```

A amostra servirá como referência para ritmo, vocabulário, pontuação,
formalidade e hábitos do autor.

## O que o Prosa Viva não fará

- Não garantirá resultados em detectores de texto gerado por IA.
- Não afirmará que um texto foi escrito por uma pessoa.
- Não funcionará como verificador de fatos.
- Não transformará incerteza legítima em certeza.
- Não acrescentará personalidade a textos que pedem neutralidade.
- Não substituirá revisão jurídica, acadêmica ou técnica especializada.

## Catálogo editorial

O catálogo inicial está sendo pesquisado e adaptado para português brasileiro.
Ele será organizado em cinco grupos:

| Grupo | Cobertura planejada |
| --- | --- |
| Conteúdo | importância inflada, promoção, atribuições vagas e seções formulaicas |
| Linguagem | vocabulário repetitivo, paralelismos, sinônimos e sintaxe artificial |
| Formatação | títulos, listas, negrito, emojis, aspas e travessões |
| Comunicação | resíduos de chatbot, bajulação, preenchimento e hesitação |
| Cadência | frases de efeito, dramatização, aforismos e falsas espontaneidades |

Os padrões não serão uma tradução mecânica de regras inglesas. A
[pesquisa linguística em português](https://github.com/thiagocorreanet/prosa-viva/issues/18)
definirá exemplos, limites e falsos positivos.

## Qualidade como requisito

Além de validar a estrutura do plugin, o projeto pretende testar o comportamento
editorial:

- preservação de todas as afirmações da fonte;
- ausência de fatos ou fontes inventadas;
- proteção de Markdown e conteúdo não textual;
- manutenção de voz e grau de formalidade;
- pouca ou nenhuma alteração em textos já adequados;
- estabilidade após executar a revisão mais de uma vez;
- casos positivos e falsos positivos para cada padrão.

Veja a [suíte de avaliações](https://github.com/thiagocorreanet/prosa-viva/issues/15)
e as [regressões de idempotência](https://github.com/thiagocorreanet/prosa-viva/issues/20).

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

## Roadmap

| Etapa | Entregas | Issues |
| --- | --- | --- |
| Fundação | Estrutura Codex, fonte única e idiomas suportados | [#2](https://github.com/thiagocorreanet/prosa-viva/issues/2), [#17](https://github.com/thiagocorreanet/prosa-viva/issues/17), [#19](https://github.com/thiagocorreanet/prosa-viva/issues/19) |
| Núcleo editorial | Contrato de reescrita, modos e calibração de voz | [#3](https://github.com/thiagocorreanet/prosa-viva/issues/3), [#4](https://github.com/thiagocorreanet/prosa-viva/issues/4) |
| Pesquisa e padrões | Português brasileiro, catálogo editorial e falsos positivos | [#5–#10](https://github.com/thiagocorreanet/prosa-viva/issues/5), [#18](https://github.com/thiagocorreanet/prosa-viva/issues/18) |
| Qualidade | Validador, CI, avaliações e regressões | [#13–#15](https://github.com/thiagocorreanet/prosa-viva/issues/13), [#20](https://github.com/thiagocorreanet/prosa-viva/issues/20) |
| Distribuição | Documentação, manutenção, instalação e release | [#11](https://github.com/thiagocorreanet/prosa-viva/issues/11), [#12](https://github.com/thiagocorreanet/prosa-viva/issues/12), [#16](https://github.com/thiagocorreanet/prosa-viva/issues/16), [#21](https://github.com/thiagocorreanet/prosa-viva/issues/21) |

Consulte o [backlog completo](https://github.com/thiagocorreanet/prosa-viva/issues)
para acompanhar decisões e progresso.

## Instalação

Ainda não há uma versão pública. Quando o primeiro pacote estiver pronto, esta
seção documentará:

- instalação como plugin do Codex;
- instalação opcional somente como skill;
- atualização, reinstalação e remoção;
- diferenças entre Codex CLI e aplicativo desktop.

O fluxo está sendo definido na
[issue #21](https://github.com/thiagocorreanet/prosa-viva/issues/21).

## Como contribuir

O projeto está no melhor momento para contribuições de pesquisa e design.

1. Leia a [épica](https://github.com/thiagocorreanet/prosa-viva/issues/1).
2. Escolha uma [issue aberta](https://github.com/thiagocorreanet/prosa-viva/issues).
3. Comente na issue antes de iniciar uma mudança grande.
4. Use exemplos próprios e preserve as fontes de qualquer material adaptado.
5. Inclua casos positivos e falsos positivos quando propuser uma regra.

Contribuições especialmente úteis agora:

- exemplos reais de padrões artificiais em português brasileiro;
- contraexemplos que evitem sobrecorreção;
- textos de diferentes registros para a suíte de avaliação;
- revisão linguística, editorial e de acessibilidade.

## Referências e independência

O Prosa Viva nasceu de uma análise do projeto
[blader/humanizer](https://github.com/blader/humanizer) e da discussão pública
sobre sinais recorrentes de escrita gerada por modelos. A implementação será
própria, orientada ao português brasileiro e empacotada nativamente para Codex.

Qualquer conteúdo efetivamente derivado de terceiros será identificado e
atribuído antes da primeira release.

## Licença

A licença será definida antes da versão `0.1.0`. Acompanhe a
[issue #16](https://github.com/thiagocorreanet/prosa-viva/issues/16).

---

<div align="center">

**Prosa Viva** — edição que preserva o que você quis dizer.

</div>
