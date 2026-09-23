# Simulado Somativo 01 - Preparacao para a Prova de Gerencia de Configuracao

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
**Tema:** Git - Arquitetura, Fundamentos e os Tres Estados do Ciclo de Vida

Com relacao a arquitetura dos sistemas de controle de versao e aos conceitos fundamentais de funcionamento do Git, analise as proposicoes a seguir:

- **(01)** Diferentemente dos Sistemas de Controle de Versao Centralizados (como CVS ou Subversion), nos quais a indisponibilidade do servidor central bloqueia o registro de versoes pelos desenvolvedores, o Git fundamenta-se em uma arquitetura distribuida, onde cada clone local contem uma copia integral do repositorio com todo o seu historico.
- **(02)** O Git estrutura o ciclo de vida dos arquivos em tres estados fundamentais: Working Directory (diretorio de trabalho contendo os arquivos modificados), Staging Area / Index (area de preparacao onde as alteracoes sao selecionadas para o proximo commit) e Repository / .git directory (banco de objetos onde os snapshots confirmados sao gravados de maneira permanente).
- **(04)** A execucao do comando git commit -m 'mensagem' consolida as modificacoes diretamente no servidor remoto (como GitHub ou GitLab), sendo desnecessario executar o comando git push para sincronizacao com a equipe.
- **(08)** O arquivo .gitignore e utilizado para listar padroes de nomes de arquivos e diretorios que nao devem ser rastreados pelo Git (como node_modules/, logs e arquivos de segredos locais), devendo ele proprio ser comitado no repositorio para garantir a padronizacao das exclusoes entre todos os colaboradores.
- **(16)** A inclusao de um padrao de arquivo no .gitignore remove automaticamente e de forma retroativa os arquivos correspondentes que ja haviam sido comitados no historico do repositorio.

**SOMA DA QUESTAO 01:** [ ______ ]

---

### Questao 02 (Valor: 2.0 pontos)
**Tema:** Git - Ramificacao (Branches), Ponteiro HEAD e Conflitos de Integracao

Em relacao ao mecanismo de ramificacao, ponteiros de navegacao e resolucao de conflitos de merge no Git, avalie as proposicoes:

- **(01)** No Git, uma branch nao e uma duplicacao fisica dos arquivos do projeto no disco, mas sim um ponteiro movel de baixo custo computacional que referencia um commit especifico na arvore historica.
- **(02)** O ponteiro HEAD referencia obrigatoriamente um commit hospedado no repositorio remoto origin, sendo tecnicamente impossivel configurar o HEAD para apontar diretamente para um commit local sem vincular a uma branch nominal.
- **(04)** A operacao de mesclagem do tipo Fast-Forward ocorre quando a branch de destino nao possui commits divergentes em relacao a branch integrada, permitindo ao Git simplesmente deslocar o ponteiro da branch de destino diretamente para o topo da branch mesclada, sem a criacao de um novo commit de merge.
- **(08)** Quando duas branches realizam alteracoes em arquivos distintos ou em trechos nao sobrepostos do mesmo arquivo, o Git nao consegue unificar as alteracoes de forma automatica, gerando compulsoriamente um conflito de merge.
- **(16)** Durante a ocorrencia de um conflito de merge, o Git inclui marcadores visuais no arquivo afetado (como <<<<<<< HEAD, ======= e >>>>>>> <branch>), cabendo ao desenvolvedor inspecionar o arquivo, reconciliar o conteudo desejado, remover os delimitadores e executar git add para assinalar a resolucao do conflito.

**SOMA DA QUESTAO 02:** [ ______ ]

---

### Questao 03 (Valor: 2.0 pontos)
**Tema:** Git - Rebase, Modos de Reset, Reflog e Stash

Sobre tecnicas avancadas de integracao de codigo, modificacao de historico e recuperacao de estados no Git, julgue as proposicoes:

- **(01)** Enquanto o git merge preserva a cronologia e a topologia original das ramificacoes gerando commits de integracao (merge commits), o git rebase reaplica linearmente os commits de uma branch sobre o topo de outra, alterando os hashes SHA-1 dos commits movidos e resultando em um historico linear sem bifurcacoes visuais.
- **(02)** O comando git rebase e uma pratica recomendada e segura para ser executada em branches publicas e compartilhadas por varios membros da equipe (como a branch main no servidor remoto), uma vez que nao afeta a rastreabilidade dos colaboradores externos.
- **(04)** O comando git reset HEAD~1 --soft desloca o ponteiro da branch corrente de volta para o commit pai imediato, mantendo intactas as alteracoes nos arquivos do projeto e conservando-as preparadas na Staging Area para um novo commit.
- **(08)** O utilitario git reflog registra a sequencia cronologica local de todas as alteracoes sofridas pelo ponteiro HEAD, constituindo um mecanismo eficaz para restaurar commits orfaos apos a execucao acidental de um git reset --hard.
- **(16)** O comando git stash isola e salva temporariamente em uma pilha de contexto local as alteracoes pendentes no Working Directory e na Staging Area, permitindo que o desenvolvedor alterne de branch com a area de trabalho limpa sem necessidade de realizar commits preliminares ou descartar codigo.

**SOMA DA QUESTAO 03:** [ ______ ]

---

### Questao 04 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Semantic Versioning (SemVer) e Gerenciamento de Dependencias

Considerando a especificacao de Versionamento Semantico (SemVer) e as declaracoes de dependencias gerenciadas no package.json de aplicacoes Node.js, analise as proposicoes:

- **(01)** De acordo com o SemVer (MAJOR.MINOR.PATCH), a transicao de versao de 5.2.0 para 6.0.0 comunica formalmente aos consumidores do pacote que modificacoes incompativeis de API (breaking changes) foram introduzidas.
- **(02)** Ao especificar a dependencia 'express': '^5.2.1', o operador circunflexo (^) autoriza o comando npm update a instalar atualizacoes dentro da mesma versao MAJOR (permitindo a instalacao automatica de versoes como 5.2.2, 5.3.0 ou 5.5.3), porem bloqueia a instalacao da versao 6.0.0.
- **(04)** No SemVer, a adicao de novas funcionalidades compativeis com as interfaces vigentes exige a atualizacao do digito MINOR, momento no qual o identificador de PATCH e reiniciado em zero (ex.: a versao 5.1.4 evolui para 5.2.0).
- **(08)** A utilizacao do operador til (~) na declaracao 'express': '~5.2.1' confere maior liberdade de atualizacao que o operador circunflexo (^), pois o til autoriza tanto novas versoes MINOR quanto novas versoes MAJOR no comando npm update.
- **(16)** Caso uma dependencia esteja declarada sob a sintaxe 'express': '~5.2.1', a execucao do comando npm update permitira a atualizacao para correcoes de bugs como 5.2.3 ou 5.2.9, mas impedira a instalacao da versao 5.3.0.

**SOMA DA QUESTAO 04:** [ ______ ]

---

### Questao 05 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Variaveis de Ambiente, Envalid e Qualidade de Codigo (ESLint e Prettier)

A respeito de gestao de variaveis de ambiente, validacao de esquemas de configuracao e ferramentas de qualidade de codigo no ecossistema Node.js/TypeScript, julgue as proposicoes:

- **(01)** Variaveis de ambiente representam configuracoes de execucao (como credenciais, portas e chaves criptograficas) que devem ser definidas em arquivos locais nao versionados (como .env), os quais devem constar obrigatoriamente no .gitignore, mantendo-se no repositorio um arquivo .env.example para documentar as variaveis requeridas.
- **(02)** O pacote envalid fornece o metodo cleanEnv, que viabiliza a implementacao de uma validacao estrita em tempo de inicializacao (fail-fast), interrompendo imediatamente o processo com erro descritivo caso o arquivo .env nao forneca as variaveis obrigatorias ou caso os dados nao correspondam aos validadores definidos (como str() ou port()).
- **(04)** O ESLint e o Prettier exercem papeis identicos e concorrentes: o ESLint e responsavel exclusivamente pela estilizacao de espacos e quebras de linha visuais, ao passo que o Prettier e a ferramenta encarregada de fazer a analise semantica profunda e deteccao de bugs no codigo-fonte.
- **(08)** No formato moderno de configuracao modular do ESLint (eslint.config.mjs), as regras individuais podem ser ajustadas explicitamente com tres niveis de severidade padronizados: 'off' (desativa a regra), 'warn' (emite advertencia sem falhar a validacao) e 'error' (emite erro impeditivo de validacao).
- **(16)** No arquivo .prettierrc, diretivas como 'printWidth': 150, 'singleQuote': true, 'semi': true e 'arrowParens': 'avoid' configuram o comportamento do formatador de codigo, o qual pode ser integrado a editores como o VS Code para reformatar os arquivos automaticamente a cada evento de salvamento.

**SOMA DA QUESTAO 05:** [ ______ ]

---

## Folha de Gabarito e Justificativas Tecnicas

### Resumo das Respostas Corretas

| Questao | Proposicoes Verdadeiras | Calculo da Soma Unica | Resposta Final (Soma) | Pontos |
| :---: | :---: | :---: | :---: | :---: |
| **Questao 01** | (01), (02), (08) | 01 + 02 + 08 | **11** | 2.0 |
| **Questao 02** | (01), (04), (16) | 01 + 04 + 16 | **21** | 2.0 |
| **Questao 03** | (01), (04), (08), (16) | 01 + 04 + 08 + 16 | **29** | 2.0 |
| **Questao 04** | (01), (02), (04), (16) | 01 + 02 + 04 + 16 | **23** | 2.0 |
| **Questao 05** | (01), (02), (08), (16) | 01 + 02 + 08 + 16 | **27** | 2.0 |
| **TOTAL** | - | - | - | **10.0** |

---

### Resolucao Detalhada Item por Item

#### Questao 01 - Soma: 11
- **(01) [VERDADEIRA]**: No modelo centralizado, a indisponibilidade do servidor impede qualquer gravacao de historico pela equipe; no Git distribuido, cada cliente possui um repositorio completo e opera de forma autônoma offline (Slides 5 a 8 de 1_git.pdf).
- **(02) [VERDADEIRA]**: Essa triade constitui o fluxo operacional central do Git, dividindo o ciclo de vida entre edicao local, preparacao de commits e persistencia definitiva no banco de dados do Git (Slide 22 de 1_git.pdf).
- **(04) [FALSA]**: O comando git commit opera estritamente no repositorio local. O envio dos commits locais para o servidor remoto exige o comando de rede git push (Slides 21 e 96 de 1_git.pdf).
- **(08) [VERDADEIRA]**: O .gitignore define padroes ignorados pelo versionador e deve ser integrado ao repositorio para que toda a equipe adote as mesmas exclusoes de dependencias e credenciais (Slides 30 a 35 de 1_git.pdf e Slide 37 de smartnotes.pdf).
- **(16) [FALSA]**: O .gitignore atua somente sobre arquivos nao rastreados (untracked). Arquivos ja comitados permanecem no historico e precisam ser removidos do indice via git rm --cached (Slides 30 a 34 de 1_git.pdf).

#### Questao 02 - Soma: 21
- **(01) [VERDADEIRA]**: Uma branch e apenas uma referencia de texto de 41 bytes contendo o hash do commit apontado, permitindo criacao e chaveamento instantaneos (Slides 45 e 46 de 1_git.pdf).
- **(02) [FALSA]**: O HEAD referencia a branch ou commit local ativo. Ao apontar diretamente para um commit (via git switch --detach <commit>), o Git entra no estado de Detached HEAD localmente (Slides 54 a 56 de 1_git.pdf).
- **(04) [VERDADEIRA]**: Na ausencia de bifurcacao divergente no historico, o Git apenas avanca o ponteiro da branch destino linearmente ate a ponta da branch mesclada (Slides 58 a 60 de 1_git.pdf).
- **(08) [FALSA]**: O Git unifica alteracoes em arquivos distintos ou regioes distintas do mesmo arquivo de modo automatico via three-way merge, gerando conflito apenas em colisoes na mesma linha (Slides 70 e 71 de 1_git.pdf).
- **(16) [VERDADEIRA]**: Os delimitadores visuais marcam as duas versoes conflitantes. A resolucao manual requer correcao do texto, remocao dos marcadores e adicao ao index via git add (Slides 76 a 82 de 1_git.pdf).

#### Questao 03 - Soma: 29
- **(01) [VERDADEIRA]**: O rebase gera novos commits reaplicados no topo da base, gerando novos hashes e garantindo grafo linear em contraposicao ao historico topologico do merge (Slides 112 a 118 de 1_git.pdf).
- **(02) [FALSA]**: A regra de ouro proibe rebase em branches publicas: alterar hashes de commits ja baixados por outros colaboradores gera graves problemas de divergencia historica (Slides 116 e 118 de 1_git.pdf).
- **(04) [VERDADEIRA]**: O modo --soft retrocede a ponta da branch sem tocar no indice nem na arvore de trabalho, deixando tudo em staging pronto para commit (Slide 133 de 1_git.pdf).
- **(08) [VERDADEIRA]**: O reflog rastreia toda mudanca de ponteiro local e retem os hashes de commits aparentemente perdidos, permitindo recupera-los com facilidade (Slides 136 a 140 de 1_git.pdf).
- **(16) [VERDADEIRA]**: O stash armazena modificacoes em andamento em uma pilha local, limpando o diretorio de trabalho para alternancia rapida de branches (Slides 146 a 148 de 1_git.pdf).

#### Questao 04 - Soma: 23
- **(01) [VERDADEIRA]**: A elevacao de MAJOR sinaliza quebras de compatibilidade retroativa e mudancas na assinatura publica do software (Slides 22 e 23 de smartnotes.pdf).
- **(02) [VERDADEIRA]**: O circunflexo permite atualizacoes de MINOR e PATCH na versao especificada, impedindo a subida para o proximo MAJOR (Slide 24 de smartnotes.pdf).
- **(04) [VERDADEIRA]**: Incrementos MINOR acrescentam funcionalidades retrocompativeis e exigem a reinicializacao do digito PATCH para zero (Slides 22 e 23 de smartnotes.pdf).
- **(08) [FALSA]**: O til e mais conservador e restrito que o circunflexo; ele permite exclusivamente atualizacoes de PATCH dentro do mesmo MINOR (Slide 25 de smartnotes.pdf).
- **(16) [VERDADEIRA]**: O operador ~ trava a versao no nivel minor 5.2, aceitando somente incrementos no digito patch 5.2.x (Slide 25 de smartnotes.pdf).

#### Questao 05 - Soma: 27
- **(01) [VERDADEIRA]**: Configuracoes sensiveis residem em .env excluido do Git, enquanto .env.example serve como gabarito publico de variaveis para a equipe (Slides 32 a 37 de smartnotes.pdf).
- **(02) [VERDADEIRA]**: O cleanEnv valida tipagem e presenca de variaveis antes que o servidor suba, lancando excecao caso as regras sejam violadas (Slides 38 a 44 de smartnotes.pdf).
- **(04) [FALSA]**: Os papeis sao opostos: o ESLint e um Linter de analise estatica e deteccao de bugs/sintaxe; o Prettier e estritamente um Formatador de codigo visual (Slides 45 a 48 de smartnotes.pdf).
- **(08) [VERDADEIRA]**: As severidades oficiais no ESLint sao off, warn e error, permitindo dosar o rigor da analise por regra (Slides 55 e 56 de smartnotes.pdf).
- **(16) [VERDADEIRA]**: O .prettierrc padroniza as regras estilisticas e sua extensao no VS Code formata o codigo automaticamente ao salvar (Slides 60 e 61 de smartnotes.pdf).
