# Exercicio 041
# Faça um programa que solicite ao usuário um número e em seguida imprima o fatorial desse número

n = int(input("Digite um número: "))

fatorial = 1
while n >= 0:
    
    if n == 0:
        fatorial *= 1
    else:
        fatorial *= n

    n -= 1

print(fatorial)