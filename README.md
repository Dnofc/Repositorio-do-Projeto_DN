# 🏭 Sistema de Automação Industrial – Controle de Peças

## 📌 Descrição

Este projeto consiste em um sistema desenvolvido em Python com o objetivo de automatizar o controle de qualidade de peças em uma linha de produção industrial.

A aplicação simula um ambiente industrial onde peças são analisadas com base em critérios pré-definidos, classificadas como aprovadas ou reprovadas e organizadas automaticamente em caixas com capacidade limitada.

---

## ⚙️ Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

1. Cadastrar nova peça
2. Listar peças aprovadas e reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final

---

## 🧠 Regras de validação

As peças são avaliadas automaticamente com base nos seguintes critérios de qualidade:

* Peso entre **95g e 105g**
* Cor **azul ou verde**
* Comprimento entre **10cm e 20cm**

Caso algum desses critérios não seja atendido, a peça é classificada como **reprovada**, sendo exibidos os motivos da reprovação.

---

## 📦 Armazenamento das peças

* Apenas peças aprovadas são armazenadas
* Cada caixa possui capacidade máxima de **10 peças**
* Ao atingir esse limite, a caixa é automaticamente fechada
* Após o fechamento, uma nova caixa é iniciada automaticamente

---

## ▶️ Como executar o projeto

### 📋 Pré-requisitos
- Python 3 instalado

### 🚀 Passo a passo

1. Baixe o arquivo do projeto ou cole do repositório
2. Abra a pasta no VSCode ou no terminal
3. Execute o arquivo
---

## 💻 Exemplo de uso

### ✔️ Exemplo de peça aprovada

Entrada:

```
ID da peça: 001
Peso: 100
Cor: azul
Comprimento: 15
```

Saída:

```
Peça Aprovada!
```

---

### ❌ Exemplo de peça reprovada

Entrada:

```
ID da peça: 002
Peso: 120
Cor: vermelho
Comprimento: 25
```

Saída:

```
Peça Reprovada!
Motivos:
- Peso fora do padrão
- Cor inválida
- Comprimento fora do padrão
```

---

## 📊 Relatório final

O sistema gera automaticamente um relatório contendo:

* Total de peças aprovadas
* Total de peças reprovadas
* Motivos de reprovação
* Quantidade de caixas utilizadas

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca Colorama (para estilização no terminal)

---

## 🚀 Possíveis melhorias

* Integração com banco de dados (SQLite, MySQL)
* Desenvolvimento de interface gráfica (GUI)
* Integração com sensores industriais
* Aplicação de inteligência artificial para análise avançada

---

Projeto desenvolvido para fins acadêmicos.
