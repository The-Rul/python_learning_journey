# ============================================================
#  CLASE TABLERO
# ============================================================

class Tablero:
    """Representa el tablero de juego."""
    
    def __init__(self, tamano=10):
        """Inicializa un tablero vacío."""
        self.tamano = tamano
        self.matriz = [["~" for _ in range(tamano)] for _ in range(tamano)]
        self.barcos = []
    
    def validar_coordenada(self, fila, col):
        """Verifica si una coordenada está dentro del tablero."""
        return 0 <= fila < self.tamano and 0 <= col < self.tamano
    
    def obtener_celda(self, fila, col):
        """Devuelve el contenido de una celda."""
        if self.validar_coordenada(fila, col):
            return self.matriz[fila][col]
        return None
    
    def se_puede_colocar(self, fila, col, tamano, orientacion):
        """Verifica si un barco puede colocarse en una posición."""
        if orientacion == "U":
            if col - tamano < 0:
                return False
            for c in range(col - tamano, col):
                if self.matriz[fila][c] != "~":
                    return False
        elif orientacion == "D":
            if col + tamano > self.tamano:
                return False
            for c in range(col, col + tamano):
                if self.matriz[fila][c] != "~":
                    return False
        elif orientacion == "R":
            if fila + tamano > self.tamano:
                return False
            for f in range(fila, fila + tamano):
                if self.matriz[f][col] != "~":
                    return False
        elif orientacion == "L":
            if fila - tamano < 0:
                return False
            for f in range(fila - tamano, fila):
                if self.matriz[f][col] != "~":
                    return False
        else:
            return False
        return True
    
    def colocar_barco(self, barco, fila, col, orientacion):
        """Coloca un barco en el tablero."""
        if not self.se_puede_colocar(fila, col, barco.tamano, orientacion):
            return False
        
        barco.colocar(fila, col, orientacion)
        
        for f, c in barco.obtener_posiciones():
            self.matriz[f][c] = "B"
        
        self.barcos.append(barco)
        return True
    
    def buscar_barco_en_posicion(self, fila, col):
        """Busca el barco que ocupa una posición específica."""
        for barco in self.barcos:
            if barco.contiene_posicion(fila, col):
                return barco
        return None
    
    def recibir_disparo(self, fila, col):
        """Procesa un disparo en el tablero y devuelve el resultado."""
        if not self.validar_coordenada(fila, col):
            return "error"
        
        celda = self.matriz[fila][col]
        
        if celda == "~":
            self.matriz[fila][col] = "A"
            return "agua"
        elif celda == "B":
            self.matriz[fila][col] = "X"
            # Buscar el barco impactado
            barco = self.buscar_barco_en_posicion(fila, col)
            if barco:
                barco.recibir_impacto(fila, col)
                if barco.esta_hundido():
                    return f"hundido:{barco.obtener_nombre()}"
            return "tocado"
        elif celda in ["A", "X"]:
            return "repetido"
        
        return "error"
    
    def quedan_barcos(self):
        """Verifica si todavía quedan barcos sin hundir."""
        for fila in self.matriz:
            if "B" in fila:
                return True
        return False
    
    def mostrar(self, ocultar_barcos=False):
        """Muestra el tablero por consola."""
        print("  " + " ".join(str(i) for i in range(self.tamano)))
        for fila_idx, fila in enumerate(self.matriz):
            fila_mostrar = []
            for celda in fila:
                if ocultar_barcos and celda == "B":
                    fila_mostrar.append("~")
                else:
                    fila_mostrar.append(celda)
            print(fila_idx, " ".join(fila_mostrar))