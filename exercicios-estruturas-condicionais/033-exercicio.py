# Exercicio 033
# Faça um programa que receba a temperatura em graus Celsius e converta para Fahrenheit ou vice-versa, de acordo com a escolha do usuário.

print("BEM VINDO AO CONVERSOR DE TEMPERATURAS")
escolha = input("Você quer converter de Fahrenheit para Celsius [s/n]").lower().strip()
temperatura = float(input("Digite a temperatura: "))

if escolha == 's':
    c = (5/9)*(temperatura-32)
    print(f"A temperatura em Celsius é de: {c:.2f} °C")
elif escolha == 'n':
    f = (9/5)*temperatura+32
    print(f"A temperatura em Fahrenheit é de {f:.2f} °F")