'''Crie uma função que retorne a quantidade de vogais (a, e, i, o, u) existentes em uma string.'''


def vogais(texto):
    texto = texto.lower()
    vogal = texto.count('a')
    vogal += texto.count('e')
    vogal += texto.count('i')
    vogal += texto.count('o')
    vogal += texto.count('u')
    return vogal

texto = input('Insira um texto: ')
print(f'A quantidade de vogais é de: {vogais(texto)}')


# outra solução 
''' 
def vogais2(texto):
    quantidade = 0
    vogais = 'aeiou'
    for caracter in texto:
        if caracter in vogais:
            quantidade += 1
    return quantidade

texto = input('Insira um texto: ')
print(f'A quantidade de vogais é de: {vogais2(texto)}')

'''


    