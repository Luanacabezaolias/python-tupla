'''Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista 
com os números pares e outra com os números ímpares. 
Exemplo: 
Suponha que os números digitados são: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]'''

pares = []
impares = []

for i in range (10):
    numero = int(input('Número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)