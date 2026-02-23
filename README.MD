# 🔐 API Gerador de Senhas

Uma API REST desenvolvida em **Flask** para geração e gerenciamento de senhas vinculadas a usuários autenticados.

Este projeto simula um pequeno sistema real com:

* Autenticação
* Sessão
* Persistência em banco relacional
* Relacionamento entre entidades

---

## 🚀 Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* PostgreSQL

---

## 📦 Funcionalidades

* Cadastro de usuário
* Login com sessão
* Geração de senha segura
* Armazenamento de senhas por usuário
* Relacionamento entre usuário e senhas
* Exclusão de senhas

---

## 🧱 Estrutura do Banco

### Tabela: users

| Campo | Tipo         |
| ----- | ------------ |
| id    | INTEGER (PK) |
| nome  | VARCHAR      |
| senha | VARCHAR      |

---

### Tabela: passwords

| Campo    | Tipo         |
| -------- | ------------ |
| id_senha | SERIAL (PK)  |
| id_user  | INTEGER (FK) |
| password | VARCHAR      |

Relacionamento:

```
passwords.id_user → users.id
```

Cada usuário pode possuir múltiplas senhas.

---

## 🔗 Modelagem ORM

O projeto utiliza relacionamento entre entidades:

* Um usuário possui várias senhas
* Cada senha pertence a um único usuário

Isso permite navegação entre objetos sem necessidade de queries manuais.

---

## 🔐 Autenticação

O login cria uma sessão contendo o ID do usuário autenticado.

```
session['conta_conectada'] = user.id
```

Essa sessão é utilizada para:

* Criar novas senhas
* Listar senhas
* Garantir vínculo com o usuário correto

---

## 🧠 Lógica de Negócio

A geração de senhas foi isolada em uma camada de serviço:

```
PasswordService
```

Isso mantém as rotas mais limpas e separa responsabilidades.

---

## ▶️ Como executar

### 1. Clone o repositório

```
git clone https://github.com/Dev2TT/Gerador_De_Senha
```

---

### 2. Crie o ambiente virtual

```
python -m venv venv
```

Ative:

Windows:

```
venv\Scripts\activate
```

Linux/Mac:

```
source venv/bin/activate
```

---

### 3. Instale dependências

```
pip install -r requirements.txt
```

---

### 4. Configure o banco PostgreSQL

Crie o banco e atualize a string de conexão no projeto.

---

### 5. Execute a aplicação

```
flask run
```

---

## 📌 Objetivo do projeto

Este projeto foi desenvolvido com fins de estudo para praticar:

* API REST
* Modelagem relacional
* Sessões
* SQLAlchemy
* Organização em camadas (Service)

---

## 📈 Possíveis melhorias futuras

* Autenticação com JWT
* Hash de senha
* Validação com Marshmallow
* Expiração de sessão
* Criptografia das senhas armazenadas

---

## 👨‍💻 Autor

Victtor Oliveira
