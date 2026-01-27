class Visualizador:
    """Clase para gestionar la visualización del juego."""
    
    @staticmethod
    def mostrar_bienvenida():
        """Muestra el mensaje de bienvenida."""
        print("=" * 50)
        print("   HUNDIR LA FLOTA - Versión POO")
        print("=" * 50)
        print()
    
    @staticmethod
    def mostrar_tablero(tablero, titulo, ocultar_barcos=False):
        """Muestra un tablero con un título."""
        print(f"\n{titulo}:")
        tablero.mostrar(ocultar_barcos)
    
    @staticmethod
    def mostrar_dos_tableros(tablero_jugador, tablero_maquina):
        """Muestra ambos tableros."""
        Visualizador.mostrar_tablero(tablero_jugador, "Tu tablero", False)
        Visualizador.mostrar_tablero(tablero_maquina, "Tablero enemigo (oculto)", True)
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        """Muestra un mensaje formateado."""
        print(f"\n>>> {mensaje}")
    
    @staticmethod
    def mostrar_resultado(resultado):
        """Muestra el resultado de un disparo de forma clara."""
        if resultado == "agua":
            print("\n💧 ¡AGUA! Has fallado.")
        elif resultado == "tocado":
            print("\n💥 ¡TOCADO! Has impactado un barco.")
        elif resultado.startswith("hundido:"):
            nombre_barco = resultado.split(":")[1]
            print(f"\n🔥 ¡TOCADO Y HUNDIDO! Has hundido el {nombre_barco}.")
        elif resultado == "repetido":
            print("\n⚠️  Ya habías disparado aquí.")
        else:
            print(f"\n❌ Error en el disparo.")