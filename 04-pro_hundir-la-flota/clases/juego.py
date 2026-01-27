# ============================================================
#  CLASE JUEGO
# ============================================================
import random
from .jugador import Jugador
from .visualizador import Visualizador
from .colocador_barcos import ColocadorBarcos
from .barco import Barco

class Juego:
    """Controla el flujo principal del juego."""
    
    def __init__(self):
        """Inicializa el juego."""
        self.jugador = Jugador("Jugador", es_humano=True)
        self.maquina = Jugador("Máquina", es_humano=False)
        self.modo_juego = "Turnos"  # "Turnos" o "Fallos"
        self.turno_actual = "jugador"
        self.partida_terminada = False
        self.visualizador = Visualizador()
    
    def elegir_modo_juego(self):
        """Permite elegir entre modo Turnos o Fallos."""
        print("\nElige el modo de juego:")
        print("1. Turnos: Se cambia de turno tras cada disparo (acierto o fallo)")
        print("2. Fallos: Solo se cambia de turno tras fallar (agua)")
        
        while True:
            opcion = input("\nIngresa 1 o 2: ").strip()
            if opcion == "1":
                self.modo_juego = "Turnos"
                print("✅ Modo seleccionado: TURNOS")
                break
            elif opcion == "2":
                self.modo_juego = "Fallos"
                print("✅ Modo seleccionado: FALLOS")
                break
            else:
                print("❌ Opción inválida. Ingresa 1 o 2.")
    
    def iniciar_partida(self):
        """Inicia una nueva partida."""
        self.visualizador.mostrar_bienvenida()
        self.elegir_modo_juego()
        
        # Colocar tablero predefinido para el jugador
        self.jugador.tablero.matriz = [
            ["~","~","~","~","~","~","B","~","~","~"],
            ["~","B","B","B","B","B","B","~","~","~"],
            ["~","~","~","~","~","~","B","~","~","~"],
            ["~","~","~","~","~","~","~","~","~","~"],
            ["~","~","~","~","~","~","~","~","~","~"],
            ["~","~","~","B","~","~","~","~","~","~"],
            ["~","~","~","B","~","~","~","~","~","~"],
            ["~","~","~","B","~","~","~","B","B","~"],
            ["~","B","B","B","B","~","~","~","~","~"],
            ["~","~","~","~","~","~","~","~","~","~"]
        ]
        
        # Crear barcos manualmente para el jugador (basado en matriz)
        barcos_jugador = [
            Barco(5), Barco(4), Barco(3), Barco(3), Barco(2)
        ]
        # Colocarlos en posiciones específicas según la matriz predefinida
        self.jugador.tablero.barcos.append(Barco(5))
        self.jugador.tablero.barcos[0].posiciones = [(1,1),(1,2),(1,3),(1,4),(1,5)]
        
        # Colocar flota de la máquina aleatoriamente
        ColocadorBarcos.colocar_flota(self.maquina.tablero)
        
        # Bucle principal
        while not self.partida_terminada:
            self.ejecutar_turno()
    
    def ejecutar_turno(self):
        """Ejecuta un turno completo."""
        if self.turno_actual == "jugador":
            self.visualizador.mostrar_dos_tableros(
                self.jugador.tablero, 
                self.maquina.tablero
            )
            print(f"\n{'='*50}")
            print("🎯 TU TURNO")
            print(f"{'='*50}")
            
            resultado = self.jugador.realizar_disparo(self.maquina.tablero)
            self.visualizador.mostrar_resultado(resultado)
            
            # Verificar si ganó el jugador
            if self.verificar_fin_partida():
                return
            
            # Decidir si cambiar turno según modo de juego
            if self.modo_juego == "Turnos":
                self.cambiar_turno()
            elif self.modo_juego == "Fallos":
                if resultado == "agua":
                    self.cambiar_turno()
                else:
                    print("\n✨ ¡Sigue disparando!")
        
        else:  # Turno de la máquina
            print(f"\n{'='*50}")
            print("🤖 TURNO DE LA MÁQUINA")
            print(f"{'='*50}")
            
            resultado = self.maquina.realizar_disparo(self.jugador.tablero)
            self.visualizador.mostrar_resultado(resultado)
            
            # Verificar si ganó la máquina
            if self.verificar_fin_partida():
                return
            
            # Decidir si cambiar turno
            if self.modo_juego == "Turnos":
                self.cambiar_turno()
            elif self.modo_juego == "Fallos":
                if resultado == "agua":
                    self.cambiar_turno()
                else:
                    print("\n🤖 La máquina dispara de nuevo...")
    
    def cambiar_turno(self):
        """Cambia el turno entre jugador y máquina."""
        if self.turno_actual == "jugador":
            self.turno_actual = "maquina"
        else:
            self.turno_actual = "jugador"
    
    def verificar_fin_partida(self):
        """Verifica si la partida ha terminado."""
        if self.maquina.has_perdido():
            print("\n" + "="*50)
            print("🎉 ¡FELICIDADES! ¡HAS GANADO!")
            print("="*50)
            self.partida_terminada = True
            return True
        elif self.jugador.has_perdido():
            print("\n" + "="*50)
            print("😢 La máquina ha ganado. ¡Mejor suerte la próxima!")
            print("="*50)
            self.partida_terminada = True
            return True
        return False