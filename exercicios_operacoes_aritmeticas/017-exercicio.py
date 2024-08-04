# Exercicio 017
# Faça um programa que leia um número e retorne seu quadrado, sua raiz quadrada e sua raíz cúbica, aproximação de 2 casas decimais.

n = int(input("Digite um número: "))

nq = n**2
nrq = n**0.5
nrc = n**(1/3)

print(f"RESULTADOS\nQuadrado: {nq:.2f}\nRaiz Quadrada: {nrq:.2f}\nRaiz Cúbica: {nrc:.2f}")