# Exercicio 034
# Faça um programa que solicite ao usuário digitar um numero e imprima a tabuada desse número.

n = int(input("Digite um número: "))

print(f"TABUADA DO NÚMERO {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
