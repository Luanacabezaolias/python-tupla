'''Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a) o maior número da lista
b) o menor número da lista
c) a média dos números contidos na lista'''

lista = []
for i in range(10):
    num = input('Insira um número: ')
    lista.append(num)
print(max(lista))
print(min(lista))
print(sum(lista)/ len(lista))