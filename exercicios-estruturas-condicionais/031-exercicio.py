# Exercicio 031
# Faça um programa que receba o salário de um funcionário e calcule o valor do seu aumento de acordo com as seguintes condições:
# salários de até 1k : aumento de 20%
# salários entre 1k e 3k: aumento de 15%
# salários acima de 3k: aumento de 10%

salario = float(input("Digite o salário: "))

if salario > 3000:
    salario = salario + salario*0.1
elif salario <= 1000:
    salario = salario + salario*0.2
else:
    salario = salario + salario*0.15

print("O salário reajustado é de: ", salario)