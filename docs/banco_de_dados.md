# 🗃 Banco de Dados — Estrutura Completa (SQLite)

O sistema utiliza **finance.db**, contendo tabelas para autenticação e controle financeiro.

---

# 1️⃣ Tabela: users

```sql
id               INTEGER PK AUTOINCREMENT
full_name        TEXT
cpf              TEXT UNIQUE
email            TEXT UNIQUE
phone            TEXT
password_hash    TEXT
salt             TEXT
created_at       TEXT
last_login       TEXT
is_active        INTEGER DEFAULT 1

2️⃣ Tabela: categories
id    INTEGER PK AUTOINCREMENT
name  TEXT UNIQUE
type  TEXT ("income", "expense", "both")
Seed recomendada:

Salary, Bonus (income)

Food, Rent, Shopping (expense)

3️⃣ Tabela: transactions
id            INTEGER PK AUTOINCREMENT
amount        REAL
type          TEXT ("income","expense")
category_id   INTEGER FK
description   TEXT
date          TEXT (ISO)
created_at    TEXT
4️⃣ Relacionamentos
categories (1) ----- (∞) transactions
users —— isolado do financial data por segurança
5️⃣ Consultas importantes
Saldo total
SELECT SUM(CASE WHEN type='income' THEN amount ELSE -amount END) AS balance FROM transactions;
Entradas/Saídas
SELECT type, SUM(amount) FROM transactions GROUP BY type;

---

# 📄 **4. auth_system.md**

```markdown
# 🔐 Sistema de Autenticação — Documentação

O sistema implementa login e cadastro com segurança moderna.

---

# 📌 Fluxo de Registro

1. Electron coleta informações
2. Python valida
3. Python gera:
   - salt
   - password_hash (bcrypt)
4. Insere no banco

Campos do cadastro:
- Nome completo
- CPF
- Email
- Telefone
- Senha (hash + salt)

---

# 📌 Fluxo de Login

1. Electron envia email/CPF + senha
2. Backend busca usuário
3. Recálculo de hash com o salt do usuário
4. Compare → aprovado ou rejeitado
5. Atualiza `last_login`

---

# 🔒 Segurança

- Nunca armazenar senha pura
- Hash com bcrypt ou argon2
- Bloqueio após X tentativas (opcional)
- Emails únicos
- CPF único

---

# 📡 Estrutura da API Python

### `/auth/login`
Entrada:
```json
{ "login": "...", "password": "..." }
Retorno:

{ "success": true, "user_id": 1 }
/auth/register
Entrada:

{ 
  "full_name": "...",
  "cpf": "...",
  "email": "...",
  "phone": "...",
  "password": "..."
}
Retorno:

{ "success": true }

---

# 📄 **5. rotas_backend.md**

```markdown
# 🛠️ Rotas do Backend (Python)

O backend se comunica com o Electron via IPC (JSON).

---

# 🔐 Autenticação
### `auth/login`
### `auth/register`

---

# 💰 Transações
### `transactions/create`
### `transactions/list`
### `transactions/update`
### `transactions/delete`
### `transactions/summary`
### `transactions/by_category`

---

# 🗂 Categorias
### `categories/list`
### `categories/create`
### `categories/delete`