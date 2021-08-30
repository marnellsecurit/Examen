#Cree una clase llamada examen la cual tenga una funcion
#de multiplicacion la cual realice la operacion sin el simbolo de multiplicacion(*) y se le pase
#los parametros por pantalla.

class examen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.resultado = 0

    def multiplicar(self):
        for a in range(int(self.x)):
            self.resultado = self.resultado + int(self.y)
        return self.resultado

x = input('ingrese x:')
y = input('ingrese y:')
solucion = examen(x, y)
print(f"la respuesta es: {solucion.multiplicar()}")
