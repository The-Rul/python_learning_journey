# UD2.1: Listas y Bucles

**Módulo:** Desarrollo de Aplicaciones con Lenguaje de Programación (DALP)  
**Primera parte:** Estructuras de datos básicas e iteración

## Índice de contenidos

1. Introducción a las estructuras de datos
   - 1.1. ¿Qué son las estructuras de datos?
   - 1.2. Tipos de datos simples vs. complejos
   - 1.3. Mutabilidad e inmutabilidad
2. Listas
   - 2.1. Concepto y sintaxis
   - 2.2. Creación y acceso a elementos
   - 2.3. Índices positivos y negativos
   - 2.4. Métodos principales de listas
   - 2.5. Operaciones con listas
   - 2.6. Listas anidadas
3. Bucle while
   - 3.1. Concepto y sintaxis
   - 3.2. Condiciones de continuación y terminación
   - 3.3. Bucles infinitos y cómo evitarlos
   - 3.4. Comparación while vs. for
4. Bucle for
   - 4.1. Concepto y sintaxis
   - 4.2. Iteración sobre listas
   - 4.3. La función range()
5. Conceptos avanzados de bucles
   - 5.1. Control de flujo en bucles
   - 5.2. Bucles con else
   - 5.3. Bucles anidados
6. Ejercicios prácticos

---

## 1. Introducción a las estructuras de datos

### 1.1. ¿Qué son las estructuras de datos?

Una **estructura de datos** es una forma organizada de almacenar, gestionar y acceder a múltiples valores relacionados. Hasta ahora hemos trabajado con variables que almacenan un único valor:

```python
nombre = "Ana"
edad = 25
precio = 19.99
aprobado = True
```

Sin embargo, en programas reales necesitamos manejar colecciones de datos: una lista de estudiantes, los precios de varios productos, las temperaturas de una semana, etc.

**Ventajas de usar estructuras de datos:**
- Organizar información relacionada bajo un único identificador
- Procesar múltiples valores con bucles
- Modelar problemas del mundo real de forma natural
- Reducir la cantidad de variables individuales

**Ejemplo comparativo:**

```python
# Sin estructura de datos (ineficiente)
estudiante1 = "Ana"
estudiante2 = "Carlos"
estudiante3 = "María"
estudiante4 = "Juan"

# Con estructura de datos (eficiente)
estudiantes = ["Ana", "Carlos", "María", "Juan"]
```

### 1.2. Tipos de datos simples vs. complejos

Python clasifica los tipos de datos en dos categorías principales:

#### Tipos de datos simples (escalares)

Almacenan un único valor atómico:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `int` | Números enteros | `42`, `-17`, `0` |
| `float` | Números decimales | `3.14`, `-0.5`, `2.0` |
| `str` | Cadenas de texto | `"Hola"`, `'Python'` |
| `bool` | Valores lógicos | `True`, `False` |
| `NoneType` | Ausencia de valor | `None` |

```python
contador: int = 10
temperatura: float = 23.5
mensaje: str = "Bienvenido"
activo: bool = True
resultado = None
```

#### Tipos de datos complejos (colecciones)

Almacenan múltiples valores en una única estructura:

| Tipo | Descripción | Mutable | Ordenado | Duplicados |
|------|-------------|---------|----------|------------|
| `list` | Secuencia ordenada | Sí | Sí | Sí |
| `tuple` | Secuencia inmutable | No | Sí | Sí |
| `set` | Colección sin orden | Sí | No | No |
| `dict` | Pares clave-valor | Sí | Sí* | No (claves) |

*Desde Python 3.7, los diccionarios mantienen el orden de inserción.

```python
numeros: list = [1, 2, 3, 4, 5]
coordenadas: tuple = (10.5, 20.3)
colores: set = {"rojo", "verde", "azul"}
estudiante: dict = {"nombre": "Ana", "edad": 25}
```

### 1.3. Mutabilidad e inmutabilidad

La **mutabilidad** determina si un objeto puede modificarse después de su creación.

#### Tipos inmutables

No se pueden modificar una vez creados. Cualquier operación que parezca modificarlos en realidad crea un nuevo objeto:

**Tipos inmutables:** `int`, `float`, `bool`, `str`, `tuple`, `frozenset`

```python
# Ejemplo con strings (inmutables)
texto = "Hola"
print(id(texto))  # 140234567890 (dirección de memoria)

texto = texto + " Mundo"
print(id(texto))  # 140234567912 (diferente dirección, nuevo objeto)

# Intentar modificar un carácter individual produce error
# texto[0] = "h"  # TypeError: 'str' object does not support item assignment
```

#### Tipos mutables

Pueden modificarse después de su creación sin cambiar su identidad en memoria:

**Tipos mutables:** `list`, `set`, `dict`

```python
# Ejemplo con listas (mutables)
numeros = [1, 2, 3]
print(id(numeros))  # 140234568000

numeros.append(4)  # Modifica la lista in-place
print(id(numeros))  # 140234568000 (misma dirección)
print(numeros)  # [1, 2, 3, 4]

numeros[0] = 10  # Modifica un elemento
print(numeros)  # [10, 2, 3, 4]
```

**¿Por qué es importante la mutabilidad?**

1. **Rendimiento:** Modificar un objeto mutable es más eficiente que crear uno nuevo
2. **Efectos secundarios:** Las funciones pueden modificar argumentos mutables
3. **Uso como claves:** Solo los inmutables pueden ser claves de diccionarios
4. **Seguridad:** Los inmutables son más seguros en entornos concurrentes

```python
# Ejemplo de copia vs. referencia
lista_a = [1, 2, 3]
lista_b = lista_a  # lista_b apunta al mismo objeto
lista_b.append(4)
print(lista_a)  # [1, 2, 3, 4] - también cambió

# Para copiar, usar .copy() o slicing
lista_c = lista_a.copy()
lista_c.append(5)
print(lista_a)  # [1, 2, 3, 4] - no cambió
print(lista_c)  # [1, 2, 3, 4, 5]
```

**Tabla resumen:**

| Característica | Inmutable | Mutable |
|----------------|-----------|---------|
| Se puede modificar | No | Sí |
| Crea nuevo objeto al cambiar | Sí | No |
| Puede ser clave de diccionario | Sí | No |
| Más eficiente al modificar | No | Sí |
| Más seguro | Sí | No |
| Ejemplos | `str`, `tuple`, `int` | `list`, `dict`, `set` |

---

## 2. Listas

### 2.1. Concepto y sintaxis

Una **lista** es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos. Es la estructura de datos más versátil y utilizada en Python.

**Características principales:**
- **Mutable:** Se puede modificar después de su creación
- **Ordenada:** Los elementos mantienen el orden de inserción
- **Indexada:** Cada elemento tiene una posición numérica (índice) que empieza en 0
- **Heterogénea:** Puede contener elementos de diferentes tipos
- **Permite duplicados:** Un mismo valor puede aparecer múltiples veces

```python
# Lista vacía
lista_vacia = []
otra_lista_vacia = list()

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Carlos", "María"]
mixta = [42, "texto", 3.14, True]  # No recomendable

# Lista creada con list()
letras = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
rango = list(range(5))  # [0, 1, 2, 3, 4]
```

### 2.2. Creación y acceso a elementos

#### Creación de listas:

```python
# Listas literales
frutas = ["manzana", "banana", "naranja"]
numeros = [10, 20, 30, 40, 50]

# Listas con repetición
ceros = [0] * 5  # [0, 0, 0, 0, 0]
patron = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Listas desde rangos
numeros_pares = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# Listas por comprensión
cuadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

#### Acceso a elementos:

```python
colores = ["rojo", "verde", "azul", "amarillo", "negro"]

# Acceso por índice positivo
primer_color = colores[0]  # "rojo"
segundo_color = colores[1]  # "verde"

# Verificar longitud antes de acceder
if len(colores) > 2:
    tercer_color = colores[2]  # Seguro
```

#### Modificación de elementos:

```python
numeros = [1, 2, 3, 4, 5]
numeros[0] = 10  # Cambia el primer elemento
print(numeros)  # [10, 2, 3, 4, 5]

numeros[2] = 99
print(numeros)  # [10, 2, 99, 4, 5]
```

### 2.3. Índices positivos y negativos

Python permite acceder a los elementos usando índices positivos (desde el inicio) o negativos (desde el final).

```python
letras = ["A", "B", "C", "D", "E"]

# Índices positivos (empiezan en 0)
#  Índice:  0    1    2    3    4
#  Valor:  "A"  "B"  "C"  "D"  "E"

print(letras[0])  # "A" - primer elemento
print(letras[4])  # "E" - quinto elemento

# Índices negativos (empiezan en -1 desde el final)
#  Índice: -5   -4   -3   -2   -1
#  Valor:  "A"  "B"  "C"  "D"  "E"

print(letras[-1])  # "E" - último elemento
print(letras[-2])  # "D" - penúltimo elemento
```

**Uso práctico de índices negativos:**

```python
numeros = [10, 20, 30, 40, 50]

# Acceder al último elemento sin saber la longitud
ultimo = numeros[-1]  # 50 (más legible que numeros[len(numeros)-1])

# Modificar desde el final
numeros[-1] = 99  # Cambia el último: [10, 20, 30, 40, 99]
```

### 2.4. Métodos principales de listas

#### Métodos para agregar elementos

**`append(elemento)`** - Agrega un elemento al final:

```python
frutas = ["manzana", "banana"]
frutas.append("naranja")
print(frutas)  # ["manzana", "banana", "naranja"]
```

**`extend(iterable)`** - Extiende la lista:

```python
numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros)  # [1, 2, 3, 4, 5, 6]

# Diferencia entre append() y extend()
lista_a = [1, 2, 3]
lista_a.append([4, 5])
print(lista_a)  # [1, 2, 3, [4, 5]]

lista_b = [1, 2, 3]
lista_b.extend([4, 5])
print(lista_b)  # [1, 2, 3, 4, 5]
```

**`insert(índice, elemento)`** - Inserta en una posición:

```python
colores = ["rojo", "verde", "azul"]
colores.insert(1, "amarillo")
print(colores)  # ["rojo", "amarillo", "verde", "azul"]
```

#### Métodos para eliminar elementos

**`remove(valor)`** - Elimina la primera ocurrencia:

```python
numeros = [1, 2, 3, 2, 4]
numeros.remove(2)  # Elimina el primer 2
print(numeros)  # [1, 3, 2, 4]

# Verificar antes de eliminar
if 3 in numeros:
    numeros.remove(3)
```

**`pop(índice=-1)`** - Elimina y devuelve:

```python
frutas = ["manzana", "banana", "naranja", "uva"]

ultima_fruta = frutas.pop()
print(ultima_fruta)  # "uva"
print(frutas)  # ["manzana", "banana", "naranja"]

primera_fruta = frutas.pop(0)
print(primera_fruta)  # "manzana"
```

**`clear()`** - Elimina todos los elementos:

```python
numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)  # []
```

#### Métodos de ordenamiento

**`sort()`** - Ordena in-place:

```python
numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 9]

# Ordenamiento descendente
numeros.sort(reverse=True)
print(numeros)  # [9, 5, 4, 3, 2, 1, 1]

# Ordenamiento por longitud
palabras = ["zebra", "ana", "Python", "manzana"]
palabras.sort(key=len)
print(palabras)  # ["ana", "zebra", "Python", "manzana"]
```

**`reverse()`** - Invierte el orden:

```python
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]
```

**`copy()`** - Crea una copia:

```python
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(original)  # [1, 2, 3]
print(copia)  # [1, 2, 3, 4]
```

#### Métodos de búsqueda

**`count(valor)`** - Cuenta ocurrencias:

```python
numeros = [1, 2, 2, 3, 2, 4, 2]
cantidad = numeros.count(2)
print(cantidad)  # 4
```

**`index(valor)`** - Devuelve el índice:

```python
letras = ["a", "b", "c", "b", "d"]
posicion = letras.index("b")
print(posicion)  # 1

# Buscar desde una posición
posicion_siguiente = letras.index("b", 2)
print(posicion_siguiente)  # 3
```

**Tabla resumen de métodos:**

| Método | Modifica | Devuelve | Descripción |
|--------|----------|----------|-------------|
| `append(x)` | Sí | `None` | Agrega al final |
| `extend(iter)` | Sí | `None` | Agrega elementos de iterable |
| `insert(i, x)` | Sí | `None` | Inserta en posición i |
| `remove(x)` | Sí | `None` | Elimina primera ocurrencia |
| `pop(i)` | Sí | Elemento | Elimina y devuelve |
| `clear()` | Sí | `None` | Elimina todos |
| `sort()` | Sí | `None` | Ordena in-place |
| `reverse()` | Sí | `None` | Invierte orden |
| `copy()` | No | Nueva lista | Crea copia |
| `count(x)` | No | `int` | Cuenta ocurrencias |
| `index(x)` | No | `int` | Devuelve índice |

### 2.5. Operaciones con listas

#### Concatenación (`+`)

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = lista1 + lista2
print(resultado)  # [1, 2, 3, 4, 5, 6]
```

#### Repetición (`*`)

```python
patron = [0, 1]
repetido = patron * 4
print(repetido)  # [0, 1, 0, 1, 0, 1, 0, 1]

# Crear lista con valores iniciales
ceros = [0] * 5  # [0, 0, 0, 0, 0]
```

#### Pertenencia (`in`, `not in`)

```python
frutas = ["manzana", "banana", "naranja"]

if "banana" in frutas:
    print("Tenemos bananas")

if "uva" not in frutas:
    print("No tenemos uvas")
```

#### Longitud (`len()`)

```python
colores = ["rojo", "verde", "azul"]
cantidad = len(colores)  # 3

# Verificar si está vacía
if not lista_vacia:
    print("La lista está vacía")
```

#### Funciones integradas útiles

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Mínimo y máximo
minimo = min(numeros)  # 1
maximo = max(numeros)  # 9

# Suma
total = sum(numeros)  # 31

# Ordenar sin modificar
ordenada = sorted(numeros)
print(ordenada)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(numeros)  # [3, 1, 4, 1, 5, 9, 2, 6] - sin cambios

# any() y all()
booleanos = [True, True, False, True]
print(any(booleanos))  # True - al menos uno es True
print(all(booleanos))  # False - no todos son True
```

### 2.6. Listas anidadas

Una lista puede contener otras listas, creando estructuras multidimensionales:

```python
# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso a elementos
primer_fila = matriz[0]  # [1, 2, 3]
elemento_central = matriz[1][1]  # 5
esquina = matriz[2][2]  # 9

# Modificar elemento
matriz[0][0] = 99

# Iterar sobre matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
```

**Creación correcta de matrices:**

```python
# ❌ Forma incorrecta
matriz_mala = [[0] * 3] * 3
matriz_mala[0][0] = 1
print(matriz_mala)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# ✅ Forma correcta
matriz_buena = [[0] * 3 for _ in range(3)]
matriz_buena[0][0] = 1
print(matriz_buena)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 3. Bucle while

### 3.1. Concepto y sintaxis

El bucle `while` repite un bloque de código mientras una condición sea verdadera.

```python
while condición:
    # Código que se repite
    # mientras la condición sea True
```

**Ejemplo básico:**

```python
# Contar del 1 al 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # IMPORTANTE: modificar la variable
```

### 3.2. Condiciones de continuación y terminación

```python
# 1. Condición numérica
contador = 0
while contador < 10:
    print(contador)
    contador += 1

# 2. Condición booleana
ejecutar = True
while ejecutar:
    respuesta = input("¿Continuar? (s/n): ")
    ejecutar = respuesta.lower() == "s"

# 3. Condición de lista no vacía
numeros = [1, 2, 3, 4, 5]
while numeros:
    print(numeros.pop())

# 4. Condición compuesta
intentos = 0
exito = False
while intentos < 3 and not exito:
    respuesta = input("Adivina: ")
    if respuesta == "7":
        exito = True
    else:
        intentos += 1
```

### 3.3. Bucles infinitos y cómo evitarlos

**Bucles infinitos intencionales:**

```python
# Menú interactivo
while True:
    print("\n--- MENÚ ---")
    print("1. Opción A")
    print("2. Opción B")
    print("3. Salir")
    
    opcion = input("Selecciona: ")
    
    if opcion == "3":
        print("Saliendo...")
        break
```

### 3.4. Comparación while vs. for

| Característica | `while` | `for` |
|----------------|---------|-------|
| Uso principal | Condición desconocida | Iterar sobre secuencia |
| Iteraciones | Desconocidas | Conocidas |
| Control | Manual | Automático |
| Legibilidad | Puede ser menos clara | Más clara |
| Riesgo bucle infinito | Alto | Bajo |

**Cuándo usar `while`:**
- Esperar una condición
- Validación de entrada
- Algoritmos con condición compleja

**Cuándo usar `for`:**
- Iterar sobre secuencia conocida
- Número fijo de iteraciones
- Recorrer archivos

---

## 4. Bucle for

### 4.1. Concepto y sintaxis

El bucle `for` recorre secuencialmente los elementos de un iterable.

```python
for variable in secuencia:
    # Código que se ejecuta
    # para cada elemento
```

**Ejemplos básicos:**

```python
# Iterar sobre lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Iterar sobre string
palabra = "Python"
for letra in palabra:
    print(letra)

# Iterar sobre rango
for numero in range(5):
    print(numero)  # 0, 1, 2, 3, 4
```

### 4.2. Iteración sobre listas

**Iteración directa:**

```python
precios = [10.5, 20.0, 15.75, 30.25]
for precio in precios:
    precio_con_iva = precio * 1.21
    print(f"Precio: {precio}€ → Con IVA: {precio_con_iva:.2f}€")
```

**Con índices usando `enumerate()`:**

```python
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Empezar en 1
for numero, fruta in enumerate(frutas, start=1):
    print(f"{numero}. {fruta}")
```

**Con `zip()` para múltiples listas:**

```python
nombres = ["Ana", "Carlos", "María"]
edades = [25, 30, 22]
ciudades = ["Madrid", "Barcelona", "Valencia"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
```

### 4.3. La función range()

**Sintaxis:**
- `range(stop)` - De 0 hasta stop-1
- `range(start, stop)` - De start hasta stop-1
- `range(start, stop, step)` - Con incremento

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

# Cuenta regresiva
for i in range(10, 0, -1):
    print(i)
print("¡Despegue!")
```

---

## 5. Conceptos avanzados de bucles

### 5.1. Control de flujo en bucles

**`break`** - Salir del bucle:

```python
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        break
    print(num)  # 1, 2
```

**`continue`** - Saltar iteración:

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9
```

**`pass`** - No hacer nada:

```python
for i in range(5):
    if i == 3:
        pass  # TODO: implementar
    else:
        print(i)
```

### 5.2. Bucles con else

La cláusula `else` se ejecuta si el bucle termina sin `break`:

```python
# Búsqueda
numeros = [2, 4, 6, 8, 10]
objetivo = 7

for num in numeros:
    if num == objetivo:
        print(f"Encontrado: {objetivo}")
        break
else:
    print(f"No se encontró {objetivo}")
```

### 5.3. Bucles anidados

```python
# Tabla de multiplicar
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print()

# Patrón de asteriscos
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# Salida:
# *
# **
# ***
# ****
# *****
```

---

## 6. Ejercicios prácticos

### Ejercicio: Gestión de tareas

```python
tareas_pendientes = []
tareas_completadas = []

def agregar_tarea(tarea: str) -> None:
    tareas_pendientes.append(tarea)
    print(f"Tarea '{tarea}' agregada")

def completar_tarea(tarea: str) -> None:
    if tarea in tareas_pendientes:
        tareas_pendientes.remove(tarea)
        tareas_completadas.append(tarea)
        print(f"Tarea completada")
```

### Ejercicio: Estadísticas

```python
calificaciones = [7.5, 4.2, 8.9, 6.0, 3.5, 9.1, 5.8, 7.0]

promedio = sum(calificaciones) / len(calificaciones)
nota_maxima = max(calificaciones)
nota_minima = min(calificaciones)
aprobados = sum(1 for nota in calificaciones if nota >= 5)

print(f"Promedio: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
```

### Ejercicio: Eliminar duplicados

```python
def eliminar_duplicados(lista: list) -> list:
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

numeros = [1, 2, 2, 3, 4, 3, 5, 1, 6]
print(eliminar_duplicados(numeros))  # [1, 2, 3, 4, 5, 6]
```

---

> **Nota:** Este documento cubre la primera parte de UD2. Las secciones sobre Tuplas, Conjuntos y Diccionarios se cubren en UD2.2.
