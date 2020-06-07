lista=[4, 12, 8, 2, 1]
for recorrido in range(1, len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion + 1]:
            temp=lista[posicion]
            lista[posicion]=lista[posicion + 1]
            lista[posicion +1] = temp
x=int(input("Escribe un numero del 1 al 20: "))
if x in lista:
    print("Este numero se encuentra en la lista:")
    print(lista)
else:
    print("Este numero no se encuentra en la lista")