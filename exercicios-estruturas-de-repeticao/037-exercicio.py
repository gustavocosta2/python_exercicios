# Exercicio 037
# Faça um programa que imprima a seguinte sequencia: 1, 2, 4, 8, 16, 32, 64... até o décimo termo.

i = 0
while i <= 10:

    if i == 0:
        n = 1
    else:
        n = 2

    operacao = n ** i 
    print(operacao)
    i += 1