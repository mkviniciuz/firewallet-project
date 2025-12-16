# 🏗 Arquitetura Geral do Projeto

Este documento descreve a arquitetura do sistema, focando em camadas, responsabilidades e comunicação.

---

## 🧱 Camadas

### 1. **Frontend — Electron**
- Responsável pela interface gráfica
- Renderização de páginas, componentes e gráficos
- Coleta inputs e envia eventos ao backend

### 2. **Backend — Python**
- Centro lógico da aplicação
- Processa dados, valida informações e acessa o banco
- Faz ponte entre Electron e as funções nativas em C

### 3. **Banco de Dados — SQLite**
- Armazena:
  - Usuários
  - Categorias
  - Transações financeiras
- Simples, leve e ideal para desktop

### 4. **Módulo Nativo — C**
- Responsável por cálculos financeiros:
  - agregações
  - rendimento
  - juros compostos
  - projeções
  
Chamado via `ctypes` no Python.

---

## 🔌 Comunicação entre camadas
Electron UI
↓ IPC
Python Backend
↓ calls
Native C module
↓ queries
SQLite Database

---

## 🧩 Responsabilidades por módulo

### Electron (app/)
- Telas (Dashboard, Transações, Login)
- Componentes (Inputs, Buttons, Cards)
- Gráficos (Chart.js ou similar)
- Comunicação com Python via processo filho

### Python (backend/)
- Autenticação
- CRUD de transações
- CRUD de categorias
- Cálculos de saldo e resumo
- Chamadas ao módulo em C

### SQLite (data/)
- Persistência e consultas

### C (src_native/)
- Funções de alta performance
- Biblioteca compilada → `.dll`, `.so`, `.dylib`

---

## 🌱 Escalabilidade
A arquitetura foi pensada para evoluir para:
- Sincronização com nuvem
- Multi-usuário
- Exportação de dados
- Gráficos avançados
- Migração para Electron + FastAPI no futuro


