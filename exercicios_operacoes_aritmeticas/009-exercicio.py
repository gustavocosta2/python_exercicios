# Exercicio 009
# Faça um programa que peça ao usuário para digitar dois números e mostre na tela o resultado da soma, subtração, multiplicação, divisão e
# resto da divisão desses números

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1 / n2 
resto = n1 % n2

print(f"RESULTADOS\nSoma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}\nResto: {resto}")
