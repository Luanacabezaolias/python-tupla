'''Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a) a quantidade de números pares contidos na lista
b) o somatório de todos os números ímpares contidos na lista.
'''

lista = []
for i in range (10):
    numero = int(input('Número: '))
    lista.append(numero)
print(lista)

cont = 0 
soma = 0
for  item in lista:

    if item % 2 == 0:
        cont += 1
    else:
        soma += item
print(f'Quantidade de pares: {cont}')
print(f'Quantidade de impares: {soma}')



