# Exercicio 050
# Crie um programa que contenha uma função chamada fibonacci que recebe um número como parâmetro e retorna a sequência de Fibonacci
# até o n-ésimo termo.


def fibonacci(n):
    i=0
    seq_fibonacci = list()

    while i<n:
        if i == 0:
            seq_fibonacci.append(1)
        elif i == 1:
            seq_fibonacci.append(1)
        else:
            seq_fibonacci.append(seq_fibonacci[i-2] + seq_fibonacci[i-1])
        
        i+=1
    
    return seq_fibonacci

n = int(input("Digite o número de termos: "))

sequencia = fibonacci(n)
print(sequencia)


