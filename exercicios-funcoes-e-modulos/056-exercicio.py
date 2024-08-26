# Exercicio 056
# Crie um programa que contenha uma função chamada fatorial que recebe um número como parâmetro e retorna o fatorial desse número.

def fatorial(n: int) -> int:
  resultado = 1

  for numero in range(1, n+1):
    resultado *= numero

  return resultado

print(fatorial(4))
