# Exercicio 052
# Crie um programa que contenha uma função chamada eh_palindromo que verifica se uma palvra é palíndromo. Teste a função com diferentes palavras

def eh_palindromo(palavra: object) -> bool:
    if palavra == palavra[::-1]:
        return True
    else:
        return False


palavra = input("Digite uma palavra: ")

print(f"A palavra é um palíndromo? {eh_palindromo(palavra)}")