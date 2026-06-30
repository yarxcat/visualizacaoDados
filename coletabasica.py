#https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/

# importando biblioteca para fazer  requisisoes HTTP
import requests
from bs4 import BeautifulSoup
import pandas 

# fazendo a requisição para o site e armazenando a resposta
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/')
#print(response.text[:600])

# usando o BeautifulSoup para analisar o conteúdo HTML da resposta
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1000])

#print('Pandas: ')
url_dados = pandas.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/')
#print(url_dados[0].head(10))

