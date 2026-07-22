---
name: refinar-prosa
description: "Use para revisar e reescrever prosa em português brasileiro, em texto colado ou arquivos, melhorando clareza e naturalidade sem alterar fatos, estrutura protegida ou voz."
---

# Refinar prosa

Revise somente a prosa em português brasileiro que o usuário colocar no escopo.
Melhore clareza, concisão, ritmo e naturalidade sem trocar o significado pela
forma.

## Fonte canônica e divulgação progressiva

Este arquivo e suas referências sob `skills/refinar-prosa/` são a única fonte
do comportamento. Não procure nem mantenha outro `SKILL.md` na raiz.

As referências gerais vivem em `references/`, e os grupos editoriais desta
versão vivem em `references/pt-BR/`. Carregue somente referências ligadas
diretamente por este arquivo e relevantes aos sinais encontrados. Não dependa de
encadeamento entre referências nem crie arquivos vazios para grupos ainda não
implementados.

## Política linguística

As versões `0.1.x` suportam somente prosa em português brasileiro. Identifique
o idioma pela prosa editável; ignore código, comandos, dados, URLs, frontmatter,
nomes próprios e citações protegidas. Não aplique regras pt-BR a outro idioma e
não use um fallback editorial genérico.

Em documentos mistos, revise apenas segmentos claramente em pt-BR. Preserve
integralmente prosa estrangeira, citações e trechos cuja fronteira linguística
seja incerta. Estrangeirismo técnico ou regionalismo isolado não muda o idioma
do trecho.

### Idioma não suportado

- Texto colado: não reescreva; informe brevemente que esta versão suporta
  somente pt-BR.
- Arquivo: não escreva no arquivo; informe que nenhuma alteração foi realizada.
- Embutido: retorne a entrada exatamente como recebida, sem comentário.

### Idioma ambíguo

- Texto colado: preserve e peça identificação do idioma ou mais contexto.
- Arquivo: não escreva; informe que não foi possível identificar o idioma com
  segurança.
- Embutido: retorne a entrada exatamente como recebida, sem comentário.

Não traduza silenciosamente. Se o pedido combinar tradução e refinamento,
informe no modo conversacional que a tradução precisa ocorrer antes; no modo
embutido, preserve a entrada.

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
