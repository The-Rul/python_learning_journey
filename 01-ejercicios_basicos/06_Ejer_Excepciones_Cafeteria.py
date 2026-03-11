'''clase TazaCafe:
	temperatura

clase Cliente:
	nombre
 TazaCafe
	
	tomar TazaCafe() -> Método 

clase Cafeteria:
	nombre
	cliente
	
	servir_cliente() -> Método
		# El cliente se toma la taz de café.
		# Si esta por debajo de 20 grados lanzar excepción y si esta por 90 grado también lanza.  

Excepciones personalizadas.

- TemperatureException (Exception)
- TooHotTemperatureException (TemperatureException) - Hereda de 
- TooColdTemperatureException(TemperatureException)

Crear cafeteria con cliente que tiene taza de café con 
una temperatura aleatoria.'''

################# IMPORTACIONES #######################
from random import randint 

################# CLASES #######################

class TazaCafe:
    def __init__(self):
        self.temperatura = randint(1,100)#generar con random
        
class Cliente:
    def __init__(self, nombre = "na", taza_cafe = None ):
        self.nombre = nombre
        self.taza_cafe = taza_cafe
    
    def tomar_taza_cafe(self):
        print(f"Tomando cafe....Temperatura cafe: {self.taza_cafe.temperatura}")
        if self.taza_cafe.temperatura < 40:
            raise TooColdTemperatureException("El cafe esta frio")
        elif self.taza_cafe.temperatura > 60:
            raise TooHotTemperatureException("El cafe esta demasiado caliente.")
        else:
            print(f"Cafe listo para tomar, {self.nombre}")
    
    
class Cafeteria:
    def __init__(self, nombre = "na", cliente:Cliente = None):
        self.nombre = nombre
        self.cliente = cliente
    
    def servir_cliente(self):
        print("Sirviendo taza de cafe...")
        cliente_sin_cafe = True
        while(cliente_sin_cafe):
            try:
                self.cliente.taza_cafe = TazaCafe() #Una nueva taza de cafe en cada vuelta
                self.cliente.tomar_taza_cafe()
                cliente_sin_cafe = False
            except TooColdTemperatureException as e_cold:
                print("Error: " + str(e_cold))
            except TooHotTemperatureException as e_hot:
                print("Error: " + str(e_hot))  
        # podria ponerse except(TooHot....Exceptio, TooCold...exception) as e
                 


##### solucion profesor
'''
        except TemperatureException as te:
            print(f"El cliente se ha quejado : {te} le pongo otro cafe")'''
# Vamos a lanzar varios cafes hasta que este la temperatura adecuada. 

########### DEFINIR EXCEPCIONES ################

class TemperatureException(Exception):
    pass

class TooHotTemperatureException(TemperatureException):
    pass

class TooColdTemperatureException(TemperatureException):
    pass

################# EJECUCIÓN PROGRAMA #######################

# 1. Creacion taza de cafe, cliente y cafeteria

taza_01 = TazaCafe()
cliente_01 = Cliente("Juan Antonio", taza_01)
cafeteria_01 = Cafeteria("Starbucks", cliente_01)

cafeteria_01.servir_cliente()
print(cafeteria_01.__dict__)
