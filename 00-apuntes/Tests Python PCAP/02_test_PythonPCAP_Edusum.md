
# Test Python PCAP - Edusum
[Fuente preguntas: Edusum ](https://www.edusum.com/python-institute/python-institute-associate-python-programmer-pcap-certification-sample-questions)

**1. A compiler is a program designed to (select two answers)**

- a) rearrange the source code to make it clearer
- b) check the source code in order to see if it’s correct
- c) execute the source code
- d) translate the source code into machine code

<details>
<summary>Solucion</summary>
Respuestas correctas: **b, d**  
Explicación: Un compilador revisa el código fuente para detectar errores (**b**) y lo traduce a código máquina (**d**). No ejecuta directamente el código ni simplemente lo reorganiza.
</details>

---

**2. You are going to read just one character from a stream called `s`. Which statement would you use?**

- a) ch = read(s, 1)
- b) ch = s.input(1)
- c) ch = input(s, 1)
- d) ch = s.read(1)

<details>
<summary>Solucion</summary>
Respuesta correcta: **d**  
Explicación: El método `read(1)` de un objeto de archivo lee exactamente un carácter del stream. Las otras opciones no son sintaxis válida en Python para esto.
</details>

---
**3. Can a module run like regular code?**

- a) yes, and it can differentiate its behavior between the regular launch and import
- b) it depends on the Python version
- c) yes, but it cannot differentiate its behavior between the regular launch and import
- d) no. it is not possible; a module can be imported, not run

<details>
<summary>Solucion</summary>
Respuesta correcta: **a**  
Explicación: Un módulo puede ejecutarse directamente y puede usar `if __name__ == "__main__":` para diferenciar su comportamiento entre ejecución directa e importación.
</details>

---
**4. Which of the following sentences are true? (Select two answers)**

- a) lists may not be stored inside tuples
- b) tuples may be stored inside lists
- c) tuples may not be stored inside tuples
- d) lists may be stored inside lists

<details>
<summary>Solucion</summary>
Respuestas correctas: **b, d**  
Explicación: Las tuplas pueden contener listas y las listas pueden contener listas. Python permite estructuras anidadas sin restricciones.
</details>

---
**5. How many elements will the `list2` list contain after execution of the following snippet?**

```python
list1 = [False for i in range(1,10)]
list2 = list1[-1:1:-1]
```
a) zero

b) five

c) seven

d) three

<details> 
<summary><b>Solucion</b></summary> Respuesta correcta: **c** Explicación: La sintaxis `list1[-1:1:-1]` invierte la lista desde el último elemento hasta el índice 2 (no incluido), produciendo 7 elementos.
 </details>

---
**6. Which of the following literals reflect the value given as 34.23? (select two answers)**

a) .3423e2

b) 3423e-2

c) .3423e-2

d) 3423e2

<details>
<summary><b>Solucion</b></summary>
Respuestas correctas: **a, b** Explicación: `.3423e2` = 0.3423 * 10² = 34.23 y `3423e-2` = 3423 * 10⁻² = 34.23. Las otras opciones dan valores diferentes. 
</details>

---

**7. What can you deduce from the following statement? (Select two answers)**

```python
str = open('file.txt', "rt")
```

a) str is a string read in from the file named file.txt

b) a new line character translation will be performed during the reads

c) if file.txt does not exist, it will be created

d) the opened file cannot be written with the use of the str variable

<details>
<summary><b> Solucion</b></summary> 
Respuestas correctas: **b, d** Explicación: `"rt"` abre el archivo en modo lectura de texto. Python traducirá los finales de línea automáticamente (**b**) y no permite escribir en el archivo abierto en modo lectura (**d**).
 </details>

---
**8. Select the true statements: (select all that apply)**  

a) The class keyword marks the beginning of the class definition

b) An object cannot contain any references to other objects

c) A class may define an object

d) A constructor is used to instantiate an object

e) An object variable is a variable that is stored separately in every object

<details> <summary><b>Solucion</b></summary> Respuestas correctas: **a, c, d** Explicación: `class` define la clase (**a**), una clase puede definir un objeto (**c**) y el constructor (`__init__`) se usa para instanciar objetos (**d**). La b y e son incorrectas. </details>

---
**9. What will the value of the `i` variable be when the following loop finishes its execution?**

```python   

for i in range(10):
    pass
```

a) 10

b) the variable becomes unavailable

c) 11

d) 9

<details>
<summary><b>Solucion</b></summary> 
Respuesta correcta: **d** Explicación: El bucle `for` termina con `i` en el último valor del rango, que es 9.
 </details>

---
**10. The first parameter of each method:**

a) holds a reference to the currently processed object

b) is always set to None

c) is set to a unique random value

d) is set by the first argument's value

<details>
<summary><b>Solucion</b></summary>
 Respuesta correcta: **a** Explicación: En Python, el primer parámetro de un método de instancia (`self`) siempre hace referencia al objeto que invoca el método.
  </details> 

---
---