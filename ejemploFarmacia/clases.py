from datetime import datetime

class Farmacia():
    def __init__(self, nombre):
        """
        Constructor de la clase medicamentos, inicializa el mombre de la farmacia
        """
        self.ventas = []
        self.nombre = nombre


    def agregarVenta(self, venta):
        """
        Agrega un medicamento vendido a la lista de ventas 
        """
        self.ventas.append(venta)


    def recuperarVenta(self,pos):
        """
        Retorna la venta de la posicion pos de la lista de ventas
        """
        return self.ventas[pos]


    def eliminarVenta(self,posicion):
        """
        Elimina una ventas
        """
        self.ventas.pop(posicion)

    
    def totalVentas(self):
        """
        Retorna la cantidad de ventas almacenadas
        """
        return len(self.ventas)


    def verVentas(self):
        return self.ventas




class Venta():
    def __init__(self,nombre,droga,obraSocial,plan,importe): 
        """
        Constructor de la clase medicamentos, inicializa el campo nombre, droga, obra social, plan, importe de una instancia de medicamento
        """
        self.nombreMedicamento = nombre
        self.droga = droga
        self.obraSocial = obraSocial
        self.plan = plan
        self.importe = importe
        self.fechaVenta =  datetime.now().date()
        self.horaVenta = datetime.now().time()