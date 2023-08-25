'''Preencha duas listas, uma para armazenar os nomes e outra para armazenar as idades de 
pessoas. A entrada de dados deve ser finalizada quando o usuário informar um nome vazio.
Na sequência informe o nome de todas as pessoas que possuem idade igual ou superior a 
18 anos.'''

nome = []
idade = []

while True:
    nomes = input('Nome: ')
    if nome == '':
        break
    idades = int(input('Idade: '))
    nome.append(nomes)
    idade.append(idades)
print(nome)
print(idade)

for indice in range(len(idade)):
    if idade[indice] >= 18:
        print(nome[indice], idade[indice])