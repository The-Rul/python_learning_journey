# ============================================================
# Tarea — Debugging con VSCode
# ESP — Entornos y Sintaxis en Python (5098)
# UD3 — Entornos y Control de Versiones
#
# Instrucciones:
#   - Cada programa tiene uno o más bugs
#   - Usar el debugger de VSCode para localizar cada bug
#   - Corregir el código directamente en este archivo
#   - Añadir un comentario junto a cada corrección explicando:
#     el resultado esperado vs el obtenido, y la causa del bug
#   - Descomentar cada ejercicio de uno en uno para trabajar
# ============================================================


# ============================================================
# BLOQUE A — Encuentra el bug con el debugger
# Cada programa tiene UN error lógico (se ejecuta sin
# excepciones pero da un resultado incorrecto)
# ============================================================


# --- A1: Contar aprobados ---
# def contar_aprobados(notas):
#     """Cuenta cuántas notas son 5 o más."""
#     contador = 0
#     for nota in notas:
#         if nota > 5:
#             contador += 1
#     return contador

# notas = [5, 7, 4, 10, 6, 3, 8, 5, 2, 9]
# print(f"Aprobados: {contar_aprobados(notas)}")
# # Esperado: 7 | Obtenido: ???


# --- A2: Media de una lista ---
# def calcular_media(numeros):
#     """Calcula la media aritmética de una lista de números."""
#     suma = 0
#     for i in range(len(numeros)):
#         suma += i
#     return suma / len(numeros)
#
# datos = [10, 20, 30, 40, 50]
# print(f"Media: {calcular_media(datos)}")
# # Esperado: 30.0 | Obtenido: ???


# --- A3: Encontrar el máximo ---
# def encontrar_maximo(numeros):
#     """Encuentra el número más grande de una lista."""
#     maximo = 0
#     for num in numeros:
#         if num > maximo:
#             maximo = num
#     return maximo
#
# temperaturas = [-5, -12, -3, -8, -1]
# print(f"Temperatura máxima: {encontrar_maximo(temperaturas)}")
# # Esperado: -1 | Obtenido: ???


# --- A4: Buscar elemento ---
# def buscar(lista, objetivo):
#     """Devuelve True si el objetivo está en la lista, False si no."""
#     for elemento in lista:
#         if elemento == objetivo:
#             return True
#         else:
#             return False
#
# print(buscar([3, 7, 1, 9, 4], 9))
# # Esperado: True | Obtenido: ???


# --- A5: Segundo mayor ---
# def segundo_mayor(numeros):
#     """Devuelve el segundo número más grande de la lista."""
#     mayor = numeros[0]
#     segundo = numeros[0]
#     for num in numeros:
#         if num > mayor:
#             segundo = mayor
#             mayor = num
#     return segundo
#
# print(segundo_mayor([3, 7, 1, 9, 4]))
# # Esperado: 7 | Obtenido: ???
# # Probar también con [9, 7, 1, 3, 4]


# --- A6: Capitalizar palabras ---
# def capitalizar_palabras(frase):
#     """Pone en mayúscula la primera letra de cada palabra."""
#     palabras = frase.split()
#     resultado = []
#     for palabra in palabras:
#         palabra.capitalize()
#         resultado.append(palabra)
#     return " ".join(resultado)
#
# print(capitalizar_palabras("hola mundo cruel"))
# # Esperado: "Hola Mundo Cruel" | Obtenido: ???


# --- A7: Fibonacci ---
# def fibonacci(n):
#     """Devuelve una lista con los primeros n números de Fibonacci."""
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     fib = [0, 1]
#     for i in range(2, n):
#         siguiente = fib[i] + fib[i - 1]
#         fib.append(siguiente)
#     return fib
#
# print(fibonacci(8))
# # Esperado: [0, 1, 1, 2, 3, 5, 8, 13] | Obtenido: ???


# --- A8: Eliminar por valor ---
# def eliminar_todos(lista, valor):
#     """Elimina todas las apariciones de valor en la lista."""
#     for elemento in lista:
#         if elemento == valor:
#             lista.remove(elemento)
#     return lista
#
# print(eliminar_todos([1, 2, 3, 2, 4, 2, 5], 2))
# # Esperado: [1, 3, 4, 5] | Obtenido: ???


# ============================================================
# BLOQUE B — Debugging avanzado
# Programas con MÁS DE UN BUG o bugs más sutiles
# ============================================================


# --- B1: Calculadora de notas (2 bugs) ---
# def calcular_nota_final(parcial1, parcial2, examen):
#     """
#     Nota final = parcial1 * 25% + parcial2 * 25% + examen * 50%
#     Solo si examen >= 4. Si no, la nota final es la del examen.
#     """
#     if examen < 4:
#         return examen
#     nota = parcial1 * 0.25 + parcial2 * 0.25 + examen * 0.50
#     if nota >= 10:
#         nota = 10
#     return int(nota)
#
# # Prueba 1:
# print(calcular_nota_final(8, 7, 6))
# # Esperado: 6.75 | Obtenido: ???
#
# # Prueba 2:
# print(calcular_nota_final(10, 10, 10))
# # Esperado: 10.0 | Obtenido: ???
#
# # Prueba 3:
# print(calcular_nota_final(9, 8, 3))
# # Esperado: 3 | Obtenido: ???


# --- B2: Cifrado César (2 bugs) ---
# def cifrar_cesar(texto, desplazamiento):
#     """Cifra un texto desplazando cada letra N posiciones en el alfabeto."""
#     resultado = ""
#     for letra in texto:
#         if letra.isalpha():
#             codigo = ord(letra) + desplazamiento
#             resultado += chr(codigo)
#         else:
#             resultado += letra
#     return resultado
#
# def descifrar_cesar(texto_cifrado, desplazamiento):
#     """Descifra un texto cifrado con César."""
#     return cifrar_cesar(texto_cifrado, desplazamiento)
#
# original = "hola mundo"
# cifrado = cifrar_cesar(original, 3)
# descifrado = descifrar_cesar(cifrado, 3)
# print(f"Original:    {original}")
# print(f"Cifrado:     {cifrado}")
# print(f"Descifrado:  {descifrado}")
# # Esperado: descifrado == original
# # Probar también con "xyz" y desplazamiento 3


# ============================================================
# BLOQUE C — Lee el traceback
# Ejecutar cada programa, leer el error y responder como
# comentario debajo de cada ejercicio:
#   1. ¿Qué tipo de error se produce?
#   2. ¿En qué línea?
#   3. ¿Por qué?
#   4. ¿Cómo se corrige?
# ============================================================


# --- C1: Saludar ---
# def saludar(nombre):
#     print("Hola, " + nombre + ". Tienes " + edad + " años.")
#
# saludar("Ana")


# --- C2: Notas ---
# notas = [7, 8, 5, 9]
# for i in range(1, 5):
#     print(f"Nota {i}: {notas[i]}")


# --- C3: Descuento ---
# def calcular_descuento(precio, porcentaje):
#     return precio - precio * porcentaje / 100
#
# precios = ["29.99", "15.50", "42.00"]
# total = 0
# for precio in precios:
#     total += calcular_descuento(precio, 10)
# print(total)


# --- C4: Longitud media ---
# def longitud_media(palabras):
#     total = 0
#     for palabra in palabras:
#         total += len(palabra)
#     return total / len(palabras)
#
# print(longitud_media([]))
