# Transcricao dos Slides Azuis - SmartNotes

> Origem: `smartnotes.pdf` (Filtro estrito de 35 slides azuis) - Gerencia de Configuracao (IC/UFAM).

## Indice dos Topicos Filtrados

- [1. Semantic Versioning - SemVer (Slides 22 a 25)](#1-semantic-versioning---semver)
- [2. Variaveis de Ambiente (Slides 32 a 37)](#2-variaveis-de-ambiente)
- [3. Validando as Variaveis de Ambiente com Envalid (Slides 38 a 44)](#3-validando-as-variaveis-de-ambiente-com-envalid)
- [4. Qualidade de Codigo: ESLint e Prettier (Slides 45 a 62)](#4-qualidade-de-codigo-eslint-e-prettier)

---

### Slide 22

Semantic Versioning - SemVer

- O Versionamento Semântico (SemVer) é uma convenção para

indicar o impacto das alterações realizadas em um software

- Uma versão SemVer contém 3 números: MAJOR.MINOR.PATCH

― MAJOR: alterações incompatíveis com versões anteriores

― MINOR: novas funcionalidades compatíveis com versões anteriores

― PATCH: correções de bugs compatíveis com versões anteriores

- Exemplo de evolução:

― 5.1.0 → 5.1.1   correções de bug

― 5.1.1 → 5.2.0   novas funcionalidades

― 5.2.0 → 6.0.0   alterações incompatíveis

---

### Slide 23

Semantic Versioning - SemVer

- O Versionamento Semântico (SemVer) é uma convenção para

indicar o impacto das alterações realizadas em um software

- Uma versão SemVer contém 3 números: MAJOR.MINOR.PATCH

― MAJOR: alterações incompatíveis com versões anteriores

― MINOR: novas funcionalidades compatíveis com versões anteriores

― PATCH: correções de bugs compatíveis com versões anteriores

- Exemplo de evolução:

― 5.1.0 → 5.1.1   correções de bug

― 5.1.1 → 5.2.0   novas funcionalidades

― 5.2.0 → 6.0.0   alterações incompatíveis

---

### Slide 24

Semantic Versioning - SemVer

- O Express utiliza versionamento semântico para numerar suas

versões – por exemplo: express@5.2.1

- O package.json normalmente registra algo semelhante a:

- Ao executarmos o comando npm update, o símbolo ^ permite

que o npm instale versões dentro da mesma versão MAJOR

- Desta forma, o ^5.2.1 permite a instalação de versões 5.2.2, 5.3.0

e 5.5.3, mas não permite 6.0.0

{

  "dependencies": {

    "express": "^5.2.1"

  }

}

---

### Slide 25

Semantic Versioning - SemVer

- No package.json, se trocarmos o ^ por ~, então as atualizações

automáticas firarão restritas à novos PATCHs

- Nesse caso, o npm pode instalar versões como 5.2.2, 5.2.3 e

5.2.9, mas não instalará automaticamente 5.2.0 e 6.0.0

- Desta forma, o uso do símbolo ~ ao invés de ^ deixa a

atualização das dependências mais conservadora

{

  "dependencies": {

    "express": "~5.2.1"

  }

}

---

### Slide 32

Variáveis de Ambiente

- Variáveis de ambiente são dados de configuração que ficam

disponíveis no ambiente de execução dos programas

- No Node, as variáveis de ambiente constituem uma ótima

maneira de definir as configurações locais de um programa

  - Como URLs, portas, chaves de autenticação, senhas, etc

- Por exemplo, para criar uma variável de ambiente para

armazenar a porta do serviço http:

process.env.DB_PORT=3333

Por convenção,

as variáveis de

ambiente são

escritas em

caixa alta

---

### Slide 33

Variáveis de Ambiente

- Uma opção para definir as variáveis de ambiente é através de

arquivos não versionados no diretório raiz da aplicação

  - Exemplos de nomes para esses arquivos

são .env, .env.development, .env.production

---

### Slide 34

Variáveis de Ambiente

- Para que as variáveis de ambiente sejam carregadas na

aplicação, podemos usar pacotes como o dotenv

---

### Slide 35

Variáveis de Ambiente

- Para que as variáveis de ambiente sejam carregadas na

aplicação, podemos usar pacotes como o dotenv

```bash
import express, { type Request, type Response } from "express";
```

```bash
import dotenv from "dotenv";
```

dotenv.config({ quiet: true });

```bash
const app = express();
```

```bash
const PORT = process.env.PORT || 3000;
```

app.get("/", (req: Request, res: Response) => {

  res.send("Hello world!");

});

app.listen(PORT, () => {

  console.log(`Server running on port ${PORT}.`);

});

---

### Slide 36

Variáveis de Ambiente

- Para que as variáveis de ambiente sejam carregadas na

aplicação, podemos usar pacotes como o dotenv

```bash
import express, { type Request, type Response } from "express";
```

```bash
import dotenv from "dotenv";
```

dotenv.config({ quiet: true });

```bash
const app = express();
```

```bash
const PORT = process.env.PORT || 3000;
```

app.get("/", (req: Request, res: Response) => {

  res.send("Hello world!");

});

app.listen(PORT, () => {

  console.log(`Server running on port ${PORT}.`);

});

---

### Slide 37

Variáveis de Ambiente

- As arquivos .env devem ser adicionados no .gitignore, pois as

variáveis de ambiente estão relacionadas com o ambiente do

usuário que está rodando a aplicação

- No entanto, quando um novo desenvolvedor faz o clone do

repositório, é importante que ele saiba o nome das variáveis

que ele precisa definir em seu ambiente

- Para resolver isso, pode-se criar arquivos versionáveis

contendo variáveis de ambientes de exemplo

  - Por exemplo, tais arquivos podem ter nomes

como .env.example

---

### Slide 38

Validando as variáveis de ambiente

- Esquecer de adicionar uma variável de ambiente ou não usar o

tipo de dado certo pode levar a erros inesperados

- Para evitar esses problemas, podemos usar o pacote envalid

para validar as variáveis de ambiente do arquivo .env

```bash
$ npm i envalid
```

---

### Slide 39

Validando as variáveis de ambiente

- Para usar o envalid, vamos criar um diretório utils no diretório

src e adicionar um arquivo chamado getEnv.ts

---

### Slide 40

Validando as variáveis de ambiente

- No arquivo getEnv.ts, definimos todas as variáveis de

ambiente necessárias para rodar a aplicação

- O envalid lançará um erro caso esqueçamos de fornecer

alguma dessas variáveis no .env ou se forem do tipo errado

```bash
import { cleanEnv, str, port } from "envalid";
```

```bash
import dotenv from "dotenv";
```

dotenv.config({ quiet: true });

```bash
export function getEnv() {
```

  return cleanEnv(process.env, {

    NODE_ENV: str(),

    PORT: port({ default: 3000 }),

  });

}

---

### Slide 41

Validando as variáveis de ambiente

- No arquivo getEnv.ts, definimos todas as variáveis de

ambiente necessárias para rodar a aplicação

- O envalid lançará um erro caso esqueçamos de fornecer

alguma dessas variáveis no .env ou se forem do tipo errado

```bash
import { cleanEnv, str, port } from "envalid";
```

```bash
import dotenv from "dotenv";
```

dotenv.config({ quiet: true });

```bash
export function getEnv() {
```

  return cleanEnv(process.env, {

    NODE_ENV: str({ default: "development" }),

    PORT: port({ default: 3000 }),

  });

}

A página do envalid

no npmjs tem uma

documentação

completa dos

validadores

disponíveis

---

### Slide 42

- Agora que implementamos a função getEnv, podemos usá-la

em nosso arquivo index.ts

Validando as variáveis de ambiente

```bash
import express, { type Request, type Response } from "express";
```

```bash
import { getEnv } from "./utils/getEnv.js";
```

```bash
const app = express();
```

```bash
const { PORT } = getEnv();
```

app.get("/", (req: Request, res: Response) => {

  res.send("Hello world!");

});

app.listen(PORT, () => {

  console.log(`Server running on port ${PORT}.`);

});

---

### Slide 43

- Agora que definimos o validEnv, podemos usá-lo em nosso

arquivo index.ts

Validando as variáveis de ambiente

```bash
import express, { Request, Response } from 'express';
```

```bash
import validateEnv from './utils/validateEnv';
```

```bash
import dotenv from 'dotenv';
```

dotenv.config();

validateEnv();

```bash
const app = express()
```

```bash
const PORT = process.env.PORT || 3333
```

app.get("/", (req: Request, res: Response) => {

  res.send("Hello world!");

});

app.listen(PORT, () => {

  console.log(`Express app iniciada na porta ${PORT}.`);

});

A aplicação passará

a reportar um erro

caso o arquivo .env

não contenha todas

as variáveis

---

### Slide 44

- Agora que definimos o validEnv, podemos usá-lo em nosso

arquivo index.ts

Validando as variáveis de ambiente

```bash
import express, { Request, Response } from 'express';
```

```bash
import validateEnv from './utils/validateEnv';
```

```bash
import dotenv from 'dotenv';
```

dotenv.config();

validateEnv();

```bash
const app = express()
```

```bash
const PORT = process.env.PORT || 3333
```

app.get("/", (req: Request, res: Response) => {

  res.send("Hello world!");

});

app.listen(PORT, () => {

  console.log(`Express app iniciada na porta ${PORT}.`);

});

A aplicação passará

a reportar um erro

caso o arquivo .env

não contenha todas

as variáveis

O erro para de

ocorrer quando

atualizamos o

.env

---

### Slide 45

ESLint e Prettier

- ESLint é uma ferramenta de lint, que analisa o código em

busca de erros de estilo e de sintaxe que possam levar a bugs

---

### Slide 46

ESLint e Prettier

- ESLint é uma ferramenta de lint, que analisa o código em

busca de erros de estilo e de sintaxe que possam levar a bugs

A listagem a seguir mostra os Linters mais usados

para as linguagens de programação mais populares

- JavaScript/TypeScript - ESLint

- Python - Ruff ou Pylint

- Java - Checkstyle

- C/C++ - Clang-Tidy

- C# - Roslyn Analyzers

- Go - golangci-lint

- Rust - Clippy

- PHP - PHP_CodeSniffer

- Ruby - RuboCop

- Kotlin - Detekt

- Swift - SwiftLint

- Bash - ShellCheck

---

### Slide 47

ESLint e Prettier

- Prettier é uma ferramenta para formatação de código, que

possibilita que os códigos sejam formatados automaticamente

---

### Slide 48

ESLint e Prettier

- Prettier é uma ferramenta para formatação de código, que

possibilita que os códigos sejam formatados automaticamente

A listagem a seguir mostra os Formatadores mais

usados em diferentes linguagens de programação

- JavaScript/TypeScript - Prettier

- Python - Black ou Ruff Formatter

- Java - google-java-format

- C/C++ - ClangFormat

- C# - dotnet format

- Go - gofmt

- Rust - rustfmt

- PHP - PHP CS Fixer

- Ruby - RuboCop

- Kotlin - ktlint

- Swift - SwiftFormat

- Bash - shfmt

---

### Slide 49

Adicionando o ESLint no projeto

- Para instalar o ESLint em seu projeto, basta adicionar o pacote

eslint como uma dependência de desenvolvimento

```bash
$ npm i -D eslint
```

- Para configurar o ESLint, usamos o comando abaixo -

```bash
$ npm init @eslint/config@latest
```

---

### Slide 50

Adicionando o ESLint no projeto

- Para instalar o ESLint em seu projeto, basta adicionar o pacote

eslint como uma dependência de desenvolvimento

```bash
$ npm i -D eslint
```

- Para configurar o ESLint, usamos o comando abaixo -

```bash
$ npm init @eslint/config@latest
```

---

### Slide 51

Instalação do ESLint

- Para instalar o ESLint em seu projeto, basta adicionar o pacote

eslint como uma dependência de desenvolvimento

```bash
$ npm i -D eslint
```

- Para configurar o ESLint, usamos o comando abaixo -

```bash
$ npm init @eslint/config@latest
```

Para uma completa compatibilidade do ESLint com o VS Code,

recomenda-se instalar a extenção ESLint do editor

---

### Slide 52

Adicionando o ESLint no projeto

- Após a configuração do ESLint, será criado um arquivo

eslint.config.mjs com o seguinte conteúdo:

```bash
import js from "@eslint/js";
```

```bash
import globals from "globals";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
import { defineConfig } from "eslint/config";
```

```bash
export default defineConfig([
```

  {

    files: ["**/*.{js,mjs,cjs,ts,mts,cts}"],

    plugins: { js },

    extends: ["js/recommended"],

    languageOptions: { globals: globals.node }

  },

  tseslint.configs.recommended,

]);

---

### Slide 53

Adicionando o ESLint no projeto

- Após a configuração do ESLint, será criado um arquivo

eslint.config.mjs com o seguinte conteúdo:

```bash
import js from "@eslint/js";
```

```bash
import globals from "globals";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
import { defineConfig } from "eslint/config";
```

```bash
export default defineConfig([
```

  {

    files: ["src/**/*.{js,mjs,cjs,ts,mts,cts}"],

    plugins: { js },

    extends: ["js/recommended"],

    languageOptions: { globals: globals.node }

  },

  tseslint.configs.recommended,

]);

No arquivo gerado,

configure o ESLint

para avaliar apenas

arquivos do diretório

src

---

### Slide 54

Instalação do ESLint e Prettier

- Após a configuração do ESLint, será criado um arquivo

eslint.config.mjs com o seguinte conteúdo:

```bash
import globals from "globals";
```

```bash
import pluginJs from "@eslint/js";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
export default [
```

  {files: ["**/*.{js,mjs,cjs,ts}"]},

  {languageOptions: { globals: globals.node }},

  pluginJs.configs.recommended,

  ...tseslint.configs.recommended,

];

A partir desse

momento, o ESLint

vai passar a acusar

eventuais problemas

no código

---

### Slide 55

Adicionando o ESLint no projeto

- Após a configuração do ESLint, será criado um arquivo

eslint.config.mjs com o seguinte conteúdo:

```bash
import js from "@eslint/js";
```

```bash
import globals from "globals";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
import { defineConfig } from "eslint/config";
```

```bash
export default defineConfig([
```

  {

    files: ["src/**/*.{js,mjs,cjs,ts,mts,cts}"],

    plugins: { js },

    extends: ["js/recommended"],

    languageOptions: { globals: globals.node }

  },

  tseslint.configs.recommended,

  { rules: { "@typescript-eslint/no-unused-vars": "off" } },

]);

Possíveis

valores:

off, warn,

error

---

### Slide 56

Instalação do ESLint e Prettier

- Podemos adicionar regras ao arquivo eslint.config.mjs, ou

então modificar as regras já definidas nos pacotes @eslint/js e

typescript-eslint

```bash
import globals from "globals";
```

```bash
import pluginJs from "@eslint/js";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
export default [
```

  {files: ["**/*.{js,mjs,cjs,ts}"]},

  {languageOptions: { globals: globals.node }},

  pluginJs.configs.recommended,

  ...tseslint.configs.recommended,

  {rules: {'@typescript-eslint/no-unused-vars': 'off'}},

];

Com a regra

desabilitada, o

ESLint não acusa

erros

---

### Slide 57

Instalação do ESLint e Prettier

- Podemos adicionar regras ao arquivo eslint.config.mjs, ou

então modificar as regras já definidas nos pacotes @eslint/js e

typescript-eslint

```bash
import globals from "globals";
```

```bash
import pluginJs from "@eslint/js";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
export default [
```

  {files: ["**/*.{js,mjs,cjs,ts}"]},

  {languageOptions: { globals: globals.node }},

  pluginJs.configs.recommended,

  ...tseslint.configs.recommended,

  {rules: {'@typescript-eslint/no-unused-vars': 'off'}},

];

Com a regra

desabilitada, o

ESLint não acusa

erros

Em https://eslint.org/docs/latest/rules/ é possível ver todas as

rules do Eslint disponíveis para JavaScript

---

### Slide 58

Instalação do ESLint e Prettier

- Podemos adicionar regras ao arquivo eslint.config.mjs, ou

então modificar as regras já definidas nos pacotes @eslint/js e

typescript-eslint

```bash
import globals from "globals";
```

```bash
import pluginJs from "@eslint/js";
```

```bash
import tseslint from "typescript-eslint";
```

```bash
export default [
```

  {files: ["**/*.{js,mjs,cjs,ts}"]},

  {languageOptions: { globals: globals.node }},

  pluginJs.configs.recommended,

  ...tseslint.configs.recommended,

  {rules: {'@typescript-eslint/no-unused-vars': 'off'}},

];

Com a regra

desabilitada, o

ESLint não acusa

erros

Em https://eslint.org/docs/latest/rules/ é possível ver todas as

rules do Eslint disponíveis para JavaScript

Em https://typescript-eslint.io/rules/ é possível ver todas as

rules do Eslint disponíveis para TypeScript

---

### Slide 59

Adicionando o Prettier no projeto

- Para instalar o Prettier em seu projeto, basta adicionar o

pacote prettier como uma dependência de desenvolvimento

```bash
$ npm i -D prettier
```

- Para configurarmos o Prettier, podemos criar um

arquivo .prettierrc com as seguintes diretrizes de formatação

{

    "printWidth": 80,

    "tabWidth": 2,

    "singleQuote": false,

    "trailingComma": "all",

    "semi": false,

    "arrowParens": "always"

}

---

### Slide 60

Configuração do Prettier

- Para configurarmos o Prettier, podemos criar um

arquivo .prettierrc com as seguintes diretrizes de formatação

- Também podemos adicionar um arquivo .prettierignore

{

    "printWidth": 150,

    "tabWidth": 2,

    "singleQuote": true,

    "trailingComma": "all",

    "semi": true,

    "arrowParens": "avoid"

}

build

Em https://prettier.io/docs/en/options.html é apresentado a

lista de opções do pacote Prettier

Em https://prettier.io/docs/en/options.html é apresentado a

lista de opções do pacote Prettier

---

### Slide 61

Configuração do Prettier

- Para configurarmos o Prettier, podemos criar um

arquivo .prettierrc com as seguintes diretrizes de formatação

- Também podemos adicionar um arquivo .prettierignore

{

    "printWidth": 150,

    "tabWidth": 2,

    "singleQuote": true,

    "trailingComma": "all",

    "semi": true,

    "arrowParens": "avoid"

}

build

Em https://prettier.io/docs/en/options.html é apresentado a

lista de opções do pacote Prettier

Em https://prettier.io/docs/en/options.html é apresentado a

lista de opções do pacote Prettier

Podemos usar

a extensão Prettier

do VSCode para

formatar o código

automaticamente

a cada salvamento

---

### Slide 62

Adicionando o Prettier no projeto

- E agora podemos adicionar os scripts lint, lint:fix e format no

package.json para rodar o eslint e o prettier

"scripts": {

  "start": "tsx watch src/index.ts",

  "build": "tsc",

  "typecheck": "tsc --noEmit",

  "start:prod": "node dist/index.js",

  "lint": "eslint src/",

  "lint:fix": "eslint --fix src/",

  "format": "prettier --write src/"

},

---

