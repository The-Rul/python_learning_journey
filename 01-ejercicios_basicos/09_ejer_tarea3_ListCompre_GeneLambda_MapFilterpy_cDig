# ============================================================
# Tarea UD3 — Programación Avanzada
# ECP — Estructuras de Control en Python (5099)
#
# Resultados de aprendizaje evaluados:
#   RA1 — Identifica estructuras de control en Python (50%)
#   RA3 — Utiliza sentencias iterativas (50%)
#   RA4 — Aplica funciones de Python (50%)
#
# Instrucciones:
#   - Completar cada función donde pone "pass"
#   - Ejecutar el archivo y elegir la función a probar en el menú
# ============================================================


# ------------------------------------------------------------
# BLOQUE 1: List Comprehensions (repaso)
# ------------------------------------------------------------

def celsius_a_fahrenheit(temperaturas):
    """
    Recibe una lista de temperaturas en Celsius.
    Devuelve una lista con las temperaturas convertidas a Fahrenheit.
    Fórmula: F = C * 9/5 + 32

    Ejemplo: [0, 100] → [32.0, 212.0]

    Ayuda: usar list comprehension → [expresión for variable in lista]
    """
    return [i * 9/5 + 32 for i in temperaturas ]


def palabras_cortas(frase, max_longitud):
    """
    Recibe una frase (string) y una longitud máxima.
    Devuelve una lista con las palabras cuya longitud sea <= max_longitud,
    convertidas a minúsculas.

    Ejemplo: "Hola Mundo De Python", 4 → ['hola', 'de']

    Ayuda: usar list comprehension con filtro → [expresión for variable in lista if condición]
           .split() separa una frase en palabras. .lower() convierte a minúsculas.
    """
    return [palabra.lower() for palabra in frase.split() if len(palabra) <= max_longitud]


def cuadrados_pares(n):
    """
    Recibe un entero n.
    Devuelve una lista con los cuadrados de los números pares del 1 a n.

    Ejemplo: cuadrados_pares(8) → [4, 16, 36, 64]

    Ayuda: usar list comprehension con filtro → [expresión for variable in range(...) if condición]
           Un número es par si número % 2 == 0.
    """
    return [i ** 2 for i in range(1, n + 1) if i % 2 == 0] # Atento al range, siempre empieza en 0 si piden 1 sumar 1 a n


# ------------------------------------------------------------
# BLOQUE 2: Generadores
# ------------------------------------------------------------

def multiplos(n, cantidad):
    """
    Función generadora que produce los primeros 'cantidad' múltiplos de n
    (empezando por n).

    Ejemplo: multiplos(3, 4) → 3, 6, 9, 12

    Ayuda: usar yield dentro de un bucle for.
           yield produce un valor y "pausa" la función hasta que se pida el siguiente.
    """
    for i in range(1, cantidad + 1 ):
        yield i * n

def suma_cuadrados_gen(n):
    """
    Calcula la suma de los cuadrados del 1 a n usando un generador.
    No crear una lista intermedia.

    Ejemplo: suma_cuadrados_gen(3) → 1 + 4 + 9 = 14

    Ayuda: usar sum() con expresión generadora → sum(expresión for variable in range(...))
    """

    return (sum(x ** 2 for x in range(1, n + 1 )))


# ------------------------------------------------------------
# BLOQUE 3: Lambda, map, filter
# ------------------------------------------------------------

def aplicar_descuento(precios, porcentaje):
    """
    Recibe una lista de precios y un porcentaje de descuento.
    Devuelve una lista con los precios rebajados, redondeados a 2 decimales.
    Usar map() con lambda.

    Ejemplo: [100, 50], 10 → [90.0, 45.0]

    Ayuda: list(map(lambda variable: transformación, lista))
           round(número, 2) redondea a 2 decimales.
    """
    return list(map(lambda precio: round(precio * (1 - porcentaje / 100), 2), precios))

def filtrar_positivos(numeros):
    """
    Recibe una lista de números.
    Devuelve una lista solo con los positivos (> 0).
    Usar filter() con lambda.

    Ejemplo: [3, -1, 0, 5, -2] → [3, 5]

    Ayuda: list(filter(lambda variable: condición, lista))
    """
    return list(filter(lambda x : x > 0, numeros))


# ------------------------------------------------------------
# BLOQUE 4: Recursión
# ------------------------------------------------------------

def factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    El factorial de 0 es 1.
    El factorial de n es n * factorial(n - 1).

    Ejemplo: factorial(5) → 120

    Ayuda: una función recursiva se llama a sí misma.
           Necesita un caso base (if) que detenga la recursión
           y un caso recursivo que llame a la función con un argumento más pequeño.
    """
    if n == 0:
        return 1
    return n * (factorial(n-1))


def suma_lista(numeros):
    """
    Calcula la suma de una lista de números de forma recursiva.
    Si la lista está vacía, devuelve 0.
    Si no, devuelve el primer elemento + la suma del resto.

    Ejemplo: suma_lista([1, 2, 3, 4]) → 10

    Ayuda: lista[0] devuelve el primer elemento.
           lista[1:] devuelve la lista sin el primer elemento.
           Caso base: lista vacía → 0.
           Caso recursivo: primer elemento + suma_lista(resto).
    """
    if len(numeros) == 0:
        return 0 
    return numeros[0] + suma_lista(numeros[1:])


# ------------------------------------------------------------
# BLOQUE 5: Integración
# ------------------------------------------------------------

def procesar_notas(notas_str):
    """
    Recibe una lista de notas como strings (ej: ["7.5", "3.2", "9.0"]).
    Devuelve una lista con las notas aprobadas (>= 5) como enteros redondeados.
    Usar cualquier combinación de técnicas: comprehensions, map, filter, generadores.

    Ejemplo: ["7.5", "3.2", "9.0", "4.8"] → [8, 9]

    Ayuda: float("7.5") convierte el string a número decimal.
           round() redondea al entero más cercano.
    """
    #return list(filter(round(float(lambda nota : nota >= 5, notas_str))))
    
    #return [round(float(nota),1) if nota >= 5 else for nota in notas_str]
    
    #return list(filter(lambda nota: float(nota) >= 5, notas_str ))
    return [round(float(nota)) for nota in notas_str if float(nota) >= 5]
# ============================================================
# Menú de pruebas
# ============================================================

def probar(nombre, pruebas):
    """Ejecuta una lista de (llamada, esperado) y muestra resultados."""
    print(f"\n  --- {nombre} ---")
    todo_ok = True
    for descripcion, fn, esperado in pruebas:
        try:
            resultado = fn()
            ok = resultado == esperado
            marca = "✓" if ok else "✗"
            print(f"  {marca} {descripcion}")
            if not ok:
                print(f"      Resultado:  {resultado!r}")
                print(f"      Esperado:   {esperado!r}")
                todo_ok = False
        except Exception as e:
            print(f"  ✗ {descripcion}")
            print(f"      Error: {e}")
            todo_ok = False
    return todo_ok


def menu():
    ejercicios = {
        "1": ("celsius_a_fahrenheit", [
            ("celsius_a_fahrenheit([0, 100])",       lambda: celsius_a_fahrenheit([0, 100]),       [32.0, 212.0]),
            ("celsius_a_fahrenheit([20, 25, 30])",   lambda: celsius_a_fahrenheit([20, 25, 30]),   [68.0, 77.0, 86.0]),
            ("celsius_a_fahrenheit([])",              lambda: celsius_a_fahrenheit([]),              []),
        ]),
        "2": ("palabras_cortas", [
            ('palabras_cortas("Hola Mundo De Python", 4)', lambda: palabras_cortas("Hola Mundo De Python", 4), ["hola", "de"]),
            ('palabras_cortas("a bb ccc dddd", 2)',         lambda: palabras_cortas("a bb ccc dddd", 2),         ["a", "bb"]),
            ('palabras_cortas("", 5)',                      lambda: palabras_cortas("", 5),                      []),
        ]),
        "3": ("cuadrados_pares", [
            ("cuadrados_pares(8)",  lambda: cuadrados_pares(8),  [4, 16, 36, 64]),
            ("cuadrados_pares(5)",  lambda: cuadrados_pares(5),  [4, 16]),
            ("cuadrados_pares(1)",  lambda: cuadrados_pares(1),  []),
        ]),
        "4": ("multiplos", [
            ("list(multiplos(3, 4))",  lambda: list(multiplos(3, 4)),  [3, 6, 9, 12]),
            ("list(multiplos(5, 3))",  lambda: list(multiplos(5, 3)),  [5, 10, 15]),
            ("list(multiplos(1, 0))",  lambda: list(multiplos(1, 0)),  []),
        ]),
        "5": ("suma_cuadrados_gen", [
            ("suma_cuadrados_gen(3)",   lambda: suma_cuadrados_gen(3),   14),
            ("suma_cuadrados_gen(5)",   lambda: suma_cuadrados_gen(5),   55),
            ("suma_cuadrados_gen(10)",  lambda: suma_cuadrados_gen(10),  385),
        ]),
        "6": ("aplicar_descuento", [
            ("aplicar_descuento([100, 50], 10)",       lambda: aplicar_descuento([100, 50], 10),       [90.0, 45.0]),
            ("aplicar_descuento([29.99, 15.50], 20)",  lambda: aplicar_descuento([29.99, 15.50], 20),  [23.99, 12.4]),
            ("aplicar_descuento([], 50)",              lambda: aplicar_descuento([], 50),              []),
        ]),
        "7": ("filtrar_positivos", [
            ("filtrar_positivos([3, -1, 0, 5, -2])",  lambda: filtrar_positivos([3, -1, 0, 5, -2]),  [3, 5]),
            ("filtrar_positivos([-1, -2, -3])",        lambda: filtrar_positivos([-1, -2, -3]),        []),
            ("filtrar_positivos([1, 2, 3])",           lambda: filtrar_positivos([1, 2, 3]),           [1, 2, 3]),
        ]),
        "8": ("factorial", [
            ("factorial(0)",   lambda: factorial(0),   1),
            ("factorial(1)",   lambda: factorial(1),   1),
            ("factorial(5)",   lambda: factorial(5),   120),
            ("factorial(10)",  lambda: factorial(10),  3628800),
        ]),
        "9": ("suma_lista", [
            ("suma_lista([])",           lambda: suma_lista([]),           0),
            ("suma_lista([5])",          lambda: suma_lista([5]),          5),
            ("suma_lista([1, 2, 3, 4])", lambda: suma_lista([1, 2, 3, 4]), 10),
            ("suma_lista([10, -3, 7])",  lambda: suma_lista([10, -3, 7]),  14),
        ]),
        "10": ("procesar_notas", [
            ('procesar_notas(["7.5", "3.2", "9.0", "4.8"])',  lambda: procesar_notas(["7.5", "3.2", "9.0", "4.8"]),  [8, 9]),
            ('procesar_notas(["3.0", "4.0"])',                  lambda: procesar_notas(["3.0", "4.0"]),                  []),
            ('procesar_notas(["5.0", "10.0"])',                 lambda: procesar_notas(["5.0", "10.0"]),                 [5, 10]),
        ]),
    }

    texto_menu = """
============================================================
  Tarea UD3 — Menú de pruebas
============================================================

  1. celsius_a_fahrenheit       6. aplicar_descuento
  2. palabras_cortas            7. filtrar_positivos
  3. cuadrados_pares            8. factorial
  4. multiplos                  9. suma_lista
  5. suma_cuadrados_gen        10. procesar_notas

  T. Probar TODOS               0. Salir
"""

    while True:
        print(texto_menu)
        opcion = input("Elige una opción: ").strip().upper()

        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion == "T":
            correctos = 0
            for clave in sorted(ejercicios, key=lambda x: int(x)):
                nombre, pruebas = ejercicios[clave]
                if probar(f"Ejercicio {clave} · {nombre}", pruebas):
                    correctos += 1
            print(f"\n  Resultado: {correctos}/{len(ejercicios)} ejercicios correctos")
        elif opcion in ejercicios:
            nombre, pruebas = ejercicios[opcion]
            probar(f"Ejercicio {opcion} · {nombre}", pruebas)
        else:
            print("Opción no válida.")

        input("\nPulsa Enter para continuar...")


if __name__ == "__main__":
    menu()
