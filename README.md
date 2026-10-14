# Simulação de Urna Eletrônica em Python

Projeto acadêmico desenvolvido em Python para praticar lógica de programação, organização de funções, validação de entradas e testes automatizados.

A aplicação simula uma votação para os cargos de **Prefeito e Vereador**, com registro de votos válidos, brancos e nulos, confirmação das escolhas e apuração dos resultados.

> **Aviso:** esta é uma simulação educacional. Não é um sistema eleitoral oficial e não deve ser utilizada em eleições reais.

## Funcionalidades

- Iniciar a votação pelo controle do mesário
- Liberar o próximo eleitor
- Encerrar o sistema ou a votação
- Registrar votos para Prefeito e Vereador
- Confirmar ou cancelar uma escolha
- Permitir corrigir a escolha após recusar um voto nulo
- Registrar votos válidos, brancos e nulos
- Contabilizar votos por candidato
- Validar entradas e tratar opções inválidas
- Apresentar os resultados ao final da votação
- Executar testes automatizados com `unittest`

## Tecnologias e conceitos

- Python 3
- Programação procedural
- Funções e parâmetros
- Estruturas condicionais e de repetição
- Dicionários
- Validação de entradas
- Testes automatizados com `unittest`

## Estrutura do projeto

```text
Projeto-Integrador/
├── urna.py
├── tests/
│   └── test_urna.py
└── README.md
```

## Pré-requisitos

- Python 3 instalado
- Terminal ou editor de código, como o Visual Studio Code

Verifique a instalação:

```bash
python --version
```

No Windows, também é possível utilizar:

```bash
py --version
```

O projeto utiliza módulos da biblioteca padrão do Python e não exige dependências externas para executar os testes apresentados.

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python urna.py
```

No controle do mesário, escolha uma opção para iniciar a votação ou encerrar o sistema. Durante a votação, o mesário pode liberar o próximo eleitor ou encerrar a votação para exibir a apuração.

## Testes automatizados

Execute os testes com:

```bash
python -m unittest discover -s tests -v
```

Os testes cobrem funcionalidades como:

- Solicitação e registro de votos
- Validação de entradas
- Contagem de votos válidos, brancos e nulos
- Confirmação e recusa de votos
- Correção após uma escolha inválida
- Processo de votação de um eleitor
- Controle do mesário
- Início e encerramento do sistema
- Configuração dos candidatos para Prefeito e Vereador
- Verificação da independência dos dicionários de candidatos
- Aceitação de números com espaços antes ou depois da entrada

### Status dos testes

**33 testes automatizados aprovados** na última execução informada.

Também foram realizados testes manuais no terminal para verificar a validação de números inexistentes, a confirmação de voto nulo, a correção da escolha, o registro de voto válido e o voto em branco.

Para verificar o estado atual do projeto, execute novamente o comando de testes antes de publicar novas alterações.

## Fluxo da aplicação

```text
Controle do mesário
        |
        v
Iniciar votação
        |
        v
Voto para Prefeito
        |
        v
Voto para Vereador
        |
        v
Registrar votos
        |
        v
Próximo eleitor ou encerrar
        |
        v
Apuração final
```

## Objetivo de aprendizagem

O projeto aplica conceitos fundamentais de programação em uma situação prática, com foco em:

- Decomposição do programa em funções
- Manipulação de dicionários
- Validação de dados
- Controle de fluxo
- Interação com o usuário
- Verificação do comportamento por meio de testes automatizados

## Autor

**Márcio Eufrazio**

Tecnólogo em Análise e Desenvolvimento de Sistemas.
