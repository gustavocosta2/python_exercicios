# Exercicio 019
# Faça um programa que receba uma frase do usuário e retorne: (i) a quantidade de caracteres da frase
# (ii) a quantidade de letras 'e' na frase
# (iii) o índice da primeira substring 'ou'
# (iv) a frase toda maiuscula
# (v) a frase toda minuscula

frase = input("Digite uma frase: ")

# (i)
print(f"Quantidade de caracteres: {len(frase)}")

# (ii)
print(f"Quantidade de caracteres 'e' : {frase.count('e')}")

# (iii)
print(f"Posição da substring 'ou': {frase.find('ou')}")
# (iv)
frase.uppercase()
print(f"Frase em maiusculo: {frase.uppercase()}")
# (v)
frase.lowercase()
print(f"Frase em minusculo: {frase.lowercase()}")
