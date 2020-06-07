#Ejercicio1

numero = int(input("Dime un número:"))
cuadrados = {}

for num in range(1,numero+1):
    cuadrados[num] = num ** 2
for num, valor in cuadrados.items():
    print("%d -> %d" % (num,valor))

#Ejercicio2

dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1	

for campo,valor in dict.items():
	print (campo,"->",valor)

#Ejercicio3

precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
while True:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower() not in precios:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * precios[fruta]))
    opcion = input("¿Quieres vender otra fruta (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta (s/n)")
    if opcion.lower() == "n":
        break

#Ejercicio4

alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))

#Ejercicio5

agenda = {}
while True:
    print("\n")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("Dime opción:"))
    if opcion == 1:
        nombre = input("Nombre del contacto:")    
        if nombre in agenda:
            print("%s ya existe su número de teléfono es %s" % (nombre,agenda[nombre]))
            opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                numero = input("Dame el nuevo número de teléfono:")
                agenda[nombre]=numero
        else:
            numero = input("Dame el número de teléfono:")
            agenda[nombre]=numero
    elif opcion == 2:
        cadena = input("Nombre del contacto a buscar:")    
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El número de teléfono de %s es el %s" % (nombre,agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre del contacto para borrar:")    
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre,"->",numero)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
