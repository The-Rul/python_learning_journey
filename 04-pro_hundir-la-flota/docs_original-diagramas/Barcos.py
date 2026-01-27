# ============================================================
#  HUNDIR LA FLOTA - Versión imperativa
# ============================================================

import random

# ------------------------------------------------------------
#  Utilidades
# ------------------------------------------------------------

def crearTablero(tamano=10):
    """Devuelve una matriz tamano x tamano inicializada con agua."""
    return [["~" for _ in range(tamano)] for _ in range(tamano)]


def imprimirTablero(tablero, ocultarBarcos=False):
    """Muestra el tablero por pantalla."""
    print("  " + " ".join(str(i) for i in range(len(tablero))))
    for fila_idx, fila in enumerate(tablero):
        filaMostrar = []
        for celda in fila:
            if ocultarBarcos and celda == "B":
                filaMostrar.append("~")
            else:
                filaMostrar.append(celda)
        print(fila_idx, " ".join(filaMostrar))


# ------------------------------------------------------------
#  Colocación de barcos
# ------------------------------------------------------------

def sePuedeColocar(tablero, fila, col, tamano, orientacion):
    """Comprueba si cabe un barco en el tablero sin solaparse."""
    #Las opciones de orientacion son arriba (U), abajo(D), izquierda (L) y derecha(R)
    match orientacion:
        case "U":
            if col - tamano < 0:
                return False
            for c in range(col - tamano, col):
                if tablero[fila][c] != "~":
                    return False
        case "D":
            if col + tamano > len(tablero):
                return False
            for c in range(col, col + tamano):
                if tablero[fila][c] != "~":
                    return False
        case "R":
            if fila + tamano > len(tablero):
                return False
            for f in range(fila, fila + tamano):
                if tablero[f][col] != "~":
                    return False
        case "L":
            if fila - tamano < 0:
                return False
            for f in range(fila - tamano, fila):
                if tablero[f][col] != "~":
                    return False
        case _:
            return False
    return True


def colocarBarco(tablero, tamano):
    """Coloca un barco de tamaño dado en el tablero de forma aleatoria."""
    colocado=False
    while not colocado:
        fila = random.randint(0, len(tablero)-1)
        col = random.randint(0, len(tablero)-1)
        orientacion = random.choice(["U", "D", "L", "R"])

        if sePuedeColocar(tablero, fila, col, tamano, orientacion):
            match orientacion:
                case "U":
                    for c in range(col - tamano, col):
                        tablero[fila][c] = "B"
                case "D":
                    for c in range(col, col + tamano):
                        tablero[fila][c] = "B"
                case "R":
                    for f in range(fila, fila + tamano):
                        tablero[f][col] = "B"
                case "L":
                    for f in range(fila - tamano, fila):
                        tablero[f][col] = "B"
            colocado=True


def colocarFlota(tablero):
    """Coloca varios barcos típicos en el tablero."""
    barcos = [5, 4, 3, 3, 2]  # tamaños clásicos
    for tam in barcos:
        colocarBarco(tablero, tam)


# ------------------------------------------------------------
#  Lógica del disparo
# ------------------------------------------------------------

def disparar(tablero, fila, col):
    """Procesa un disparo sobre el tablero."""
    celda = tablero[fila][col]

    match celda:
        case "~":
            tablero[fila][col] = "A"  # agua fallada
            return "agua"
        case "B":
            tablero[fila][col] = "X"  # barco tocado
            return "tocado"
        case "A" | "X":
            return "repetido"
        case _:
            return "error"


def quedanBarcos(tablero):
    """Devuelve True si todavía queda algún barco."""
    for fila in tablero:
        if "B" in fila:
            return True
    return False


# ------------------------------------------------------------
#  Bucle principal del juego
# ------------------------------------------------------------

def jugar():
    print("=== Hundir la Flota (versión imperativa) ===")

    tableroJugador = [
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
    tableroMaquina = crearTablero()

    colocarFlota(tableroMaquina)  # la máquina coloca barcos
    partidaTerminada = False
    while not partidaTerminada:
        print("\nTu tablero:")
        imprimirTablero(tableroJugador)

        print("\nTablero enemigo (oculto):")
        imprimirTablero(tableroMaquina, ocultarBarcos=True)

        # --- pedir coordenadas ---
        fila = int(input("Fila: "))
        col = int(input("Columna: "))

        resultado = disparar(tableroMaquina, fila, col)
        print("Resultado:", resultado)

        if not quedanBarcos(tableroMaquina):
            print("¡Has ganado!")
            partidaTerminada = True

        # Turno de la máquina
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        disparar(tableroJugador, fila, col)

        if not quedanBarcos(tableroJugador):
            print("La máquina ha ganado.")
            partidaTerminada = True


# ------------------------------------------------------------
#  Ejecución
# ------------------------------------------------------------

if __name__ == "__main__":
    jugar()
