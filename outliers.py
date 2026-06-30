import pandas as pd
from scipy import stats

pd.set_option('display.width', None) 

df = pd.read_csv('clientes_limpos.csv')

df_filtro_basico = df[df['idade'] > 100] 

print('\nFiltro básico :\n', df_filtro_basico[['nome', 'idade']])

#identificar outliers com z-score
z_score = stats.zscore(df['idade'].dropna())
outliers_z = df[z_score >= 3]
print('\nOutliers pelo Z-Scores:\n', outliers_z)

# filtrar outliers com zscore
df_zscore = df[(stats.zscore(df['idade'])< 3)]

#filtrar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('\nLimites IQR: \n', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('\nOutliers pelo IQR:\n',outliers_iqr)

#filtrar outliers com iqr

df_iqr = df[((df['idade'] >= limite_baixo) | (df['idade'] <= limite_alto))]

#filtrar endereços invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)

#tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('\nQuantidade de resgistros com nomes grandes: ', (df['nome'] == 'Nome inválido').sum())

print('\nDados com Outliers tratados:\n', df)

#salvar df
df.to_csv('clientes_remove_outliers.csv', index= False)