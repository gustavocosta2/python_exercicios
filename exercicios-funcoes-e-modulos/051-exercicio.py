# Exercicio 051
# Desenvolva um programa que inclua uma função chamada eh_primo que verifica se um número é primo ou não. Solicite ao usuário um número e
# utilize a função para determinar se é primo.

def eh_primo(n: int) -> bool:
    qtdDivisores = 0
    for numero in range(1, n+1):
        if n % numero == 0:
            qtdDivisores +=1
    
    if qtdDivisores == 2:
        return True
    else:
        return False


n = int(input("Digite o número: "))
