# Exercicio 047
# Faça um programa que utilizando a lógica do exercicio anterior, retorne o maior elemento de cada uma das linhas da 
# matriz

i = int(input("Digite a quantidade de linhas: "))
j = int(input("Digite a quantidade de colunas: "))

matriz = list()

for linha in range(i):
    listaLinha = list()
    for coluna in range(j):
        n = float(input(f"Digite o valor do elemento [{linha+1}]x[{coluna+1}]: "))
        listaLinha.append(n)
    
    matriz.append(listaLinha)

# Encontrando o maior elemento da linha
listaMaiores = list()

for linha in range(i):
    maior = matriz[linha][0]
    for coluna in range(j):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
    
    listaMaiores.append(maior)


print(listaMaiores)