#Ordenar una lista de numeros de forma ascendente
print("Vamos a ordenar de forma ascendente los siguientes numeros (4, 12, 8, 2, 1):")
lista=[4, 12, 8, 2, 1]
for recorrido in range(1, len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion + 1]:
            temp=lista[posicion]
            lista[posicion]=lista[posicion + 1]
            lista[posicion + 1] = temp
print(lista)

#Ordenar una lista de numeros de forma descendente
print("Vamos a ordenar de forma descendente los siguientes numeros (4, 12, 8, 2, 1):")
lista=[4, 12, 8, 2, 1]
for recorrido in range(1, len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] < lista[posicion + 1]:
            temp=lista[posicion]
            lista[posicion]=lista[posicion + 1]
            lista[posicion + 1] = temp
print(lista)