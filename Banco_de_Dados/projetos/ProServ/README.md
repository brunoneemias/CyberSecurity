# 🧾ProServ: Portal de Transparência Documental

Este laboratório propõe a modelagem lógica de um banco de dados para um sistema de gestão documental digital, voltado para empresas terceirizadoras como a fictícia **ProServ Limpeza e Segurança**. O foco está na organização, rastreabilidade e compartilhamento seguro de documentos com empresas contratantes.

## 🏢 Cenário

A ProServ atua no ramo de terceirização de serviços, alocando profissionais como vigilantes, porteiros e faxineiros em empresas contratantes (hospitais, escolas, condomínios, etc.). Cada colaborador gera documentos obrigatórios que devem ser entregues mensalmente de forma organizada e segura.

## 🎯 Objetivos do Sistema

- Armazenar documentos por colaborador, tipo e período
- Compartilhar documentos com representantes das empresas contratantes
- Controlar acessos com login/senha e registrar logs de visualização

## 🗃️ Entidades Principais

- **Colaborador**: funcionário alocado em empresas contratantes
- **Empresa Contratante**: cliente da ProServ que recebe os documentos
- **Documento**: arquivos como folha de pagamento, ponto, ASO, etc.
- **Tipo de Documento**: classificação dos documentos
- **Histórico de Acesso**: logs de visualização por representantes

## 🧱 Modelo Lógico

O projeto inclui:

- Diagrama lógico com entidades, atributos e relacionamentos
- Cardinalidades entre colaborador, empresa, documentos e acessos
- Representação de chaves primárias e estrangeiras

> ⚠️ *Este projeto não inclui os scripts SQL de criação de tabelas, apenas o modelo lógico.*

## 🛠️ Ferramentas Utilizadas

- brModelo
- MySQL Workbench
- SQLite Online (para testes conceituais)
- Draw.io ou Lucidchart (opcional para diagramas)

## 📎 Arquivos

- `PROJETO DE BANCO DE DADOS.pdf` – Documento original com instruções e contexto
- `README.md` – Este documento com a descrição do projeto
---

> 💡 *Este projeto é ideal para praticar modelagem de dados em cenários reais, com foco em segurança, rastreabilidade e transparência documental.*
