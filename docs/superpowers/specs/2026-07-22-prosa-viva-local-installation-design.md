# Instalação, atualização e reinstalação local do Prosa Viva

## Contexto

Esta especificação registra a decisão da issue #21 e prepara a distribuição da
#16. O repositório é a fonte canônica do plugin, mas o Codex instala plugins
locais em cache. Alterar diretamente o checkout não garante que uma conversa já
aberta carregue a versão nova.

O fluxo precisa testar o pacote real sem registrar cachebusters de desenvolvimento
no Git, duplicar manualmente a skill ou editar configurações internas do Codex.

## Decisão

Usar o marketplace pessoal como fonte de desenvolvimento e uma cópia de staging
fora do repositório:

```text
checkout limpo
  → validar
  → copiar pacote instalável para ~/plugins/prosa-viva
  → aplicar um cachebuster somente na cópia
  → marketplace pessoal aponta para ./plugins/prosa-viva
  → codex plugin add prosa-viva@<nome-do-marketplace>
  → testar em conversa nova
```

O checkout preserva a versão SemVer limpa, como `0.1.0`. A cópia de staging usa
`0.1.0+codex.local-<timestamp UTC>` e pode ser recriada a qualquer momento.

## Alternativas consideradas

### Marketplace pessoal com staging — escolhida

Exercita manifesto, cache e instalação reais sem sujar a release nem exigir uma
cópia versionada dentro do projeto.

### Marketplace do próprio repositório

Exigiria transformar o repositório-plugin em catálogo e manter outra árvore
`plugins/prosa-viva`, duplicando o pacote. Foi rejeitado.

### Instalação somente como skill

É útil como alternativa, mas não testa manifesto, metadados nem cache do plugin.
Foi rejeitada como fluxo principal; continua como teste secundário da #17.

## Estado local

- Fonte: checkout atual do repositório.
- Staging padrão: `~/plugins/prosa-viva`.
- Marketplace padrão: `~/.agents/plugins/marketplace.json`.
- Nome do marketplace: lido do arquivo, nunca presumido como `personal`.
- Cache instalado: gerenciado pelo Codex, sem edição manual.

O marketplace e o staging são estado local do desenvolvedor e não entram no
repositório. O projeto não cria `.agents/plugins/marketplace.json` local nem
mantém manifesto do Claude.

## Conteúdo do staging

A cópia contém somente componentes distribuíveis existentes:

```text
.codex-plugin/
skills/
LICENSE, quando existir
README.md
```

Não copia `.git`, `docs/superpowers`, `evals`, caches, arquivos temporários ou
configurações pessoais. A sincronização substitui o staging anterior por uma
nova cópia completa; não mescla árvores antigas.

## Instalação inicial

1. Validar arquitetura, skill e plugin no checkout.
2. Confirmar que o Git está limpo para evitar testar mudanças acidentais.
3. Criar o staging com uma ferramenta versionada no projeto.
4. Aplicar cachebuster no manifesto da cópia usando o helper oficial do
   `plugin-creator`.
5. Criar ou atualizar a entrada do marketplace pessoal pelo fluxo oficial do
   `plugin-creator`, sem edição manual de `config.toml`.
6. Ler o nome do marketplace com `read_marketplace_name.py`.
7. Instalar com `codex plugin add prosa-viva@<nome>`.
8. Confirmar descoberta com `codex plugin list` e no aplicativo, quando
   disponível.
9. Abrir uma conversa nova e invocar `$refinar-prosa`.

Se o marketplace pessoal já tiver outra entrada `prosa-viva`, o fluxo confirma
que ela aponta para o staging esperado antes de substituí-la. Não usa `--force`
sem essa verificação.

## Atualização e reinstalação

Para cada alteração no manifesto, skill ou metadados:

1. validar o checkout;
2. recriar o staging;
3. substituir o sufixo anterior por um único cachebuster UTC;
4. ler novamente o nome do marketplace;
5. executar `codex plugin add prosa-viva@<nome>`;
6. confirmar que a versão instalada contém o novo cachebuster;
7. testar em conversa nova.

O helper preserva tudo antes de `+` e gera exatamente:

```text
<versão-base>+codex.local-YYYYMMDD-HHMMSS
```

Nunca incrementa a versão base para invalidar cache e nunca acumula dois
sufixos `+codex`.

## Reinicialização

- Mudança em skill, manifesto ou metadados após reinstalação: testar em conversa
  nova.
- Criação, remoção ou mudança de fonte do marketplace: reiniciar o aplicativo
  desktop antes de procurar o plugin.
- Interface ainda desatualizada após reinstalação: atualizar a lista e reiniciar
  o aplicativo; não editar o cache.
- Codex CLI: iniciar nova sessão depois da reinstalação.

## Remoção

A implementação primeiro consultará `codex plugin --help` para usar o comando de
remoção disponível na versão instalada. Depois:

1. remover/desabilitar o plugin pelo comando público;
2. confirmar ausência na listagem;
3. remover a entrada local com o fluxo oficial do marketplace, quando o teste
   exigir limpeza total;
4. remover apenas o staging conhecido `~/plugins/prosa-viva`;
5. confirmar que não restou entrada quebrada.

Não apagar caches, diretórios amplos ou arquivos de configuração manualmente.

## Ferramenta de staging

O projeto terá um script Python sem dependências externas que:

- exige a raiz do repositório como fonte;
- valida nome `prosa-viva` e manifesto antes de copiar;
- aceita destino explícito e usa o padrão somente quando omitido;
- recusa raiz, home ou destino fora do staging esperado;
- cria staging temporário, copia a allowlist e troca os diretórios de modo
  recuperável;
- não altera a versão; o helper oficial aplica o cachebuster depois;
- imprime origem, destino e arquivos copiados.

A separação evita duplicar no projeto a lógica oficial de versionamento do
`plugin-creator`.

## Testes

- staging contém somente a allowlist;
- checkout permanece byte a byte com versão limpa;
- cachebuster novo substitui o anterior na cópia;
- manifesto e skill do staging passam nos validadores;
- marketplace tem uma única entrada `prosa-viva`;
- reinstalação torna uma mudança observável em conversa nova;
- remoção elimina a instalação sem entrada quebrada;
- `npx skills add . --list` continua encontrando a skill independente;
- CLI é testado sempre; aplicativo desktop é testado quando disponível.

## Falhas seguras

- Git sujo: parar antes de staging, salvo quando o teste explicitamente visar as
  mudanças locais já revisadas.
- Marketplace ausente: criar pelo `plugin-creator`; não editar `config.toml`.
- Marketplace não local ou fonte divergente: parar e corrigir a origem.
- Validador falha: não instalar.
- Comando público de remoção indisponível: registrar a limitação e não apagar
  estado interno manualmente.
- Aplicativo desktop indisponível: concluir testes CLI e registrar o teste de UI
  como não executado, sem alegar cobertura desktop.

## Documentação

O README terá comandos separados para instalação inicial, atualização,
reinstalação, remoção e instalação apenas como skill. Comandos específicos do
Claude não serão citados. A #11 reutilizará este fluxo verificado e a #16 o usará
como pré-requisito de distribuição.

## Fora de escopo

- marketplace público ou de equipe;
- publicação de release;
- edição manual de `config.toml` ou cache;
- suporte a app, MCP ou hook;
- sincronização automática em background;
- garantia de teste desktop quando a superfície não estiver disponível.
