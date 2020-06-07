valores=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
def busquedaBinaria(buscar,inicio,fin,iteraciones):
    centro=int((fin-inicio)/2)+inicio
    if centro>len(valores)-1 or inicio>fin:
        return (False,iteraciones)
    if buscar>valores[centro]:
        return busquedaBinaria(buscar,centro+1,fin,iteraciones+1)
    elif buscar<valores[centro]:
        return busquedaBinaria(buscar,inicio,centro-1,iteraciones+1)
    else:
        return (True,iteraciones)
while True:
    buscar=input("Indica un numero a buscar: ")
    if buscar=="":
        break
    try:
        buscar=int(buscar)
    except:
        print("El valor tiene que ser numerico")
        continue
    conseguido,iteraciones=busquedaBinaria(buscar,0,len(valores),1)
    if conseguido:
        print("Encontrado en {} iteraciones".format(iteraciones))
    else:
        print("El valor introducido no se encuentra en la lista de valores. Se han necesitado {} iteraciones".format(iteraciones))