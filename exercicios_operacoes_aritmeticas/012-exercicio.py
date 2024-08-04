# Exercicio 012
# Faça um programa que leia a temperatura em graus Celsius e exiba a temperatura em graus Fahrenheit. A fórmula para converter de Celsius para
# Fahrenheit é F = (9/5)*C + 32

temp = float(input("Digite a temperatura em graus Celsius: "))

conversao_fahrenheit = (9/5)*temp+32

print(f"A temperatura em Fahrenheit é: {conversao_fahrenheit:.2f}°F")