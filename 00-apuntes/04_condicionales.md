# 04 - Condicionales - Tomar Decisiones

## ¿Qué son los condicionales?

Los condicionales permiten que el programa tome **diferentes caminos** según las condiciones que establezcas.

## Estructura if / else

### Sintaxis básica

```python
if condición:
    # Código que se ejecuta si la condición es True
else:
    # Código que se ejecuta si la condición es False
```

### Ejemplo simple

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### Con input()

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### IMPORTANTE: La indentación

La **indentación** (espacios al inicio) es **obligatoria** en Python:

```python
# CORRECTO
if edad >= 18:
    print("Mayor de edad")  # 4 espacios (o 1 tab)
    print("Puedes votar")

# ERROR
if edad >= 18:
print("Mayor de edad")  # Sin espacios → ERROR!
```

## Múltiples condiciones: if / elif / else

Cuando tienes más de dos opciones:

```python
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

- `if`: primera condición
- `elif`: condiciones adicionales (else if)
- `else`: si ninguna condición anterior fue True

### Con input()

```python
nota = float(input("Introduce tu nota (0-10): "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

## Operadores de comparación

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual que | `5 == 5` | True |
| `!=` | Diferente de | `5 != 3` | True |
| `>` | Mayor que | `5 > 3` | True |
| `<` | Menor que | `5 < 3` | False |
| `>=` | Mayor o igual | `5 >= 5` | True |
| `<=` | Menor o igual | `5 <= 3` | False |

### Ejemplos

```python
x = 10
y = 5

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= 10) # True
print(y <= 5)  # True
```

### Cuidado: = vs ==

```python
# = es asignación (dar valor)
edad = 18

# == es comparación (comprobar igualdad)
if edad == 18:
    print("Tienes 18 años")
```

## Operadores lógicos

Permiten combinar varias condiciones:

### AND (y)

**Ambas** condiciones deben ser True:

```python
edad = int(input("¿Cuántos años tienes? "))
tiene_carnet = input("¿Tienes carnet? (si/no): ").lower()

if edad >= 18 and tiene_carnet == "si":
    print("Puedes conducir")
else:
    print("No puedes conducir")
```

| Condición 1 | Condición 2 | Resultado |
|------------|-------------|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR (o)

**Al menos una** condición debe ser True:

```python
dia = input("¿Qué día es hoy? ").lower()

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana!")
else:
    print("Es día laboral")
```

| Condición 1 | Condición 2 | Resultado |
|------------|-------------|-----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT (no)

Invierte el valor (True → False, False → True):

```python
llueve = input("¿Está lloviendo? (si/no): ").lower() == "si"

if not llueve:
    print("Puedes salir sin paraguas")
else:
    print("Lleva paraguas")
```

## Combinar operadores

```python
temperatura = float(input("Temperatura actual: "))
hace_sol = input("¿Hace sol? (si/no): ").lower() == "si"

if temperatura > 20 and hace_sol:
    print("Buen día para la playa")
elif temperatura > 20 and not hace_sol:
    print("Está caluroso pero nublado")
else:
    print("Hace frío")
```

## Condicionales con strings

```python
color = input("¿Cuál es tu color favorito? ").lower()

if color == "rojo":
    print("El rojo es un color intenso")
elif color == "azul":
    print("El azul es relajante")
elif color == "verde":
    print("El verde es natural")
else:
    print(f"El {color} también es bonito")
```

## Condicionales anidados

Puedes poner un `if` dentro de otro:

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    tiene_entrada = input("¿Tienes entrada? (si/no): ").lower()
    if tiene_entrada == "si":
        print("Puedes entrar")
    else:
        print("Necesitas una entrada")
else:
    print("Eres menor de edad, no puedes entrar")
```

---

## Ejercicios

### Ejercicio 1: Detector de par o impar con input()

Pide un número al usuario.
Si es par (resto al dividir por 2 es 0), muestra "Es par".
Si no, muestra "Es impar".

**Pista:** Usa el operador `%` (módulo)

---

### Ejercicio 2: Mayor de edad con input()

Pide la edad al usuario.
Si tiene 18 o más, muestra "Eres mayor de edad".
Si no, muestra "Eres menor de edad".

---

### Ejercicio 3: Clasificador de notas con input()

Pide una nota (0-10) al usuario.
Clasifícala según:
- 9-10: Sobresaliente
- 7-8: Notable
- 5-6: Aprobado
- 0-4: Suspenso

---

### Ejercicio 4: Control de acceso al concierto con input()

Pide al usuario:
- Su edad
- Si tiene entrada (si/no)

Puede entrar si tiene 18 o más años **Y** tiene entrada.
Muestra "Puedes entrar" o "No puedes entrar" según corresponda.

---

### Ejercicio 5: Descuento en tienda con input()

Pide el precio de un producto.
Si el precio es mayor a 100 euros, aplica 20% de descuento.
Si no, no hay descuento.
Muestra el precio final.

---

### Ejercicio 6: Día de la semana con input()

Pide al usuario un día de la semana.
Si es "sábado" o "domingo", muestra "Es fin de semana".
Si no, muestra "Es día laboral".

**Pista:** Usa `.lower()` y `or`

---

### Ejercicio 7: Verificador de contraseña con input()

Pide una contraseña al usuario.
La contraseña correcta es "python2024".
Si la contraseña es correcta, muestra "Acceso permitido".
Si no, muestra "Contraseña incorrecta".

---

### Ejercicio 8: Calculadora con operación con input()

Pide al usuario:
- Un número
- Una operación (+, -, *, /)
- Otro número

Realiza la operación correspondiente y muestra el resultado.

**Pista:** Usa if/elif para cada operación

---

### Ejercicio 9: Clasificador de temperatura con input()

Pide la temperatura actual.
Clasifícala según:
- Menos de 10: "Hace frío"
- 10-20: "Temperatura agradable"
- 21-30: "Hace calor"
- Más de 30: "Hace mucho calor"

---

### Ejercicio 10: Decisión de salir con input()

Pide al usuario:
- Si está lloviendo (si/no)
- Temperatura actual

Decide:
- Si llueve: "Lleva paraguas"
- Si no llueve y temperatura > 25: "Hace buen tiempo para salir"
- Si no llueve y temperatura <= 25: "Hace fresco, lleva chaqueta"

---

## Tips

- La **indentación** es obligatoria (usa 4 espacios o 1 tab)
- Usa `==` para comparar, no `=`
- Para comparar strings ignorando mayúsculas: `.lower()`
- `and` requiere que **ambas** condiciones sean True
- `or` requiere que **al menos una** condición sea True
- Usa `.lower()` en inputs para aceptar "SI", "Si", "si", etc.

## Errores comunes

```python
# ERROR 1: Usar = en vez de ==
if edad = 18:  # ERROR!
if edad == 18: # CORRECTO

# ERROR 2: Olvidar los dos puntos :
if edad >= 18  # ERROR!
if edad >= 18: # CORRECTO

# ERROR 3: Sin indentación
if edad >= 18:
print("Mayor")  # ERROR!

if edad >= 18:
    print("Mayor")  # CORRECTO
```

## Resumen

```python
# Estructura básica
if condición:
    # código si True
else:
    # código si False

# Múltiples condiciones
if condición1:
    # código
elif condición2:
    # código
else:
    # código

# Operadores de comparación: ==, !=, >, <, >=, <=
# Operadores lógicos: and, or, not
```
