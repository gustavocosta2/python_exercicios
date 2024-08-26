# Exercicio 028
# Verifique se um ano é bissexto ou não.

ano = int(input("Digite o ano: "))

ano = ano % 1000
ano = ano % 100

if ano % 4 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")