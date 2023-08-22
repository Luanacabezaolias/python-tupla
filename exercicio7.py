'''Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a) o maior número da lista
b) o menor número da lista
c) a média dos números contidos na lista'''

def preenche_lista():
    lista = []
    for i in range(10):
        num = int(input('Insira um número: '))
        lista.append(num)
    print(lista)

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    return maior, menor, media

resultado = preenche_lista()
print(resultado)
print(f'Maior: {resultado[0]}')
print(f'Menor: {resultado[1]}')
print(f'Media: {resultado[2]}')