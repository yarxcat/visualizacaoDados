import requests
from bs4 import BeautifulSoup
import pandas as pd

# Evita avisos de segurança do requests
requests.packages.urllib3.disable_warnings()

# URL do site que será acessado
url = 'https://books.toscrape.com/'

# Faz a requisição para o site
requisicao = requests.get(url)

# Define a codificação dos caracteres
requisicao.encoding = 'utf-8'

# Converte o HTML da página em um objeto BeautifulSoup
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Variável para contar quantos livros existem na página
contar_livros = 0

# Lista que armazenará todos os livros
catalogo = []

# Procura todos os artigos que representam livros
for artigo in extracao.find_all('article', class_='product_pod'):

    # Soma 1 a cada livro encontrado
    contar_livros += 1

    # Cria um dicionário vazio para armazenar os dados do livro
    livro = {}

    # Procura a tag h3 dentro do artigo
    for h3 in artigo.find_all('h3'):

        # Pega o título do livro
        titulo = h3.find('a')['title']

        # Armazena o título no dicionário
        livro['Título'] = titulo

    # Procura a tag p com a classe price_color
    for p in artigo.find_all('p', class_='price_color'):

        # Pega o texto do preço
        preco = p.text

        # Armazena o preço no dicionário
        livro['Preço'] = preco

    # Adiciona o dicionário na lista de livros
    catalogo.append(livro)

# Mostra a quantidade total de livros encontrados
print('Total livros:', contar_livros)

# Mostra todos os livros com seus respectivos preços
for livro in catalogo:
    print(livro)