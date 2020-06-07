class persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=0
    def imprimir(self):
        print("Mi nombre es %s y tengo %i años" %(self.nombre +" "+ self.apellido,self.edad))
    def setedad(self,edad):
        self.edad=edad
    def getedad(self):
        return self.edad
    def setestado(self,estado):
        self.estado=estado
    def getestado(self):
        return self.estado

persona1=persona("Jose","Manuel")
persona1.setedad(24)
persona1.setestado("soltero")
persona1.imprimir()
print("Mi estado actual es %s" %(persona1.getestado()))