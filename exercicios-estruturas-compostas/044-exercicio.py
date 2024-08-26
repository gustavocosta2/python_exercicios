# Exercicio 044
# Faça um programa que receba informações de 4 pessoas. As informações são: 'nome', 'idade' e 'cidade'. Armazene essas infor
# mações em uma lista de dicionários e, ao final, retorne a seguinte mensagem: {nome} é o mais velho e mora em {cidade}.

lista = list()

for indicePessoa in range(4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")

    #Procurando a pessoa mais velha.
    if indicePessoa == 0:
        maisVelho = indicePessoa
    elif  idade > lista[maisVelho]['idade']:
        maisVelho = indicePessoa

    dicionario = {'nome': nome, 'idade': idade, 'cidade': cidade}
    lista.append(dicionario)

print(f"{lista[maisVelho]['nome']} é o mais velho e mora em {lista[maisVelho]['cidade']}")

