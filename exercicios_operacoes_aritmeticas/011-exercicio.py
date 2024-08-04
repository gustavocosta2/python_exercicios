# Exercício 011
# Faça um programa que peça ao usuário o preço de um produto e exiba o preço com um desconto de 10%

preco = float(input("Digite o valor do produto: "))

preco = preco - preco*0.1

print(f"O valor final do produto com 10% de desconto é: R${preco:,.2f}")