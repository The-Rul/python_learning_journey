# ============================================================
# Tarea UD4 — Código Robusto y Testing
# ECP — Estructuras de Control en Python (5099)
#
# Instrucciones:
#   - Completar cada función donde pone "pass"
#   - Ejercicios 1 y 2: ejecutar este archivo y usar el menú
#   - Ejercicios 3 y 4: ejecutar con  pytest tarea_ud4.py -v
# ============================================================


# ------------------------------------------------------------
# Ejercicio 1: Leer números de un archivo
# ------------------------------------------------------------

def leer_numeros(ruta):
    """
    Lee un archivo que contiene un número por línea.
    Devuelve una lista con los números como float.
    Las líneas que no se puedan convertir a número se ignoran.
    Si el archivo no existe, devuelve una lista vacía.

    Ejemplo: leer_numeros("numeros.txt") → [10.0, 3.5, 7.0]
             leer_numeros("no_existe.txt") → []

    Ayuda: usar with para abrir, try/except ValueError para cada línea.
    """
    numeros = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    numero = float(linea)
                except ValueError:
                    continue
                numeros.append(numero)
    except FileNotFoundError:
        return []
    return numeros


# ------------------------------------------------------------
# Ejercicio 2: Copiar aprobados a otro archivo
# ------------------------------------------------------------

def copiar_aprobados(ruta_entrada, ruta_salida):
    """
    Lee un archivo con formato "nombre: nota" (una por línea).
    Escribe en otro archivo solo las líneas con nota >= 5.
    Devuelve el número de aprobados escritos.

    Si el archivo de entrada no existe, devuelve -1.
    Las líneas con formato incorrecto se ignoran.

    Ejemplo: copiar_aprobados("notas.txt", "aprobados.txt") → 2
             (escribe "Ana: 7.5" y "Marta: 9.0" en aprobados.txt)

    Ayuda: usar with para abrir ambos archivos.
           linea.strip().split(": ") separa nombre y nota.
           try/except para manejar líneas con formato incorrecto.
    """
    try:
        with open(ruta_entrada, "r", encoding="utf-8") as entrada:
            lineas = entrada.readlines()
    except FileNotFoundError:
        return -1

    aprobados = []
    for linea in lineas:
        try:
            nombre, nota_str = linea.strip().split(": ")
            nota = float(nota_str)
        except (ValueError, TypeError):
            continue
        if nota >= 5:
            aprobados.append(f"{nombre}: {nota}\n")

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        salida.writelines(aprobados)

    return len(aprobados)


# ------------------------------------------------------------
# Ejercicio 3: Implementar función para que pasen los tests
# ------------------------------------------------------------

def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento aplicado.
    - Si precio no es int ni float, lanza TypeError
    - Si porcentaje < 0 o porcentaje > 100, lanza ValueError
    - Devuelve el precio con el descuento aplicado, redondeado a 2 decimales

    Ejemplo: calcular_descuento(100, 20) → 80.0
             calcular_descuento(49.99, 10) → 44.99
    """
    if isinstance(precio, bool) or not isinstance(precio, (int, float)):
        raise TypeError("El precio debe ser un número")
    if isinstance(porcentaje, bool) or not isinstance(porcentaje, (int, float)):
        raise TypeError("El porcentaje debe ser un número")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    resultado = precio * (1 - porcentaje / 100)
    return round(resultado, 2)


def test_descuento_basico():
    assert calcular_descuento(100, 20) == 80.0

def test_descuento_con_decimales():
    assert calcular_descuento(49.99, 10) == 44.99

def test_descuento_cero():
    assert calcular_descuento(100, 0) == 100.0

def test_descuento_total():
    assert calcular_descuento(100, 100) == 0.0

def test_descuento_precio_invalido():
    import pytest
    with pytest.raises(TypeError):
        calcular_descuento("cien", 20)

def test_descuento_porcentaje_invalido():
    import pytest
    with pytest.raises(ValueError):
        calcular_descuento(100, 150)


# ------------------------------------------------------------
# Ejercicio 4: Escribir los tests
#
# La función es_aprobado ya está implementada.
# Escribir los tests indicados abajo para comprobar que funciona.
# Ejecutar con:  pytest tarea_ud4.py -v
# ------------------------------------------------------------

def es_aprobado(nota):
    """Devuelve True si la nota es >= 5, False en caso contrario.
    Si nota no es int ni float, lanza TypeError."""
    if not isinstance(nota, (int, float)):
        raise TypeError("La nota debe ser un número")
    return nota >= 5


# Escribir aquí los tests:
#
# test_aprobado_justo:    comprobar que es_aprobado(5) devuelve True
# test_suspenso:          comprobar que es_aprobado(4.9) devuelve False
# test_nota_maxima:       comprobar que es_aprobado(10) devuelve True
# test_tipo_invalido:     comprobar que es_aprobado("cinco") lanza TypeError
#                         (usar: import pytest / with pytest.raises(TypeError))

def test_aprobado_justo():
    assert es_aprobado(5) == True
def test_suspenso():
    assert es_aprobado(4.9) == False
def test_nota_maxima():
    assert es_aprobado(10) == True
def test_tipo_invalido():
    import pytest
    with pytest.raises(TypeError):
        es_aprobado("cinco")    


# ============================================================
# Menú de pruebas (Ejercicios 1-2)
# ============================================================

def probar(nombre, pruebas):
    print(f"\n  --- {nombre} ---")
    todo_ok = True
    for descripcion, fn, esperado in pruebas:
        try:
            resultado = fn()
            ok = resultado == esperado
            marca = "+" if ok else "X"
            print(f"  {marca} {descripcion}")
            if not ok:
                print(f"      Resultado:  {resultado!r}")
                print(f"      Esperado:   {esperado!r}")
                todo_ok = False
        except Exception as e:
            print(f"  X {descripcion}")
            print(f"      Error: {e}")
            todo_ok = False
    return todo_ok


def menu():
    import tempfile, os

    tmp_dir = tempfile.mkdtemp()

    archivo_numeros = os.path.join(tmp_dir, "numeros.txt")
    with open(archivo_numeros, "w") as f:
        f.write("10\nhola\n3.5\nabc\n7\n")

    archivo_notas = os.path.join(tmp_dir, "notas.txt")
    with open(archivo_notas, "w") as f:
        f.write("Ana: 7.5\nLuis: 3.2\nMarta: 9.0\nPedro: 4.8\n")

    ruta_inexistente = os.path.join(tmp_dir, "no_existe_xyz.txt")
    ruta_salida = os.path.join(tmp_dir, "salida.txt")

    ejercicios = {
        "1": ("leer_numeros", [
            ("leer_numeros (con datos)",
             lambda: leer_numeros(archivo_numeros), [10.0, 3.5, 7.0]),
            ("leer_numeros (no existe)",
             lambda: leer_numeros(ruta_inexistente), []),
        ]),
        "2": ("copiar_aprobados", [
            ("copiar_aprobados (con notas)",
             lambda: copiar_aprobados(archivo_notas, ruta_salida), 2),
            ("copiar_aprobados (no existe)",
             lambda: copiar_aprobados(ruta_inexistente, ruta_salida), -1),
        ]),
    }

    texto_menu = """
============================================================
  Tarea UD4 — Menu de pruebas
============================================================

  1. leer_numeros
  2. copiar_aprobados

  Ejercicios 3 y 4 (testing) se ejecutan con:
      pytest tarea_ud4.py -v

  T. Probar TODOS (Ej. 1-2)      0. Salir
"""

    while True:
        print(texto_menu)
        opcion = input("Elige una opcion: ").strip().upper()

        if opcion == "0":
            print("Hasta luego!")
            break
        elif opcion == "T":
            correctos = 0
            total = 0
            for clave in ["1", "2"]:
                nombre, pruebas = ejercicios[clave]
                total += 1
                if probar(f"Ejercicio {clave} - {nombre}", pruebas):
                    correctos += 1
            print(f"\n  Resultado: {correctos}/{total} ejercicios correctos")
        elif opcion.lower() in ejercicios:
            nombre, pruebas = ejercicios[opcion.lower()]
            probar(f"Ejercicio {opcion} - {nombre}", pruebas)
        else:
            print("Opcion no valida.")

        input("\nPulsa Enter para continuar...")


if __name__ == "__main__":
    menu()
