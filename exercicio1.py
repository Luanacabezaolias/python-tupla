'''Escreva uma função que receba uma string e retorne o número de caracteres nela'''
def conta_caracteres(frase):
    return len(frase)

frase = input('Digite a frase: ')
print(conta_caracteres(frase))