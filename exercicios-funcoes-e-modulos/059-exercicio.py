# Exercicio 059
# Desenvolva um programa que inclua uma função chamada numeros_unicos que recebe duas listas como parâmetros e retorna
# uma lista contendo apenas os elementos que são únicos em ambas as listas. Teste a função com diferentes conjuntos de lis
# tas

def numeros_unicos(lista1: list, lista2: list) -> list:
    
    set1 = set(lista1)
    set2 = set(lista2)
    
    lista_unica = set1 & set2
    return list(lista_unica)
