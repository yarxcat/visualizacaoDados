import pandas as pd
import random
from faker import Faker

# Gerar dados fictícios usando a biblioteca Faker
fake = Faker('pt_BR')

dados_pessoas = []
# Gerar dados fictícios para 10 pessoas
for _ in range(10):
    nome = fake.name()
    cpf = fake.cpf()
    idade = random.randint(18, 80)
    endenereco = fake.address().replace('\n', ', ')
    estado = fake.estado_sigla()
    pais = 'Brasil'

    # Criar um dicionário para cada pessoa gerada
    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'endereco': endenereco,
        'estado': estado,
        'pais': pais
    }
    # Adicionar a pessoa gerada à lista de dados
    dados_pessoas.append(pessoa)
# Criar um DataFrame a partir dos dados gerados
df = pd.DataFrame(dados_pessoas)
print(df)

