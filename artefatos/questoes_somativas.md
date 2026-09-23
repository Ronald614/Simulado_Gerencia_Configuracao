# Caderno de Questoes Somativas - Simulado de Estudos para a Prova de Gerencia de Configuracao

**Disciplina:** Gerencia de Configuracao  
**Material de Referencia:** Aulas e Slides do Prof. David Fernandes de Oliveira (IC/UFAM)  
**Elaboracao:** Simulado Independente de Estudos para a Prova  
**Valor Total da Prova:** 10,0 pontos (5 questoes de 2,0 pontos cada)  
**Formato:** Questoes de Verdadeiro (V) ou Falso (F) no Formato Somativo

---

## Instrucoes para Resolucao

1. Cada questao e composta por 5 proposicoes numeradas com potencias de base 2: **(01)**, **(02)**, **(04)**, **(08)** e **(16)**.
2. Analise cada proposicao julgando-a tecnicamente como **Verdadeira (V)** ou **Falsa (F)**.
3. A resposta de cada questao e calculada somando-se exclusivamente os valores associados as proposicoes que voce identificou como **Verdadeiras**.
4. Pela propriedade dos sistemas numericos em potencias de 2 (base binaria), **existe uma unica soma possivel** para cada combinacao correta de proposicoes verdadeiras.
5. Cada questao correta vale **2,0 pontos**, totalizando **10,0 pontos**.

---

## Questoes

### Questao 01 (Valor: 2,0 pontos)
**Tema:** Git - Arquitetura, Fundamentos e os Tres Estados do Ciclo de Vida

Com relacao a arquitetura dos sistemas de controle de versao e aos conceitos fundamentais de funcionamento do Git, analise as proposicoes a seguir:

- **(01)** Diferentemente dos Sistemas de Controle de Versao Centralizados (como CVS ou Subversion), nos quais a indisponibilidade do servidor central bloqueia o registro de versoes pelos desenvolvedores, o Git fundamenta-se em uma arquitetura distribuida, onde cada clone local contem uma copia integral do repositorio com todo o seu historico.
- **(02)** O Git estrutura o ciclo de vida dos arquivos em tres estados fundamentais: *Working Directory* (diretorio de trabalho contendo os arquivos modificados), *Staging Area* / *Index* (area de preparacao onde as alteracoes sao selecionadas para o proximo commit) e *Repository* / `.git directory` (banco de objetos onde os snapshots confirmados sao gravados de maneira permanente).
- **(04)** A execucao do comando `git commit -m "mensagem"` consolida as modificacoes diretamente no servidor remoto (como GitHub ou GitLab), sendo desnecessario executar o comando `git push` para sincronizacao com a equipe.
- **(08)** O arquivo `.gitignore` e utilizado para listar padroes de nomes de arquivos e diretorios que nao devem ser rastreados pelo Git (como `node_modules/`, logs e arquivos de segredos locais), devendo ele proprio ser comitado no repositorio para garantir a padronizacao das exclusoes entre todos os colaboradores.
- **(16)** A inclusao de um padrao de arquivo no `.gitignore` remove automaticamente e de forma retroativa os arquivos correspondentes que ja haviam sido comitados no historico do repositorio.

**SOMA DA QUESTAO 01:** [ ______ ]

---

### Questao 02 (Valor: 2,0 pontos)
**Tema:** Git - Ramificacao (Branches), Ponteiro HEAD e Conflitos de Integracao

Em relacao ao mecanismo de ramificacao, ponteiros de navegacao e resolucao de conflitos de merge no Git, avalie as proposicoes:

- **(01)** No Git, uma *branch* nao e uma duplicacao fisica dos arquivos do projeto no disco, mas sim um ponteiro movel de baixo custo computacional que referencia um commit especifico na arvore historica.
- **(02)** O ponteiro `HEAD` referencia obrigatoriamente um commit hospedado no repositorio remoto `origin`, sendo tecnicamente impossivel configurar o `HEAD` para apontar diretamente para um commit local sem vincular a uma branch nominal.
- **(04)** A operacao de mesclagem do tipo *Fast-Forward* ocorre quando a branch de destino nao possui commits divergentes em relacao a branch integrada, permitindo ao Git simplesmente deslocar o ponteiro da branch de destino diretamente para o topo da branch mesclada, sem a criacao de um novo commit de merge.
- **(08)** Quando duas branches realizam alteracoes em arquivos distintos ou em trechos nao sobrepostos do mesmo arquivo, o Git nao consegue unificar as alteracoes de forma automatica, gerando compulsoriamente um conflito de merge.
- **(16)** Durante a ocorrencia de um conflito de merge, o Git inclui marcadores visuais no arquivo afetado (como `<<<<<<< HEAD`, `=======` e `>>>>>>> <branch>`), cabendo ao desenvolvedor inspecionar o arquivo, reconciliar o conteudo desejado, remover os delimitadores e executar `git add` para assinalar a resolucao do conflito.

**SOMA DA QUESTAO 02:** [ ______ ]

---

### Questao 03 (Valor: 2,0 pontos)
**Tema:** Git - Rebase, Modos de Reset, Reflog e Stash

Sobre tecnicas avancadas de integracao de codigo, modificacao de historico e recuperacao de estados no Git, julgue as proposicoes:

- **(01)** Enquanto o `git merge` preserva a cronologia e a topologia original das ramificacoes gerando commits de integracao (*merge commits*), o `git rebase` reaplica linearmente os commits de uma branch sobre o topo de outra, alterando os hashes SHA-1 dos commits movidos e resultando em um historico linear sem bifurcacoes visuais.
- **(02)** O comando `git rebase` e uma pratica recomendada e segura para ser executada em branches publicas e compartilhadas por varios membros da equipe (como a branch `main` no servidor remoto), uma vez que nao afeta a rastreabilidade dos colaboradores externos.
- **(04)** O comando `git reset HEAD~1 --soft` desloca o ponteiro da branch corrente de volta para o commit pai imediato, mantendo intactas as alteracoes nos arquivos do projeto e conservando-as preparadas na *Staging Area* para um novo commit.
- **(08)** O utilitario `git reflog` registra a sequencia cronologica local de todas as alteracoes sofridas pelo ponteiro `HEAD`, constituindo um mecanismo eficaz para restaurar commits orfaos apos a execucao acidental de um `git reset --hard`.
- **(16)** O comando `git stash` isola e salva temporariamente em uma pilha de contexto local as alteracoes pendentes no *Working Directory* e na *Staging Area*, permitindo que o desenvolvedor alterne de branch com a area de trabalho limpa sem necessidade de realizar commits preliminares ou descartar codigo.

**SOMA DA QUESTAO 03:** [ ______ ]

---

### Questao 04 (Valor: 2,0 pontos)
**Tema:** SmartNotes - Semantic Versioning (SemVer) e Gerenciamento de Dependencias

Considerando a especificacao de Versionamento Semantico (SemVer) e as declaracoes de dependencias gerenciadas no `package.json` de aplicacoes Node.js, analise as proposicoes:

- **(01)** De acordo com o SemVer (`MAJOR.MINOR.PATCH`), a transicao de versao de `5.2.0` para `6.0.0` comunica formalmente aos consumidores do pacote que modificacoes incompativeis de API (*breaking changes*) foram introduzidas.
- **(02)** Ao especificar a dependencia `"express": "^5.2.1"`, o operador circunflexo (`^`) autoriza o comando `npm update` a instalar atualizacoes dentro da mesma versao MAJOR (permitindo a instalacao automatica de versoes como `5.2.2`, `5.3.0` ou `5.5.3`), porem bloqueia a instalacao da versao `6.0.0`.
- **(04)** No SemVer, a adicao de novas funcionalidades compativeis com as interfaces vigentes exige a atualizacao do digito MINOR, momento no qual o identificador de PATCH e reiniciado em zero (ex.: a versao `5.1.4` evolui para `5.2.0`).
- **(08)** A utilizacao do operador til (`~`) na declaracao `"express": "~5.2.1"` confere maior liberdade de atualizacao que o operador circunflexo (`^`), pois o til autoriza tanto novas versoes MINOR quanto novas versoes MAJOR no comando `npm update`.
- **(16)** Caso uma dependencia esteja declarada sob a sintaxe `"express": "~5.2.1"`, a execucao do comando `npm update` permitira a atualizacao para correcoes de bugs como `5.2.3` ou `5.2.9`, mas impedira a instalacao da versao `5.3.0`.

**SOMA DA QUESTAO 04:** [ ______ ]

---

### Questao 05 (Valor: 2,0 pontos)
**Tema:** SmartNotes - Variaveis de Ambiente, Envalid e Qualidade de Codigo (ESLint e Prettier)

A respeito de gestao de variaveis de ambiente, validacao de esquemas de configuracao e ferramentas de qualidade de codigo no ecossistema Node.js/TypeScript, julgue as proposicoes:

- **(01)** Variaveis de ambiente representam configuracoes de execucao (como credenciais, portas e chaves criptograficas) que devem ser definidas em arquivos locais nao versionados (como `.env`), os quais devem constar obrigatoriamente no `.gitignore`, mantendo-se no repositorio um arquivo `.env.example` para documentar as variaveis requeridas.
- **(02)** O pacote `envalid` fornece o metodo `cleanEnv`, que viabiliza a implementacao de uma validacao estrita em tempo de inicializacao (*fail-fast*), interrompendo imediatamente o processo com erro descritivo caso o arquivo `.env` nao forneca as variaveis obrigatorias ou caso os dados nao correspondam aos validadores definidos (como `str()` ou `port()`).
- **(04)** O ESLint e o Prettier exercem papeis identicos e concorrentes: o ESLint e responsavel exclusivamente pela estilizacao de espacos e quebras de linha visuais, ao passo que o Prettier e a ferramenta encarregada de fazer a analise semantica profunda e deteccao de bugs no codigo-fonte.
- **(08)** No formato moderno de configuracao modular do ESLint (`eslint.config.mjs`), as regras individuais podem ser ajustadas explicitamente com tres niveis de severidade padronizados: `"off"` (desativa a regra), `"warn"` (emite advertencia sem falhar a validacao) e `"error"` (emite erro impeditivo de validacao).
- **(16)** No arquivo `.prettierrc`, diretivas como `"printWidth": 150`, `"singleQuote": true`, `"semi": true` e `"arrowParens": "avoid"` configuram o comportamento do formatador de codigo, o qual pode ser integrado a editores como o VS Code para reformatar os arquivos automaticamente a cada evento de salvamento.

**SOMA DA QUESTAO 05:** [ ______ ]

---

## Folha de Gabarito e Justificativa Tecnica

### Resumo das Respostas Corretas

| Questao | Proposicoes Verdadeiras | Calculo da Soma Unica | Resposta Final (Soma) | Pontuacao |
| :---: | :---: | :---: | :---: | :---: |
| **Questao 01** | (01), (02), (08) | 01 + 02 + 08 | **11** | 2,0 pontos |
| **Questao 02** | (01), (04), (16) | 01 + 04 + 16 | **21** | 2,0 pontos |
| **Questao 03** | (01), (04), (08), (16) | 01 + 04 + 08 + 16 | **29** | 2,0 pontos |
| **Questao 04** | (01), (02), (04), (16) | 01 + 02 + 04 + 16 | **23** | 2,0 pontos |
| **Questao 05** | (01), (02), (08), (16) | 01 + 02 + 08 + 16 | **27** | 2,0 pontos |
| **TOTAL** | - | - | - | **10,0 pontos** |

---

### Resolucao Comentada Item por Item

#### Questao 01 - Soma: 11
- **(01) [VERDADEIRA]**: Nos sistemas centralizados (CVS/SVN), a queda do servidor central paralisa o controle de versao de toda a equipe. No Git, o modelo distribuido assegura que cada estacao de trabalho possua um repositorio local independente com o grafo completo de revisoes (Slides 5 a 8 de `1_git.pdf`).
- **(02) [VERDADEIRA]**: A arquitetura do Git divide as alteracoes em tres areas: Working Directory (arquivos locais editaveis), Staging Area/Index (arquivos preparados para commit) e Repository/`.git` (armazenamento permanente de commits) (Slide 22 de `1_git.pdf`).
- **(04) [FALSA]**: O comando `git commit` opera de forma estritamente local, gravando o commit no repositorio local (`.git`). O envio para servidores remotos exige a execucao explicita do comando de rede `git push` (Slides 21 e 96 de `1_git.pdf`).
- **(08) [VERDADEIRA]**: Arquivos gerados em tempo de execucao, dependencias locais (`node_modules`) e credenciais nao devem ser rastreados. O `.gitignore` define esses padroes e deve ser comitado para que todos os membros do projeto compartilhem as mesmas regras de exclusao (Slides 30 a 35 de `1_git.pdf` e Slide 37 de `smartnotes.pdf`).
- **(16) [FALSA]**: O arquivo `.gitignore` atua apenas sobre arquivos nao rastreados (*untracked*). Arquivos que ja foram comitados continuam no historico e precisam ser removidos do indice manualmente via `git rm --cached` (Slides 30 a 34 de `1_git.pdf`).

#### Questao 02 - Soma: 21
- **(01) [VERDADEIRA]**: Uma branch no Git e implementada como uma referencia simples (um arquivo contendo o hash de 40 caracteres do commit correspondente), tornando sua criacao e alternancia operacoes instantaneas (Slides 45 e 46 de `1_git.pdf`).
- **(02) [FALSA]**: O `HEAD` aponta normalmente para a branch local ativa. Quando o `HEAD` e apontado diretamente para um hash de commit (usando `git switch --detach <commit>`), o Git entra no estado de *Detached HEAD*, sem depender de repositorios remotos (Slides 54 a 56 de `1_git.pdf`).
- **(04) [VERDADEIRA]**: O *Fast-Forward merge* acontece quando a branch a ser integrada e uma descendente direta da branch atual, permitindo apenas avancar o ponteiro sem necessidade de reconciliacao de tres vias ou novo commit de merge (Slides 58 a 60 de `1_git.pdf`).
- **(08) [FALSA]**: O Git consegue mesclar automaticamente arquivos distintos e trechos disjuntos do mesmo arquivo atraves do algoritmo de *three-way merge*. Conflitos ocorrem apenas em sobreposicao de alteracoes nas mesmas linhas de um mesmo arquivo (Slides 70 e 71 de `1_git.pdf`).
- **(16) [VERDADEIRA]**: Em caso de conflito, o Git injeta delimitadores visuais (`<<<<<<<`, `=======`, `>>>>>>>`). A resolucao exige edicao manual, remocao dos delimitadores e posterior `git add` no arquivo para marcar o conflito como sanado (Slides 76 a 82 de `1_git.pdf`).

#### Questao 03 - Soma: 29
- **(01) [VERDADEIRA]**: O comando `git rebase` reescreve o historico pegando os commits da branch de topico e reaplicando-os linearmente a partir do commit de ponta da branch base, gerando novos identificadores de commit e mantendo o grafo linear, em contraste com a topologia ramificada do `git merge` (Slides 112 a 118 de `1_git.pdf`).
- **(02) [FALSA]**: A regra de ouro do Git contraindica rebase em branches publicas/compartilhadas. Como o rebase cria novos commits e descarta os antigos, forcar essa alteracao no remoto quebra o historico de trabalho de outros colaboradores que ja clonaram ou basearam branches nos commits originais (Slides 116 e 118 de `1_git.pdf`).
- **(04) [VERDADEIRA]**: O parametro `--soft` no `git reset` move exclusivamente a referencia da branch para o commit indicado, mantendo as diferencas na *Staging Area* prontas para um novo commit (Slide 133 de `1_git.pdf`).
- **(08) [VERDADEIRA]**: O `git reflog` guarda o log de todas as movimentacoes de `HEAD` na maquina local por um periodo de retencao. Mesmo apos um `git reset --hard`, o hash do commit descartado pode ser localizado no `reflog` e recuperado (Slides 136 a 140 de `1_git.pdf`).
- **(16) [VERDADEIRA]**: O `git stash` fornece um mecanismo de armazenamento em pilha para guardar o trabalho incompleto do diretorio de trabalho e da staging area, restaurando o diretorio para o estado limpo do ultimo commit (Slides 146 a 148 de `1_git.pdf`).

#### Questao 04 - Soma: 23
- **(01) [VERDADEIRA]**: No SemVer, o incremento de MAJOR e formalmente reservado para incompatibilidades de contrato/API (ex.: `5.2.0` -> `6.0.0`), alertando os utilizadores sobre a necessidade de ajustes em seus codigos (Slides 22 e 23 de `smartnotes.pdf`).
- **(02) [VERDADEIRA]**: O operador circunflexo `^` permite a instalacao de quaisquer novas versoes MINOR ou PATCH dentro daquela versao MAJOR (permitindo `5.2.2`, `5.3.0`), mas barra rigorosamente a entrada de versoes com MAJOR diferente, como `6.0.0` (Slide 24 de `smartnotes.pdf`).
- **(04) [VERDADEIRA]**: Conforme a regra formal do SemVer, toda adicao de funcionalidade compativel eleva o digito MINOR e zera o digito PATCH (ex.: `5.1.4` -> `5.2.0`) (Slides 22 e 23 de `smartnotes.pdf`).
- **(08) [FALSA]**: O operador til (`~`) e mais restritivo que o circunflexo (`^`). Ele restringe a atualizacao estritamente a novos PATCHs dentro do mesmo MINOR (ex.: `~5.2.1` so aceita `5.2.x`), nunca autorizando saltos de MINOR ou de MAJOR (Slide 25 de `smartnotes.pdf`).
- **(16) [VERDADEIRA]**: Sob a regra de `"express": "~5.2.1"`, versoes de correcao de bug dentro do minor 2 (como `5.2.3` e `5.2.9`) sao aceitas, mas mudancas de MINOR como `5.3.0` sao rejeitadas (Slide 25 de `smartnotes.pdf`).

#### Questao 05 - Soma: 27
- **(01) [VERDADEIRA]**: Segredos e configuracoes de infraestrutura nao devem ser expostos em controle de versao. Ficam em `.env` (ignorado no `.gitignore`), e o `.env.example` e versionado como documentacao das variaveis necessarias (Slides 32 a 37 de `smartnotes.pdf`).
- **(02) [VERDADEIRA]**: O `envalid` valida a presenca e tipagem das variaveis lidas pelo `dotenv` logo na inicializacao da aplicacao. Se faltar alguma variavel ou se o tipo for inconsistente, lanca excecao imediata (fail-fast), prevenindo execucao com ambiente corrompido (Slides 38 a 44 de `smartnotes.pdf`).
- **(04) [FALSA]**: As ferramentas tem propositos distintos: o ESLint e um *Linter* voltado para analise estatica de regras de codificacao, bugs potenciais e padroes de sintaxe, enquanto o Prettier e estritamente um *Formatador de codigo* focado em estetica visual, indentacao e layout de texto (Slides 45 a 48 de `smartnotes.pdf`).
- **(08) [VERDADEIRA]**: No arquivo `eslint.config.mjs`, o ESLint suporta os tres modificadores universais de severidade para cada regra: `"off"`, `"warn"` e `"error"` (Slides 55 e 56 de `smartnotes.pdf`).
- **(16) [VERDADEIRA]**: O `.prettierrc` centraliza parametros de estilo como largura de linha (`printWidth`), uso de aspas simples (`singleQuote`), ponto-e-virgula (`semi`) e parenteses em arrow functions (`arrowParens`), permitindo automacao total integrada ao editor (Slides 60 e 61 de `smartnotes.pdf`).
