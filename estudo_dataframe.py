import pandas as pd

#Lista : uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Alice', 'Bob', 'Charlie', 'David']
#print('Lista de nomes :\n', lista_nomes) # Acessando o primeiro elemento da lista
#print('Primeiro nome na lista :\n', lista_nomes[0]) 

#Dicionário: estrutura composta de pares de chave-valor
dicionario_pessoas = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'São Paulo'
}
#print('Dicionário de uma pessoa :\n', dicionario_pessoas)
#print('Atributo do dicionario :\n', dicionario_pessoas.get('nome')) # Acessando o valor associado à chave 'nome'

#Lista de dicionários: uma coleção ordenada de dicionários
dados = [
    {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'},
    {'nome': 'Bob', 'idade': 25, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Charlie', 'idade': 35, 'cidade': 'Belo Horizonte'}
]

#DataFrame: estrutura de dados tabular bidimensional, semelhante a uma tabela em um banco de dados ou a uma planilha do Excel'
df = pd.DataFrame(dados)
print('DataFrame:\n', df) 
# Acessando a coluna 'nome' do DataFrame
print('\nColuna "nome":\n', df['nome'])

#selecionar varias colunas
print('\nColunas "nome" e "cidade":\n', df[['nome', 'cidade']])

#selecionar linhas pelo indice
print('\nPrimeira linha do DataFrame:\n', df.iloc[0])

#adicionar uma nova coluna
df['salario'] = [5000, 4500, 6000]

#adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'David',
    'idade': 28,
    'cidade': 'Curitiba',
    'salario': 5500
}

print('\nDataFrame atualizado:\n', df)

# removendo uma coluna
df.drop('salario', axis=1, inplace=True)

#filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] > 29]
print('\nPessoas com mais de 29 anos:\n', filtro_idade)

#salvando o DataFrame em um arquivo CSV
df.to_csv('dados_pessoas.csv', index=False)

#lendo o DataFrame de um arquivo CSV
df_lido = pd.read_csv('dados_pessoas.csv')
print('\nDataFrame lido do arquivo CSV:\n', df_lido)