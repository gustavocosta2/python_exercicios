# Exercicio 042
# Faça um programa que solicite ao usuário digitar um número N e, em seguida, imprima N números da sequencia de Fibonacci

n = int(input("Digite um número: "))

sequencia_fibonacci = list()

i = 0
while i < n:
    
    if i == 0:
        elemento = 1
    elif i == 1:
        elemento = 1
    else:
        elemento = sequencia_fibonacci[i-2] + sequencia_fibonacci[i-1]

    print(elemento)
    sequencia_fibonacci.append(elemento)
    i += 1    

