# Exercicio 021
# Faça um programa que peça ao usuário para digitar seu nome e retorne True caso o nome contenha "Oliveira" e false
# caso contrário.

nome = input("Digite seu nome completo: ").lower()
print(f"O nome contém 'Oliveira'? {'oliveira' in nome}")