# Exercicio 008
# Faça um programa que receba os seguintes dados de um funcionário: nome, idade e salario. Na empresa que esse funcionário trabalha, seu salário
# é aumentado de ano em ano em R$800,90
# Sabendo disso, imprima o nome, salário do funcionário daqui um ano e a sua idade.

nome = input("Digite o nome do funcionário: ")
idade = int(input("Digite a idade do funcionário: "))
salario = float(input("Digite o salário atual do funcionário: "))

print(f"O funcionário {nome}, daqui um ano terá {idade+1} anos de idade e receberá um salário de {salario+800.9}")