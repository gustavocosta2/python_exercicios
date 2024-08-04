# Exercicio 015
# Faça um programa que leia dois números inteiros do usuário e troque seus valores, ou seja, se o primeiro número for 5 e o segundo número
# for 7, o programa deve fazer com que o primeiro número seja igual a 7 e o segundo número seja igual a 5.

n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo número: "))

aux = n2
n2 = n1
n1 = aux

print(f"O primeiro número trocado é: {n1}\nO segundo número trocado é: {n2}")