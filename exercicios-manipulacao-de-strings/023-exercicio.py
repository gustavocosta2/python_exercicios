# Exercicio 023
# Faça um programa que recebe uma frase como entrada e conte quantas vezes uma determinada palavra aparece na frase

frase = input("Digite a frase: ")
palavra = input("Digite a palavra que você quer procurar e contar: ")

qtd = frase.count(palavra)

print(f"A palavra procurada aparece {qtd} vezes na frase digitada.")