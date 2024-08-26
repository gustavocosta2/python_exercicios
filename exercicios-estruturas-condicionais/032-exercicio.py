# Exercicio 032
# Faça um programa que verifique se um número é divisível por outro número fornecido pelo usuário.

n = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n % n2 == 0:
    print(f"O número {n} é divisível por {n2}")
else:
    print("Não é divísivel.")