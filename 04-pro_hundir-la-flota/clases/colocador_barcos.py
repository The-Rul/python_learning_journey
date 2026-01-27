# ============================================================
#  CLASE COLOCADOR DE BARCOS
# ============================================================
import random
from .barco import Barco    

class ColocadorBarcos:
    """Clase utilitaria para colocar barcos en un tablero."""
    
    @staticmethod
    def colocar_flota(tablero):
        """Coloca una flota completa de barcos de forma aleatoria."""
        tamanos = [5, 4, 3, 3, 2]
        for tamano in tamanos:
            ColocadorBarcos.colocar_barco_aleatorio(tablero, tamano)
    
    @staticmethod
    def colocar_barco_aleatorio(tablero, tamano):
        """Coloca un barco de forma aleatoria en el tablero."""
        barco = Barco(tamano)
        colocado = False
        
        while not colocado:
            fila = random.randint(0, tablero.tamano - 1)
            col = random.randint(0, tablero.tamano - 1)
            orientacion = random.choice(["U", "D", "L", "R"])
            
            if tablero.colocar_barco(barco, fila, col, orientacion):
                colocado = True