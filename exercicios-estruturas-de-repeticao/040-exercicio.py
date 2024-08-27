# Exercicio 040
# Faça um programa que solicite ao usuário digitar uma palavra e verifique se a palavra é um palíndromo utilizando
# um loop for

palavra = input("Digite uma palavra: ").lower().strip()

i = -1

for caractere in palavra:

    if caractere == palavra[i]:
        print(caractere, " ", palavra[i])
        i -= 1
    else:
        print("Não é um palíndromo.")
        break
    

    