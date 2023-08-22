'''Escreva um programa que receba uma frase como entrada e retorne uma lista das palavras 
presentes na frase.'''

def lista_palavras(frase):
    return frase.split('')  # divide a frase onde houver um espaço em branco

frase = input('Informa uma frase: ')
print(lista_palavras(frase))
