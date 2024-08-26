# Exercicio 046
# Faça um programa que receba duas entradas: a quantidade de linhas e colunas, nessa ordem, de uma matriz. Após isso, solicite
# que ele digite o valor correspondente a cada valor dessa matriz "Digite o valor ixj: " Ao final retorne a multiplicação
# de todos os elementos dessa matriz.

i = int(input("Digite a quantidade de linhas: "))
j = int(input("Digite a quantidade de colunas: "))

matriz = list()

for linha in range(i):
    listaLinha = list()
    for coluna in range(j):
        n = float(input(f"Digite o valor do elemento [{linha+1}]x[{coluna+1}]: "))
        listaLinha.append(n)
    
    matriz.append(listaLinha)

print(matriz)

# Multiplicação da matriz.
multiplicacao = 1
for linha in range(i):
    for coluna in range(j):
        multiplicacao *= matriz[linha][coluna]


print(multiplicacao)