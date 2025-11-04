# 🚚Transportadora SQL: Modelagem de Frota, Motoristas e Produtos

Este laboratório propõe a criação de um modelo de banco de dados para uma empresa de transporte, com foco na gestão de caminhões, motoristas, empresas contratantes, produtos transportados e registros de transporte. A atividade envolve a modelagem de entidades, atributos e relacionamentos com base em um cenário logístico real.

## 🎯 Objetivos

- Modelar um banco de dados relacional para uma transportadora
- Representar caminhões, motoristas, empresas, produtos e transportes
- Estabelecer relacionamentos entre entidades com cardinalidades apropriadas
- Preparar a estrutura para consultas e relatórios logísticos

## 🗃️ Entidades e Atributos

### Caminhão

- `chassi` (PK)
- `modelo`
- `cor`
- `capacidade_carga`

### Motorista

- `registro` (PK)
- `carteira_motorista`
- `vencimento_carteira`
- Relacionamento 1:1 com Caminhão

### Empresa

- `codigo` (PK)
- `nome`
- `endereco`

### Produto

- `codigo` (PK)
- `tipo`
- `descricao`
- `destino`
- Relacionamento N:1 com Empresa

### Transporte

- `id_transporte` (PK)
- `data`
- `peso`
- Relacionamento N:N com Produto e Caminhão

## 🔗 Relacionamentos

- Um motorista dirige apenas um caminhão
- Um caminhão pode prestar serviço para várias empresas
- Uma empresa possui vários produtos
- Produtos são transportados por caminhões
- Cada transporte envolve um ou mais produtos e um caminhão

## 🧱 Modelo Entidade-Relacionamento

O DER inclui:

- Entidades com atributos bem definidos
- Relacionamentos com cardinalidades 1:1, 1:N e N:N
- Tabela intermediária para transporte de produtos (ex: `itens_transporte`)
- Chaves primárias e estrangeiras

## 🛠️ Ferramentas Utilizadas

- brModelo
- MySQL Workbench
- SQLite Online (para testes conceituais)

## 📎 Arquivos

- `transportadora-der.png` – Diagrama Entidade-Relacionamento (opcional)
- `README.md` – Este documento com a descrição do projeto
- `modelo-logico.sql` – Script opcional com estrutura de tabelas (se criado)

---

> 💡 *Este projeto é ideal para praticar modelagem de dados em cenários logísticos, com foco em rastreabilidade, alocação de recursos e controle de transporte.*
