# Exercicio 006
# Faça um programa que leia algo digitado pelo usuário, mostre seu tipo e tudo a respeito dele.

var = input("Digite algo")

print(f"É um digito? {var.isdigit()}")
print(f"É um caractere alfabético? {var.isaplha()}")
print(f"É um caractere alfanumérico? {var.isalnum()}")
print(f"É tudo minusculo? {var.islower()}")
print(f"É tudo maiusculo? {var.isupper()}")
print(f"É apenas espaço em branco? {var.isspace()}")
