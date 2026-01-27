import time

# =============================================================================
# TAREA 2 - ESP / ECP
# Desarrollo de Aplicaciones con Lenguaje de Programación
# Unidad 2: Estructuras de datos complejas e iteración
# =============================================================================
# Nombre: Raúl
# Apellidos: Gómez Sanz
# Fecha: 26/02/2026
# =============================================================================

# -----------------------------------------------------------------------------
# EJERCICIO 1 - Gestión de lista de compras
# -----------------------------------------------------------------------------
# - Crea una lista vacía llamada 'lista_compras'.
# - Usa un bucle while para pedir productos al usuario hasta que escriba "fin".
# - Muestra la lista final y el número total de productos.
# - Usa los métodos append() y len().
#
# Ejemplo:
# Producto (o 'fin' para terminar): leche
# Producto (o 'fin' para terminar): pan
# Producto (o 'fin' para terminar): fin
# Lista de compras: ['leche', 'pan']
# Total de productos: 2
#''' -----------------------------------------------------------------------------

print("=" * 50)
print("EJERCICIO 1 - Lista de compras")
print("=" * 50)

# Tu código aquí:

lista_compras = []
producto = ""
while producto.lower() != "fin":
    producto = input("Producto (o 'fin' para terminar): ")
    if producto.lower() != "fin":
        lista_compras.append(producto)
print("Lista de compras:", lista_compras)
print("Total de productos:", len(lista_compras))



# -----------------------------------------------------------------------------
# EJERCICIO 2 - Análisis de temperaturas semanales
# -----------------------------------------------------------------------------
# - Dada la lista temperaturas = [22.5, 19.0, 25.3, 28.1, 24.0, 18.5, 21.0]
#   (temperaturas de lunes a domingo)
# - Calcula e imprime: temperatura máxima, mínima y promedio (2 decimales).
# - Cuenta cuántos días superaron los 23 grados (días calurosos).
# - Muestra qué días de la semana fueron calurosos.
# - Usa max(), min(), sum(), len() y un bucle for con enumerate().
#
# Ejemplo de salida:
# Temperatura máxima: 28.1 °C
# Temperatura mínima: 18.5 °C
# Promedio semanal: 22.63 °C
# Días calurosos (>23°C): 3
# Días calurosos: Miércoles, Jueves, Viernes
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 2 - Análisis de temperaturas semanales")
print("=" * 50)

temperaturas = [22.5, 19.0, 25.3, 28.1, 24.0, 18.5, 21.0]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Tu código aquí:

# Calculos temperaturas
temp_max = max(temperaturas)
temp_min = min(temperaturas)
temp_promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura máxima:{temp_max} ºC")
print(f"Temperatura mínima:{temp_min} ºC")
print(f"Promedio semanal:{temp_promedio:.2f} ºC")

# Dias calurosos 
dias_calurosos = []
for i, temperatura in enumerate(temperaturas):
    if temperatura > 23 :
        dias_calurosos.append(dias_semana[i])

##Imprimir resultados
print(f"Días calurosos (>23°C): {len(dias_calurosos)}")
print(f"Días calurosos: {dias_calurosos}")



# -----------------------------------------------------------------------------
# EJERCICIO 3 - Generador de serie numérica
# -----------------------------------------------------------------------------
# - Pide al usuario un número inicial, un número final y un incremento.
# - Usa un bucle for con range() para generar la serie.
# - Calcula y muestra la suma de todos los números de la serie.
# - Valida que el número inicial sea menor que el final.
#
# Ejemplo:
# Número inicial: 5
# Número final: 25
# Incremento: 5
#
# Serie generada: 5, 10, 15, 20
# Cantidad de números: 4
# Suma total: 50
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 3 - Generador de serie numérica")
print("=" * 50)

# Tu código aquí:

# Paso 1: Pedir datos al usuario validando inicial menor que final.
while True:
    num_inicial = int(input("Número inicial: "))
    num_final = int(input("Número final: "))
    incremento = int(input("Incremento: "))
    
    if num_inicial >= num_final:
        print("Error: El número inicial debe ser menor que el número final. Por favor, inténtalo de nuevo.")
    else:
        break
# Paso 2: Generar la serie y calcular la suma.
serie = [i for i in range(num_inicial, num_final, incremento)]

print()
print(f"Serie generada: {serie}")
print(f"Cantidad de numeros: {len(serie)}")
print(f"Suma total: {sum(serie)}")



# -----------------------------------------------------------------------------
# EJERCICIO 4 - Búsqueda en lista con while
# -----------------------------------------------------------------------------
# - Dada la lista ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
# - Pide una ciudad al usuario y busca si está en la lista usando un bucle while.
# - Si la encuentra, muestra su posición (índice) y usa break para salir.
# - Si no la encuentra, muestra un mensaje apropiado (usa else del bucle).
#
# Ejemplo 1:
# Ciudad a buscar: Valencia
# Valencia encontrada en la posición 2
#
# Ejemplo 2:
# Ciudad a buscar: Málaga
# Málaga no está en la lista
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 4 - Búsqueda en lista")
print("=" * 50)

ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]

# Tu código aquí:
busqueda = str(input("Ciudad a buscar: "))
indice = 0
# Búsqueda con while. Recoremos toda la lista y si encontramos la ciudad, con el indice la mostramos.
# Recordad aumentar el indice en cada iteración y salir. XXXXXXXXXXXXXX
while indice < len(ciudades):
    if ciudades[indice] == busqueda:
        print(f"{busqueda} encontrada en la posición {indice}")
        break
    indice += 1
else:
    print(f"{busqueda} no está en la lista")
        
            
            
            
# -----------------------------------------------------------------------------
# EJERCICIO 5 - Diccionario de películas favoritas
# -----------------------------------------------------------------------------
# - Crea un diccionario 'peliculas' donde cada clave es el título y el valor
#   es otro diccionario con 'año', 'genero' y 'valoracion' (del 1 al 10).
# - Añade al menos 4 películas iniciales.
# - Implementa las siguientes funciones:
#   - agregar_pelicula(titulo, año, genero, valoracion): añade una película.
#   - peliculas_por_genero(genero): devuelve lista de títulos de ese género.
#   - mejor_valorada(): devuelve el título de la película con mayor valoración.
# - Muestra el catálogo completo con un bucle for.
#
# Ejemplo:
# --- Catálogo de películas ---
# Inception (2010) - Ciencia ficción - 9/10
# El Padrino (1972) - Drama - 10/10
# Toy Story (1995) - Animación - 8/10
# Matrix (1999) - Ciencia ficción - 9/10
#
# Películas de Ciencia ficción: ['Inception', 'Matrix']
# Mejor valorada: El Padrino (10/10)
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 5 - Diccionario de películas")
print("=" * 50)

# Tu código aquí:

## Paso 1 : Generar diccionario y añadir peliculas.  
peliculas = {
    "Inception": {"año": 2010, "genero": "Ciencia ficción", "valoracion": 9},
    "El Padrino": {"año": 1972, "genero": "Drama", "valoracion": 10},
    "Toy Story": {"año": 1995, "genero": "Animación", "valoracion": 8},
    "Matrix": {"año": 1999, "genero": "Ciencia ficción", "valoracion": 9}
}

## Definir funciones

def agregar_pelicula(titulo, año, genero, valoracion):
    peliculas[titulo] = {"año": año, "genero": genero, "valoracion": valoracion}    

def peliculas_por_genero(genero):
    lista_titulos = []
    for titulo, detalles in peliculas.items():
        if detalles["genero"].lower() == genero.lower(): # Cambiamos a minusculas para evitar errores
            lista_titulos.append(titulo)
    return lista_titulos

def mejor_valorada():
    mejor_titulo = None
    mejor_valoracion = -1
    for titulo, detalles in peliculas.items():
        if detalles["valoracion"] > mejor_valoracion:
            mejor_valoracion = detalles["valoracion"]
            mejor_titulo = titulo
    return mejor_titulo

## Probamos las funciones
agregar_pelicula("peli1",2026,"invent", 5)
peliculas_ciencia_ficcion = peliculas_por_genero("Ciencia ficción")
mejor_pelicula = mejor_valorada()

## Imprimir catalogo peliculas
print("--- Catalogo de peliculas ---")
for pelicula in peliculas:
    año = peliculas[pelicula]["año"]
    genero = peliculas[pelicula]["genero"]
    valoracion = peliculas[pelicula]["valoracion"]  
    print(f"{pelicula}({año}) - {genero} - {valoracion}/10")

print()
print(f"Películas de Ciencia ficción: {peliculas_ciencia_ficcion}")
print(f"Mejor valorada: {mejor_pelicula} ({peliculas[mejor_pelicula]['valoracion']}/10)")




# -----------------------------------------------------------------------------
# EJERCICIO 6 - Análisis de ventas por categoría
# -----------------------------------------------------------------------------
# - Dada la siguiente lista de ventas (cada venta es una tupla):
#
# ventas = [
#     ("Electrónica", 450),
#     ("Ropa", 120),
#     ("Electrónica", 280),
#     ("Hogar", 95),
#     ("Ropa", 200),
#     ("Electrónica", 175),
#     ("Hogar", 310),
#     ("Ropa", 85)
# ]
#
# - Usa un diccionario para acumular el total de ventas por categoría.
# - Muestra el resumen de ventas por categoría.
# - Indica cuál es la categoría con mayores ventas totales.
# - Calcula el promedio de venta por transacción.
#
# Ejemplo de salida:
# Resumen de ventas por categoría:
# Electrónica: 905 €
# Ropa: 405 €
# Hogar: 405 €
#
# Categoría líder: Electrónica (905 €)
# Total de transacciones: 8
# Promedio por transacción: 213.75 €
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 6 - Análisis de ventas")
print("=" * 50)

ventas = [
    ("Electrónica", 450),
    ("Ropa", 120),
    ("Electrónica", 280),
    ("Hogar", 95),
    ("Ropa", 200),
    ("Electrónica", 175),
    ("Hogar", 310),
    ("Ropa", 85)
]

# Tu código aquí:

diccionario_ventas = {}
for venta in ventas:
    categoria = venta[0] # Miramos la categoria de la venta
    monto = venta[1] # Miramos el precio de la venta
    if categoria in diccionario_ventas: # Si la categoria ya existe, sumamos el monto
        diccionario_ventas[categoria] += monto
    else:                               # Si no existe la categoria, la creamos con el monto 
        diccionario_ventas[categoria] = monto

# Imprimir resumen de ventas por categoria
print("Resumen de ventas por categoría: \n")

for categoria, montos in diccionario_ventas.items():
    print(f"{categoria}: {montos} €")    
print()

# Categoria con mayores ventas totales
categoria_lider = max(diccionario_ventas, key = diccionario_ventas.get)
monto_maximo = diccionario_ventas[categoria_lider]
print(f"Categoria líder: {categoria_lider} ({monto_maximo} €)")

# Total de transacciones y promedio
print(f"Total de transacciones: {len(ventas)}")
#Calcular promedio
total_ventas = sum([venta[1] for venta in ventas]) # Sumatorio de todos los montos. Acceso en la tupla ventas
promedio = total_ventas / len(ventas)
print(f"Promedio por transaccion: {promedio:.2f} €")   

 

# -----------------------------------------------------------------------------
# EJERCICIO 7 - Comparador de listas de reproducción
# -----------------------------------------------------------------------------
# - Define dos conjuntos que representen canciones de dos playlists:
#
# playlist_rock = {"Bohemian Rhapsody", "Stairway to Heaven", "Hotel California",
#                  "Back in Black", "Sweet Child O Mine"}
# playlist_favoritos = {"Bohemian Rhapsody", "Billie Jean", "Hotel California",
#                       "Thriller", "Imagine"}
#
# - Calcula y muestra usando operadores de conjuntos (&, -, |, ^):
#   - Canciones que están en ambas playlists (intersección).
#   - Canciones exclusivas de Rock (diferencia).
#   - Canciones exclusivas de Favoritos (diferencia).
#   - Canciones en una u otra, pero no en ambas (diferencia simétrica).
#   - Total de canciones únicas en tu biblioteca (unión).
#
# Ejemplo:
# Canciones en común: {'Bohemian Rhapsody', 'Hotel California'}
# Solo en Rock: {'Stairway to Heaven', 'Back in Black', 'Sweet Child O Mine'}
# Solo en Favoritos: {'Billie Jean', 'Thriller', 'Imagine'}
# Total en biblioteca: 8 canciones únicas
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 7 - Comparador de playlists")
print("=" * 50)

playlist_rock = {"Bohemian Rhapsody", "Stairway to Heaven", "Hotel California",
                 "Back in Black", "Sweet Child O Mine"}
playlist_favoritos = {"Bohemian Rhapsody", "Billie Jean", "Hotel California",
                      "Thriller", "Imagine"}

# Tu código aquí:

## INTERSECCIÓN
interseccion = playlist_rock & playlist_favoritos
print(f"Canciones en común: {interseccion}")

## SOLO ROCK
solo_rock = playlist_rock - playlist_favoritos
print(f"Solo en Rock: {solo_rock}") 

## SOLO FAVORITOS
solo_favoritos = playlist_favoritos - playlist_rock
print(f"Solo en Favoritos: {solo_favoritos}")

## DIFERENCIA SIMÉTRICA
diferencia_simetrica = playlist_rock ^ playlist_favoritos
print(f"Diferencia simétrica: {diferencia_simetrica}")

## TOTAL CANCIONES ÚNICAS
total_canciones_unicas = len(playlist_rock | playlist_favoritos)
print(f"Total de canciones únicas: {total_canciones_unicas}")



# -----------------------------------------------------------------------------
# EJERCICIO 8 - Gestión de biblioteca con diccionarios anidados
# -----------------------------------------------------------------------------
# - Usa el siguiente diccionario de biblioteca:
#
# biblioteca = {
#     "978-0-13-468599-1": {"titulo": "Python Crash Course", "autor": "Eric Matthes",
#                          "año": 2019, "disponible": True},
#     "978-1-59327-584-6": {"titulo": "Automate the Boring Stuff", "autor": "Al Sweigart",
#                          "año": 2020, "disponible": False},
#     "978-0-596-51774-8": {"titulo": "Learning Python", "autor": "Mark Lutz",
#                          "año": 2013, "disponible": True},
#     "978-1-491-95036-8": {"titulo": "Fluent Python", "autor": "Luciano Ramalho",
#                          "año": 2022, "disponible": True}
# }
#
# - Implementa las funciones:
#   - libros_disponibles(): devuelve lista de títulos disponibles.
#   - buscar_por_autor(autor): devuelve lista de libros de ese autor.
#   - libro_mas_reciente(): devuelve tupla (ISBN, título, año) del más nuevo.
#   - prestar_libro(isbn): cambia disponible a False si está disponible.
# - Muestra los resultados de cada función.
#
# Ejemplo:
# Libros disponibles: ['Python Crash Course', 'Learning Python', 'Fluent Python']
# Libros de Mark Lutz: ['Learning Python']
# Libro más reciente: ('978-1-491-95036-8', 'Fluent Python', 2022)
#
# Prestando libro 978-0-13-468599-1...
# Préstamo realizado: Python Crash Course
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 8 - Gestión de biblioteca")
print("=" * 50)

biblioteca = {
    "978-0-13-468599-1": {"titulo": "Python Crash Course", "autor": "Eric Matthes",
                         "año": 2019, "disponible": True},
    "978-1-59327-584-6": {"titulo": "Automate the Boring Stuff", "autor": "Al Sweigart",
                         "año": 2020, "disponible": False},
    "978-0-596-51774-8": {"titulo": "Learning Python", "autor": "Mark Lutz",
                         "año": 2013, "disponible": True},
    "978-1-491-95036-8": {"titulo": "Fluent Python", "autor": "Luciano Ramalho",
                         "año": 2022, "disponible": True}
}

# Tu código aquí:

## LIBROS DISPONIBLES.
def libros_disponibles():
    disponibles = []
    for libro in biblioteca.values():
        if libro["disponible"]:
            disponibles.append(libro["titulo"])
    return disponibles

## BUSCAR POR AUTOR. 
def buscar_por_autor(autor):
    libros_autor = []
    for libro in biblioteca.values():
        if libro["autor"].lower() == autor.lower(): # Evitar errores de mayúsculas o minusculas
            libros_autor.append(libro["titulo"])
    return libros_autor

## LIBRO MÁS RECIENTE.
# Devuelve tupla (ISBN, título, año) del más nuevo.
def libro_mas_reciente():
    libro_reciente = None
    anyo_nuevo = 0
    for isbn, info in biblioteca.items():
        if info["año"] > anyo_nuevo: # Si el año del libro es mayor que el año nuevo
            anyo_nuevo = info["año"]
            libro_reciente = (isbn, info["titulo"], info["año"])  # Tupla con la info requerida (isbn, titulo, año )
    return libro_reciente

## PRESTAR LIBRO.
def prestar_libro(isbn):
    print(f"Prestando libro {isbn}...")
    time.sleep(1)  # Simular tiempo de procesamiento
    if isbn in biblioteca and biblioteca[isbn]["disponible"]:
        biblioteca[isbn]["disponible"] = False
        print(f"Préstamo realizado: {biblioteca[isbn]['titulo']}")
    else:
        print("El libro no está disponible.")
        
# Mostrar resultados de las funciones
print(f"Libros disponibles: {libros_disponibles()}")
print(f"Libros de Mark Lutz: {buscar_por_autor('Al Sweigart')}")
print(f"Libro más reciente: {libro_mas_reciente()}")
print()
prestar_libro("978-1-59327-584-6")  


# -----------------------------------------------------------------------------
# EJERCICIO 9 - Procesamiento de tuplas
# -----------------------------------------------------------------------------
# - Dada la lista de tuplas con datos de estudiantes:
#
# estudiantes = [
#     ("Ana", 20, 8.5),
#     ("Carlos", 22, 6.0),
#     ("María", 21, 9.2),
#     ("Juan", 23, 4.5),
#     ("Pedro", 20, 7.8)
# ]
#
# - Usa desempaquetado de tuplas en un bucle for para:
#   - Mostrar nombre y nota de cada estudiante.
#   - Calcular el promedio de notas.
#   - Crear una lista con los nombres de los aprobados (nota >= 5).
#   - Encontrar al estudiante con la nota más alta.
#
# Ejemplo:
# --- Listado de estudiantes ---
# Ana: 8.5
# Carlos: 6.0
# María: 9.2
# Juan: 4.5
# Pedro: 7.8
#
# Promedio de notas: 7.20
# Estudiantes aprobados: ['Ana', 'Carlos', 'María', 'Pedro']
# Mejor estudiante: María con 9.2
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 9 - Procesamiento de tuplas")
print("=" * 50)

estudiantes = [
    ("Ana", 20, 8.5),
    ("Carlos", 22, 6.0),
    ("María", 21, 9.2),
    ("Juan", 23, 4.5),
    ("Pedro", 20, 7.8)
]

# Tu código aquí:

# Mostrar nombre y nota de cada estudiante
print("--- Listado de estudiantes ---")
total_notas = 0
aprobados = []
mejor_nota = ("", 0)  # Tupla (nombre, nota)

for nombre, edad, nota in estudiantes:
    print(f"{nombre}: {nota}")
    total_notas += nota
    if nota >= 5:
        aprobados.append(nombre)
    if nota > mejor_nota[1]:
        mejor_nota = (nombre, nota) 

# Calcular promedio de notas
promedio_notas = total_notas / len(estudiantes)

# Imprimir los resultados
print()
print(f"Promedio de notas: {promedio_notas:.2f}")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Mejor estudiante: {mejor_nota[0]} con {mejor_nota[1]}")


# -----------------------------------------------------------------------------
# EJERCICIO 10 - Menú interactivo con todas las estructuras
# -----------------------------------------------------------------------------
# - Crea un programa con un menú que permita gestionar una lista de tareas:
#   1. Agregar tarea
#   2. Eliminar tarea
#   3. Marcar tarea como completada
#   4. Mostrar tareas pendientes
#   5. Mostrar tareas completadas
#   6. Salir
# - Usa un diccionario con dos claves: "pendientes" (lista) y "completadas" (lista).
# - El menú debe repetirse con un bucle while hasta que el usuario elija salir.
# - Valida las opciones del menú y muestra mensajes apropiados.
#
# Ejemplo:
# === GESTOR DE TAREAS ===
# 1. Agregar tarea
# 2. Eliminar tarea
# 3. Marcar como completada
# 4. Mostrar pendientes
# 5. Mostrar completadas
# 6. Salir
#
# Opción: 1
# Nueva tarea: Estudiar Python
# Tarea agregada correctamente
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("EJERCICIO 10 - Gestor de tareas")
print("=" * 50)

# Tu código aquí:

tareas = {
    "pendientes": [],
    "completadas": []
}

# FUNCIONES NECESARIAS
## Imprimir menú
def imprimir_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar como completada")
    print("4. Mostrar pendientes")
    print("5. Mostrar completadas")
    print("6. Salir")

## Agregar tarea
def agregar_tarea(tarea):
    tareas["pendientes"].append(tarea)
    print("Tarea agregada correctamente.")  
    
## Eliminar tarea
def eliminar_tarea(indice_tarea):
        indice = int(indice_tarea) - 1 ## Ajustar indice para la lista que empieza en 0. Y parsear a entero
        if 0 <= indice < len(tareas["pendientes"]):
            tarea = tareas["pendientes"].pop(indice)
            print(f"Tarea '{tarea}' eliminada correctamente.")
        else:
            print("Índice no válido.")

## Marcar tarea como completada
def marcar_como_completada(indice_tarea):
        indice = int(indice_tarea) - 1
        if 0 <= indice < len(tareas["pendientes"]):
            tarea = tareas["pendientes"].pop(indice)
            tareas["completadas"].append(tarea)
            print(f"Tarea '{tarea}' marcada como completada.")
        else:
            print("Índice no válido.")


## Mostrar tareas pendientes para poder elegirla. 
def mostrar_pendientes():
    print("__Tareas pendientes:__")
    for i, tarea in enumerate(tareas["pendientes"], 1):
        print(f"{i}. {tarea}")

## Mostrar tareas completadas con numero para poder elegirla 
def mostrar_completadas():
    print("__Tareas completadas:__")
    for i, tarea in enumerate(tareas["completadas"], 1):
        print(f"{i}. {tarea}")

##### PROGRAMA PRINCIPAL #####
while True: 
    imprimir_menu()
    print()
    opcion = input("Opción (1-6): ")
    print()
    
    match opcion:
        case "1":
            nueva_tarea = input("Nueva tarea: ")
            agregar_tarea(nueva_tarea)
        case "2":
            mostrar_pendientes()
            tarea_eliminar = input("¿Qué tarea quieres eliminar (número)?: ")
            eliminar_tarea(tarea_eliminar)
        case "3":
            mostrar_pendientes()
            tarea_completar = input("¿Qué tarea quieres marcar como completada? (elige numero): ")
            marcar_como_completada(tarea_completar)
        case "4":
            mostrar_pendientes()
        case "5":
            mostrar_completadas()
        case "6":
            print("Saliendo del gestor de tareas...")
            time.sleep(1)
            break
        case _:
            print("No valido. Elegir opción entre 1 y 6.")

# =============================================================================
# FIN DE LA TAREA 2
# =============================================================================
print("\n" + "=" * 50)
print("FIN DE LA TAREA 2")
print("=" * 50)
