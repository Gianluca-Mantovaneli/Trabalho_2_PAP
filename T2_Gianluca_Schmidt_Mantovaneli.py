import requests
from functools import reduce

# Função para realizar a consulta SPARQL
def query_sparql(endpoint, query):
    """Realiza uma consulta SPARQL e retorna os resultados em formato JSON."""
    response = requests.get(endpoint, params={'query': query, 'format': 'json'})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Falha na consulta SPARQL")

# Função para extrair dados de livros
def extract_books(data):
    """Extrai informações de livros dos resultados da consulta SPARQL."""
    return [
        {
            'titulo': item['titulo']['value'],
            'autor': item['autor']['value'],
            'pais': item['pais']['value'],
            'paginas': int(item['paginas']['value']) if 'paginas' in item else 0,
            'genero': item['genero']['value'],
            'dataLancamento': item['dataLancamento']['value'],
            'linguagem': item['linguagem']['value']
        }
        for item in data['results']['bindings']
    ]

# Consulta SPARQL para obter livros da DBpedia
endpoint = "http://dbpedia.org/sparql"
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?titulo ?autor ?pais ?paginas ?genero ?dataLancamento ?linguagem
WHERE {
    ?s rdf:type dbo:Book ;
       rdfs:label ?titulo ;
       dbo:author ?autor ;
       dbp:country ?pais ;
       dbo:numberOfPages ?paginas ;
       dbo:literaryGenre ?genero ;
       dbp:releaseDate ?dataLancamento ;
       dbp:language ?linguagem .
} LIMIT 1000
"""

# Realiza a consulta e extrai os livros
try:
    sparql_results = query_sparql(endpoint, query)
    livros = extract_books(sparql_results)
except Exception as e:
    print(f"Erro: {e}")

# Função para verificar se um livro é longo (mais de 300 páginas)
def livro_longo(titulo):
    """Verifica se um livro é longo e imprime a informação."""
    for livro in livros:
        if livro['titulo'] == titulo and livro['paginas'] > 300:
            print(f'Livro: {titulo} | Status: É longo ({livro["paginas"]} páginas)')

# Função para exibir a data de lançamento de um livro
def exibir_ano_lancamento(titulo):
    """Exibe a data de lançamento de um livro."""
    for livro in livros:
        if livro['titulo'] == titulo:
            ano = livro['dataLancamento'].split("-")[0]  # Extrai o ano da data
            print(f'Livro: {titulo} | Lançado em: {ano}')

# Função para verificar se um livro é antigo (lançado antes de 1960)
def livro_antigo(titulo):
    """Verifica se um livro é antigo e imprime a informação."""
    for livro in livros:
        if livro['titulo'] == titulo:
            ano = int(livro['dataLancamento'].split("-")[0])
            if ano < 1960:
                print(f'Livro: {titulo} | Status: É um livro antigo')

# Função para listar livros de um determinado autor
def livros_autor(autor):
    """Lista livros de um determinado autor."""
    return list(filter(lambda livro: livro['autor'] == autor, livros))

# Função para listar livros de um determinado país
def livros_pais(pais):
    """Lista livros de um determinado país."""
    return list(filter(lambda livro: livro['pais'] == pais, livros))

# Função para verificar se dois livros têm o mesmo idioma
def mesmo_idioma(titulo1, titulo2):
    """Verifica se dois livros têm o mesmo idioma."""
    livro1 = next((livro for livro in livros if livro['titulo'] == titulo1), None)
    livro2 = next((livro for livro in livros if livro['titulo'] == titulo2), None)
    
    if livro1 and livro2 and livro1['linguagem'] == livro2['linguagem']:
        print(f'Livro 1: {titulo1} | Livro 2: {titulo2} | Status: Têm o mesmo idioma')

# Função para listar livros por gênero
def livros_genero(genero):
    """Lista livros de um determinado gênero."""
    return list(filter(lambda livro: livro['genero'] == genero, livros))

# Função para verificar se dois livros foram lançados no mesmo ano
def mesmo_ano(titulo1, titulo2):
    """Verifica se dois livros foram lançados no mesmo ano."""
    livro1 = next((livro for livro in livros if livro['titulo'] == titulo1), None)
    livro2 = next((livro for livro in livros if livro['titulo'] == titulo2), None)
    
    if livro1 is None:
        print(f'Livro 1: "{titulo1}" não encontrado.')
    if livro2 is None:
        print(f'Livro 2: "{titulo2}" não encontrado.')
    
    if livro1 and livro2 and livro1['dataLancamento'].split("-")[0] == livro2['dataLancamento'].split("-")[0]:
        print(f'Livro 1: {titulo1} | Livro 2: {titulo2} | Status: Foram lançados no mesmo ano')

# Função para listar livros com mais de um certo número de páginas
def livros_com_mais_paginas(num):
    """Lista livros com mais de um certo número de páginas."""
    return list(filter(lambda livro: livro['paginas'] > num, livros))

# Exemplos de consultas equivalentes
if __name__ == "__main__":
    print("Exemplo de consultas:\n")
    
    # Exemplo: verificar se o livro é muito longo
    print("Verificando se o livro 'Before Mars (novel)' é longo:")
    livro_longo("Before Mars (novel)")
    
    # Exemplo: verificar se o livro é mais antigo do que 1960
    print("\nVerificando se o livro 'Beezus and Ramona' é antigo:")
    livro_antigo("Beezus and Ramona")
    
    # Listar livros de um autor específico
    print("\nListando livros de Stephen King:")
    livros_por_autor = livros_autor('http://dbpedia.org/resource/Stephen_King')
    print("Livros de Stephen King:", [livro['titulo'] for livro in livros_por_autor])
    
    # Listar livros de um gênero específico
    print("\nListando livros do gênero 'Fantasy fiction':")
    livros_fantasia = livros_genero('http://dbpedia.org/resource/Fantasy_fiction')
    print("Livros de Fantasia:", [livro['titulo'] for livro in livros_fantasia])
    
    # Verificar se dois livros são do mesmo ano
    print("\nVerificando se 'Moo (novel)' e 'Monsters (collection)' foram lançados no mesmo ano:")
    mesmo_ano("Hlava XXII", "Moment 22")  # Use títulos verificados da lista de livros

    
    # Listar livros com mais que 400 páginas
    print("\nListando livros com mais de 400 páginas:")
    livros_largos = livros_com_mais_paginas(400)
    print("Livros com mais de 400 páginas:", [livro['titulo'] for livro in livros_largos])
