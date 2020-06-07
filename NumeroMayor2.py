print("Averiguemos que numero es mayor")
x=int(input("Introduzca el primer numero: "))
y=int(input("Introduzca el segundo numero: "))
if x > y:
    value = x
elif y > x:
    value = y
else:
    value =("Los numeros son iguales")
print(value)