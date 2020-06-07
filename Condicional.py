name=input("¿Como te llamas?")
if name=="Jose Manuel":
    print ("Bienvenido Jose Manuel")
else:
    print ("No tienes poder aqui")
age=int(input("¿Cuantos años tienes?"))
if age >= 18:
    print ("Eres mayor de edad")
else:
    print ("Eres menor de edad")

age=input("Introduce tu edad")
if type(age)==str:
    print("Es una String")
if type(int(age))==int:
    print("es un entero")
print(type(age))
print(type(int(age)))

x=int(input("¿Cuanto has sacado en el examen?"))
if x < 5:
    print ("Debes estudiar mas")
else:
    print ("Enhorabuena")