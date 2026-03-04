class Instrumento: 
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo #cuerda, viento, percusion
        self.afinado = False
    
    def afinar(self):
        self.afinado = True
        return f"Se ha afinado el instrumento: {self.nombre}"
    
    def tocar(self):
        return f"El instrumento {type(self).__name__}: {self.nombre} esta tocando"
    
    
class Guitarra (Instrumento):
    def __init__(self, nombre:str, numero_cuerdas:int)-> None:
        super().__init__(nombre=nombre, tipo ="cuerda") # Le paso directamente el tipo como cuerda
        self.numero_cuerdas = numero_cuerdas
    
    def tocar(self)-> str:
        """ Toca """
        if self.afinado:
            return f"Esta tocando la guitarra: {self.nombre}"
        else:
            return f"El instrumento {type(self).__name__}: {self.nombre} no esta afinado"   

class Guitarra_electrica(Guitarra):
    """ Hereda de guitarra y tendra potencia como var de instancia
    su metodo tocar , "tocando guitarra electrica y su nombre"""
    
    def __init__(self, nombre, numero_cuerdas, potencia):
        super().__init__(nombre=nombre, tipo="cuerda", numero_cuerdas=numero_cuerdas)
        self.potencia = potencia
            
    def tocar(self):
        return f"Tocando guitarra electrica: {self.nombre}"        
            
            
class Bateria(Instrumento):
    """Tendra marca y platillos. Hereda insturmento. Platillo es un objeto."""
    def __init__(self, nombre:str, marca:str, platillos: list):
        super().__init__(nombre=nombre, tipo="percusion")
        self.marca = marca
        self.platillos = platillos
 
class Platillo:
    pass
 
class BandaDeMusica:
    """ Tendra nombre, guitarra, guitarra electrica y bateria. Hereda de instrumento.
    Metodo afinar instrumentos y metodo tocar instrumentos"""   
    def __init__(self, nombre, guitarra:Guitarra, guitarra_electrica:Guitarra_electrica, bateria:Bateria):
        self.nombre = nombre
        self.guitarra = guitarra
        self.guitarra_electrica = guitarra_electrica
        self.bateria = bateria

    def afinar_instrumentos(self) -> str:
        self.guitarra.afinar()
        self.guitarra_electrica.afinar()
        self.bateria.afinar()
        return f"Se han afinado todos los instrumentos de la banda: {self.nombre}"
    
    def tocar_instrumentos(self) -> str:
        return f"{self.guitarra.tocar()}\n{self.guitarra_electrica.tocar()}\n{self.bateria.tocar()}"

    

#-------------------------
#----Ejemplo uso
#--------------------------

"""Crar objeto banda de musica y sus otros objetos y afinar instrumentos 
y tocar la banda de musica """

guitarra = Guitarra("Fender Stratocaster", "cuerda", 6)
guitarra_electrica = Guitarra_electrica("Gibson Les Paul", "cuerda", 6, 100)

# Lista de platillos
platillo1 = Platillo()
platillo2 = Platillo()
platillos = [platillo1, platillo2]

# Bateria
bateria = Bateria("Yamaha Stage Custom", "percusion", "Yamaha", platillos)

# Banda de musica
banda = BandaDeMusica("Los Pythoneros", guitarra, guitarra_electrica, bateria)  
print(banda.afinar_instrumentos())
print(banda.tocar_instrumentos())


for atribute, value in vars(banda).items():
    if isinstance(value, Instrumento):
        print(f"{atribute}: {value.afinado}")
