# Exercicio 053
# Desenvolva um programa que inclua uma função chamada conta_caracteres que recebe uma string como parâmetro e retorna um dicionário com a 
# contagem de cada caractere

def conta_caracteres(palavra: object) -> dict:
    finalDict = dict()
    for caractere in palavra:
        if caractere in finalDict:
            finalDict[caractere] += 1
        else:
            finalDict[caractere] = 1
    
    return finalDict

conta_caracteres('passaro')