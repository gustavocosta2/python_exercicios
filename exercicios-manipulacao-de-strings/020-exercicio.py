    # Exercicio 020
    # Faça um programa que peça ao usuário a cidade que ele mora e retorne True caso o nome da cidade inicie com "Rio" e 
    # False caso não

    nomeCidade = input("Digite o nome da sua cidade: ")

    print(f"A cidade começa com 'Rio'? {nomeCidade[0:3]=="Rio"}")