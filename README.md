
# 🗳️ Simulação de Urna Eletrônica em Python

Projeto desenvolvido em Python para praticar lógica de programação, organização de funções, validação de entradas e testes automatizados.

A aplicação simula uma votação para os cargos de **Prefeito e Vereador**, com registro de votos válidos, brancos e nulos, confirmação das escolhas e apuração dos resultados.

> **Aviso:** este é um projeto acadêmico para fins educacionais. Não é um sistema eleitoral oficial e não deve ser utilizado em eleições reais.

## 🚀 Funcionalidades

- Iniciar a votação por meio do controle do mesário
- Encerrar o sistema antes do início da votação
- Liberar o próximo eleitor
- Encerrar a votação e apresentar a apuração
- Registrar votos para Prefeito e Vereador
- Confirmar ou refazer uma escolha
- Registrar votos brancos e nulos
- Contabilizar votos por candidato
- Validar entradas e tratar opções inválidas
- Executar testes automatizados com `unittest`

## 🛠️ Tecnologias e conceitos

- **Python 3**
- Programação procedural
- Funções e parâmetros
- Estruturas condicionais e de repetição
- Dicionários para contabilização de votos
- Validação de entradas do usuário
- Testes automatizados com `unittest`
- Simulação de um fluxo de controle de votação

## 📁 Estrutura do projeto

```text
Projeto-Integrador/
├── urna.py
├── tests/
│   └── test_urna.py
└── README.md
```

## ⚙️ Pré-requisitos

- Python 3 instalado
- Terminal ou editor de código, como o Visual Studio Code

Para verificar se o Python está instalado, execute:

```bash
python --version
```

No Windows, também é possível utilizar:

```bash
py --version
```

O projeto utiliza módulos da biblioteca padrão do Python, incluindo `unittest`, sem necessidade de instalar dependências externas para executar os testes apresentados.

## ▶️ Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python urna.py
```

No início, o mesário poderá escolher:

```text
1 - Iniciar votação
2 - Encerrar sistema
```

Depois de cada eleitor votar para Prefeito e Vereador, o mesário poderá escolher:

```text
1 - Liberar próximo eleitor
2 - Encerrar votação
```

Ao encerrar a votação, o programa apresenta a quantidade de votos por candidato, além dos votos brancos e nulos.

## 🧪 Testes automatizados

Para executar os testes, utilize:

```bash
python -m unittest discover -s tests -v
```

Os testes verificam comportamentos como:

- Solicitação de voto válido
- Tratamento de entrada não numérica
- Registro e contagem de votos
- Registro de votos brancos e nulos
- Confirmação e recusa de votos
- Processo de votação de um eleitor
- Controle do mesário
- Início e encerramento do sistema
- Tratamento de opções inválidas

### Resultado atual

**24 testes automatizados aprovados**, conforme a última execução local confirmada.

Para conferir o resultado novamente, execute o comando de testes acima. Se o código for alterado, rode os testes antes de publicar as mudanças.

## 🔄 Fluxo da aplicação

```text
Sistema aguardando início
          |
          v
     Controle do mesário
       /           \
 Iniciar          Encerrar
 votação          sistema
    |
    v
 Eleitor vota para Prefeito
    |
    v
 Eleitor vota para Vereador
    |
    v
 Controle do mesário
    /           \
 Próximo       Encerrar
 eleitor       votação
                  |
                  v
             Apuração final
```

## 🎯 Objetivo de aprendizagem

Este projeto foi desenvolvido para aplicar conceitos fundamentais de programação em uma situação prática, com foco em:

- Decomposição do programa em funções
- Manipulação de dicionários
- Validação de dados
- Controle de fluxo
- Separação entre lógica e interação com o usuário
- Verificação do comportamento por meio de testes automatizados

## 👨‍💻 Autor

**Márcio Eufrazio**

Tecnólogo em Análise e Desenvolvimento de Sistemas.
