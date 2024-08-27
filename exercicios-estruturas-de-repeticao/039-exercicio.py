# Exercicio 039
# Faça um programa que solicite ao usuário digitar uma lista de números e encontre o maior numero da lista.

n = int(input("Digite o tamanho da lista: "))

lista = list()

for i in range(n):
    elemento = int(input("Digite um numero: "))
    lista.append(elemento)

for i in range(len(lista)):
    if i==0:
        maior = lista[i]
    
    if lista[i] > maior:
        maior = lista[i]

print(maior)