#https://python.org.br/web/

import requests
from bs4 import BeautifulSoup

# fazendo a requisição para o site e armazenando a resposta
url = 'https://www.python.org.br/web/'
requisicao= requests.get(url)
extracao = BeautifulSoup(requisicao.text, features='html.parser')
#exibir o resultado da extração
#print(extracao.text.strip())

#filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Título: ', titulo )

'''
Desafio
Filtrar tags ['h2','p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''
#filtrar a exibição pela tag
elementos = extracao.find_all(['h2','p'])
contador_h2 = 0
contador_p = 0

#print(elementos)
for tag in elementos:
    if tag.name == 'h2':
        contador_h2 += 1 #contador_h2 = contador_h2 + 1
    elif tag.name == 'p':
        contador_p += 1 

print(f'Quantidade de H2: {contador_h2}')
print(f'Quantidade de P: {contador_p}')

#Exibir o texto de cada elemento
for linha_texto in elementos:
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip().upper()
        print('\nTítulo: \n', titulo )
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('\nParágrafo: \n', paragrafo)
    
#Exibir tags aninhadas
for titulo in extracao.find_all('h2'):
    print('\nTítulo: \n', titulo.text.strip().upper() )
    for link in titulo.find_next_siblings('p'):
        #print(link)
        for a in link.find_all('a', href=True):
            print('Texto Link: ',a.text.strip(), '| URL: ', a['href'])