# Exercicio 014
# Faça um programa que leia o peso e a altura de uma pessoa e exiba o índice de massa corporal (IMC) dela. A fórmula do IMC é:
# IMC = peso/altura^2, com aproximação de 3 casas decimais.

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (metros): "))

imc = peso/(altura**2)

print(f"O seu índice de massa corporal (IMC) é de: {imc:.3f}")