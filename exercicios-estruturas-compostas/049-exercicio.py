# Exercicio 049
# Faça um programa que receba o nome e a temperatura máxima de várias cidades e ao longo de uma semana e armazene essas 
# informações em um dicionário, onde a chave é o nome da cidade e o valor é a temperatura máxima (pare de receber infor
# mações quando o usuário digitar 'goiabada' no nome da cidade). O programa deverá retornar em quantos graus a maior tem
# peratura supera a média das temperaturas.

#Lista para armazenar cada cidade e sua respectiva temperatura.
cidades = list()


nome = input("Digite o nome da cidade: ").lower().strip()
while nome != "goiabada":
    temperaturaMaxima = float(input("Digite a temperatura em C°: "))
    dicionario = {nome: temperaturaMaxima}

    cidades.append(dicionario)#Lista de dicionários.
    
    nome = input("Digite o nome da cidade: ").lower().strip()


somaTemperaturas = 0

# Agora, para a lista de dicionários, vamos procurar pela maior temperatura registrada.
for i, cidade in enumerate(cidades):
     
    #Obtenção da chave para acessar o valor das temperaturas de cada cidade.
    chave = list(cidade.keys())[0]
    somaTemperaturas += cidade[chave]

    if i==0:
        maiorTemperatura = cidade[chave]
    
    if cidade[chave] > maiorTemperatura:
        maiorTemperatura = cidade[chave]


# Cálculo da média.
media = somaTemperaturas / len(cidades)

print(f"A maior temperatura foi de {maiorTemperatura}C° e a média das temperaturas das cidades é de {media:.2f}°C, a diferença da máxima para a média é de: {maiorTemperatura - media:.2f}°C")
