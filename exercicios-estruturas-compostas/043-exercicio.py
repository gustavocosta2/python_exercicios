# Exercicio 043
# Faça um programa que receba números do usuário até ele digitar -1 e armazene todos esses números em uma lista. Por fim,
# exiba na tela "A soma dos numeros que você passou foi: {soma}"

def soma_acumulada(n: int) -> int:
    
    lista = list()
    while n != -1:
        lista.append(n)
        n = int(input("Digite um número: "))
    
    return sum(lista)


n = (int(input("Digite um número: ")))
soma = soma_acumulada(n)

print(f"A soma dos números que você passou foi: {soma}")
    
