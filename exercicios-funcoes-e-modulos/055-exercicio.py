# Exercicio 055
# Desenvolva um programa que inclua uma função chamada ordena_lista que ordena uma lista de números em ordem crescente.
# Teste a função com diferentes listas. Não utilize a função sorted nem o método sort.

def ordena_lista(lista: list) -> list:
    
    for iteracao in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista

print(ordena_lista([3,4,1,2]))
