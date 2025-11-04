# 📚Livraria SQL

Este exercício tem como objetivo criar e manipular um banco de dados para uma livraria, utilizando comandos SQL para modelagem, inserção de dados e consultas. 
A atividade foi desenvolvida como exercício prático para consolidar conhecimentos em estrutura de tabelas, relacionamentos e análise de dados.

## 🎯 Objetivos

- Criar um banco de dados relacional para uma livraria
- Modelar tabelas com relacionamento entre clientes e compras
- Inserir dados simulados de clientes e suas compras
- Realizar consultas SQL para análise de dados

## 🗃️ Estrutura do Banco de Dados

### Tabelas criadas:

- `clientes`: armazena dados pessoais dos clientes
- `compras`: registra os livros comprados e valores

### Relacionamento:

- Um cliente pode realizar várias compras (1:N)
- A tabela `compras` possui chave estrangeira `id_cliente` referenciando `clientes`

## 🧱 Scripts SQL

- Criação do banco de dados: `CREATE DATABASE Livraria;`
- Criação das tabelas: `clientes` e `compras`
- Inserção de dados simulados
- Consultas para análise de clientes, compras e valores

## 🔍 Consultas Realizadas

- Listar todos os clientes
- Exibir todas as compras
- Mostrar livros comprados por cliente
- Calcular total gasto por cliente
- Filtrar compras feitas em fevereiro de 2024
- Contar número de livros comprados por cliente
- Identificar o cliente que mais comprou
- Calcular valor médio das compras
- Somar o total arrecadado

## 🛠️ Ferramentas Utilizadas

- MySQL via XAMPP
- Alternativas online: [SQLiteOnline](https://sqliteonline.com)
- Editor de texto para scripts `.sql`

## 📎 Arquivos
- `Exercício BD 07-03-24.pdf` – Arquivo original do exercício (opcional)

> 💡 *Este laboratório é ideal para praticar modelagem de dados e consultas SQL em um cenário real de vendas e clientes.*
