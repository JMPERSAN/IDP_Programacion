class fecha():
    def __init__(self,dia,mes,año):
        self.dia=dia
        self.mes=mes
        self.año=año
    def imprimir(self):
        print("Hoy es %s de %s del %s" %(self.dia,fecha1.nombremes(),self.año))
    def nombremes(self):
        nombremes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
        return nombremes[self.mes-1]
    def diasem(self):
        a = (14 - self.mes) // 12
        m = self.mes + 14 * a - 2
        diasem=["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
        valor=(self.dia + self.año + (self.año//4) - (self.año//100) + (self.año//400) + ((31 * m)//12)) % 7
        return diasem[valor]
fecha1=fecha(7,10,2020)
fecha1.imprimir()
print(fecha1.nombremes())
print(fecha1.diasem())