# Simulado Somativo 03 - Preparacao para a Prova de Gerencia de Configuracao

**Disciplina:** Gerencia de Configuracao  
**Material de Referencia:** Aulas e Slides do Prof. David Fernandes de Oliveira (IC/UFAM)  
**Elaboracao:** Simulado Independente de Estudos para a Prova  
**Pontuacao Total:** 10.0 pontos  
**Formato:** Questoes de Verdadeiro (V) ou Falso (F) no Formato Somativo

---

## Instrucoes

Cada questao contem 5 proposicoes com valores binarios (01, 02, 04, 08, 16). A resposta corresponde a soma exclusiva das proposicoes verdadeiras. Cada questao vale 2,0 pontos.

---

## Questoes

### Questao 01 (Valor: 2.0 pontos)
**Tema:** Git - Desfazimento de Alteracoes e Diferencas entre Modos de Reset

Em relacao as operacoes de cancelamento e desfazimento de mudancas no Git, julgue as assertivas a seguir:

- **(01)** O comando git restore <arquivo> descarta as modificacoes nao indexadas de um arquivo no Working Directory, revertendo-o ao estado atualmente registrado na Staging Area ou no ultimo commit.
- **(02)** O comando git restore --staged <arquivo> retira o arquivo indicado da Staging Area (desindexacao), preservando integralmente o conteudo modificado no Working Directory.
- **(04)** O modo padrao do comando git reset (equivalente a git reset --mixed) move o ponteiro da branch de volta ao commit informado e remove as alteracoes da Staging Area, mantendo as modificacoes no Working Directory.
- **(08)** O comando git commit --amend permite incorporar novos arquivos da Staging Area ao ultimo commit realizado ou alterar a mensagem desse commit, sem gerar um commit adicional no historico.
- **(16)** A execucao de git reset --hard HEAD~1 e uma operacao branda que cria um commit de reversao sem eliminar quaisquer arquivos do disco.

**SOMA DA QUESTAO 01:** [ ______ ]

---

### Questao 02 (Valor: 2.0 pontos)
**Tema:** Git - Detached HEAD, Diagnostico de Conflitos e Aborto de Merge

A respeito de situacoes excepcionais de navegacao e resolucao de conflitos no Git, avalie as proposicoes:

- **(01)** Quando um conflito de merge acontece, os arquivos conflitantes continuam compativeis para compilacao imediata, pois o compilador ignora nativamente os caracteres <<<<<<< e >>>>>>>.
- **(02)** No estado de Detached HEAD (obtido, por exemplo, com git switch --detach <commit>), o HEAD aponta diretamente para um commit e nao para uma branch, de modo que commits criados nesse estado nao pertencem automaticamente a nenhuma branch.
- **(04)** Caso ocorram conflitos complexos durante uma operacao de integracao e o desenvolvedor opte por desistir do processo, o comando git merge --abort interrompe a mesclagem e restaura o estado exato anterior ao comando de merge.
- **(08)** A expressao HEAD~2 referencia o commit correspondente ao 'avo' do commit atualmente ativo.
- **(16)** O utilitario git stash pop restaura as modificacoes mais recentes salvas na pilha de stash e as remove automaticamente dessa pilha de armazenamento temporario.

**SOMA DA QUESTAO 02:** [ ______ ]

---

### Questao 03 (Valor: 2.0 pontos)
**Tema:** Git - Integracao com Rebase versus Three-Way Merge e Regra de Ouro

Comparando as abordagens de integracao de codigo no Git por git merge e git rebase, julgue as assertivas:

- **(01)** O git merge e a abordagem preferencial quando se deseja preservar a fidelidade historica e cronologica das bifurcacoes ou quando se esta integrando branches colaborativas de longa duracao.
- **(02)** O git rebase e frequentemente utilizado em branches locais de feature antes do merge na main para incorporar atualizacoes recentes da branch base e evitar commits de merge desnecessarios.
- **(04)** Ao sofrer rebase, os commits originais mantem seus mesmos identificadores de hash SHA-1 inalterados, viabilizando o pareamento perfeito com branches remotas clonadas por terceiros.
- **(08)** Um merge commit e necessario quando as duas branches avancaram separadamente, ou seja, quando nao e possivel realizar um fast-forward; esse novo commit integra o historico das duas branches.
- **(16)** Se um commit for descartado indevidamente por um git reset --hard, o comando git log sem argumentos especiais sera a ferramenta indicada para localiza-lo e resgata-lo.

**SOMA DA QUESTAO 03:** [ ______ ]

---

### Questao 04 (Valor: 2.0 pontos)
**Tema:** SmartNotes - SemVer Estrito e Resolucao de Versoes no Ecossistema NPM

A respeito das convencoes de numeracao de software e especificacao SemVer (Semantic Versioning), avalie as proposicoes:

- **(01)** Uma versao SemVer obedece rigidamente ao formato MAJOR.MINOR.PATCH, no qual cada segmento possui significado semantico formal definido pelo impacto da mudanca no sistema.
- **(02)** O operador de dependencia ^ (circunflexo) instalado na versao ^5.2.1 autoriza o npm update a instalar uma versao 6.0.0 lancada posteriormente pelos mantenedores da biblioteca.
- **(04)** A evolucao de 5.1.0 para 5.1.1 representa uma correcao de falha (patch) que nao introduz novas funcionalidades e preserva completa compatibilidade retroativa com versoes anteriores.
- **(08)** A declaracao de versao 'express': '5.2.1' (sem prefixos como ^ ou ~) impoe a instalacao estrita e exata da versao 5.2.1, nao sofrendo atualizacoes automaticas via npm update.
- **(16)** O operador ~ (til) e mais conservador do que o circunflexo (^), permitindo ao npm instalar apenas novas versoes de correcao de bug (PATCHs), protegendo a aplicacao contra alteracoes de comportamento em funcionalidades novas.

**SOMA DA QUESTAO 04:** [ ______ ]

---

### Questao 05 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Validacao com Envalid e Configuracao Flat no ESLint

No contexto da configuracao robusta de servidores Node.js com TypeScript, analise as proposicoes sobre o envalid e o ESLint:

- **(01)** A biblioteca envalid impede falhas silenciosas na aplicacao por meio da abordagem fail-fast, garantindo que o servidor nao inicie se configuracoes vitais de conexao ou seguranca estiverem ausentes.
- **(02)** A funcao cleanEnv do envalid aceita validadores de tipo como str() para cadeias de caracteres e port() para portas de rede com limites numericos validos e valores default opcionais.
- **(04)** Configurar uma regra no ESLint com o valor 'off' faz com que o linter interrompa a compilacao do projeto emitindo um codigo de erro fatal para o sistema operacional.
- **(08)** No novo sistema de configuracao flat do ESLint (arquivo eslint.config.mjs), e possivel definir regras especificas para o compilador TypeScript atraves do pacote typescript-eslint.
- **(16)** A utilizacao da extensao oficial do ESLint ou Prettier no VS Code permite identificar violacoes de regras em tempo real no editor e reformatar o arquivo automaticamente ao pressionar Ctrl+S.

**SOMA DA QUESTAO 05:** [ ______ ]

---

## Folha de Gabarito e Justificativas Tecnicas

### Resumo das Respostas Corretas

| Questao | Proposicoes Verdadeiras | Calculo da Soma Unica | Resposta Final (Soma) | Pontos |
| :---: | :---: | :---: | :---: | :---: |
| **Questao 01** | (01), (02), (04), (08) | 01 + 02 + 04 + 08 | **15** | 2.0 |
| **Questao 02** | (02), (04), (08), (16) | 02 + 04 + 08 + 16 | **30** | 2.0 |
| **Questao 03** | (01), (02), (08) | 01 + 02 + 08 | **11** | 2.0 |
| **Questao 04** | (01), (04), (08), (16) | 01 + 04 + 08 + 16 | **29** | 2.0 |
| **Questao 05** | (01), (02), (08), (16) | 01 + 02 + 08 + 16 | **27** | 2.0 |
| **TOTAL** | - | - | - | **10.0** |

---

### Resolucao Detalhada Item por Item

#### Questao 01 - Soma: 15
- **(01) [VERDADEIRA]**: O restore restaura o arquivo de trabalho com base no index, descartando edicoes locais nao salvas (1_git.pdf).
- **(02) [VERDADEIRA]**: O --staged desfaz apenas o git add: o arquivo volta de staged para modified sem perder o trabalho editado (1_git.pdf, Desfazendo alteracoes).
- **(04) [VERDADEIRA]**: O comportamento padrao do reset e o --mixed, que desfaz a preparacao no index mantendo os arquivos no disco para revisao (1_git.pdf).
- **(08) [VERDADEIRA]**: O --amend retifica o commit mais recente combinando alteracoes pendentes no index com o snapshot imediatamente anterior (1_git.pdf).
- **(16) [FALSA]**: O reset --hard e uma operacao destrutiva que descarta sumariamente tanto a staging area quanto as edicoes no working directory, sem gerar novo commit (1_git.pdf).

#### Questao 02 - Soma: 30
- **(01) [FALSA]**: Os marcadores geram graves erros sintaticos na linguagem de programacao e impedem a compilacao/execucao do codigo ate serem removidos manualmente (1_git.pdf).
- **(02) [VERDADEIRA]**: E o alerta do slide de Detached HEAD: e possivel commitar nesse estado, mas os commits nao ficam associados a uma branch; o uso tipico e inspecionar ou testar versoes antigas (1_git.pdf).
- **(04) [VERDADEIRA]**: O comando git merge --abort limpa os marcadores de conflito e restabelece a branch local ao momento anterior a solicitacao de integracao (1_git.pdf).
- **(08) [VERDADEIRA]**: A notacao de til com numero (HEAD~n) navega retroativamente na linhagem de ancestrais primarios (1_git.pdf).
- **(16) [VERDADEIRA]**: Diferente de git stash apply (que mantem na pilha), o pop aplica o stash e o desempilha imediatamente (1_git.pdf).

#### Questao 03 - Soma: 11
- **(01) [VERDADEIRA]**: O merge preserva o contexto de ramificacao e nao distorce a linha do tempo colaborativa (1_git.pdf).
- **(02) [VERDADEIRA]**: O rebase local lineariza a branch do desenvolvedor, tornando a posterior integracao na base limpa e direta (1_git.pdf).
- **(04) [FALSA]**: O rebase calcula novos hashes SHA-1 para cada commit reaplicado, destruindo a compatibilidade com colaboradores que tenham os hashes anteriores (1_git.pdf).
- **(08) [VERDADEIRA]**: Se as branches divergiram, o Git cria um novo commit de merge unindo as duas linhas; sem divergencia, basta o fast-forward (1_git.pdf, Mesclando Branches).
- **(16) [FALSA]**: O git log apenas percorre commits alcancaveis na arvore atual. Commits orfaos so podem ser localizados via git reflog (1_git.pdf).

#### Questao 04 - Soma: 29
- **(01) [VERDADEIRA]**: A semantica do versionamento divide as modificacoes entre quebras de contrato, adicoes funcionais e correcoes de bugs (smartnotes.pdf).
- **(02) [FALSA]**: O circunflexo bloqueia categoricamente versoes com MAJOR diferente, impedindo que breaking changes sejam instaladas involuntariamente (smartnotes.pdf).
- **(04) [VERDADEIRA]**: PATCH destina-se exclusivamente a correcoes de bugs estaveis e retrocompativeis (smartnotes.pdf).
- **(08) [VERDADEIRA]**: Sem prefixos de intervalo de versao, a dependencia fica fixada (pinned) de maneira deterministica no numero informado (smartnotes.pdf).
- **(16) [VERDADEIRA]**: O til confina o npm update estritamente a correcoes de falhas na mesma versao minor (smartnotes.pdf).

#### Questao 05 - Soma: 27
- **(01) [VERDADEIRA]**: O envalid aborta a execucao imediatamente no bootstrap caso os requisitos do esquema de variaveis nao sejam cumpridos (smartnotes.pdf).
- **(02) [VERDADEIRA]**: Os validadores embutidos asseguram tipos corretos como portas validas e strings obrigatorias ou com valores padrao (smartnotes.pdf).
- **(04) [FALSA]**: O modificador 'off' desativa inteiramente a regra, fazendo com que o ESLint a ignore sem disparar avisos ou erros (smartnotes.pdf).
- **(08) [VERDADEIRA]**: O arquivo modular eslint.config.mjs carrega as recomendacoes de typescript-eslint para aplicar analise estatica ao TypeScript (smartnotes.pdf).
- **(16) [VERDADEIRA]**: A integracao no editor proporciona feedback imediato ao desenvolvedor e formatacao automatica ao salvar arquivos (smartnotes.pdf).
