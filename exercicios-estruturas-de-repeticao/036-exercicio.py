# Exercicio 036
# Faça um programa que solicite ao usuário digitar uma frase e conte quantas vogais existem na frase usando um loop for.

frase = input("Digite uma frase: ").lower().strip()

soma = 0
for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        soma += 1

print(soma)