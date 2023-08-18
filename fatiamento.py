# FATIAMENTO / SLICE
# Seleciona um pedaço de uma string (ou lista, ou tupla)

#[inicio:fim:passo]

nome = 'Luane Camile'
primeiro_nome = nome[0:5]
print(primeiro_nome)

segundo_nome = nome[6:12]
print(segundo_nome)

exemplo = nome [3:12:2]
print(exemplo)

# caso não seja informado o valor de inicio, é considerado o zero 
exemplo = nome [ :10]
print(exemplo)

# caso não seja informado o valor final, é considerado o ultimo indice 
exemplo = nome [2:]
print(exemplo)

exemplo = nome [:]
print(exemplo)

# fatiamento em ordem inversa
exemplo = nome [::-1]
print(exemplo)

exemplo = nome[15:2:-2]
print(exemplo)

lista = [3, 5, 7, 9]
lista2 = lista[:2]
print(lista2)
