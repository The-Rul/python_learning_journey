# ============================================
# EJERCICIOS DE PYTHON - CONCEPTOS BÁSICOS
# ============================================
# Completa el código donde veas "# TU CÓDIGO AQUÍ"

print("=" * 60)
print("EJERCICIOS DE PYTHON - CONCEPTOS BÁSICOS")
print("=" * 60)
"""
# ============================================
# CAPÍTULO 1: VARIABLES Y TIPOS DE DATOS
# ============================================

print("\n" + "=" * 60)
print("CAPÍTULO 1: VARIABLES Y TIPOS DE DATOS")
print("=" * 60)

# --- Ejercicio 1.1: Tus datos personales ---
print("\n--- Ejercicio 1.1: Tus datos personales ---")
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en metros? "))
es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == "si"

# TU CÓDIGO AQUÍ: Imprime cada dato con su tipo usando type()
# Ejemplo: print(f"Nombre: {nombre} (tipo: {type(nombre)})")
print("=" * 60)
print(f"Nombre:{nombre} (tipo:{type(nombre)})")
print(f"Edad:{edad} (tipo:{type(edad)})")
print(f"Altura:{altura} (tipo:{type(altura)})")
print(f"¿Es estudiante?:{es_estudiante} (tipo:{type(es_estudiante)})")
print("=" * 60)


# --- Ejercicio 1.2: Área de un rectángulo ---
print("\n--- Ejercicio 1.2: Área de un rectángulo ---")
base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))

# TU CÓDIGO AQUÍ: Calcula el área e imprímela
print("=" * 60)
print(f"El area del rectangulo es: {(base*altura)}")
print("=" * 60)

# --- Ejercicio 1.3: Información de un producto ---
print("\n--- Ejercicio 1.3: Información de un producto ---")
nombre_producto = input("Nombre del producto: ")
precio = float(input("Precio en euros: "))
stock = int(input("Cantidad en stock: "))
en_oferta = input("¿Está en oferta? (si/no): ").lower() == "si"

# TU CÓDIGO AQUÍ: Imprime toda la información del producto
print(f"{nombre_producto} tiene un precio de {precio}€ hay {stock} ud en stock. \n {en_oferta})} esta en oferta. ")

"""
# --- Ejercicio 1.4: Acumulador de puntos ---
print("\n--- Ejercicio 1.4: Acumulador de puntos ---")
puntos = 0
print(f"Puntos iniciales: {puntos}")

ronda1 = int(input("Puntos ganados en ronda 1: "))
# TU CÓDIGO AQUÍ: Suma ronda1 a puntos y muestra el total
puntos += ronda1
print(f"Puntos al final ronda 1: {puntos}")

ronda2 = int(input("Puntos ganados en ronda 2: "))
# TU CÓDIGO AQUÍ: Suma ronda2 a puntos y muestra el total
puntos += ronda2
print(f"Puntos al final ronda 2: {puntos}")

ronda3 = int(input("Puntos ganados en ronda 3: "))
# TU CÓDIGO AQUÍ: Suma ronda3 a puntos y muestra el total final
puntos += ronda3
print(f"Puntos al final ronda 3: {puntos}")


# --- Ejercicio 1.5: Perímetro de un cuadrado ---
print("\n--- Ejercicio 1.5: Perímetro de un cuadrado ---")
lado = float(input("Lado del cuadrado: "))

# TU CÓDIGO AQUÍ: Calcula el perímetro (lado * 4) e imprímelo


# ============================================
# CAPÍTULO 2: OPERACIONES MATEMÁTICAS
# ============================================

print("\n" + "=" * 60)
print("CAPÍTULO 2: OPERACIONES MATEMÁTICAS")
print("=" * 60)

# --- Ejercicio 2.1: Calculadora básica ---
print("\n--- Ejercicio 2.1: Calculadora básica ---")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

# TU CÓDIGO AQUÍ: Calcula e imprime suma, resta, multiplicación y división




# --- Ejercicio 2.2: Calculadora de propina ---
print("\n--- Ejercicio 2.2: Calculadora de propina ---")
cuenta = float(input("Total de la cuenta: "))
porcentaje = float(input("Porcentaje de propina: "))

# TU CÓDIGO AQUÍ: Calcula la propina y el total a pagar



# --- Ejercicio 2.3: Conversor de temperatura ---
print("\n--- Ejercicio 2.3: Conversor de temperatura ---")
celsius = float(input("Temperatura en Celsius: "))

# TU CÓDIGO AQUÍ: Convierte a Fahrenheit: (celsius * 9/5) + 32


# --- Ejercicio 2.4: Área y perímetro de un círculo ---
print("\n--- Ejercicio 2.4: Área y perímetro de un círculo ---")
radio = float(input("Radio del círculo: "))
pi = 3.14159

# TU CÓDIGO AQUÍ: Calcula área (pi * radio²) y perímetro (2 * pi * radio)



# --- Ejercicio 2.5: Repartir en partes iguales ---
print("\n--- Ejercicio 2.5: Repartir en partes iguales ---")
caramelos = int(input("Cantidad total de caramelos: "))
amigos = int(input("Número de amigos: "))

# TU CÓDIGO AQUÍ: Calcula cuántos recibe cada uno (//) y cuántos sobran (%)



# --- Ejercicio 2.6: Calculadora de potencias ---
print("\n--- Ejercicio 2.6: Calculadora de potencias ---")
base = float(input("Número base: "))
exponente = float(input("Exponente: "))

# TU CÓDIGO AQUÍ: Calcula base elevado a exponente (**)


# --- Ejercicio 2.7: Precio con IVA ---
print("\n--- Ejercicio 2.7: Precio con IVA ---")
precio_sin_iva = float(input("Precio del producto (sin IVA): "))

# TU CÓDIGO AQUÍ: Calcula precio con IVA (21%): precio * 1.21


# --- Ejercicio 2.8: Contador con operadores compuestos ---
print("\n--- Ejercicio 2.8: Contador con operadores compuestos ---")
puntos = 0
print(f"Puntos iniciales: {puntos}")

ronda1 = int(input("¿Puntos ganados en ronda 1? "))
# TU CÓDIGO AQUÍ: Usa += para sumar ronda1 a puntos

ronda2 = int(input("¿Puntos ganados en ronda 2? "))
# TU CÓDIGO AQUÍ: Usa += para sumar ronda2 a puntos

ronda3 = int(input("¿Puntos ganados en ronda 3? "))
# TU CÓDIGO AQUÍ: Usa += para sumar ronda3 a puntos y muestra total


# ============================================
# CAPÍTULO 3: STRINGS Y TEXTO
# ============================================

print("\n" + "=" * 60)
print("CAPÍTULO 3: STRINGS Y TEXTO")
print("=" * 60)

# --- Ejercicio 3.1: Presentación personalizada ---
print("\n--- Ejercicio 3.1: Presentación personalizada ---")
nombre = input("¿Cómo te llamas? ")
ciudad = input("¿De qué ciudad eres? ")
edad = input("¿Cuántos años tienes? ")

# TU CÓDIGO AQUÍ: Crea un mensaje con f-string y muéstralo


# --- Ejercicio 3.2: Manipular texto ---
print("\n--- Ejercicio 3.2: Manipular texto ---")
frase = input("Escribe una frase: ")

# TU CÓDIGO AQUÍ: Muestra la frase en mayúsculas, su longitud y con guiones bajos



# --- Ejercicio 3.3: Información de película ---
print("\n--- Ejercicio 3.3: Información de película ---")
titulo = input("Título de la película: ")
año = input("Año de estreno: ")
puntuacion = input("Puntuación (0-10): ")

# TU CÓDIGO AQUÍ: Crea un mensaje formateado con f-string


# --- Ejercicio 3.4: Formatear nombre ---
print("\n--- Ejercicio 3.4: Formatear nombre ---")
nombre_completo = input("Escribe tu nombre completo: ")

# TU CÓDIGO AQUÍ: Usa .title() para formatear el nombre


# --- Ejercicio 3.5: Creador de email ---
print("\n--- Ejercicio 3.5: Creador de email ---")
nombre = input("Tu nombre: ")
apellido = input("Tu apellido: ")
dominio = input("Dominio del email (ej: gmail.com): ")

# TU CÓDIGO AQUÍ: Crea el email: nombre.apellido@dominio (todo en minúsculas)


# --- Ejercicio 3.6: Búsqueda en texto ---
print("\n--- Ejercicio 3.6: Búsqueda en texto ---")
frase = input("Escribe una frase: ")
palabra = input("Palabra a buscar: ")

# TU CÓDIGO AQUÍ: Comprueba si palabra está en frase (usa 'in')


# --- Ejercicio 3.7: Contador de vocales ---
print("\n--- Ejercicio 3.7: Contador de vocales ---")
palabra = input("Escribe una palabra: ")

# TU CÓDIGO AQUÍ: Cuenta cuántas veces aparece 'a' (usa .count())


# ============================================
# CAPÍTULO 4: CONDICIONALES
# ============================================

print("\n" + "=" * 60)
print("CAPÍTULO 4: CONDICIONALES")
print("=" * 60)

# --- Ejercicio 4.1: Par o impar ---
print("\n--- Ejercicio 4.1: Par o impar ---")
numero = int(input("Introduce un número: "))

# TU CÓDIGO AQUÍ: Usa if/else y % para determinar si es par o impar


# --- Ejercicio 4.2: Mayor de edad ---
print("\n--- Ejercicio 4.2: Mayor de edad ---")
edad = int(input("¿Cuántos años tienes? "))

# TU CÓDIGO AQUÍ: Comprueba si es mayor de edad (>= 18)


# --- Ejercicio 4.3: Clasificador de notas ---
print("\n--- Ejercicio 4.3: Clasificador de notas ---")
nota = float(input("Introduce tu nota (0-10): "))

# TU CÓDIGO AQUÍ: Usa if/elif/else para clasificar la nota
# 9-10: Sobresaliente, 7-8: Notable, 5-6: Aprobado, 0-4: Suspenso




# --- Ejercicio 4.4: Control de acceso ---
print("\n--- Ejercicio 4.4: Control de acceso ---")
edad = int(input("¿Cuántos años tienes? "))
tiene_entrada = input("¿Tienes entrada? (si/no): ").lower()

# TU CÓDIGO AQUÍ: Puede entrar si edad >= 18 AND tiene_entrada == "si"


# --- Ejercicio 4.5: Descuento en tienda ---
print("\n--- Ejercicio 4.5: Descuento en tienda ---")
precio = float(input("Precio del producto: "))

# TU CÓDIGO AQUÍ: Si precio > 100, aplica 20% descuento



# --- Ejercicio 4.6: Día de la semana ---
print("\n--- Ejercicio 4.6: Día de la semana ---")
dia = input("¿Qué día es hoy? ").lower()

# TU CÓDIGO AQUÍ: Si es sábado o domingo, es fin de semana


# --- Ejercicio 4.7: Verificador de contraseña ---
print("\n--- Ejercicio 4.7: Verificador de contraseña ---")
contraseña = input("Introduce la contraseña: ")

# TU CÓDIGO AQUÍ: La contraseña correcta es "python2024"


# --- Ejercicio 4.8: Calculadora con operación ---
print("\n--- Ejercicio 4.8: Calculadora con operación ---")
num1 = float(input("Primer número: "))
operacion = input("Operación (+, -, *, /): ")
num2 = float(input("Segundo número: "))

# TU CÓDIGO AQUÍ: Usa if/elif para cada operación




# --- Ejercicio 4.9: Clasificador de temperatura ---
print("\n--- Ejercicio 4.9: Clasificador de temperatura ---")
temperatura = float(input("Temperatura actual: "))

# TU CÓDIGO AQUÍ: <10: frío, 10-20: agradable, 21-30: calor, >30: mucho calor




# --- Ejercicio 4.10: Decisión de salir ---
print("\n--- Ejercicio 4.10: Decisión de salir ---")
llueve = input("¿Está lloviendo? (si/no): ").lower()
temperatura = float(input("Temperatura actual: "))

# TU CÓDIGO AQUÍ: Decide según lluvia y temperatura




print("\n" + "=" * 60)
print("¡EJERCICIOS COMPLETADOS!")
print("=" * 60)
