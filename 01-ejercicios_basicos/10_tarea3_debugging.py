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
#         if nota >= 5: # Error: if nota > 5
#             contador += 1 
#     return contador

# notas = [5, 7, 4, 10, 6, 3, 8, 5, 2, 9]
# print(f"Aprobados: {contar_aprobados(notas)}")
# # Esperado: 7 | Obtenido: 5

# # BUG: Un 5 es aprobado pero el codigo solo recoge los mayores de 5 excluyendo los iguales a 5 
# # FIX: Añadir '=' en la linea 'if nota >= 5'


# --- A2: Media de una lista ---
# def calcular_media(numeros):
#     """Calcula la media aritmética de una lista de números."""
#     suma = 0
#     for i in range(len(numeros)):
#         suma += datos[i] # Error: suma += i
#     return suma / len(numeros)

# datos = [10, 20, 30, 40, 50]
# print(f"Media: {calcular_media(datos)}")
# # Esperado: 30.0 | Obtenido: 2.0

# # BUG: Estamos sumando el indice del bucle ('i') no el contenido del la lista en ese indice datos[i]
# # FIX: En la variable suma, sumar el contenido del array 'datos' en la posiciíon 'i'.


# --- A3: Encontrar el máximo ---
# def encontrar_maximo(numeros):
#     """Encuentra el número más grande de una lista."""
#     maximo = temperaturas[0] # Error: maximo = 0
#     for num in numeros:
#         if num > maximo: 
#             maximo = num
#     return maximo

# temperaturas = [-5, -12, -3, -8, -1]
# print(f"Temperatura máxima: {encontrar_maximo(temperaturas)}")
# Esperado: -1 | Obtenido: 0

# # BUG: La variable máximo se inicializa en 0 y todas las temperaturas de la lista son negativas. 0 siempre sera la máxima. 
# # FIX: Inicializar con la primera del array: `temperaturas[0]`


# --- A4: Buscar elemento ---
# def buscar(lista, objetivo):
#     """Devuelve True si el objetivo está en la lista, False si no."""
#     for elemento in lista:
#         if elemento == objetivo:
#             return True
#     else: # Error: 'else' dentro del bucle
#         return False

# print(buscar([3, 7, 1, 9, 4], 9))
# # Esperado: True | Obtenido: False

# # BUG: Solo revisa el 3, devuelve False y termina el bucle. No llega a revisar el resto de números 
# # FIX: Sacar el else fuera del bucle. Si el bucle no encuentra el objetivo devolvera false. 


# --- A5: Segundo mayor ---
# def segundo_mayor(numeros):
#     """Devuelve el segundo número más grande de la lista."""
#     mayor = min(numeros) #Error
#     segundo = min(numeros) #Error
#     for num in numeros:
#         if num > mayor:
#             segundo = mayor
#             mayor = num
#         elif num > segundo: # Añadido 
#             segundo = num
#     return segundo

# print(segundo_mayor([3, 7, 1, 9, 4]))
# print(segundo_mayor([9, 7, 1, 3, 4]))

# Esperado: 7 | Obtenido: 7 , 9
# Probar también con [9, 7, 1, 3, 4]

# # BUG: Aunque para el primer test funciona bien, en el segundo test, donde el primer número con el que se
# # inicializan las variables es a su vez el máximo, da error porque ningún otro número cumplirá la
# # condición de ser mayor y por tanto no entrará en la lógica de ordenación.
# # FIX: Inicializar las variables con el elemento mínimo de la lista. Añadir un 'elif' para comprobar
# # también la variable segundo y actualizarlo. Si el número no es mayor que mayor, pero sí mayor que segundo.

# --- A6: Capitalizar palabras ---
# def capitalizar_palabras(frase):
#     """Pone en mayúscula la primera letra de cada palabra."""
#     palabras = frase.split()
#     resultado = []
#     for palabra in palabras:
# #        palabra.capitalize() # Error. Capitaliza pero no guarda. 
#         resultado.append(palabra.capitalize()) 
#     return " ".join(resultado)

# print(capitalizar_palabras("hola mundo cruel"))
# # # Esperado: "Hola Mundo Cruel" | Obtenido: "hola mundo cruel"

# # BUG: Al emplear '.capitalize()' no guardamos el resultado ni modificamos la palabra. Por tanto al 
# # al realizar append lo suqe estamos guardando es la palabra original. 
# # FIX: Realizar el .capitalize() dentro del append()


# --- A7: Fibonacci ---
# def fibonacci(n):
#     """Devuelve una lista con los primeros n números de Fibonacci."""
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     fib = [0, 1]
#     for i in range(1, n-1): # Error: for i in range(2, n)
#         siguiente = fib[i] + fib[i - 1]
#         fib.append(siguiente)
#     return fib

# print(fibonacci(8))
# # Esperado: [0, 1, 1, 2, 3, 5, 8, 13] | Obtenido: IndexError: list index out of range

# # BUG: Lanza un error 'list index out of range'. El bucle,(line 140), comienza en 2 cuando
# # solamente hay dos elementos, por tanto el máximo índice es 1. 
# # FIX: Modificar el range() en el que se realiza el bucle. Si queremos que empieze  
# # en el segundo elemento empezaremos por 1, y como ya tenemos el primer de la serie, el 0, solamente
# # se necesitan 7 más (n-1).


# --- A8: Eliminar por valor ---
# def eliminar_todos(lista, valor):
#     """Elimina todas las apariciones de valor en la lista."""
#     lista_nueva = []
#     for elemento in lista:
#         if elemento != valor:
#             lista_nueva.append(elemento)
#     return lista_nueva

# print(eliminar_todos([1, 2, 3, 2, 4, 2, 5], 2))
# print(eliminar_todos([1, 2, 2, 4, 2, 5], 2))

# # Esperado: [1, 3, 4, 5] | Obtenido: [1, 3, 4, 5] | [1, 4, 2, 5]

# # BUG: Si los elementos a eliminar están consecutivos (ej. [1, 2, 2, 3]), el remove() 
# # modifica la lista mientras se itera, causando que el bucle se salte elementos. 
# # FIX: Se crea una nueva lista donde añadirmos solo los elementos distintos de objetivo. De esta 
# # manera evitamos modificar la lista original y saltarnos elementos. 


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
#         nota = 10.0
#     return round(nota,2) # Error int(nota)

# # Prueba 1:
# print(calcular_nota_final(8, 7, 6))
# # Esperado: 6.75 | Obtenido: 6

# # Prueba 2:
# print(calcular_nota_final(10, 10, 10))
# # Esperado: 10.0 | Obtenido: 10

# # Prueba 3:
# print(calcular_nota_final(9, 8, 3))
# # Esperado: 3 | Obtenido: 3

# # BUG: No muestra los decimales porque lo parseamos a entero 'int()' al devolver el valor  
# # FIX: Mantenerlo en float y redondear a dos decimales. En el caso de ser 10 añadir un decimal
# # 10.0  


# --- B2: Cifrado César (2 bugs) ---
# def cifrar_cesar(texto, desplazamiento):
#     """Cifra un texto desplazando cada letra N posiciones en el alfabeto."""
#     resultado = ""
#     for letra in texto:
#         if letra.isalpha():
#             base = ord('a') if letra.islower() else ord('A')
#             codigo = (ord(letra) - base + desplazamiento) % 26 + base
#             resultado += chr(codigo)
#         else:
#             resultado += letra
#     return resultado

# def descifrar_cesar(texto_cifrado, desplazamiento):
#     """Descifra un texto cifrado con César."""
#     return cifrar_cesar(texto_cifrado, -desplazamiento)

# original = "hola mundo"
# original = "xyz"
# cifrado = cifrar_cesar(original, 3)
# descifrado = descifrar_cesar(cifrado, 3)
# print(f"Original:    {original}")
# print(f"Cifrado:     {cifrado}")
# print(f"Descifrado:  {descifrado}")
# # Esperado: descifrado == original | Obtenido = 'nurg s{tju'
# # Probar también con "xyz" y desplazamiento 3

# # BUG 1 : La función descifrar_cesar usa el mismo desplazamiento en lugar de restarlo. 
# # FIX 1: Cambiar el signo al aplicar cifrar_cesar(-desplazamiento) dentro de descigrar_csar

# # BUG 1 : No se controla el “wrap-around” del alfabeto (por ejemplo, después de z debería volver a a).
# # FIX 1: Aplicar módulo 26 para mantener las letras dentro del rango alfabético.



# ============================================================
# BLOQUE C — Lee el traceback
# Ejecutar cada programa, leer el error y responder como
# comentario debajo de cada ejercicio:
#   1. ¿Qué tipo de error se produce?
#   2. ¿En qué línea?
#   3. ¿Por qué?
#   4. ¿Cómo se corrige?
# ============================================================


# # --- C1: Saludar ---
# def saludar(nombre, edad):
#     print("Hola, " + nombre + ". Tienes " + str(edad) + " años.")

# saludar("Ana" ,12)

# #   1. NameError
# #   2. Linea 259
# #   3. La variable 'edad' no esta definida. No se crea en ningún momento. 
# #   4. Incluir la variable 'edad' en los parametros de la funcion e incluir un valor compatible al llamar a "Saludar". 
# #   Parsear la edad a string al concatenar el texto. 


# # --- C2: Notas ---
# notas = [7, 8, 5, 9]
# for i in range(len(notas)):
#     print(f"Nota {i}: {notas[i]}")

# 1. IndexError: list index out of range
# 2. Linea 272
# 3. El bucle se realiza de 1 a 5, pero la lista tiene 4 elementos (índices 0 a 3). Cuando i=4, 
#    intenta acceder a notas[4] que no existe.
# 4. Cambiar range(1, 5) a range(len(notas)). Para iterar sobre indices existentes.


# --- C3: Descuento ---
# def calcular_descuento(precio, porcentaje):
#     return precio - precio * porcentaje / 100

# precios = ["29.99", "15.50", "42.00"]
# total = 0
# for precio in precios:
#     total += calcular_descuento(float(precio), 10)
# print(total)

# 1. TypeError: unsupported operand type(s) for /: 'str' and 'int'
# 2. Linea 288
# 3. Se esta intentando dividir string por entero. Los precios estan definidos como strings (line 286)
# 4. Parsear a float antes de llamar a calcula_descuento


# --- C4: Longitud media ---
# def longitud_media(palabras):
#     total = 0
#     for palabra in palabras:
#         total += len(palabra)
#     if len(palabras) == 0: # Añadido para evitar división por cero
#         print("La lista esta vacía. No se puede calcular la media")
#         return 0
#     else:
#         return total / len(palabras)

# print(longitud_media([]))

# 1. ZeroDivisionError: division by zero
# 2. Linea 303
# 3. La lista de palabras esta vacia, su longitud es 0. Al intentar dividir el total por la 
#    longitud de la lista, se produce una división por cero.
# 4. Añadir una condición para comprobar si la lista esta vacia antes de realizar la división. 
# Si esta vacia, devolver 0 o un mensaje indicando que no se pueden calcular la longitud media.