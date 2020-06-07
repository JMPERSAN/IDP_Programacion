print("Ordenaremos la siguiente lista de numeros (7, 82, 22, 20, 1, 95, 42, 74, 56, 98, 30) y sacaremos el numero menor: ")
numbers = [7, 82, 22, 20, 1, 95, 42, 74, 56, 98, 30]
for recorrido in range(1, len(numbers)):
    for posicion in range(len(numbers) - recorrido):
        if numbers[posicion] > numbers[posicion + 1]:
            temp=numbers[posicion]
            numbers[posicion]=numbers[posicion + 1]
            numbers[posicion + 1] = temp
print(numbers)
minimo = min(numbers)
print("El numero menor de esta lista es: " f"{minimo}")