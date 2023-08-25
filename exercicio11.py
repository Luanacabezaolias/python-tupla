'''Preencha duas listas, uma para armazenar os nomes e outra para armazenar as idades de 
pessoas. A entrada de dados deve ser finalizada quando o usuário informar um nome vazio.
Na sequência informe o nome de todas as pessoas que possuem idade igual ou superior a 
18 anos.'''

lista1 = []
lista2 = []

for i in range(5):
    n = int(input('Número: '))
    lista1.append(n)

for i in  range(5):
    n = int(input('Número: '))
    lista2.append(n)

tupla1 = tuple(lista1)
tupla2 = tuple(lista2)

tupla3 = tupla1 + tupla2
print(tupla3)
