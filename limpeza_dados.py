import pandas as pd

df = pd.read_csv('clientes.csv')

# Exibir as primeiras linhas do DataFrame para verificar os dados
pd.set_option('display.width', None)
print(df.head())

#Remover dados
df.drop(labels=['pais'], axis=1, inplace=True) #Remover a coluna 'país' do DataFrame
df.drop(labels=[2], axis=0, inplace=True) #Remover a linha de índice 2 do DataFrame

#normalizar campos de texto
df['nome'] = df['nome'].str.title() #Converter os nomes para título (primeira letra maiúscula)
df['endereco'] = df['endereco'].str.upper() #Converter os endereços para minúsculas
df['estado'] = df['estado'].str.upper()

#converter tipos de dados
df['idade'] = df['idade'].astype(int) #Converter a coluna 'idade' para o tipo inteiro

#tratar valores nulos (ausentes)
df_fillna = df.fillna(0) #Preencher valores nulos com 0
df_dropna = df.dropna() #Remover linhas com valores nulos
df_dropna4 = df.dropna(thresh=4) #Remover linhas que não possuem pelo menos 4 valores não nulos
df = df.dropna(subset =['cpf']) #Remover linhas onde a coluna 'cpf' possui valores nulos

print('\n valores nulos :\n', df.isnull().sum()) #Exibir a contagem de valores nulos em cada coluna
print('\n quantidade de nulos com fillna:\n', df_fillna.isnull().sum()) #Exibir a contagem de valores nulos após preencher com 0
print('\n quantidade de nulos com dropna:\n', df_dropna.isnull().sum()) #Exibir a contagem de valores nulos após remover linhas com valores nulos
print('\n quantidade de nulos com dropna(thresh=4):\n', df_dropna4.isnull().sum()) #Exibir a contagem de valores nulos após remover linhas que não possuem pelo menos 4 valores não nulos
print('\n quantidade de nulos com dropna(subset=[cpf]):\n', df.isnull().sum()) #Exibir a contagem de valores nulos após remover linhas onde a coluna 'cpf' possui valores nulos
print('\nDataFrame limpo:\n', df)

df.fillna({'estado': 'Desconhecido'}, inplace=True) #Preencher valores nulos na coluna 'estado' com 'Desconhecido'
df['endereco'] = df['endereco'].fillna('Endereço não informado') #Preencher valores nulos na coluna 'endereco' com 'Endereço não informado'
df['idade_corrida'] = df['idade'].fillna(df['idade'].mean()) #Preencher valores nulos na coluna 'idade' com a média da coluna

#Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') #Converter a coluna 'data' para o formato datetime, tratando erros

#Tratar duplicatas
print('\nQuantidade de duplicatas antes da remoção:', df.duplicated().sum()) #Exibir a quantidade de duplicatas antes da remoção
df = df.drop_duplicates() #Remover duplicatas
print('\nQuantidade de duplicatas após a remoção:', df.duplicated().sum()) #Exibir a quantidade de duplicatas após a remoção

print('\nDataFrame final:\n', df) #Exibir o DataFrame final após todas as limpezas e transformações

#salvar o DataFrame 
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'idade', 'cpf', 'endereco', 'estado', 'data']]
df_salvar.to_csv('clientes_limpos.csv', index=False) #Salvar o DataFrame limpo em um novo arquivo CSV

print('\nDataFrame salvo em clientes_limpos.csv') #Exibir mensagem indicando que o DataFrame foi salvo