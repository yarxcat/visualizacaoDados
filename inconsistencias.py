import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())
# Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

#corrigir datas
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', erros='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

#corrigir campo com multiplas informações
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
#df['estado_sigla'] = df['endereco'].apply(lambda x: x.split('/')[1].strip() if len(x.split('\n')) . 1 else ' Desconhecido')

#verificando formato do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço invalido' if len(x) > 50 or len(x) < 5 else x)

# corrigir dados erroneos
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido')


