# Transcricao dos Slides - Git e GitHub

> Origem: `1_git.pdf` (148 paginas) - Gerencia de Configuracao (IC/UFAM).

## Indice dos Topicos

- [1. Fundamentos de Controle de Versao (Slides 2 a 9)](#1-fundamentos-de-controle-de-versao)
- [2. Arquitetura e Principios Basicos do Git (Slides 10 a 14)](#2-arquitetura-e-principios-basicos-do-git)
- [3. Configuracao Inicial e Autoria (Slides 15 a 19)](#3-configuracao-inicial-e-autoria)
- [4. Ciclo de Vida e os Tres Estados (Slides 20 a 29)](#4-ciclo-de-vida-e-os-tres-estados)
- [5. Ignorando Arquivos com .gitignore (Slides 30 a 35)](#5-ignorando-arquivos-com-gitignore)
- [6. Visualizacao de Mudancas, Status e Logs (Slides 36 a 44)](#6-visualizacao-de-mudancas-status-e-logs)
- [7. Branches e o Ponteiro HEAD (Slides 45 a 56)](#7-branches-e-o-ponteiro-head)
- [8. Integracao de Branches: Fast-Forward e Merge Commit (Slides 57 a 69)](#8-integracao-de-branches-fast-forward-e-merge-commit)
- [9. Conflitos de Merge e Resolucao (Slides 70 a 85)](#9-conflitos-de-merge-e-resolucao)
- [10. Repositorios Remotos, Clones e Push (Slides 86 a 102)](#10-repositorios-remotos-clones-e-push)
- [11. Git Pull, Git Fetch e Sincronizacao (Slides 103 a 111)](#11-git-pull-git-fetch-e-sincronizacao)
- [12. Rebase versus Merge (Slides 112 a 118)](#12-rebase-versus-merge)
- [13. Desfazendo Alteracoes e Modos de Reset (Slides 119 a 135)](#13-desfazendo-alteracoes-e-modos-de-reset)
- [14. Historico de Movimentos com Git Reflog (Slides 136 a 140)](#14-historico-de-movimentos-com-git-reflog)
- [15. Corrigindo Commits com Git Amend (Slides 141 a 145)](#15-corrigindo-commits-com-git-amend)
- [16. Armazenamento Temporario com Git Stash (Slides 146 a 148)](#16-armazenamento-temporario-com-git-stash)

---

### Slide 1

Prof. David Fernandes de Oliveira

Instituto de Computação

UFAM

Git + GitHub

---

### Slide 2

Controle de Versão

- Sistemas de Controle de Versão registram as alterações

realizadas em um conjunto de arquivos ao longo do tempo.

- O uso de um sistema de controle de versão permite:

  - restaurar arquivos ou todo o projeto para uma versão anterior

  - comparar as alterações realizadas ao longo do tempo

  - facilitar o trabalho colaborativo de uma equipe

  - registrar a data, a hora, o autor e a descrição de cada alteração

---

### Slide 3

Controle de Versão Local

- Uma das formas mais simples de controlar versões é criar

cópias dos arquivos ou projetos em diferentes diretórios

- Embora seja uma prática comum, essa abordagem não gera

histórico estruturado das alterações e é propensa a erros

  - É difícil saber o que alteriou de uma pasta para outra

---

### Slide 4

Controle de Versão Local

- Para lidar com esse problema, alguns programadores

desenvolveram sistemas de controle de versão locais

  - Tais sistemas armazenavam todas as alterações dos arquivos em

várias versões dos mesmos

Imagens retiradas do

livro Pro Git,

disponível

gratuitamente no

site oficial do Git

---

### Slide 5

Controle de Versão Centralizado

- Em muitas ocasiões, é necessário trabalhar em conjunto com

outros desenvolvedores

- Para lidar com isso, foram desenvolvidos os sistemas de

controle de versão centralizados

---

### Slide 6

Controle de Versão Centralizado

- Problemas com o controle de versão centralizado:

  - Se o servidor ficar fora do ar, ninguém poderá acessar o

mecanismo de versionamento ou salvar seus arquivos

  - Se o servidor for corrompido e não houver backup, perde-se

todo o histórico de mudanças do projeto

- Os desenvolvedores ficam apenas com a versão atual do projeto

de suas máquinas

---

### Slide 7

Controle de Versão Distribuídos

- Na abordagem distribuída, as estações de trabalho (clientes)

também possuem cópias completas do repositório

---

### Slide 8

Centralizado x Distribuído

- Uma desvantagem da abordagem centralizada é que quase

nada do controle de versão funciona offiline

Centralizado (Subversion)

Servidor

cópia

cópia

cópia

Histórico existe só no servidor. Offline, quase

nada funciona.

Distribuído (Git)

Remoto

repo completo

repo completo

repo completo

Cada clone tem todo o histórico. Commit, branch

e log funcionam offline.

---

### Slide 9

Popularidade do Git

---

### Slide 10

O que é o Git?

- É um sistema de controle de

versão distribuído, desen-

volvido a partir de 2005

- Foi criado em 2005 por Linus

Torvalds, com algumas

contribuições da comunidade de

desenvolvedores do kernel do

Linux

---

### Slide 11

Noções Básicas de Git

- Outra diferença entre Git e outros SCV (Subversion, CVS, etc)

está na forma que o Git armazena os dados

- A maior parte dos sistemas armazena informação como uma

lista de mudanças por arquivo

---

### Slide 12

Noções Básicas de Git

- O Git, por outro lado, registra cada commit como uma

fotografia completa dos arquivos do projeto

- Arquivos que não foram modificados são reutilizados por

referência, evitando cópias desnecessárias

---

### Slide 13

Inicializando um Repositório

- Para começar a versionar com Git um projeto que já existe,

acesse o diretório do projeto pelo terminal e execute:

  - git init

  - Esse comando cria um diretório .git dentro do projeto, que

armazena todos os dados de controle de versões do sistema

---

### Slide 14

Exercício

- Desenvolva um sistema Hello World usando Express/TypeScript

e então inicialize o repositório Git usando git init

  - Para isso, siga as intruções dos slides sobre o SmartNotes, até a

seção Hello World em Express/TypeScript

---

### Slide 15

Configuração Inicial do Git

- O Git possui uma ferramenta chamada git config, utilizada

para definir e consultar variáveis de configuração

- Essas configurações podem ser armazenadas em três níveis:

  - /etc/gitconfig: aplica-se a todos os usuários e repositórios do

sistema. É configurado com a opção --system

  - ~/.gitconfig: aplica-se a todos os repositórios do usuário atual.

É configurado com a opção --global

  - .git/config: aplica-se apenas ao repositório atual. É configurado

com a opção --local

- Quando uma mesma configuração é definida em mais de um

nível, o nível mais específico tem prioridade:

  - local > global > system

---

### Slide 16

Configuração Inicial do Git

- Após instalar o Git, é importante configurar o nome e o

endereço de e-mail do usuário

  - O Git essas informações para identificar o autor de cada commit

e registrar quem realizou as alterações no repositório

  - Também é útil definir o editor e o nome da branch padrões

---

### Slide 17

Configuração Inicial do Git

- Após instalar o Git, é importante configurar o nome e o

endereço de e-mail do usuário

  - O Git essas informações para identificar o autor de cada commit

e registrar quem realizou as alterações no repositório

  - Também é útil definir o editor e o nome da branch padrões

Muito importante: É preciso configurar seu nome de usuário e email sempre

que for usar uma máquina dos labs para trabalhar nas atividades da

disciplina. Isso é importante para viabilizar o acesso ao histórico de commits

e analisar a contribuição de cada um no projeto da disciplina.

---

### Slide 18

Configuração Inicial do Git

- Após instalar o Git, é importante configurar o nome e o

endereço de e-mail do usuário

  - O Git essas informações para identificar o autor de cada commit

e registrar quem realizou as alterações no repositório

  - Também é útil definir o editor e o nome da branch padrões

Muito importante: É preciso configurar seu nome de usuário e email sempre

que for usar uma máquina dos labs para trabalhar nas atividades da

disciplina. Isso é importante para viabilizar o acesso ao histórico de commits

e analisar a contribuição de cada um no projeto da disciplina.

Para isso, siga as orientações do README.md do repositório

https://github.com/dbfernandes/git-config

---

### Slide 19

Configuração Inicial do Git

- Após instalar o Git, é importante configurar o nome e o

endereço de e-mail do usuário

  - O Git essas informações para identificar o autor de cada commit

e registrar quem realizou as alterações no repositório

  - Também é útil definir o editor e o nome da branch padrões

Muito importante: É preciso configurar seu nome de usuário e email sempre

que for usar uma máquina dos labs para trabalhar nas atividades da

disciplina. Isso é importante para viabilizar o acesso ao histórico de commits

e analisar a contribuição de cada um no projeto da disciplina.

Para isso, siga as orientações do README.md do repositório

https://github.com/dbfernandes/git-config

---

### Slide 20

Fluxo de Trabalho

- Após criar um repositório, o fluxo básico de trabalho consiste em:

  - Modificar os arquivos do projeto

  - Selecionar as alterações que farão parte do próximo commit,

utilizando git add

  - Registrar essas alterações no histórico, utilizando git commit

---

### Slide 21

O Primeiro Commit

- Para começar a versionar os arquivos existentes de um

projeto, é necessário:

  - adicionar os arquivos desejados à staging area

  - criar um commit para registrar essas alterações no histórico do

repositório

---

### Slide 22

Os Três Estados

- Desta forma, o Git faz com que seus arquivos sempre estejam

em um dos três estados fundamentais:

  - Modificado (modified), quando

o arquivo sofreu mudanças

mas ainda não foi selecionado

  - Selecionado (staged), quando

você marca um arquivo

modificado para que ele faça

parte do  próximo commit

(consolidação)

  - Consolidado (committed),

quando os arquivos estão

seguramente salvos em seu

repositório local

---

### Slide 23

Adicionando um arquivo

- É possível incluir novos arquivos no repositório local

normalmente, usando editores ou recursos do SO

- A ferramenta git status pode ser usada para identificar os

estados dos arquivos do repositório

---

### Slide 24

Adicionando um arquivo

- É possível incluir novos arquivos no repositório local

normalmente, usando editores ou recursos do SO

- A ferramenta git status pode ser usada para identificar os

estados dos arquivos do repositório

---

### Slide 25

Variações de add e commit

```bash
git add <arquivo>
```

Adiciona um arquivo específico à staging area.

```bash
git add .
```

Adiciona tudo no diretório atual e subdiretórios. Use com atenção.

```bash
git add -p
```

Interativo: escolhe trecho a trecho o que entra no commit.

```bash
git commit -m "..."
```

Commit com mensagem na própria linha de comando.

```bash
git commit
```

Abre o editor, permitindo escrever corpo de mensagem completo.

```bash
git commit -a -m "..."
```

Adiciona automaticamente arquivos já rastreados e comita.

```bash
git commit --amend
```

Substitui o último commit. Nunca use em commits já publicados.

---

### Slide 26

Mensagens de Commit

- A mensagem deve deixar claro o propósito do commit no

histórico de mudanças do código

- Conversão amplamente adotada:

Mensagens de commit pouco úteis

ajustes

fix

asdf

funcionou agora

commit

Mensagens de commit informativas

Corrige cálculo de juros em

faturas vencidas

Adiciona validação de CPF no

cadastro

Remove dependência não utilizada

de moment.js

Adiciona validação de CPF no formulário de cadastro

O formulário aceitava CPFs com dígito verificador inválido,

o que gerava falha apenas na integração com a Receita.

A validação passa a ocorrer no cliente e no servidor.

Refs #142

---

### Slide 27

Exercício

- Adicione um arquivo README.md em seu projeto usando os

orientações passadas nos slides anteriores

---

### Slide 28

Exercício

- Instale o pacote dotenv e crie um arquivo .env com uma

variável com o número da porta do servidor

  - Para isso, siga as intruções dos slides sobre o SmartNotes, até a

seção Variáveis de Ambiente

---

### Slide 29

Exercício

- Crie o arquivo src/utils/getEnv.ts para validar e recuperar as

variáveis de ambiente do arquivo .env

  - Para isso, siga as intruções dos slides sobre o SmartNotes, até a

seção Validando as variáveis de ambiente

---

### Slide 30

Ignorando Arquivos

- É muito comum que um dado projeto tenha arquivos que

não devam ser não versionados pelo git

  - Por exemplo, arquivos de logs, arquivos com variáveis de

ambiente, códigos compilados, dependências de terceiros, etc

---

### Slide 31

Ignorando Arquivos

- Por isso, criamos um arquivo .gitignore com uma lista de

arquivos e diretórios que devem ser ignorados pelo Git

# Logs

logs/*

!logs/.gitkeep

# Node files

node_modules/

# Environment files

.env

# Build folders

dist/

build/

Ordem

importa

---

### Slide 32

Ignorando Arquivos

- Após criar o .gitignore e adicioná-lo no staging area, o git

passa a ignorar todos os arquivos listados em seu interior

---

### Slide 33

Ignorando Arquivos

- Após criar o .gitignore e adicioná-lo no staging area, o git

passa a ignorar todos os arquivos listados em seu interior

Caso deseje adicionar um arquivo ou diretório já commitado ao .gitignore, é

preciso remover ele do índice:

```bash
$ git rm --cached .env
```

```bash
$ git add .gitignore
```

```bash
$ git commit -m "Stop tracking the .env file"
```

---

### Slide 34

Ignorando Arquivos

- Após criar o .gitignore e adicioná-lo no staging area, o git

passa a ignorar todos os arquivos listados em seu interior

Caso deseje adicionar um arquivo ou diretório já commitado ao .gitignore, é

preciso remover ele do índice:

```bash
$ git rm --cached .env
```

```bash
$ git add .gitignore
```

```bash
$ git commit -m "Stop tracking the .env file"
```

O --cached é importante porque remove os arquivos apenas do índice do

Git, mantendo-os no seu diretório de trabalho

Sem --cached, o git rm remove o arquivo do índice do Git e também do seu

diretório de trabalho

O git rm apenas remove o arquivo do rastreamento do Git. Se precisar

remover o arquivo de todos os commits anteriores, precisa reescrever o

histórico com git filter-repo

---

### Slide 35

Exercício

- Adicione o arquivo .gitignore no seu projeto, deixando o

arquivo .env não versionado

- Crie um arquivo .env.example para servir de base para a

criação de arquivos .env em novos ambientes de execução

- Faça um commit com essas últimas alterações

---

### Slide 36

Alterando um arquivo

- Os arquivos também podem ser editados usando editores de

texto ou outros recursos de seu SO

- Novamente, usamos a ferramenta git status para identificar

os estados dos arquivos do repositório

---

### Slide 37

Alterando um arquivo

- Os arquivos também podem ser editados usando editores de

texto ou outros recursos de seu SO

- Novamente, usamos a ferramenta git status para identificar

os estados dos arquivos do repositório

O Visual Studio Code possui

uma excelente interface

trabalhar com o Git,

incluindo opções para

adicionar as mudanças na

área de seleção, fazer um

novo commit, e de visualizar

o histórico de commits.

---

### Slide 38

Alterando um arquivo

- Os arquivos também podem ser editados usando editores de

texto ou outros recursos de seu SO

- Novamente, usamos a ferramenta git status para identificar

os estados dos arquivos do repositório

O Visual Studio Code possui

uma excelente interface

trabalhar com o Git,

incluindo opções para

adicionar as mudanças na

área de seleção, fazer um

novo commit, e de visualizar

o histórico de commits.

Mensagem

do

commit

---

### Slide 39

Alterando um arquivo

- Os arquivos também podem ser editados usando editores de

texto ou outros recursos de seu SO

- Novamente, usamos a ferramenta git status para identificar

os estados dos arquivos do repositório

O Visual Studio Code possui

uma excelente interface

trabalhar com o Git,

incluindo opções para

adicionar as mudanças na

área de seleção, fazer um

novo commit, e de visualizar

o histórico de commits.

---

### Slide 40

Visualizando o Histórico de Commits

- Para ver o histórico de commits de um repositório,

podemos utilizar o git log

---

### Slide 41

Visualizando o Histórico de Commits

- O commando git log possui um conjunto de opções úteis:

  - --oneline - uma linha por commit

  - --graph - desenha a topologia dos branches

  - --author - filtra por autoria

  - -- <caminho> - só commits que envolveram o arquivo

  - -S <termo> - commits que adicionaram ou removeram o termo nos arquivos

  - -p - mostra o diff de cada commit

---

### Slide 42

Visualizando as Mudanças

- 

O comando git status informa quais arquivos foram

modificados em um dado momento do fluxo de trabalho

- 

Para obter informações sobre o que foi modificado dentro dos

arquivos você pode usar o git diff

- 

Por exemplo, para verificar as diferenças entre os arquivos do

diretório de trabalho e a área de seleção:

---

### Slide 43

Visualizando as Mudanças

- 

O git diff também é usado para listar as diferenças entre os

arquivos do diretório de trabalho e o último commit

---

### Slide 44

Visualizando as Mudanças

```bash
git diff
```

Diretório de trabalho × área de seleção

```bash
git diff --staged
```

Área de seleção × último commit

```bash
git diff HEAD
```

Diretório de trabalho × último commit

```bash
git diff main develop
```

Diferença entre as branches main e develop

```bash
git show <hash>
```

Metadados e diff completo de um commit específico com o commit anterior.

```bash
git blame <arquivo>
```

Para cada linha, o commit e o autor que a introduziu.

diff --git a/src/juros.ts b/src/juros.ts

@@ -12,7 +12,7 @@ export function calcular(valor: number) {

-  return valor * 0.02;

+  return valor * taxaVigente();

---

### Slide 45

O que é uma branch?

- 

Uma branch é uma linha independente de desenvolvimento

dentro do mesmo repositório

- 

Ela permite trabalhar em uma nova funcionalidade ou correção

sem alterar imediatamente a versão principal do projeto

- 

Uma branch não é uma cópia completa do projeto, é apenas

um ponteiro para um commit

A

B

D

main

chore/eslint

A

C

E

---

### Slide 46

O que é uma branch?

- 

Quando um novo commit é criado, a branch atual passa a

apontar para ele

- 

Antes do commit:

A

B

- 

Depois do commit:

- 

O Git armazena cada commit e move o ponteiro da branch

conforme novos commits são criados

main

main

C

A

B

C

D

---

### Slide 47

O que é uma branch?

- 

Quando um novo commit é criado, a branch atual passa a

apontar para ele

- 

Antes do commit:

A

B

- 

Depois do commit:

- 

O Git armazena cada commit e move o ponteiro da branch

conforme novos commits são criados

main

main

C

A

B

C

D

---

### Slide 48

Comandos para Branches

```bash
git branch nome-da-branch
```

Cria a branch, mas não muda para ela.

```bash
git switch -c nome-da-branch
```

Cria a branch e muda para ela

```bash
git switch nome-da-branch
```

Muda a branch atual (branch para onde o HEAD está apontando)

```bash
git branch -
```

Volta para a branch anterior

```bash
git branch -m novo-nome
```

Renomeia a branch atual

```bash
git branch -d nome-da-branch
```

Exclui a branch nome-da-branch

```bash
git branch
```

Lista branchs locais

```bash
git branch -a
```

Lista branches locais e remotas

---

### Slide 49

Comandos para Branches

```bash
git branch nome-da-branch
```

Cria a branch, mas não muda para ela.

```bash
git switch -c nome-da-branch
```

Cria a branch e muda para ela

```bash
git switch nome-da-branch
```

Muda a branch atual (branch para onde o HEAD está apontando)

```bash
git branch -
```

Volta para a branch anterior

```bash
git branch -m novo-nome
```

Renomeia a branch atual

```bash
git branch -d nome-da-branch
```

Exclui a branch nome-da-branch

```bash
git branch
```

Lista branchs locais

```bash
git branch -a
```

Lista branches locais e remotas

---

### Slide 50

Criando um feature branch

- Ao criar uma branch chore/eslint a partir da branch main, as

duas branches permanecem apontando para o mesmo commit

main

chore/eslint

- Exemplos comuns de nomes para branches:

  - feat/login

  - chore/setup-orm

  - fix/update-user-validation

  - docs/update-readme

  - refactor/user-service

A

B

A

C

---

### Slide 51

Criando um feature branch

- Ao criar uma branch chore/eslint a partir da branch main, as

duas branches permanecem apontando para o mesmo commit

main

chore/eslint

- Exemplos comuns de nomes para branches:

  - feat/login

  - chore/setup-orm

  - fix/update-user-validation

  - docs/update-readme

  - refactor/user-service

A

B

A

C

---

### Slide 52

Criando um feature branch

- Após finalizar a instalação do ESLint no projeto, podemos

criar um novo commit

main

chore/eslint

D

- A partir disso, cada branch passa a apontar para um commit

diferente

A

B

A

C

---

### Slide 53

Criando um feature branch

- Após finalizar a instalação do ESLint no projeto, podemos

criar um novo commit

main

chore/eslint

D

- A partir disso, cada branch passa a apontar para um commit

diferente

A

B

A

C

---

### Slide 54

O que é o HEAD?

- 

O HEAD indica onde o usuário está trabalhando atualmente, e

normalmente é apenas um ponteiro para uma branch

- 

Quando um commit é criado em uma branch:

  - o Git cria o novo commit

  - a branch atual passa a apontar para ele

  - o HEAD continua apontando para a branch

HEAD

A

B

D

main

chore/eslint

A

C

E

---

### Slide 55

Detached HEAD

- Em algumas situações, podemos apontar o HEAD

diretamente para um commit, e não para uma branch

  - Isso é feito com o comando git switch --detach <commit>

- 

Cuidado: É possível criar commits nesse estado, mas eles não

pertencem automaticamente a uma branch

HEAD

A

B

D

main

chore/eslint

A

C

E

---

### Slide 56

Detached HEAD

- Em algumas situações, podemos apontar o HEAD

diretamente para um commit, e não para uma branch

  - Isso é feito com o comando git switch --detach <commit>

- 

Cuidado: É possível criar commits nesse estado, mas eles não

pertencem automaticamente a uma branch

HEAD

A

B

D

main

chore/eslint

A

C

E

Detached HEAD é útil principalmente para:

- inspecionar uma versão antiga do projeto

- testar o código de um commit específico

- investigar quando um bug apareceu

- comparar o comportamento atual com uma versão anterior

---

### Slide 57

Mesclando Branches

- Depois da instalação e configuração do ESLint, podemos fazer

o merge entre as branches chore/eslint e main

- Note que a branch que recebe as alterações deve estar

ativa

---

### Slide 58

Merge fast-forward

- O fast-forward ocorre quando a branch de destino não

recebeu novos commits depois da criação da outra branch

- Antes:

- Depois:

main

chore/eslint

main

chore/eslint

D

A

B

A

C

D

A

B

A

C

---

### Slide 59

Merge fast-forward

- O fast-forward ocorre quando a branch de destino não

recebeu novos commits depois da criação da outra branch

- Antes:

- Depois:

main

chore/eslint

main

chore/eslint

D

A

B

A

C

D

A

B

A

C

---

### Slide 60

Exercício

- Crie uma branch chore/eslint em seu projeto, e então instale

e configure o ESLint nessa branch

- Após isso, faça o merge da branch chore/eslint na main

usando fast-forward

  - Para isso, siga as

intruções dos slides

sobre o SmartNotes,

até a seção

Adicionando o ESLint

no projeto

---

### Slide 61

Merge commit

- Um merge commit é necessário quando as duas branches

avançaram separadamente

- Antes:

- Depois:

F

main

Novo commit F

integrando as

mudanças das

duas branches

A

B

D

main

chore/prettier

A

C

E

A

B

D

A

C

E

---

### Slide 62

Merge commit

- Um merge commit é necessário quando as duas branches

avançaram separadamente

- Antes:

- Depois:

F

main

Novo commit F

integrando as

mudanças das

duas branches

A

B

D

main

chore/prettier

A

C

E

A

B

D

A

C

E

O commit F possui dois commits pai: (i) o último commit da main, e

(ii) o último commit da chore/prettier.

Ao fazer o merger, o Git abre um editor para confirmar a mensagem

do novo commit: Merge branch 'chore/prettier'

---

### Slide 63

Exemplo de Merge commit

- Commits da branch main:

- Commits da branch chore/prettier:

---

### Slide 64

- Ao executar o comando merge a partir de branch main, um

editor é aberto para edição da mensagem do merge commit

```bash
$ git merge chore/prettier
```

Exemplo de Merge commit

---

### Slide 65

- Ao executar o comando merge a partir de branch main, um

editor é aberto para edição da mensagem do merge commit

```bash
$ git merge chore/prettier
```

Exemplo de Merge commit

Ostensibly

Recursive's

Twin (ort)

O nome ORT, Ostensibly Recursive's Twin (em português:

“aparentemente, o gêmeo da Recursive”) é uma brincadeira com o

nome da estratégia anterior, que era chamada de Recursive

---

### Slide 66

- Como resultado, os commits da branch chore/prettier são

mesclados com os commits da branch main

Exemplo de Merge commit

- Note que, além dos commits das duas branches, o HEAD está

apontando para um commit adicional, criado a partir do

merge commit

---

### Slide 67

- A opção --graph do comando git log mostra os commits que

participaram do merge entre duas branches

Exemplo de Merge commit

---

### Slide 68

- A opção --graph do comando git log mostra os commits que

participaram do merge entre duas branches

Exemplo de Merge commit

O grafo de

mudanças

também pode

ser visto no Visual

Studio Code

---

### Slide 69

Exercício

- Crie uma branch chore/prettier em seu projeto, e então

instale e configure o Prettier nessa branch

- Volte para a branch main, adicione algumas informações no

README.md sobre o seu projeto, e faça um commit

- Após isso, faça o merge da branch chore/pretter na main

usando merge commit

  - Para isso, siga as

intruções dos slides

sobre o SmartNotes,

até a seção

Adicionando o

Prettier no projeto

---

### Slide 70

Conflitos de Merge

- Um conflito ocorre quando o Git não consegue fazer o merge

automático das alterações de duas branches

- Considere, por exemplo, as alterações abaixo, que ocorreram

na mesma linha do README.md em duas branches distintas:

  - Na branch main:

  - Na branch feat/router:

## Descrição

API para gerenciamento de notas pessoais.

## Descrição

API REST para criação e organização de notas pessoais.

- Ao fazer o merge de feat/router na main, o Git cancela o

merge para que o conflito seja resolvido manualmente

---

### Slide 71

Conflitos de Merge

- Um conflito ocorre quando o Git não consegue fazer o merge

automático das alterações de duas branches

- Considere, por exemplo, as alterações abaixo, que ocorreram

na mesma linha do README.md em duas branches distintas:

  - Na branch main:

  - Na branch feat/router:

## Descrição

API para gerenciamento de notas pessoais.

## Descrição

API REST para criação e organização de notas pessoais.

- Ao fazer o merge de feat/router na main, o Git cancela o

merge para que o conflito seja resolvido manualmente

Note que nenhuma

mudança pode ser

feita diretamente na

main. Essa mudança

deve ter ocorrido a partir

do merge com outra

branch

---

### Slide 72

Conflitos de Merge

- Um conflito ocorre quando o Git não consegue fazer o merge

automático das alterações de duas branches

- Considere, por exemplo, as alterações abaixo, que ocorreram

na mesma linha do README.md em duas branches distintas:

  - Na branch main:

  - Na branch feat/router:

## Descrição

API para gerenciamento de notas pessoais.

## Descrição

API REST para criação e organização de notas pessoais.

- Ao fazer o merge de feat/router na main, o Git cancela o

merge para que o conflito seja resolvido manualmente

Note que nenhuma

mudança pode ser

feita diretamente na

main. Essa mudança

deve ter ocorrido a partir

do merge com outra

branch

---

### Slide 73

Conflitos de Merge

- Um conflito ocorre quando o Git não consegue fazer o merge

automático das alterações de duas branches

---

### Slide 74

Conflitos de Merge

- Um conflito ocorre quando o Git não consegue fazer o merge

automático das alterações de duas branches

---

### Slide 75

Conflitos de Merge

- O Git modifica o arquivo README.md e adiciona marcadores

- Esses marcadores não podem permanecer no código final, e

para resolver o conflito o arquivo deve ser editado,

escolhendo ou combinando as alterações

---

### Slide 76

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

---

### Slide 77

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

O Visual Studio Code tem uma ótima interface para ajudar na

resolução dos conflitos

O Visual Studio Code tem uma

ótima interface para ajudar na

resolução dos conflitos

---

### Slide 78

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

O Visual Studio Code tem uma ótima interface para ajudar na

resolução dos conflitos

Se desejar a versão vindo da

branch feat/router, clique em

Accept Incoming. Se deseja manter

a versão que está na branch main,

clique em Accept Current.

---

### Slide 79

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

O Visual Studio Code tem uma ótima interface para ajudar na

resolução dos conflitos

---

### Slide 80

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

O Visual Studio Code tem uma ótima interface para ajudar na

resolução dos conflitos

---

### Slide 81

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

O Visual Studio Code tem uma ótima interface para ajudar na

resolução dos conflitos

---

### Slide 82

Resolvendo Conflitos

- Para resolver o conflito, deve-se seguir esses passos:

  - Identificar os arquivos em conflito com git status

  - Abrir cada arquivo que deu confito e localizar os marcadores:

<<<<<<<

=======

>>>>>>>

  - Escolher ou combinar as alterações

API REST para criação e organização de notas pessoais.

  - Remover os marcadores

  - Marcar o conflito como resolvido com o comando git add

  - Concluir o merge com git commit

O Visual Studio Code tem uma ótima interface para ajudar na

resolução dos conflitos

---

### Slide 83

Cancelando um merge

- Caso não queira continuar a resolução, o comando abaixo

tenta restaurar o repositório ao estado anterior ao merge

```bash
git merge --abort
```

- Com o merge abortado, pode-se tentar fazer novos commits

nas branches para desfazer as causas dos conflitos

---

### Slide 84

Exercício (parte 1)

- Reproduza o cenário apresentado nos slides anteriores,

provocando e resolvendo um conflito no arquivo README.md:

  - A partir da branch main, crie a branch docs/update, adicione a

seção Descrição com uma única linha no arquivo README.md, e

faça um commit

  - Volte para a main e, antes de fazer o merge da docs/update com

a branch main, crie a branch feat/router

  - Na branch feat/router:

- Crie o arquivo src/router/router.ts com as rotas da API, seguindo

os slides do SmartNotes até a seção Arquivo Separado de Rotas

- Adicione a seção Descrição no README.md, com um conteúdo

diferente daquele escrito em docs/update

- Faça um commit com essas alterações

---

### Slide 85

Exercício (parte 2)

- Continuação...

  - Volte para a branch main e faça o merge de docs/update

  - Em seguida, ainda na main, faça o merge de feat/router

- O Git deverá detectar um conflito no arquivo README.md

  - Resolva o conflito utilizando a interface do Visual Studio Code,

escolhendo qual alteração manter ou combinando as duas

versões. Depois, conclua o merge.

- Ao final, use git log --oneline --graph para verificar o histórico

das branches e dos merges

---

### Slide 86

Repositórios Remotos

- Um repositório remoto é um repositório hospedado em

algum servidor, como GitHub, GitLab ou servidor privado

  - Conforme já dito anteriormente, o Git é distribuído: cada clone,

remoto ou local, possui seu próprio histórico completo

- origin é o nome convencional dado ao repositório remoto

principal, e é basicamente uma URL

---

### Slide 87

Comandos para Remotes

```bash
git remote show origin
```

Exibe informações detalhadas sobre o remoto origin, incluindo

branches rastreadas e configuração de push/pull.

```bash
git remote add origin URL
```

Adiciona um novo repositório remoto chamado origin, associado à

URL informada.

```bash
git remote set-url origin URL
```

Altera a URL associada ao repositório remoto origin. Pode ser usado

com a opção --push, para configurar apenas a URL dos pushes.

```bash
git remote remove origin
```

Remove o repositório remoto chamado origin da configuração local.

```bash
git remote
```

Lista os repositórios remotos configurados.

```bash
git remote -v
```

Lista os repositórios remotos de forma detalhada (v = verbose),

mostrando também as URLs usadas para fetch e push.

---

### Slide 88

Comandos para Remotes

```bash
git remote show origin
```

Exibe informações detalhadas sobre o remoto origin, incluindo

branches rastreadas e configuração de push/pull.

```bash
git remote add origin URL
```

Adiciona um novo repositório remoto chamado origin, associado à

URL informada.

```bash
git remote set-url origin URL
```

Altera a URL associada ao repositório remoto origin. Pode ser usado

com a opção --push, para configurar apenas a URL dos pushes.

```bash
git remote remove origin
```

Remove o repositório remoto chamado origin da configuração local.

```bash
git remote
```

Lista os repositórios remotos configurados.

```bash
git remote -v
```

Lista os repositórios remotos de forma detalhada (v = verbose),

mostrando também as URLs usadas para fetch e push.

---

### Slide 89

Git Clone

- O comando git clone cria uma cópia local completa de um

repositório remoto existente

  - O comando configura automaticamente o remoto origin

  - Também cria a branch local principal e configura o upstream da

branch remota

---

### Slide 90

Git Clone

- Após clonar um repositório, o Git cria automaticamente

referências locais como main e origin/main, onde:

  - main é a branch local na qual o usuário trabalha

  - origin/main representa o último estado conhecido da branch

main no repositório remoto origin

- origin/main não é consultada continuamente pela internet;

ela é atualizada por comandos como git fetch e git pull

---

### Slide 91

Exercício

- Faça um clone do seu repositório em um diretório diferente

do que você tem usado

- Nesse diretório, crie uma branch feat/helmet, instale e

configure o Helmet nessa branch, e então crie um commit

  - Para isso, siga as intruções dos slides sobre o SmartNotes, até a

seção Segurança da API

  - Não envie essa branch para o servidor remoto, ainda

---

### Slide 92

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), deve-se usar

a opção -u para criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 93

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), deve-se usar

a opção -u para criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 94

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 95

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 96

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

Uma Pull Request (PR) é uma solicitação feita por um dev no Github

para mesclar suas alterações de uma branch em outra, como

feat/helmet em main

Uma PR permite visualizar commits e arquivos modificados, comentar

linhas específicas, solicitar mudanças, executar testes automáticos,

aprovar ou rejeitar a integração e realizar o merge

A Pull Request é um recurso do GitHub, não um comando nativo do

Git

---

### Slide 97

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

Uma Pull Request (PR) é uma solicitação feita por um dev no Github

para mesclar suas alterações de uma branch em outra, como

feat/helmet em main

Uma PR permite visualizar commits e arquivos modificados, comentar

linhas específicas, solicitar mudanças, executar testes automáticos,

aprovar ou rejeitar a integração e realizar o merge

A Pull Request é um recurso do GitHub, não um comando nativo do

Git

Durante a PR, outras pessoas podem comentar, pedir mudanças,

aprovar e verificar testes automáticos

Se forem necessárias novas alterações, faça novos commits e envie-

os; a Pull Request é atualizada automaticamente.

```bash
$ git add .
```

```bash
$ git commit -m "Adição de novas regras de segurança"
```

```bash
$ git push
```

---

### Slide 98

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 99

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 100

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

---

### Slide 101

Primeiro push de uma branch

- Usamos o comando git push para enviar os commits de uma

branch local para uma branch remota no repositório origin

  - Exemplo: git push -u origin feat/helmet

- No primeiro push de uma branch (feat/helmet), use -u para

criar o upstream (origin/feat/helmet)

  - Upstream é uma referência local à uma branch remota, usada

como referência padrão para operações como git push e git pull

  - No nosso exemplo:

- branch local: feat/helmet

- upstream configurado: origin/feat/helmet

- branch real no servidor remoto: feat/helmet

- Depois disso, normalmente basta usar git push e git pull

sem informar origin e o nome da branch

Com a Pull Request mesclada à origin/main, podemos atualizar o

repositório main local

---

### Slide 102

Exercício

- No repositório local criado no exercício anterior, execute o

comando git push -u origin feat/helmet

  - Como vimos, esse comando irá salvar feat/helmet no servidor

remoto e configurar o upstream origin/feat/helmet

- Seguindo os passos dos slides anteriores, crie um pull request

e faça o merge de feat/helmet com a branch main do Github

- Depois, ainda no repositório local criado no exercício

anterior, use o git pull para atualizar a branch main local com

a branch main do Github

---

### Slide 103

Git Pull e Git Fetch

- Nos últimos slides, a dev Lucy usou o git pull para atualizar a

branch main local com a branch main do Github

  - O git pull baixa as alterações do repositório remoto, atualiza o

upstream e faz o merge desse upstream com a branch local

- Além do git pull, também podemos usar o git fetch, que

atualiza o upstream mas não faz o merge com a branch local

A

B

D

main

origin/main

A

C

E

A

B

D

main

A

C

E

F

Situação inicial:

Depois de git fetch:

origin/main

---

### Slide 104

Git Pull e Git Fetch

- Nos últimos slides, a dev Lucy usou o git pull para atualizar a

branch main local com a branch main do Github

  - O git pull baixa as alterações do repositório remoto, atualiza o

upstream e faz o merge desse upstream com a branch local

- Além do git pull, também podemos usar o git fetch, que

atualiza o upstream mas não faz o merge com a branch local

A

B

D

main

origin/main

A

C

E

A

B

D

main

A

C

E

F

Situação inicial:

Depois de git fetch:

origin/main

---

### Slide 105

Git Pull e Git Fetch

- Nos últimos slides, a dev Lucy usou o git pull para atualizar a

branch main local com a branch main do Github

  - O git pull baixa as alterações do repositório remoto, atualiza o

upstream e faz o merge desse upstream com a branch local

- Além do git pull, também podemos usar o git fetch, que

atualiza o upstream mas não faz o merge com a branch local

A

B

D

main

origin/main

A

C

E

A

B

D

main

origin/main

A

C

E

F

Situação inicial:

Depois de git fetch:

---

### Slide 106

Git Pull e Git Fetch

- Nos últimos slides, a dev Lucy usou o git pull para atualizar a

branch main local com a branch main do Github

  - O git pull baixa as alterações do repositório remoto, atualiza o

upstream e faz o merge desse upstream com a branch local

- Além do git pull, também podemos usar o git fetch, que

atualiza o upstream mas não faz o merge com a branch local

A

B

D

main

origin/main

A

C

E

A

B

D

main

origin/main

A

C

E

F

Situação inicial:

Depois de git fetch:

---

### Slide 107

Exercício

- No repositório local original, use o git fetch para atualizar o

origin/main com as alterações da main do Github

- Caso não esteja na branch main, use o comando git switch

para mudar o HEAD para essa branch

- Como o comando git fetch não faz o merge entre origin/main

e o repositório main local, use o comando git merge

origin/main para atualizar a branch main com o conteúdo do

repositório remoto

---

### Slide 108

Atualização de Branches

- Durante o desenvolvimento, outros desenvolvedores podem

atualizar a branch main do Github com:

  - correções de bugs

  - novas funcionalidades

  - refatorações

  - mudanças em arquivos usados pela feature

- No exemplo abaixo, a branch feat/morgan foi criada a partir

do commit A, mas a origin/main já recebeu os commits B e C

A

B

D

origin/main

feat/morgan

A

C

E

---

### Slide 109

Atualização de Branches

- Quanto mais tempo a feature demorar para ser concluída,

mais conflitos podem se acumular ao integrá-la com a main

- Por isso, uma prática comum é trazer periodicamente as

mudanças da main remota para a branch da nova feature

  - Atualizar a feature durante o desenvolvimento ajuda a

descobrir incompatibilidades antes da integração final

A

B

D

origin/main

feat/morgan

A

C

E

---

### Slide 110

Atualização de Branches

- Para trazer as mudanças mais recentes da main do

repositório remoto para a branch local da feature:

```bash
$ git switch feat/morgan
```

```bash
$ git fetch origin
```

```bash
$ git merge origin/main
```

- Resultado:

F

A

B

D

A

C

E

origin/main

feat/morgan

A

B

D

origin/main

feat/morgan

A

C

E

O commit F

representa a

união dos

dois históricos

---

### Slide 111

Atualização de Branches

- Para trazer as mudanças mais recentes da main do

repositório remoto para a branch local da feature:

```bash
$ git switch feat/morgan
```

```bash
$ git fetch origin
```

```bash
$ git merge origin/main
```

- Resultado:

F

A

B

D

A

C

E

origin/main

feat/morgan

A

B

D

origin/main

feat/morgan

A

C

E

O commit F

representa a

união dos

dois históricos

É preferível usar origin/main após executar git fetch, pois isso garante

que a integração será feita com o estado mais recente da main no

repositório remoto

---

### Slide 112

Atualização com Rebase

- Outra possibilidade é reposicionar os commits da feature

sobre a versão mais recente da main, usando o rebase:

```bash
$ git switch feat/morgan
```

```bash
$ git fetch origin
```

```bash
$ git rebase origin/main
```

A

B

D

origin/main

feat/note-crud

A

C

E

- O rebase reaplica os commits da feature sobre o commit mais

recente de origin/main, criando novos commits e produzindo

um histórico mais linear que o merge

’

’

---

### Slide 113

Atualização com Rebase

A

B

D

origin/main

feat/morgan

A

C

E

’

’

A

B

D

origin/main

feat/morgan

A

C

E

- Note que os commits D e F são recriados, e por isso o rebase

não é recomendado quando os commits que já foram

compartilhados com outros desenvolvedores

---

### Slide 114

Atualização com Rebase

A

B

D

origin/main

feat/morgan

A

C

E

’

’

A

B

D

origin/main

feat/morgan

A

C

E

- Note que os commits D e F são recriados, e por isso o rebase

não é recomendado quando os commits que já foram

compartilhados com outros desenvolvedores

Se a branch é compartilhada com outros desenvolvedores,

normalmente é mais seguro atualizá-la com merge, porque o merge

não reescreve o histórico existente

---

### Slide 115

Merge ou Rebase?

- Prefira merge quando:

  - quiser preservar o histórico completo

  - estiver integrando uma branch compartilhada

  - quiser evitar reescrever commits

- Prefira rebase quando:

  - quiser produzir um histórico linear

  - os commits ainda não tiverem sido compartilhados

  - quiser organizar o histórico antes de abrir uma Pull Request

---

### Slide 116

Merge ou Rebase?

- Prefira merge quando:

  - quiser preservar o histórico completo

  - estiver integrando uma branch compartilhada

  - quiser evitar reescrever commits

  - estiver concluindo uma Pull Request

- Prefira rebase quando:

  - quiser atualizar uma branch local

  - quiser produzir um histórico linear

  - os commits ainda não tiverem sido compartilhados

  - quiser organizar o histórico antes de abrir uma Pull Request

Em um Pull

Request, também

podemos fazer

o rebase dos

commits antes

de integrá-los

à branch main

---

### Slide 117

Exercício

- Crie uma branch feat/morgan em seu projeto e, nessa

branch, instale e configure o Morgan

  - Para isso, siga as instruções dos slides sobre o SmartNotes, até

a seção Registro das Requisições

- Após concluir a configuração, envie a branch feat/morgan

para o GitHub, configurando o upstream

- Crie um Pull Request para integrar feat/morgan à branch

main e depois escolha a opção Rebase and merge

  - Os commits de feat/morgan serão reaplicados sobre a ponta

atual da main, sem a criação de um merge commit

- Após a integração, atualize sua branch main local com as

alterações do repositório remoto

---

### Slide 118

Merge ou rebase?

- Prefira merge quando:

  - quiser preservar o histórico completo

  - estiver integrando uma branch compartilhada

  - quiser evitar reescrever commits

  - estiver concluindo uma Pull Request

- Prefira rebase quando:

  - quiser atualizar uma branch local

  - quiser produzir um histórico linear

  - os commits ainda não tiverem sido compartilhados

  - quiser organizar o histórico antes de abrir uma Pull Request

O Learn Git Branching é uma excelente ferramenta para aprender e

praticar mais sobre as branches: https://learngitbranching.js.org

---

### Slide 119

Desfazendo alterações no Git

- O Git oferece diferentes comandos para desfazer alterações,

dependendo de onde a alteração está:

  - Diretório de trabalho

  - Staging area

  - Histórico de commits

  - Repositório remoto

- Principais comandos:

  - git restore

  - git reset

  - git revert

  - git commit --amend

---

### Slide 120

Desfazendo alterações em arquivo

- Para descartar alterações feitas no diretório de trabalho:

- Com isso, o arquivo volta para a versão registrada na staging

area, e as alterações feitas no arquivo são perdidas

```bash
$ git restore arquivo.txt
```

---

### Slide 121

Desfazendo alterações em arquivo

- Para descartar alterações feitas no diretório de trabalho:

- Com isso, o arquivo volta para a versão registrada na staging

area, e as alterações feitas no arquivo são perdidas

```bash
$ git restore arquivo.txt
```

Para restaurar todos os arquivos modificados, usamos

```bash
git restore .
```

---

### Slide 122

Removendo arquivo da staging area

- Para remover as alterações de um arquivo da staging area,

mantendo suas modificações no diretório de trabalho:

- As modificações no arquivo não são perdidas, apenas deixam

de fazer parte do próximo commit

```bash
$ git restore --staged arquivo.txt
```

---

### Slide 123

Removendo arquivo da staging area

- Para remover um arquivo da staging area, mantendo suas

modificações no diretório de trabalho:

- As modificações no arquivo não são perdidas, apenas deixam

de fazer parte do próximo commit

```bash
$ git restore --staged arquivo.txt
```

---

### Slide 124

Exercício

- Na branch feat/morgan, acrescente a string Teste no final do

arquivo README.md e execute o git status

- Descarte a alteração com git restore README.md e confirme

que o arquivo voltou à versão anterior

- Acrescente novamente a linha Teste, execute git add

README.md e consulte o status do repositório

- Remova o arquivo da staging area com git restore --staged

README.md, sem perder a modificação

- Confirme o resultado com git status. Depois, adicione

novamente o arquivo à staging area e crie o commit:

  - git commit -m "Practice git restore"

---

### Slide 125

Desfazendo o último commit

- Para os próximos slides, vamos executar o código bash

abaixo, que cria 4 commits na branch feat/morgan

```bash
$ for letra in A B C D; do
```

  echo "$letra" >> README.md

  git add .

  git commit -m "$letra"

done

---

### Slide 126

Desfazendo o último commit

- Para os próximos slides, vamos executar o código bash

abaixo, que cria 4 commits na branch feat/morgan

```bash
$ for letra in A B C D; do
```

  echo "$letra" >> README.md

  git add .

  git commit -m "$letra"

done

---

### Slide 127

Desfazendo o último commit

- Após o último comando, os commits da branch feat/morgan

passam a seguir a disposição abaixo

A

B

A

C

D

HEAD

feat/morgan

---

### Slide 128

Desfazendo o último commit

- O comando git reset permite mover a branch atual para um

commit a partir de seu HASH

```bash
$ git reset 5352dbd
```

A

B

A

C

HEAD

feat/morgan

D

---

### Slide 129

Desfazendo o último commit

- O comando git reset permite mover a branch atual para um

commit a partir de seu HASH

```bash
$ git reset 5352dbd
```

A

B

A

C

HEAD

feat/morgan

D

Após o reset, a branch feat/morgan passa a apontar para 5352dbd (C),

e os commits posteriores deixam de fazer parte da branch

---

### Slide 130

Desfazendo o último commit

- O comando git reset permite mover a branch atual para um

commit a partir de seu HASH

```bash
$ git reset 5352dbd
```

A

B

A

C

HEAD

feat/morgan

D

Após o reset, a branch feat/morgan passa a apontar para 5352dbd (C),

e os commits posteriores deixam de fazer parte da branch

As alterações de D permanecem no diretório de trabalho

---

### Slide 131

Desfazendo o último commit

- Também podemos usar HEAD~1 para referenciar o pai de

HEAD, HEAD~2 para referenciar o avô, e assim por diante

```bash
$ git reset HEAD~1
```

- Depois do reset, o commit C é removido do histórico da

branch e as alterações de C continuam no diretório de

trabalho

A

B

A

A

B

A

C

HEAD

feat/morgan

HEAD

feat/morgan

C

---

### Slide 132

Desfazendo o último commit

- O git reset move a referência da branch para outro commit

- Mas existem diferentes maneiras de tratar as mudanças nos

arquivos dos commits removidos:

  - soft

  - mixed

  - hard

```bash
git reset <commit>
```

---

### Slide 133

Git Reset Soft

- Usando a opção soft, podemos mover a branch para um

commit anterior, mas matendo as alterações na staging area

```bash
git reset --soft HEAD~1
```

A

B

HEAD

A

C

A

B

HEAD

A

Antes:

Depois:

- Nesse caso, todas as mudanças feitas no commit C são

mantidas na staging área, e podemos refazer o commit C

---

### Slide 134

Git Reset Mixed

- Usando a opção mixed, movemos a branch para um commit

anterior, mas matendo as alterações no diretório de trabalho

```bash
git reset --mixed HEAD~1
```

A

B

HEAD

A

C

A

B

HEAD

A

Antes:

Depois:

- As alterações do commit removido permanecem no diretório

de trabalho, mas saem da staging area

- Essa é a opção padrão do comando git reset

---

### Slide 135

Git Reset Hard

- Usando a opção hard, movemos a branch para um commit

anterior, mas descartando todas as alterações nos arquivos

```bash
git reset --hard HEAD~1
```

A

B

HEAD

A

C

A

B

HEAD

A

Antes:

Depois:

- Com a opção hard, as alterações feitas em C desaparecem do

diretório de trabalho, sendo a forma mais destrutiva

de reset

---

### Slide 136

Histórico dos movimentos do HEAD

- O git reflog registra os movimentos recentes do HEAD e das

referências locais

```bash
$ git reflog
```

- O reflog mostra onde o HEAD estava ao longo do tempo,

mesmo que um commit não apareça mais no git log

---

### Slide 137

```bash
git log × git reflog
```

- O git log mostra os commits alcançáveis pelo histórico atual

- O git reflog mostra por onde o HEAD passou

---

### Slide 138

```bash
git log × git reflog
```

- O git log mostra os commits alcançáveis pelo histórico atual

- O git reflog mostra por onde o HEAD passou

O commit 9990fe3

desapareceu do

```bash
git log, mas
```

ainda pode ser

encontrado pelo

```bash
git reflog
```

---

### Slide 139

Recuperando um commit

- Para recuperar um commit <hash> eliminado através de um

```bash
git reset --hard, podemos usar reset --hard <hash>
```

---

### Slide 140

Recuperando um commit

Além da opção com o git reset, também podemos criar nova

uma branch apontando para o commit recuperado

---

### Slide 141

Exercício (parte I)

- Na branch feat/morgan, execute o laço apresentado para

acrescentar A, B, C e D ao README.md e criar um commit

para cada letra

- Anote os hashes de C e D. Execute git reset <hash-de-C>.

Confirme que D saiu do git log e permaneceu no diretório de

trabalho

- Volte a D com git reset --hard <hash-de-D>. Execute git reset

--soft HEAD~1 e confirme que as alterações de D estão na

staging area

- Volte novamente a D. Execute git reset --hard HEAD~1 e

confirme que D desapareceu do git log e do README.md

---

### Slide 142

Exercício (parte II)

- Compare git log --oneline -4 com git reflog -5 e localize o

hash de D no reflog

- Recupere D na feat/morgan com git reset --hard <hash-de-

D>. Verifique o histórico e o conteúdo do README.md

- Execute novamente git reset --hard HEAD~1. Crie a branch

recuperacao apontando para D e mude para ela

- Na branch recuperacao, gere o arquivo evidencia-reset-

reflog.txt. Faça o commit Practice git reset and reflog e envie

a branch ao GitHub

  - git log --oneline --all --decorate --graph > evidencia-

reset-reflog.txt

  - git reflog -10 >> evidencia-reset-reflog.txt

---

### Slide 143

Corrigindo o último commit

- O comando git reset HEAD~1 remove o último commit

- Mas se quisermos corrigir o último commit sem removê-lo,

podemos usar o comando git commit --amend

```bash
$ git add arquivo-esquecido.txt
```

```bash
$ git commit --amend
```

- Também podemos apenas alterar a mensagem do último

commit:

```bash
$ git add arquivo-esquecido.txt
```

```bash
$ git commit --amend -m "Nova mensagem"
```

---

### Slide 144

Corrigindo o último commit

- O comando git commit --amend reescreve o histórico, pois o

o último commit é apagado e substituido por um novo

A

B

HEAD

A

C

Antes:

Depois:

A

B

HEAD

A

C’

- Desta forma, a opção --amend não deve ser usada em

commits que já foram enviados para o repositório remoto

C' é um

novo commit,

com outro

hash

---

### Slide 145

E se o commit já está no GitHub?

- Quando um commit já foi compartilhado, normalmente não

queremos apagar ou reescrever o histórico

- Nesses casos, podemos usar o git revert para criar um novo

commit que desfaz as alterações de outro commit

```bash
$ git revert HEAD
```

A

B

HEAD

A

C

Antes:

Depois:

A

B

A

HEAD

D

C

D desfaz

as alterações

realizadas

por C, e o C

continua no

histórico

---

### Slide 146

Git Stash

- O git stash guarda temporariamente alterações que ainda

não estão prontas para um commit

- É útil quando você está trabalhando no codígo, precisa mudar

de branch e não quer criar um commit incompleto

```bash
$ git add .
```

```bash
$ git commit -m "Work In Progress"
```

```bash
$ git switch main
```

×

```bash
$ git stash
```

```bash
$ git switch main
```

[OK]

- Depois de executar o comando git stash, o diretório de

trabalho volta ao estado do último commit

  - As alterações ficam armazenadas em uma pilha temporária

---

### Slide 147

Git Stash

- Após o comando git stach, pode-se trocar de branch e

trabalhar normalmente nela

- Ao voltar para a branch anterior, podese restaurar as

alterações do último git stach usando a opção pop

```bash
$ git switch -
```

```bash
$ git stash pop
```

---

### Slide 148

Comandos principais do Stash

```bash
git stash -u
```

Incluir arquivos untracked

```bash
git stash list
```

Listar stashes

```bash
git stash pop
```

Restaurar e remover

```bash
git stash apply
```

Restaurar e manter

```bash
git stash clear
```

Remover todos os stashes armazenados

```bash
git stash drop
```

Remover um stash

```bash
git stash
```

Guardar alterações

```bash
git stash push -m "mensagem"
```

Guardar com descrição

---

