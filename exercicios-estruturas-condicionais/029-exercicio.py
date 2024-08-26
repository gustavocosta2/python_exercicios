# Exercicio 029
# Faça um programa que calcule o IMC (Índice de Massa Corporal) e exiba a categoria correspondente (abaixo do peso, peso normal, sobrepeso, 
# obesidade grau I, grau II ou grau III)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso/(altura**2)

if imc >=40:
    print("Obesidade classe III")
elif imc >=35:
    print("Obesidade classe II")
elif imc >=30:
    print("Obesidade classe I")
elif imc >=25:
    print("Excesso de peso")
elif imc >=18.5:
    print("Peso normal.")
else:
    print("Abaixo do peso normal.")

