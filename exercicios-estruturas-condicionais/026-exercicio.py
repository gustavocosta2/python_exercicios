# Exercicio 026
# Faça um programa que verifique se o número é divisivel por 3 e 5 ao mesmo tempo.

n = int(input("Digite um número: "))

if n % 3 == 0 and n % 5 == 0:
    print("É divisivel por 3 e 5 ao mesmo tempo")
else:
    print("Não é.")
    