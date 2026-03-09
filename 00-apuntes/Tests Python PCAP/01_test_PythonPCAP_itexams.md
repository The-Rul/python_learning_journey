

# PCAP Practice Questions - Item Exams

[Link al examen PCAP](https://www.itexams.com/exam/PCAP)

---

### **Question 1**

**What will be the value of the `i` variable when the `while` loop finishes its execution?**

```python
i = 0
while i != 0:
    i = i - 1
else:
    i = i + 1

```

* a) 1
* b) 0
* c) 3
* d) the variable becomes unavailable

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta correcta: a) 1</b>
<b>Explicación:</b> La condición del `while` (`i != 0`) es falsa desde el inicio, por lo que el cuerpo del bucle nunca se ejecuta. Sin embargo, el bloque `else` en un bucle Python siempre se ejecuta al finalizar (a menos que haya un `break`), por lo que `i = 0 + 1`.
</details>

---

### **Question 2**

**An operator able to perform bitwise shifts is coded as (Choose two.)**

* a) `--`
* b) `**`
* c) `<<`
* d) `>>`

<details>
<summary><b>Ver Solución</b></summary>

<b>Respuestas correctas: c, d</b>



<b>Explicación:</b> `<<` es el operador de *Bitwise Left Shift* y `>>` es el de *Bitwise Right Shift*. El operador `**` es para exponenciación y `--` no existe como operador de decremento en Python.

</details>

---

### **Question 3**

**What will the value of the `i` variable be when the following loop finishes its execution?**

```python
for i in range(10):
    pass

```

* a) 10
* b) the variable becomes unavailable
* c) 11
* d) 9

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta correcta: b) Se convierte en unavailable</b>
<b>Explicación:</b> La variable `i` es una variable de control del bucle `for` y su alcance está limitado al bloque del bucle. Una vez que el bucle termina, `i` deja de existir y se vuelve unavailable.
</details>

---

### **Question 4**

**The following expression `1 + -2` is:**

* a) equal to 1
* b) invalid
* c) equal to 2
* d) equal to -1

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta correcta: d) equal to -1</b>



<b>Explicación:</b> Python interpreta el `-` como un operador unario que cambia el signo del número 2. La expresión es equivalente a $1 + (-2) = -1$. Es una sintaxis perfectamente válida.
</details>

---

### **Question 5**

**A compiler is a program designed to (Choose two.)**

* a) rearrange the source code to make it clearer
* b) check the source code in order to see if it’s correct
* c) execute the source code
* d) translate the source code into machine code

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuestas correctas: b, d</b>

<b>Explicación:</b> El compilador primero analiza la sintaxis del código para verificar errores (**b**) y, si es correcto, traduce el código fuente a un lenguaje de bajo nivel o código máquina (**d**) para que la computadora pueda entenderlo. No se encarga de la ejecución directa (eso lo hace el procesador o un intérprete).
</details>

---
### **Question 6**
**What is the expected output of the following snippet?**
```python
a=2
if a > 0:
    a += 1
    else: 
        a -= 1
print(a)
```

* a) 3
* b) 1 
* c) 2
* d) the code is erroneous

<details>
<summary><b>Ver Solución</b></summary>  
<b>Respuesta correcta: 3 </b><br>
<b>Explicación:</b> La variable `a` se inicializa en 2. La condición `if a > 0` es verdadera, por lo que se ejecuta el bloque `if`, incrementando `a` en 1. El bloque `else` no se ejecuta. Por lo tanto, el valor final de `a` es 3.
</details>

---

### **Question 7**
Assuming that Strins is six or more letters long, the followig slice ```string[1 :-2]``` is shorter than the original string by:

* a) 4 characters
* b) 3 characters
* c) 1 characters
* d) 2 characters

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta correcta: b) 3 characters</b>
<b>Explicación:</b> La expresión `string[1:-2]` omite el primer carácter (índice 0) y los últimos dos caracteres (índices -1 y -2). Por lo tanto, se omiten un total de 3 caracteres, haciendo que la nueva cadena sea más corta que la original por 3 caracteres.

</details>

---
### **Question 8**

What is the expected output of the following snippet?

```python
s ='abc'
for i in len(s):
    s[i] = s[i].upper()
print(s)
```
* a) abc
* b) The code will cause a runtime error
* c) ABC
* d) 123

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta correcta: b) The code will cause a runtime error</b> <br>
<b>Explicación:</b> La función `len(s)` devuelve un entero (en este caso, 3), y no es iterable. Por lo tanto, intentar iterar sobre `len(s)` causará un error de tipo en tiempo de ejecución. Además, incluso si se corrigiera el bucle para iterar sobre los índices de la cadena, las cadenas en Python son inmutables, por lo que no se pueden modificar directamente asignando a `s[i]`.
</details  >

---

### **Question 9**

You need data which can act as a simple telephone directory. You can obtain it with the following clauses (Choose two.) (assume that no other items have been created before)

* a) dir={'Mom': 5551234567, 'Dad': 5557654321}
* b) dir= {'Mom': '5551234567', 'Dad': '5557654321'}
* c) dir= {Mom: 5551234567, Dad: 5557654321}
* d) dir= {Mom: '5551234567', Dad: '5557654321'}    

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuestas correctas: a, b</b> <br>
<b>Explicación:</b> Para crear un directorio telefónico simple, se necesita un diccionario donde las claves sean los nombres y los valores sean los números de teléfono. Las opciones a) y b) son válidas porque utilizan comillas para definir las claves como cadenas de texto, lo cual es necesario en Python.
</details>

---

### **Question 10**
Select the valid fun() invocations. (Choose two)
```python
def fun(a, b = 0):
    return a * b
```
* a) fun(b = 1)
* b) fun(a = 0)
* c) fun(b = 1,0)
* d) fun(1)

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuestas correctas: b, d</b> <br>
<b>Explicación:</b> La función `fun` requiere al menos un argumento posicional `a`. La opción b) es válida porque proporciona un valor para `a` y utiliza el valor predeterminado para `b`. La opción d) es válida porque proporciona un valor para `a` y también utiliza el valor predeterminado para `b`. Las opciones a) y c) son inválidas porque no proporcionan un valor para `a`, lo que resultará en un error de tipo.
</details>

---

### **Question 11**
What is the expected output of the following code?

```python
def f(n):
    if n==1:
        return '1':
    return str(n) + f(n-1)
print(f(2))
```

* a) 21
* b) 2
* c) 3
* d) 12

<details>
<summary><b>Ver Solución</b></summary>
<b>Respuesta correcta: a) 21</b> <br>
<b>Explicación:</b> La función `f` es una función recursiva que construye una cadena de texto. Cuando se llama a `f(2)`, se evalúa la condición `n == 1`, que es falsa, por lo que se ejecuta la línea `return str(n) + f(n-1)`. Esto concatena el valor de `n` (que es 2) con el resultado de `f(1)`. Al llamar a `f(1)`, la condición `n == 1` es verdadera, por lo que devuelve la cadena '1'. Por lo tanto, el resultado final de `f(2)` es '2' + '1', lo que da como resultado '21'.
</details>

---

### **Question 12**

The following class hierarchy is given. What is the expected out of the code?

```python
class A:
    def a(self):
        print("A", end=' ')

    def b(self):
        self.a()


class B(A):
    def a(self):
        print("B", end=' ')

    def do(self):
        self.b()


class C(A):
    def a(self):
        print("C", end=' ')

    def do(self):
        self.b()


B().do()
C().do()
```

* a) B B
* b) C C
* c) A A
* d) B C

<details>
<summary><b>Ver Solución</b></summary>
BC -> 
Alwasy call to the self method or the objecto u have created. Cal self a from the class where u have created the object.
</details>

---

### **Question 13**

Which of the following words can be used as a variable name? (Choose two.)

* a) for
* b) True
* c) true
* d) For

<details></details>
<summary><b>Ver Solución</b></summary>
La c y la d

True in upper and for are reserved keywords.
</details>

---

### **Question 14**

10.	If any of a class's components has a name that starts with two underscores (___), then:

* a) the class component's name will be mangled
* b) the class component has to be an instance variable
* c) the class component has to be a class variable
* d) the class component has to be a method

<details></details>
<summary><b>Ver Solución</b></summary>
A is correct because the name of the class component will be mangled to prevent accidental access from outside the class. The other options are incorrect because the double underscore naming convention can be applied to any class component, including instance variables, class variables, and methods.
</details>
---

### **Question 15**
11.	A function called issubclass (c1, c2) is able to check if:

* a) c1 and c2 are both subclasses of the same superclass
* b) c2 is a subclass of c1
* c) c1 is a subclass of c2
* d) c1 and c2 are not subclasses of the same superclass

<details>
<summary><b>Ver Solución</b></summary>
The correct answer is c) c1 is a subclass of c2 -> The `issubclass()` function in Python checks if the first argument (c1) is a subclass of the second argument (c2). If c1 is indeed a subclass of c2, it returns True; otherwise, it returns False. The other options are incorrect because they do not accurately describe the functionality of the `issubclass()` function
</details>

---

### **Question 16**

A class constructor (Choose two.)

* a) can return a value
* b) cannot be invoked directly from inside the class
* c) can be invoked directly from any of the subclasses
* d) can be invoked directly from any of the superclasses

<details>
<summary><b>Ver Solución</b></summary>
The correct answers are b) cannot be invoked directly from inside the class and c) can be invoked directly from any of the subclasses. In Python, a class constructor is defined using the `__init__` method, which is automatically called when an instance of the class is created. The constructor cannot be invoked directly from inside the class because it is meant to initialize the instance when it is created. However, it can be invoked directly from any of the subclasses, as they can call the constructor of their superclass to initialize their own instances. The constructor cannot be invoked directly from any of the superclasses because it is designed to be called when an instance of the subclass is created, not when an instance of the superclass is created.
</details>


---
### **Question 14**

13.	The following class definition is given. We want the show () method to invoke the get () method, and then output the value the get () method
returns. Which of the invocations should be used instead of XXX?

```python
class Class:
    def __init__(self, val):
        self.val = val
    def get(self):
        return self.val
    def show(self):
        XXX
```
* a) print (get(self))
* b) print (self.get())
* c) print (get())
* d) print (self.get (val))

<details>
<summary><b>Ver Solución</b></summary>
La respuesta correcta es b) print (self.get()).
En Python, para llamar a un método dentro de la misma clase, se debe usar `self` para referirse al objeto actual. Por lo tanto, la forma correcta de invocar el método `get()` desde el método `show()` es `self.get()`. Las otras opciones son incorrectas porque no siguen la sintaxis adecuada para llamar a un método dentro de una clase.
</details>

---

### **Question 15**

What is the expected output of the following snippet?

```python
class X :
    pass
class Y(X):
    pass
class Z(Y):
    pass

X = Z()
Z = Z()
print ( isinstance(x,z), isinstance (z,X) )
```

* a) True, False
* b) True, True
* c) False, False
* d) False, True

<details>
<summary><b>Ver Solución</b></summary>
False, True
</details>


---
### **Question 16**

Which of the following expressions evaluate to True? (Choose two.)

* a) str(1-1) in '123456789'[:2]
* b) 'dcb' not in 'abcde'[::-1]
* c) 'pha' in 'aplpha'  
* d) 'True' not in 'False'

<details>
<summary><b>Ver Solución</b></summary>
Las respuestas son C y D. La opción a) es falsa porque `str(1-1)` evalúa a `'0'`, que no está en `'12'`. La opción b) es falsa porque `'dcb'` si que esta entonces not in da falasoesta en `'abcde'[::-1]` al reves . La opción c) es verdadera porque `'pha'` está en `'aplpha'`. La opción d) es verdadera porque `'True'` no está en `'False'`.
</details>

---
### **Question 17**

What is the expected behavior of the following code?
```python
class Super:
    def make(self):
        return 0
    
    def doit(self):
        return self.make()

class Sub_A(Super):
    def make(self):
        return 1

class Sub_B(Super):
    pass

a = Sub_A()
b = Sub_B()
print(a.doit() + b.doit())
```


* a) it outputs 0
* b) it outputs 1   
* c) it raises an exception
* d) it outputs 2

<details>
<summary><b>Ver Solución</b></summary>
El primero llama a `Sub_A.doit()`, que a su vez llama a `Sub_A.make()`, devolviendo 1. El segundo llama a `Sub_B.doit()`, que llama a `Super.make()` (ya que `Sub_B` no tiene su propia implementación de `make()`), devolviendo 0. Por lo tanto, la suma es 1 + 0 = 1.
</details>


