# Exercicio 010
# Faça um programa que peça ao usuário um raio de um círculo e exiba na tela a área e o perímetro desse círculo (considere pi=3,14)
# Aproxime para duas casas decimais

raio = float(input("Digite o raio do círculo: "))

print(f"RESULTADOS\nPERÍMETRO: {2*raio*3.14:.2f}\nÁREA: {3.14*(raio**2):.2f}")