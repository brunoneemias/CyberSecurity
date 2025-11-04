# 🍬 Doceria SQL: Modelagem de Vendas e Clientes

Este laboratório propõe a criação de um modelo de banco de dados para uma doceria, com foco na organização de informações sobre clientes, doces e vendas. A atividade envolve a modelagem de entidades, atributos e relacionamentos, com base em um cenário real de comércio varejista.

## 🎯 Objetivos

- Modelar um banco de dados relacional para uma doceria
- Representar clientes, produtos (doces) e vendas
- Estabelecer relacionamentos entre entidades
- Preparar a estrutura para futuras consultas e relatórios

## 🗃️ Entidades e Atributos

### Clientes

- `CPF`: chave primária
- `Nome`
- `Endereço`
- `Fone`

### Doces

- `Código`: chave primária
- `Descrição`
- `Categoria`
- `Preço unitário`
- `Quantidade em estoque`

### Venda

- `Data da venda`
- `Valor total`
- Relacionamento com cliente (1:N)
- Relacionamento com doces (N:N, via tabela intermediária)

## 🔗 Relacionamentos

- Um cliente pode realizar várias vendas
- Uma venda pode incluir vários doces
- Cada doce pode estar em várias vendas

## 🧱 Modelo Entidade-Relacionamento

O DER inclui:

- Entidades com atributos bem definidos
- Relacionamentos com cardinalidades apropriadas
- Chaves primárias e estrangeiras
- Tabela intermediária para vendas de múltiplos doces (ex: `itens_venda`)

## 🛠️ Ferramentas Utilizadas

- brModelo
- MySQL Workbench
- SQLite Online (para testes)
- Draw.io ou Lucidchart (opcional para diagramas)

## 📎 Arquivos

- `doceria-der.png` – Diagrama Entidade-Relacionamento (opcional)
- `README.md` – Este documento com a descrição do projeto
- `modelo-logico.sql` – Script opcional com estrutura de tabelas (se criado)

> 💡 *Este projeto é ideal para praticar modelagem de dados em cenários comerciais, com foco em controle de vendas, estoque e relacionamento com clientes.*
