print("Averiguemos que numero es mayor")
x=int(input("Introduzca el primer numero: "))
y=int(input("Introduzca el segundo numero: "))
z=int(input("Introduzca el tercer numero: "))
if x > y:
    value=x
else:
    value=y
if z > value:
    value=z
if x==y==z:
    print("Los tres numeros son iguales")
else:
    print("El numero mayor es :", value)