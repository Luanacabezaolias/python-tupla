'''Implemente uma função que retorne a quantidade de palavras existentes em uma string'''
def conta_palavras(frase):
    lista = frase.split('')
    return len(lista)

frase = input('Informa uma frase: ')
print(f'Quantidade de palavras na frase: {conta_palavras(frase)}')

