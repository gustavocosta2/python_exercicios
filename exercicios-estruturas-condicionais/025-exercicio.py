# Exercicio 025
# Faça um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero.

n = int(input("Digite um número: "))

if n > 0:
    print("O número é maior que zero.")
elif n < 0:
    print("O número é menor que zero.")
else:
    print("O número é zero.")
