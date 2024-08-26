# Exercicio 048
# Faça um programa que recebe palavras de um usuário até que ele digite "goiabada" e adicione todas essas palavras em uma
# lista. Após isso retorne uma lista com todas as palavras que não possuam vogais (utilize a função filter())

listaPalavras = list()

palavra = input("Digite uma palavra: ")
while palavra != "goiabada":
    listaPalavras.append(palavra)
    palavra = input("Digite uma palavra: ")

lista = filter(lambda palavra: not (('a' in palavra) or ('e' in palavra) or ('i' in palavra) or ('o' in palavra) or ('u' in palavra)),listaPalavras)
lista = list(lista)

print(lista)