import Usuario
import Libro
from datetime import date, datetime

class Prestamo():
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        libro.copias_disponibles -= 1
        self.fecha_prestamo = datetime.now()
        
    def devolver_prestamo(self):
        if(self.__calcular_multa() > 0):
            print("Tienes que pagar " + self.__calcular_multas() + " euros de multa.")
        self.libro.copias_disponibles += 1
        self.fecha_devolucion = datetime.now()
        
    def __calcular_multa(self):
        diferencia = datetime.now() - self.fecha_prestamo
        return diferencia.days