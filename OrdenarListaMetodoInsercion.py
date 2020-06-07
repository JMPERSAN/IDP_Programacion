lista=[27, 40, 12, 1, 21]
for recorrido in range(1, len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion + 1]:
            temp=lista[posicion]
            lista[posicion]=lista[posicion + 1]
            lista[posicion + 1]=temp
print(lista)