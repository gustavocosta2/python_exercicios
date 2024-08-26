# Exercicio 058
# Desenvolva um programa que inclua uma função chamada cria_dataframe que recebe duas listas: uma com o nome das colunas e a outra com os valores
# que cada coluna terá. A função deve retornar um dataframe

import pandas as pd

def cria_dataframe(lista1: list, lista2: list[list]) -> pd.DataFrame:
    df = pd.DataFrame(lista1, lista2)
    return df

cria_dataframe(['Idade', 'Nome', 'Cidade'], [[22, 'Gustavo', 'BH'], [23, 'Fernando', 'SP']])
