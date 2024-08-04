# Exercicio 013
# Faça um programa que peça ao usuário para digitar 3 números inteiros e exiba a média aritmética desses números, aproxime 1 casa decimal.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

media = (n1+n2+n3)/3

print(f"A média aritmética desses números é de: {media:.1f}")
