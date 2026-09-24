# Simulado Somativo 02 - Preparacao para a Prova de Gerencia de Configuracao

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
**Tema:** Git - Configuracao de Identidade, Inicializacao e Semantica de Commits

A respeito dos passos iniciais de configuracao de ambiente no Git e boas praticas de criacao de historico, analise as proposicoes:

- **(01)** A utilizacao do comando git add . adiciona compulsoriamente todos os arquivos do computador ao commit, ignorando quaisquer regras declaradas no arquivo .gitignore.
- **(02)** Apos a instalacao do Git, a configuracao de user.name e user.email via comando git config e essencial, pois o Git incorpora essas informacoes como metadados imutaveis de autoria em cada commit gerado.
- **(04)** O comando git init cria um diretorio oculto denominado .git no diretorio raiz do projeto, responsavel por armazenar todos os metadados, configuracoes, objetos blob, arvores e o historico integral de commits.
- **(08)** A mensagem de commit deve deixar claro o proposito da mudanca no historico do codigo (ex.: 'Corrige calculo de juros em faturas vencidas'), sendo mensagens como 'ajustes', 'fix' ou 'funcionou agora' consideradas pouco uteis.
- **(16)** O comando git status e a ferramenta primordial para inspecionar quais arquivos foram modificados no Working Directory, quais estao preparados na Staging Area e quais estao desprovidos de rastreamento (untracked).

**SOMA DA QUESTAO 01:** [ ______ ]

---

### Questao 02 (Valor: 2.0 pontos)
**Tema:** Git - Rastreamento, Analise de Diffs e Visualizacao de Topologia com Git Log

Sobre tecnicas de inspecao de diferencas e historico de commits no Git, julgue as afirmacoes:

- **(01)** O comando git diff sem argumentos adicionais exibe as diferencas pontuais entre o Working Directory e a Staging Area, isto e, as alteracoes feitas nos arquivos que ainda nao foram preparadas para commit.
- **(02)** A execucao de git log --oneline resume cada commit em uma unica linha composta pelo hash abreviado e pelo texto da primeira linha da mensagem de commit.
- **(04)** O comando git diff --staged e equivalente a git commit --amend, efetuando a substituicao automatica do commit anterior sem necessidade de intervencao do usuario.
- **(08)** O modificador --graph no comando git log renderiza uma representacao textual em arte ASCII das ramificacoes e juncoes da arvore de commits, permitindo compreender a topologia de branches mescladas.
- **(16)** Linhas iniciadas com o caractere cerquilha (#) no arquivo .gitignore sao interpretadas como comentarios pelo Git e desconsideradas na definicao dos padroes de exclusao.

**SOMA DA QUESTAO 02:** [ ______ ]

---

### Questao 03 (Valor: 2.0 pontos)
**Tema:** Git - Repositorios Remotos, Upstream Tracking, Git Fetch e Git Pull

Em relacao a integracao de repositorios locais com servidores remotos (GitHub/GitLab), avalie as proposicoes:

- **(01)** O comando git fetch busca os objetos e referencias do repositorio remoto e os incorpora compulsoriamente a branch local de trabalho, sobrescrevendo quaisquer alteracoes nao salvas do usuario.
- **(02)** Um repositorio Git requer conexao permanente e estavel com a internet para executar operacoes como git commit, git branch, git log e git reset.
- **(04)** O comando git clone cria um repositorio local identico ao remoto, configurando automaticamente um vinculo de remote denominado origin e baixando todos os branches e historico existentes.
- **(08)** O comando git pull e essencialmente uma combinacao logica sequencial de duas operacoes do Git: um git fetch seguido por um git merge da branch rastreada correspondente.
- **(16)** O parametro -u (ou --set-upstream) no comando git push -u origin <branch> estabelece uma ligacao direta de rastreamento entre a branch local e a branch remota, simplificando os proximos comandos para apenas git push ou git pull.

**SOMA DA QUESTAO 03:** [ ______ ]

---

### Questao 04 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Principios 12-Factor, Variaveis de Ambiente e Biblioteca Dotenv

A respeito do armazenamento de configuracoes de aplicacao e do uso do pacote dotenv em projetos Node.js, analise as proposicoes:

- **(01)** Uma opcao para definir variaveis de ambiente e utilizar arquivos nao versionados no diretorio raiz da aplicacao, com nomes como .env, .env.development e .env.production, permitindo configuracoes diferentes por ambiente sem alterar o codigo.
- **(02)** No Node.js, o pacote dotenv e empregado para ler pares chave=valor a partir de um arquivo de texto local (padrao .env) e popula-los automaticamente na variavel global process.env no momento da execucao.
- **(04)** A adocao de um arquivo versionado chamado .env.example serve como gabarito de configuracao para novos desenvolvedores, listando as variaveis necessarias sem expor valores ou senhas confidenciais.
- **(08)** E recomendavel comitar o arquivo .env de producao no GitHub com o intuito de viabilizar deploys automatizados sem demandar configuracoes adicionais no servidor de hospedagem.
- **(16)** Caso a variavel PORT nao esteja definida no ambiente ou no arquivo .env, construcoes como const PORT = process.env.PORT || 3000 garantem que a aplicacao adote uma porta padrao alternativa em vez de falhar abruptamente.

**SOMA DA QUESTAO 04:** [ ______ ]

---

### Questao 05 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Linters versus Formatadores, Ecossistema e Integracao com Editores

Sobre a padronizacao de codigo-fonte, ecossistema de linters e integracao com ferramentas de desenvolvimento, julgue as assertivas:

- **(01)** Em Python, ferramentas como Ruff ou Pylint atuam como linters de analise de codigo, ao passo que Black ou Ruff Formatter sao utilizados especificamente como formatadores de codigo.
- **(02)** O utilitario ESLint e restrito estritamente a arquivos JavaScript simples, sendo incapaz de efetuar a verificacao estatica em bases de codigo TypeScript.
- **(04)** Em linguagens como Go e Rust, as ferramentas oficiais padroes para formatacao automatica de codigo sao, respectivamente, gofmt e rustfmt.
- **(08)** O arquivo .prettierignore serve para instruir o Prettier a nao formatar determinados diretorios e arquivos compilados ou externos, tais como build/, dist/ ou dependencias de terceiros.
- **(16)** A definicao de scripts no package.json como 'lint': 'eslint src/' e 'format': 'prettier --write src/' permite incorporar facilmente a verificacao e correcao de estilo nas rotinas de integracao continua (CI) da equipe.

**SOMA DA QUESTAO 05:** [ ______ ]

---

## Folha de Gabarito e Justificativas Tecnicas

### Resumo das Respostas Corretas

| Questao | Proposicoes Verdadeiras | Calculo da Soma Unica | Resposta Final (Soma) | Pontos |
| :---: | :---: | :---: | :---: | :---: |
| **Questao 01** | (02), (04), (08), (16) | 02 + 04 + 08 + 16 | **30** | 2.0 |
| **Questao 02** | (01), (02), (08), (16) | 01 + 02 + 08 + 16 | **27** | 2.0 |
| **Questao 03** | (04), (08), (16) | 04 + 08 + 16 | **28** | 2.0 |
| **Questao 04** | (01), (02), (04), (16) | 01 + 02 + 04 + 16 | **23** | 2.0 |
| **Questao 05** | (01), (04), (08), (16) | 01 + 04 + 08 + 16 | **29** | 2.0 |
| **TOTAL** | - | - | - | **10.0** |

---

### Resolucao Detalhada Item por Item

#### Questao 01 - Soma: 30
- **(01) [FALSA]**: O comando git add . respeita estritamente os filtros definidos no .gitignore, indexando somente arquivos rastreaveis nao ignorados (1_git.pdf).
- **(02) [VERDADEIRA]**: O Git vincula permanentemente nome e email a cada commit para assegurar a rastreabilidade e responsabilidade dos autores (1_git.pdf).
- **(04) [VERDADEIRA]**: O diretorio .git e a base interna do repositorio Git onde reside toda a estrutura do versionamento (1_git.pdf).
- **(08) [VERDADEIRA]**: Mensagens informativas descrevem o que foi feito e por que, facilitando a leitura do git log; mensagens genericas nao ajudam a entender o historico (1_git.pdf, secao Mensagens de Commit).
- **(16) [VERDADEIRA]**: O git status exibe com exatidao o estado das tres areas e arquivos nao monitorados pelo controle de versao (1_git.pdf).

#### Questao 02 - Soma: 27
- **(01) [VERDADEIRA]**: Por padrao, git diff compara o diretorio de trabalho com o indice; para comparar o indice com o ultimo commit usa-se --staged (1_git.pdf).
- **(02) [VERDADEIRA]**: A flag --oneline condensa a exibicao para proporcionar uma visualizacao rapida do historico recente (1_git.pdf).
- **(04) [FALSA]**: git diff --staged apenas visualiza as alteracoes indexadas no staging em comparacao com o HEAD; nao altera nem cria commits (1_git.pdf).
- **(08) [VERDADEIRA]**: O --graph desenha graficamente a convergencia e divergencia de branches e commits de merge (1_git.pdf).
- **(16) [VERDADEIRA]**: Linhas com '#' no .gitignore sao comentarios explicativos que documentam os motivos de exclusao de pastas e arquivos (1_git.pdf).

#### Questao 03 - Soma: 28
- **(01) [FALSA]**: O git fetch apenas baixa dados para o repositorio local atualizando remote-tracking branches (como origin/main); ele nao altera os arquivos do working directory nem a branch local corrente (1_git.pdf).
- **(02) [FALSA]**: Sendo distribuido, todas as operacoes de commit, criacao de branches, consulta de log e reset sao puramente locais e offline (1_git.pdf).
- **(04) [VERDADEIRA]**: O clone copia o repositorio integral e estabelece origin como apelido padrao do endereco remoto (1_git.pdf).
- **(08) [VERDADEIRA]**: O git pull sincroniza os metadados remotos (fetch) e imediatamente mescla as alteracoes na branch local ativa (merge) (1_git.pdf).
- **(16) [VERDADEIRA]**: A flag -u configura a associacao upstream permanente para aquela branch (1_git.pdf).

#### Questao 04 - Soma: 23
- **(01) [VERDADEIRA]**: Os slides apresentam exatamente esses nomes de arquivo como exemplos para separar configuracoes por ambiente (smartnotes.pdf, Variaveis de Ambiente).
- **(02) [VERDADEIRA]**: O metodo dotenv.config() analisa o arquivo .env e injeta as chaves em process.env para acesso programatico (smartnotes.pdf).
- **(04) [VERDADEIRA]**: O .env.example informa a lista de chaves obrigatorias para que cada membro configure seu proprio .env local (smartnotes.pdf).
- **(08) [FALSA]**: Arquivos .env contem senhas, segredos e chaves que nunca devem ser expostos em repositorios versionados, devendo constar impreterivelmente no .gitignore (smartnotes.pdf).
- **(16) [VERDADEIRA]**: O operador de fallback '||' define um valor alternativo seguro caso a propriedade nao esteja presente em process.env (smartnotes.pdf).

#### Questao 05 - Soma: 29
- **(01) [VERDADEIRA]**: A listagem comparativa de linguagens define Ruff/Pylint para analise estatica e Black/Ruff Formatter para diagramacao visual automatica (smartnotes.pdf).
- **(02) [FALSA]**: O pacote typescript-eslint permite ao ESLint analisar codigo TypeScript de forma completa, integrando regras recomendadas no eslint.config.mjs (smartnotes.pdf).
- **(04) [VERDADEIRA]**: Ambos os ecossistemas padronizam a formatacao nativamente atraves de gofmt e rustfmt (smartnotes.pdf).
- **(08) [VERDADEIRA]**: Assim como o .gitignore, o .prettierignore poupa diretorios de saida gerados ou bibliotecas de reformatacoes desnecessarias (smartnotes.pdf).
- **(16) [VERDADEIRA]**: Os scripts encapsulam a chamada aos utilitarios e uniformizam sua execucao em ambientes de desenvolvimento e pipelines de automacao (smartnotes.pdf).
