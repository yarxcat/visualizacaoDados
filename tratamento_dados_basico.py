import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('clientes.csv')

#verificar os primeiros registros
print(df.head().to_string())

#verificar quantidade de linhas e colunas
print('\nQuantidade de linhas e colunas: ', df.shape)

#verificar tipo de dados
print('\nTipos de dados: \n', df.dtypes)

#checar valores nulos
print('\nValores nulos: \n', df.isnull().sum())

