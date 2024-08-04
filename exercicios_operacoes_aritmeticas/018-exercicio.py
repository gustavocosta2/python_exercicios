# Exercicio 018
# Faça um programa que leia o valor de dois catetos e retorne o valor da hipotenusa, assumindo que seja possível formar um triângulo.

c1 = int(input("Digite um cateto: "))
c2 = int(input("Digite outro cateto: "))

hipotenusa = (c1**2 + c2**2)**0.5

print(f"A hipotenusa desse triângulo é: {hipotenusa}")