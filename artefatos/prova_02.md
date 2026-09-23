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

- **(01)** Apos a instalacao do Git, a configuracao de user.name e user.email via comando git config e essencial, pois o Git incorpora essas informacoes como metadados imutaveis de autoria em cada commit gerado.
- **(02)** O comando git init cria um diretorio oculto denominado .git no diretorio raiz do projeto, responsavel por armazenar todos os metadados, configuracoes, objetos blob, arvores e o historico integral de commits.
- **(04)** Mensagens de commit devem ser concisas e estruturadas segundo convencao reconhecida, sendo considerado boa pratica em projetos de software registrar a finalidade da mudanca (ex.: prefixos convencionais como feat, fix, chore, docs).
- **(08)** A utilizacao do comando git add . adiciona compulsoriamente todos os arquivos do computador ao commit, ignorando quaisquer regras declaradas no arquivo .gitignore.
- **(16)** O comando git status e a ferramenta primordial para inspecionar quais arquivos foram modificados no Working Directory, quais estao preparados na Staging Area e quais estao desprovidos de rastreamento (untracked).

**SOMA DA QUESTAO 01:** [ ______ ]

---

### Questao 02 (Valor: 2.0 pontos)
**Tema:** Git - Rastreamento, Analise de Diffs e Visualizacao de Topologia com Git Log

Sobre tecnicas de inspecao de diferencas e historico de commits no Git, julgue as afirmacoes:

- **(01)** O comando git diff sem argumentos adicionais exibe as diferencas pontuais entre o Working Directory e a Staging Area, isto e, as alteracoes feitas nos arquivos que ainda nao foram preparadas para commit.
- **(02)** A execucao de git log --oneline resume cada commit em uma unica linha composta pelo hash abreviado e pelo texto da primeira linha da mensagem de commit.
- **(04)** O modificador --graph no comando git log renderiza uma representacao textual em arte ASCII das ramificacoes e juncoes da arvore de commits, permitindo compreender a topologia de branches mescladas.
- **(08)** O comando git diff --staged e equivalente a git commit --amend, efetuando a substituicao automatica do commit anterior sem necessidade de intervencao do usuario.
- **(16)** Linhas iniciadas com o caractere cerquilha (#) no arquivo .gitignore sao interpretadas como comentarios pelo Git e desconsideradas na definicao dos padroes de exclusao.

**SOMA DA QUESTAO 02:** [ ______ ]

---

### Questao 03 (Valor: 2.0 pontos)
**Tema:** Git - Repositorios Remotos, Upstream Tracking, Git Fetch e Git Pull

Em relacao a integracao de repositorios locais com servidores remotos (GitHub/GitLab), avalie as proposicoes:

- **(01)** O comando git clone cria um repositorio local identico ao remoto, configurando automaticamente um vinculo de remote denominado origin e baixando todos os branches e historico existentes.
- **(02)** O comando git fetch busca os objetos e referencias do repositorio remoto e os incorpora compulsoriamente a branch local de trabalho, sobrescrevendo quaisquer alteracoes nao salvas do usuario.
- **(04)** O comando git pull e essencialmente uma combinacao logica sequencial de duas operacoes do Git: um git fetch seguido por um git merge da branch rastreada correspondente.
- **(08)** O parametro -u (ou --set-upstream) no comando git push -u origin <branch> estabelece uma ligacao direta de rastreamento entre a branch local e a branch remota, simplificando os proximos comandos para apenas git push ou git pull.
- **(16)** Um repositorio Git requer conexao permanente e estavel com a internet para executar operacoes como git commit, git branch, git log e git reset.

**SOMA DA QUESTAO 03:** [ ______ ]

---

### Questao 04 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Principios 12-Factor, Variaveis de Ambiente e Biblioteca Dotenv

A respeito do armazenamento de configuracoes de aplicacao e do uso do pacote dotenv em projetos Node.js, analise as proposicoes:

- **(01)** O manifesto Twelve-Factor App prescreve a estrita separacao entre codigo-fonte e dados de configuracao, preconizando que parametros dependentes de ambiente devam ser injetados exclusivamente via variaveis de ambiente.
- **(02)** No Node.js, o pacote dotenv e empregado para ler pares chave=valor a partir de um arquivo de texto local (padrao .env) e popula-los automaticamente na variavel global process.env no momento da execucao.
- **(04)** E recomendavel comitar o arquivo .env de producao no GitHub com o intuito de viabilizar deploys automatizados sem demandar configuracoes adicionais no servidor de hospedagem.
- **(08)** A adocao de um arquivo versionado chamado .env.example serve como gabarito de configuracao para novos desenvolvedores, listando as variaveis necessarias sem expor valores ou senhas confidenciais.
- **(16)** Caso a variavel PORT nao esteja definida no ambiente ou no arquivo .env, construcoes como const PORT = process.env.PORT || 3000 garantem que a aplicacao adote uma porta padrao alternativa em vez de falhar abruptamente.

**SOMA DA QUESTAO 04:** [ ______ ]

---

### Questao 05 (Valor: 2.0 pontos)
**Tema:** SmartNotes - Linters versus Formatadores, Ecossistema e Integracao com Editores

Sobre a padronizacao de codigo-fonte, ecossistema de linters e integracao com ferramentas de desenvolvimento, julgue as assertivas:

- **(01)** Em Python, ferramentas como Ruff ou Pylint atuam como linters de analise de codigo, ao passo que Black ou Ruff Formatter sao utilizados especificamente como formatadores de codigo.
- **(02)** Em linguagens como Go e Rust, as ferramentas oficiais padroes para formatacao automatica de codigo sao, respectivamente, gofmt e rustfmt.
- **(04)** O arquivo .prettierignore serve para instruir o Prettier a nao formatar determinados diretorios e arquivos compilados ou externos, tais como build/, dist/ ou dependencias de terceiros.
- **(08)** O utilitario ESLint e restrito estritamente a arquivos JavaScript simples, sendo incapaz de efetuar a verificacao estatica em bases de codigo TypeScript.
- **(16)** A definicao de scripts no package.json como 'lint': 'eslint src/' e 'format': 'prettier --write src/' permite incorporar facilmente a verificacao e correcao de estilo nas rotinas de integracao continua (CI) da equipe.

**SOMA DA QUESTAO 05:** [ ______ ]

---

## Folha de Gabarito e Justificativas Tecnicas

### Resumo das Respostas Corretas

| Questao | Proposicoes Verdadeiras | Calculo da Soma Unica | Resposta Final (Soma) | Pontos |
| :---: | :---: | :---: | :---: | :---: |
| **Questao 01** | (01), (02), (04), (16) | 01 + 02 + 04 + 16 | **23** | 2.0 |
| **Questao 02** | (01), (02), (04), (16) | 01 + 02 + 04 + 16 | **23** | 2.0 |
| **Questao 03** | (01), (04), (08) | 01 + 04 + 08 | **13** | 2.0 |
| **Questao 04** | (01), (02), (08), (16) | 01 + 02 + 08 + 16 | **27** | 2.0 |
| **Questao 05** | (01), (02), (04), (16) | 01 + 02 + 04 + 16 | **23** | 2.0 |
| **TOTAL** | - | - | - | **10.0** |

---

### Resolucao Detalhada Item por Item

#### Questao 01 - Soma: 23
- **(01) [VERDADEIRA]**: O Git vincula permanentemente nome e email a cada commit para assegurar a rastreabilidade e responsabilidade dos autores (Slide 16 de 1_git.pdf).
- **(02) [VERDADEIRA]**: O diretorio .git e a base interna do repositorio Git onde reside toda a estrutura do versionamento (Slide 13 de 1_git.pdf).
- **(04) [VERDADEIRA]**: A adocao de mensagens descritivas e padronizadas facilita a navegacao no git log e a geracao de changelogs automaticos (Slides 26 a 29 de 1_git.pdf).
- **(08) [FALSA]**: O comando git add . respeita estritamente os filtros definidos no .gitignore, indexando somente arquivos rastreaveis nao ignorados (Slides 23 e 30 de 1_git.pdf).
- **(16) [VERDADEIRA]**: O git status exibe com exatidao o estado das tres areas e arquivos nao monitorados pelo controle de versao (Slides 21, 23 e 36 de 1_git.pdf).

#### Questao 02 - Soma: 23
- **(01) [VERDADEIRA]**: Por padrao, git diff compara o diretorio de trabalho com o indice; para comparar o indice com o ultimo commit usa-se --staged (Slide 42 de 1_git.pdf).
- **(02) [VERDADEIRA]**: A flag --oneline condensa a exibicao para proporcionar uma visualizacao rapida do historico recente (Slide 41 de 1_git.pdf).
- **(04) [VERDADEIRA]**: O --graph desenha graficamente a convergencia e divergencia de branches e commits de merge (Slides 41 e 67 de 1_git.pdf).
- **(08) [FALSA]**: git diff --staged apenas visualiza as alteracoes indexadas no staging em comparacao com o HEAD; nao altera nem cria commits (Slide 42 de 1_git.pdf).
- **(16) [VERDADEIRA]**: Linhas com '#' no .gitignore sao comentarios explicativos que documentam os motivos de exclusao de pastas e arquivos (Slide 31 de 1_git.pdf).

#### Questao 03 - Soma: 13
- **(01) [VERDADEIRA]**: O clone copia o repositorio integral e estabelece origin como apelido padrao do endereco remoto (Slides 89 e 90 de 1_git.pdf).
- **(02) [FALSA]**: O git fetch apenas baixa dados para o repositorio local atualizando remote-tracking branches (como origin/main); ele nao altera os arquivos do working directory nem a branch local corrente (Slide 104 de 1_git.pdf).
- **(04) [VERDADEIRA]**: O git pull sincroniza os metadados remotos (fetch) e imediatamente mescla as alteracoes na branch local ativa (merge) (Slide 105 de 1_git.pdf).
- **(08) [VERDADEIRA]**: A flag -u configura a associacao upstream permanente para aquela branch (Slide 96 de 1_git.pdf).
- **(16) [FALSA]**: Sendo distribuido, todas as operacoes de commit, criacao de branches, consulta de log e reset sao puramente locais e offline (Slides 7 e 8 de 1_git.pdf).

#### Questao 04 - Soma: 27
- **(01) [VERDADEIRA]**: Guardar configuracoes em variaveis de ambiente evita recompilacao e vazamento de chaves entre ambientes de desenvolvimento, homologacao e producao (Slide 32 de smartnotes.pdf).
- **(02) [VERDADEIRA]**: O metodo dotenv.config() analisa o arquivo .env e injeta as chaves em process.env para acesso programatico (Slides 34 a 36 de smartnotes.pdf).
- **(04) [FALSA]**: Arquivos .env contem senhas, segredos e chaves que nunca devem ser expostos em repositorios versionados, devendo constar impreterivelmente no .gitignore (Slide 37 de smartnotes.pdf).
- **(08) [VERDADEIRA]**: O .env.example informa a lista de chaves obrigatorias para que cada membro configure seu proprio .env local (Slide 37 de smartnotes.pdf).
- **(16) [VERDADEIRA]**: O operador de fallback '||' define um valor alternativo seguro caso a propriedade nao esteja presente em process.env (Slides 35 e 36 de smartnotes.pdf).

#### Questao 05 - Soma: 23
- **(01) [VERDADEIRA]**: A listagem comparativa de linguagens define Ruff/Pylint para analise estatica e Black/Ruff Formatter para diagramacao visual automatica (Slides 46 e 48 de smartnotes.pdf).
- **(02) [VERDADEIRA]**: Ambos os ecossistemas padronizam a formatacao nativamente atraves de gofmt e rustfmt (Slide 48 de smartnotes.pdf).
- **(04) [VERDADEIRA]**: Assim como o .gitignore, o .prettierignore poupa diretorios de saida gerados ou bibliotecas de reformatacoes desnecessarias (Slides 60 e 61 de smartnotes.pdf).
- **(08) [FALSA]**: O pacote typescript-eslint permite ao ESLint analisar codigo TypeScript de forma completa, integrando regras recomendadas no eslint.config.mjs (Slides 52 e 58 de smartnotes.pdf).
- **(16) [VERDADEIRA]**: Os scripts encapsulam a chamada aos utilitarios e uniformizam sua execucao em ambientes de desenvolvimento e pipelines de automacao (Slide 62 de smartnotes.pdf).
