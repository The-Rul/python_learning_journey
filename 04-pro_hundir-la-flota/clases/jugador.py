# ============================================================
#  CLASE JUGADOR
# ============================================================
import random
from .tablero import Tablero 

class Jugador:
    """Representa un jugador (humano o máquina)."""
    
    def __init__(self, nombre, es_humano=True):
        """Inicializa un jugador."""
        self.nombre = nombre
        self.es_humano = es_humano
        self.tablero = Tablero()
        self.disparos_realizados = 0
        self.impactos_logrados = 0
        self.disparos_previos = set()
    
    def obtener_tablero(self):
        """Devuelve el tablero del jugador."""
        return self.tablero
    
    def has_perdido(self):
        """Verifica si el jugador ha perdido (todos sus barcos hundidos)."""
        return not self.tablero.quedan_barcos()
    
    def pedir_coordenadas(self):
        """Solicita coordenadas al jugador humano."""
        while True:
            try:
                fila = int(input("Ingresa la fila (0-9): "))
                col = int(input("Ingresa la columna (0-9): "))
                if self.tablero.validar_coordenada(fila, col):
                    return (fila, col)
                else:
                    print("❌ Coordenadas fuera del tablero. Intenta de nuevo.")
            except ValueError:
                print("❌ Entrada inválida. Debes ingresar números.")
    
    def disparar_aleatorio(self, tablero_enemigo):
        """Realiza un disparo aleatorio (para la máquina)."""
        while True:
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            if (fila, col) not in self.disparos_previos:
                self.disparos_previos.add((fila, col))
                return (fila, col)
    
    def realizar_disparo(self, tablero_enemigo):
        """Realiza un disparo al tablero enemigo."""
        if self.es_humano:
            fila, col = self.pedir_coordenadas()
        else:
            fila, col = self.disparar_aleatorio(tablero_enemigo)
            print(f"\n🤖 La máquina dispara a ({fila}, {col})")
        
        resultado = tablero_enemigo.recibir_disparo(fila, col)
        self.disparos_realizados += 1
        
        if resultado in ["tocado"] or resultado.startswith("hundido"):
            self.impactos_logrados += 1
        
        return resultado