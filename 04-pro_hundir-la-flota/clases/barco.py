# ============================================================
#  CLASE BARCO
# ============================================================

class Barco:
    """Representa un barco en el tablero."""
    
    NOMBRES = {
        5: "Portaaviones",
        4: "Acorazado",
        3: "Crucero",
        2: "Destructor"
    }
    
    def __init__(self, tamano):
        """Inicializa un barco con un tamaño dado."""
        self.tamano = tamano
        self.nombre = self.NOMBRES.get(tamano, f"Barco de {tamano}")
        self.posiciones = []
        self.impactos = set()
        self.hundido = False
    
    def colocar(self, fila, col, orientacion):
        """Calcula y guarda las posiciones del barco según orientación."""
        self.posiciones = []
        
        if orientacion == "U":
            self.posiciones = [(fila, col - i) for i in range(self.tamano)]
        elif orientacion == "D":
            self.posiciones = [(fila, col + i) for i in range(self.tamano)]
        elif orientacion == "R":
            self.posiciones = [(fila + i, col) for i in range(self.tamano)]
        elif orientacion == "L":
            self.posiciones = [(fila - i, col) for i in range(self.tamano)]
    
    def recibir_impacto(self, fila, col):
        """Registra un impacto en el barco."""
        if (fila, col) in self.posiciones:
            self.impactos.add((fila, col))
            if len(self.impactos) == self.tamano:
                self.hundido = True
            return True
        return False
    
    def esta_hundido(self):
        """Devuelve True si el barco está completamente hundido."""
        return self.hundido
    
    def contiene_posicion(self, fila, col):
        """Verifica si el barco ocupa una posición específica."""
        return (fila, col) in self.posiciones
    
    def obtener_posiciones(self):
        """Devuelve la lista de posiciones del barco."""
        return self.posiciones
    
    def obtener_nombre(self):
        """Devuelve el nombre del barco."""
        return self.nombre