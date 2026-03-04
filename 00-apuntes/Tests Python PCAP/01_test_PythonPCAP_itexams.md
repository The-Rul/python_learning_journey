

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
<b>Respuesta correcta: d) 9</b>



<b>Explicación:</b> La función `range(10)` genera una secuencia de 0 a 9. Al terminar el bucle, la variable de control `i` conserva el último valor asignado por el iterador, que en este caso es 9.
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
---