# 📦 Gestão de Estoque para Mini Mercados

FRONT-END: 
```bash
https://github.com/DevAlberissi/Inventory_Managment-FrontEnd
```

## 👥 Integrantes
- Anderson Alberissi 2403321
- Jullya Nigro 2402577
- Melissa Moura 2403008
- Humberto Lisboa 2402662

## 📌 Objetivo
Desenvolver um sistema para gestão de estoque e vendas de mini mercados, garantindo segurança, controle de acesso e gestão eficiente de produtos e vendas.

---

## 🚀 Funcionalidades Principais

### 1️⃣ Cadastro de Mini Mercado (Seller)
Os mini mercados devem se cadastrar informando os seguintes campos:
- **Nome**
- **CNPJ**
- **E-mail**
- **Celular**
- **Senha**
- **Status** (Padrão: Ativo)

Após o cadastro, o seller já pode fazer login e gerenciar produtos.

---

### 2️⃣ Autenticação do Seller
- O sistema deve utilizar **JWT** ou **OAuth** para autenticação.
- Sellers inativados não podem fazer login.

---

### 3️⃣ Gerenciamento de Produtos
Um seller autenticado pode:
- **Cadastrar produtos** com os seguintes campos:
  - Nome
  - Preço
  - Quantidade
  - Status (Ativo/Inativo)
  - Imagem
- **Listar produtos** cadastrados
- **Editar produto**
- **Ver detalhes de um produto**
- **Inativar produtos**

**Regras:**
- O seller só pode visualizar e gerenciar seus próprios produtos.

---

### 4️⃣ Venda de Produtos
- O seller pode realizar uma venda informando:
  - Produto
  - Quantidade
- As vendas devem ser armazenadas na tabela `Vendas`, contendo:
  - ID do Produto
  - Quantidade vendida
  - Preço do produto no momento da venda

**Regras:**
- Não é possível vender mais do que a quantidade disponível em estoque.
- Produtos inativados não podem ser vendidos.
- Sellers inativos não podem realizar vendas.

---

## 📡 Endpoints da API

### 1️⃣ Cadastro do Seller
- **Criar Seller**
  ```bash
  curl -X POST "http://localhost:5000/users" \
       -H "Content-Type: application/json" \
       -d '{"name": "Mini Mercado X", "cnpj": "00.000.000/0001-00", "email": "mercado@email.com", "celular": "99999999999", "password": "123456"}'
  ```

### 2️⃣ Autenticação
- **Login**
  ```bash
  curl -X POST "http://localhost:5000/auth/login" \
       -H "Content-Type: application/json" \
       -d '{"email": "mercado@email.com", "senha": "123456"}'
  ```

### 3️⃣ Gerenciamento de Produtos
- **Cadastrar Produto**
  ```bash
  curl -X POST "http://localhost:5000/products" \
       -H "Authorization: Bearer SEU_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Arroz", "preco": 10.50, "quantidade": 100, "status": "Ativo", "img": "url_da_imagem"}'
  ```
- **Listar Produtos**
  ```bash
  curl -X GET "http://localhost:5000/products" \
       -H "Authorization: Bearer SEU_TOKEN"
  ```
- **Editar Produto**
  ```bash
  curl -X PATCH "http://localhost:5000/products/1" \
       -H "Authorization: Bearer SEU_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"nome": "Arroz Integral", "preco": 12.00, "quantidade": 50, "status": "Ativo"}'
  ```
- **Ver Detalhes de um Produto**
  ```bash
  curl -X GET "http://localhost:5000/products/1" \
       -H "Authorization: Bearer SEU_TOKEN"
  ```
- **Inativar Produto**
  ```bash
  curl -X PATCH "http://localhost:5000/products/1/deactivate" \
       -H "Authorization: Bearer SEU_TOKEN"
  ```

### 4️⃣ Realizar Venda
- **Criar Venda**
  ```bash
  curl -X POST "http://localhost:5000/vendas" \
       -H "Authorization: Bearer SEU_TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"produtoId": 1, "quantidade": 2}'
  ```

---

## 🛠️ Tecnologias Utilizadas
- **Back-end:** Kotlin + Spring Boot
- **Front-end:** React.js
- **Banco de Dados:** MySQL ou PostgreSQL
- **Autenticação:** JWT ou OAuth

---

## 📊 Dashboard e Relatórios
- Implementação de um painel para exibição de relatórios e análise de vendas.
- Monitoramento de estoque em tempo real.

---

## 📌 Considerações Finais
Este projeto fornece um sistema completo para mini mercados gerenciarem seus estoques e vendas com segurança e eficiência. 🚀

