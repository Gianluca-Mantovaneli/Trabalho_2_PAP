# Trabalho de Programação Funcional em Python

## Descrição
Este projeto tem como objetivo demonstrar o uso do paradigma de programação funcional em Python, extraindo dados da DBpedia sobre livros. O programa realiza consultas SPARQL e implementa diversas funções que replicam o comportamento de regras de um programa em Prolog.

## Objetivos
- Aprender sobre programação funcional e suas aplicações.
- Utilizar dados disponíveis na web como base de fatos.
- Reproduzir resultados de um programa Prolog usando Python e conceitos funcionais.

## Tecnologias Utilizadas
- Python 3.x
- Biblioteca `requests` para consultas HTTP
- Funções de programação funcional (`map`, `filter`, `reduce`, `lambda`)

## Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3 e a biblioteca `requests` instalada. Você pode instalar a biblioteca com o seguinte comando:

```bash
pip install requests
```

### Executando o Código
1. Clone este repositório ou baixe o arquivo Python.
2. Abra o terminal e navegue até o diretório onde o arquivo está localizado.
3. Execute o script:

```bash
python3 T2_Gianluca_Schmidt_Mantovaneli.py
```

## Estrutura do Código
O código é organizado em funções que realizam as seguintes tarefas:

- **query_sparql(endpoint, query)**: Realiza a consulta SPARQL e retorna os resultados em formato JSON.
- **extract_books(data)**: Extrai informações de livros dos resultados da consulta SPARQL.
- Funções para verificar características de livros (como se são longos, antigos, etc.).
- Funções para listar livros por autor, país ou gênero.
- Funções para verificar se dois livros têm o mesmo idioma ou foram lançados no mesmo ano.

## Exemplos de Consultas
O código contém exemplos de como usar as funções implementadas. Os resultados são impressos no terminal para fácil visualização.

## Considerações Finais
Este projeto é uma aplicação prática dos conceitos de programação funcional em Python, demonstrando a manipulação de dados provenientes de uma fonte externa (DBpedia) e a replicação de lógicas que foram inicialmente escritas em Prolog.

## Autor
Gianluca Schmidt Mantovaneli
