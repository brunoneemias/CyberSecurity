# 🏨 Hotel SQL: Modelagem de Hospedagens e Ambientes

Este laboratório propõe a criação de um modelo de banco de dados para um sistema de gestão hoteleira, com foco na organização de ambientes, clientes, funcionários e hospedagens. A atividade envolve a modelagem de entidades com especialização, atributos específicos e relacionamentos entre os participantes do sistema.

## 🎯 Objetivos

- Modelar um banco de dados relacional para um hotel
- Representar ambientes, clientes, funcionários e hospedagens
- Estabelecer relacionamentos com cardinalidades apropriadas
- Preparar a estrutura para controle de reservas e rastreabilidade

## 🗃️ Entidades e Atributos

### Ambiente (superclasse)

- `numero` (PK)
- `quantidade_ocupantes`

### Apartamento (subclasse de Ambiente)

- `tipo`
- `nivel`

### Sala de Apresentação (subclasse de Ambiente)

- `equipamento_disponivel`

### Cliente

- `codigo` (PK)
- `nome`
- `endereco`
- `cidade`
- `estado`
- `fone`

### Funcionário

- `codigo` (PK)
- `nome`
- `endereco`
- `data_nascimento`
- `funcao`
- `salario`

### Hospedagem

- `id_hospedagem` (PK)
- `data`
- `hora`
- `duracao`
- `codigo_cliente` (FK)
- `numero_ambiente` (FK)
- `codigo_funcionario` (FK)

## 🔗 Relacionamentos

- Um cliente pode realizar várias hospedagens
- Uma hospedagem ocorre em um ambiente específico
- Um funcionário libera a hospedagem em determinado horário
- Ambientes são especializados em apartamentos ou salas

## 🧱 Modelo Entidade-Relacionamento

O DER inclui:

- Herança entre Ambiente, Apartamento e Sala de Apresentação
- Relacionamentos 1:N entre clientes e hospedagens
- Relacionamentos 1:N entre funcionários e hospedagens
- Chaves primárias e estrangeiras bem definidas

## 🛠️ Ferramentas Utilizadas

- brModelo
- MySQL Workbench
- SQLite Online (para testes conceituais)

## 📎 Arquivos

- `hotel-der.png` – Diagrama Entidade-Relacionamento (opcional)
- `README.md` – Este documento com a descrição do projeto
- `modelo-logico.sql` – Script opcional com estrutura de tabelas (se criado)

---

> 💡 *Este projeto é ideal para praticar modelagem com herança e controle de hospedagens, simulando um sistema completo de gestão hoteleira.*
