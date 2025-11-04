# 💻 EletroLoca SQL: Modelagem de Aluguel de Equipamentos

Este laboratório propõe a criação de um modelo de banco de dados para a empresa fictícia **EletroLoca**, especializada no aluguel de projetores, notebooks e dispositivos multimídia. A atividade envolve a modelagem de entidades com herança, atributos específicos e relacionamentos entre clientes, funcionários e aparelhos alugados.

## 🎯 Objetivos

- Modelar um banco de dados relacional com especialização de entidades
- Representar clientes, funcionários, aparelhos e registros de aluguel
- Estabelecer relacionamentos entre entidades com cardinalidades apropriadas
- Preparar a estrutura para controle de aluguel e rastreabilidade

## 🗃️ Entidades e Atributos

### Aparelhos (superclasse)

- `codigo` (PK)
- `descricao`
- `marca`
- `preco_dia`

### Projetores (subclasse de Aparelhos)

- `resolucao`
- `conexoes`

### Notebooks (subclasse de Aparelhos)

- `conexoes`
- `processador`

### Clientes

- `cpf` (PK)
- `nome`
- `endereco`
- `fone`

### Funcionários

- `codigo` (PK)
- `nome`
- `fone`
- `data_admissao`
- `cargo`

### Aluguel

- `id_aluguel` (PK)
- `data`
- `tempo_duracao`
- `cpf_cliente` (FK)
- `codigo_funcionario` (FK)
- `codigo_aparelho` (FK)

## 🔗 Relacionamentos

- Um cliente pode realizar vários aluguéis
- Um aluguel é autorizado por um funcionário
- Um aluguel envolve um aparelho específico
- Aparelhos são especializados em projetores ou notebooks

## 🧱 Modelo Entidade-Relacionamento

O DER inclui:

- Herança entre Aparelhos, Projetores e Notebooks
- Relacionamentos 1:N entre clientes e aluguéis
- Relacionamentos 1:N entre funcionários e aluguéis
- Chaves primárias e estrangeiras bem definidas

## 🛠️ Ferramentas Utilizadas

- brModelo
- MySQL Workbench
- SQLite Online (para testes conceituais)

## 📎 Arquivos

- `eletroloca-der.png` – Diagrama Entidade-Relacionamento (opcional)
- `README.md` – Este documento com a descrição do projeto
- `modelo-logico.sql` – Script opcional com estrutura de tabelas (se criado)

---

> 💡 *Este projeto é ideal para praticar modelagem com herança e controle de aluguel, simulando um sistema completo de gestão de equipamentos.*
