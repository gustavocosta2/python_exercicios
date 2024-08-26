# Exercicio 030
# Faça um programa que verifique se uma palavra digitada pelo usuário é um palíndromo

palavra = input("Digite uma palavra: ")

palavra = palavra.lower()

if palavra[::-1] == palavra:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")