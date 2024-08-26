# Exercicio 045
# Faça um programa que peça ao usuário para digitar números até ele digitar -1. Armazene todos esses números em uma lista, e
# por fim, exiba na tela essa lista com todos os elementos somados em 10 unidades (utilize a função map())

def soma_10(n: int) -> int:
    return n+10


n = int(input("Digite um número: "))
lista = list()

while n != -1:
    lista.append(n)
    n = int(input("Digite um número: "))

lista = list(map(soma_10, lista))
print(lista)