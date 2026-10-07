# 🗳️ Projeto Integrador - Simulação de Urna Eletrônica

Projeto desenvolvido em Python como parte dos estudos de programação.

A aplicação simula uma votação para os cargos de **Prefeito e Vereador**, permitindo registrar votos válidos, votos brancos e votos nulos.

O projeto também possui um fluxo de controle do mesário para iniciar, continuar ou encerrar a votação, além da apuração dos resultados ao final.

> **Observação:** este projeto é uma simulação acadêmica desenvolvida para fins de estudo e não representa um sistema eleitoral real.

## 🚀 Funcionalidades

* Início da votação pelo mesário
* Encerramento do sistema antes do início da votação
* Liberação do próximo eleitor pelo mesário
* Encerramento da votação pelo mesário
* Registro de votos para Prefeito
* Registro de votos para Vereador
* Confirmação do voto
* Possibilidade de refazer o voto
* Registro de votos brancos
* Registro de votos nulos
* Contagem dos votos
* Apuração dos resultados ao final da votação
* Exibição da quantidade de votos por candidato
* Validação das entradas do usuário
* Testes automatizados com `unittest`

## 🛠️ Tecnologias e conceitos utilizados

* Python
* Programação procedural
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Dicionários
* Validação de entradas
* Tratamento de entradas inválidas
* Testes automatizados com `unittest`

## 📁 Estrutura do projeto

```text
Projeto-Integrador/
│
├── urna.py
│
├── tests/
│   └── test_urna.py
│
└── README.md
```

## ▶️ Como executar

É necessário ter o Python instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python urna.py
```

Ao iniciar o sistema, o mesário poderá escolher:

```text
1 - Iniciar votação
2 - Encerrar sistema
```

Após o início da votação, cada eleitor realiza seus votos para Prefeito e Vereador.

Depois de cada eleitor, o mesário poderá escolher:

```text
1 - Liberar próximo eleitor
2 - Encerrar votação
```

Ao encerrar a votação, o sistema apresenta a apuração dos votos.

## 🧪 Executando os testes

Para executar os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

### Resultado dos testes

O projeto possui atualmente **15 testes automatizados**, abrangendo:

* Solicitação de voto válido
* Validação de entrada não numérica
* Registro de voto válido
* Registro de voto branco
* Registro de voto nulo
* Contagem de votos
* Confirmação de voto
* Recusa de confirmação de voto
* Confirmação de voto branco
* Confirmação de voto nulo
* Processo completo de votação de um eleitor
* Controle do mesário para liberar o próximo eleitor
* Controle do mesário para encerrar a votação
* Início da votação
* Encerramento do sistema antes do início da votação

Todos os **15 testes automatizados** foram executados com sucesso.

## 🎯 Fluxo da aplicação

```text
Votação não iniciada
        │
        ▼
Controle do mesário
   ┌────┴────┐
   │         │
   1         2
   │         │
   ▼         ▼
Iniciar    Encerrar
votação    sistema
   │
   ▼
Novo eleitor
   │
   ├──► Voto para Prefeito
   │
   └──► Voto para Vereador
   │
   ▼
Votos registrados
   │
   ▼
Controle do mesário
   ┌────┴────┐
   │         │
   1         2
   │         │
   ▼         ▼
Próximo    Encerrar
eleitor    votação
             │
             ▼
          Apuração
          dos votos
```

## 📚 Objetivo do projeto

O objetivo deste projeto é praticar conceitos fundamentais de programação em Python, incluindo:

* criação e utilização de funções;
* estruturas condicionais;
* estruturas de repetição;
* utilização de dicionários;
* validação de dados;
* organização de código;
* testes automatizados;
* simulação de um fluxo de aplicação.

O projeto também busca aplicar conceitos de programação em uma situação prática, utilizando um sistema de votação como exemplo.

## 👨‍💻 Autor

**Márcio Eufrazio**

Tecnólogo em Análise e Desenvolvimento de Sistemas
