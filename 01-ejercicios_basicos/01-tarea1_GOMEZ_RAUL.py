"""
Tarea integrada ESP + ECP
Completa los ejercicios en este archivo. Cada bloque incluye el enunciado.
"""
""""""

# ============================================================================
# Ejercicio 1: Precio final con descuento
# - Pide al usuario el precio base y un porcentaje de descuento.
# - Si el precio base es mayor que 100, aplica el descuento; si no, deja el precio igual.
# - Muestra el subtotal, el descuento aplicado (en euros) y el total final.
# ===========================================================================
print("=" * 60)    
print("--- Ejercicio 1: Precio final con descuento ---")
print("=" * 60)    


# Paso 1: Pedimos los datos al usuario e inicializamos variables
precio_base = float(input("Introduzca el precio base: "))
descuento = float(input("Introduzca el descuento a aplicar: "))
descuento_aplicado = 0
precio_final = precio_base

# PASO 2: Comprobamos la condición de aplicación del descuento (>100).
if precio_base > 100:
    descuento_aplicado = precio_base * (descuento / 100)
    precio_final -= descuento_aplicado
else:
    descuento = 0
    
# PASO 3: Se imprime el ticket por consola.  
print("-" * 60)    
print(f"Precio base: {precio_base} €")
print(f"Descuento: {descuento} %")
print(f"Subtotal: {precio_base} €")
print(f"Descuento aplicado: {precio_base-precio_final} €")
print(f"Precio final: {precio_final} €")



# ============================================================================
# Ejercicio 2: Conversor de temperatura
# - Pregunta al usuario si quiere convertir de Celsius a Fahrenheit o al revés.
# - Según la opción elegida, pide la temperatura y realiza la conversión.
# - Muestra el resultado con dos decimales.
# ============================================================================
print("=" * 60)    
print("--- Ejercicio 2: Conversor de temperatura ---")
print("=" * 60)    
# PASO 1: Se piden accion y datos al usuario. 
print("Bienvenido al conversor de temperatura.")
print("1 - De Celsius a Fahrenheit")
print("2 - De Fahrenheit a Celsius")
print("0 - Salir del programa")
print("-" * 60)    
# PASO 2: Segun lo elegido (con match), realizamos una conversión u otra. 

while True:
    # Pedimos la opción una sola vez y validamos el valor
    try:
        opcion = int(input("¿Que te gustaria convertir? \n "))
    except ValueError: #excepcion incorporada en Python para chequear que lo introducido es numero
        print("Opción no válida. Introduzca un numero valido")
        continue

    match opcion:
        case 1:
            try:
                celsius = float(input("Introduce la temperatura en grados Celsius: "))
            except ValueError:
                print("Temperatura inválida. Introduce un número.")
                continue
            fahrenheit = (celsius * 9/5) + 32 #Aplicamos formula de conversion 
            print(f"{celsius:.2f} °C son {fahrenheit:.2f} °F")
        case 2:
            try:
                fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            except ValueError:
                print("Temperatura inválida. Introduce un número.")
                continue
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f} °F son {celsius:.2f} °C")
        case 0:
            print("Saliendo del programa...")
            break # Sale del blucel
        case _:
            print("Opción no válida. Por favor, elige 1, 2 o 0.")
print("-" * 60 )      
# ============================================================================
# Ejercicio 3: Calculadora básica con funciones
# - Define funciones sumar(a, b), restar(a, b), multiplicar(a, b) y dividir(a, b).
# - Valida la división entre cero antes de llamar a dividir.
# - Pide dos números al usuario y muestra cada operación usando f-strings.
# ============================================================================
print()
print("=" * 60)    
print("--- Ejercicio 3: Calculadora ---")
print("=" * 60) 

# PASO 1 : Definir las funciones básicas para operar 
#Funciones introduciendo dos parametros y devolviendo resultado. 

def sumar(a, b):
    resultado = a + b
    return resultado
def restar(a, b):
    resultado = a - b
    return resultado
def multiplicar(a, b):
    resultado = a * b
    return resultado
def dividir(a, b):
    if b == 0:
        print("Error al dividir por 0.")
    else:
        resultado = a / b
        return resultado

# PASO 2: Pedir dos numeros. 
print("Bienvenido a la CALCULADORA divertida.")
print("Introduce dos numeros a calcular:")
a = float(input())
b = float(input())

#PASO 3 : Pintar los resultados por pantalla con f string
print("-" * 60)
print("RESULTADOS: ") 
print(f"Suma: {sumar(a,b):.2f} \nResta: {restar(a,b):.2f} \nMultiplicacion: {multiplicar(a,b):.2f} \nDivision: {dividir(a,b):.2f}")

print("_" * 60 )      


# ============================================================================
# Ejercicio 4: Mayoría de edad
# - Crea una función es_mayor_edad(edad) que devuelva True si edad >= 18.
# - Pide la edad al usuario, llama a la función y muestra un mensaje acorde.
# ============================================================================
print()
print("=" * 60)    
print("--- Ejercicio 4: Mayoría de edad  ---")
print("=" * 60) 

#PASO 1 : Funcion chequeo edad

def comprabar_edad(edad):
    #Cambio desde el futuro la comparación devuelve un bool podría cambiarlo a return edad>=18
    if edad >= 18:
        return True
    return False 

#PASO 2 : Aplicacion funcion y pintar por pantalla
edad = int(input("¿Que edad tienes?"))

#No existe el operador ternario como tal pero si una alternativa en Python. 
print ("Eres mayor de edad." if comprabar_edad(edad) else "Eres menor de edad.")

print("_" * 60 )      

# ============================================================================
# Ejercicio 5: Detector de vocales
# - Crea una función es_vocal(letra) que devuelva True si letra es a/e/i/o/u.
# - Pide una letra, normalízala con .lower() y muestra si es vocal o no.
# ============================================================================
print()
print("=" * 60)    
print("--- Ejercicio 5: Detector de vocales  ---")
print("=" * 60) 
#PASO 1 : Funcion chequeo vocal
def es_vocal(letra):
    vocales = 'aeiou'
    if letra in vocales and len(letra) == 1:
        return True
    return False

#PASO 2 : Pedir letra al usuario y aplicar funcion
letra = str(input("Introduce una letra: "))
if es_vocal(letra.lower()):
    print(f"La letra '{letra}' es una vocal.")
else:
    print("La letra NO es una vaocal.")
print("_" * 60 )      
# ============================================================================
# Ejercicio 6: Analizador de texto básico
# - Pide una frase (asegúrate de que no esté vacía).
# - Cuenta cuántas vocales, consonantes y palabras tiene (puedes crear funciones).
# - Muestra un resumen con esos datos.
# ============================================================================

print()
print("=" * 60)    
print("--- Ejercicio 6: Analizador de texto básico  ---")
print("=" * 60) 

# PASO 1: Funciones para contar vocales, consonantes y palabras
# Se usa la funcion es_vocal del ejercicio anterior
'''
Recorremos todas las letras de la frase chequeando si es vocal. 
'''
def contar_vocales(frase):
    contador = 0
    for char in frase:
        if es_vocal(char.lower()):
            contador += 1
    return contador
'''
Al principio pense en usar "es_vocal" pero en false. Pero puede haber simbolos, lo que no es vocal no tiene por que ser consonante

'''
def es_consonantes(consonante):
    letras = 'bcdfghjklmnpqrstvwxyz'
    if consonante in letras and len(consonante) == 1:
        return True
    return False
'''
Recorremos todas las letras de la frase chequeando si es consonante. 
La funcion exige que pasar la letra en minuscula
'''
def contar_consonantes(frase):
    contador = 0
    for char in frase:
        if es_consonantes(char.lower()):
            contador += 1
    return contador
'''
Para contar plabras usamos el metodo split que devuelve una lista con las palabras separadas por espacios. 
Devolvemos la longitud de esa lista.
'''
def contar_palabras(frase):
    palabras = frase.strip().split()
    return len(palabras)

# PASO 2: Pedir una frase asegurarse de que no esté vacía
frase = ""
# .strip() eliminamos espacios en blanco al inicio y al final si esta vacia el string sera nulo y
# y se repettira el while hasta introducir algo valido
while not frase.strip():  
    frase = input("Introduce una frase: ")
    frase.strip() #Procuramos que no tenga espacios al inicio ni al final.

print("-" * 60)
# PASO 3: Pintamos los resultados del conteo. 
print("Resultados del analisis de texto: ")
print(f"Vocales: {contar_vocales(frase)}")  
print(f"Consontantes: {contar_consonantes(frase)}")  
print(f"Palabras: {contar_palabras(frase)}")  

print("_" *60 )

# ============================================================================
# Ejercicio 7: Par o impar y múltiplo de 3
# - Pide un número entero.
# - Indica si es par o impar.
# - Indica si además es múltiplo de 3.
# ============================================================================

print()
print("=" * 60)    
print("--- Ejercicio 7: Par o impar y múltiplo de 3  ---")
print("=" * 60)
# PASO 1: Pedir un numero entero al usuario
numero = int(input("Introduce un número entero: "))
# PASO 2: Comprobar si es par o impar
print(f"El número {numero} es PAR."if numero % 2 == 0 else f"El número {numero} es IMPAR.")
# PASO 3: Comprobar si es multiplo de 3
print(f"El número {numero} es MÚLTIPLO DE 3."if numero % 3 == 0 else f"El número {numero} NO es MÚLTIPLO DE 3.")    
print("_" *60 )

# ============================================================================
# Ejercicio 8: Clasificador de notas
# - Pide una nota entre 0 y 10.
# - Valida el rango y muestra: Sobresaliente, Notable, Aprobado o Suspenso.
# ============================================================================
print()
print("=" * 60)
print("--- Ejercicio 8: Clasificador de notas  ---")
print("=" * 60)
# PASO 1: Pedir una nota entre 0 y 10
while True:
    try:
        nota = float(input("Introduce una nota entre 0 y 10: "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida. Debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")
# PASO 2: Clasificar la nota
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
print("_" *60 )


# ============================================================================
# Ejercicio 9: Calculadora de IMC
# - Pide peso (kg) y altura (m).
# - Calcula el IMC y determina la categoría (bajo peso, normal, sobrepeso, obesidad).
# ============================================================================
print()
print("=" * 60)
print("--- Ejercicio 9: Calculadora de IMC  ---")
print("=" * 60)
# PASO 1: Pedir peso y altura al usuario
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
# PASO 2: Calcular el IMC
imc = peso / (altura ** 2)
# PASO 3: Determinar la categoría del IMC.
# Las categorias las he sacado de internet
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"
# PASO 4: Mostrar el resultado
print(f"IMD:{imc:.2f} -> {categoria}.")
print("_" *60 )

# ============================================================================
# Ejercicio 10: Control de acceso
# - Pide edad, si tiene entrada (si/no) y si es VIP (si/no).
# - Decide si puede entrar (edad >= 18 y tiene entrada) o (es VIP).
# - Muestra un mensaje explicando la razón.
# ============================================================================
print()
print("=" * 60)
print("--- Ejercicio 10: Control de acceso  ---")
print("=" * 60)
# PASO 1: Pedir datos al usuario
edad = int(input("Introduce tu edad: "))
tiene_entrada = input("¿Tienes entrada? (si/no): ").strip().lower()
es_vip = input("¿Eres VIP? (si/no): ").strip().lower()

# PASO 2: Decidir si puede entrar
puede_entrar = edad > 18 and (tiene_entrada == 'si' or es_vip == 'si')

# PASO 3: Mostrar el mensaje correspondiente
if edad >= 18:
    if tiene_entrada == "si":
        print("Puedes entrar: Eres mayor de edad y tienes entrada.")
    elif es_vip == "si":  
        print("Puedes entrar: Eres mayor de edad y eres VIP.")
    else:
        print("No puedes entrar: Eres mayor de edad pero no tienes entrada ni eres VIP.")
else:
    if es_vip == "si":
        print("Puedes entrar: Aun siendo menor, eres VIP.")
    else:
        print("No puedes entrar: Eres menor de edad. No importa si tienes entrada o no.")  

print("_" *60 )
print("_" *60 )
