# Exercicio 038
# Faça um programa que imprima os números 1 a 100, mas substitua os multiplos de 3 por "Fizz", os múltiplos de 5 por
# "Buzz" e os multiplos de 3 e 5 por "Fiz Buzz"

i = 0
while i <= 100:
    
    if i % 3 == 0 and not i % 5 == 0: # Se é múltiplo de 3, então imprima "Fizz"
        print("Fizz")
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("Fiz Buzz")
    else:
        print(i)
    
    i += 1

    