'''## Ejercicio 1: solo diccionarios
### Enunciado
Crea un programa para gestionar las notas de varios alumnos usando un diccionario. </br>
El diccionario tendrá:
 * como clave el nombre del alumno
 * como valor su nota </br>
 
Se pide:
1.	Crear un diccionario con al menos 5 alumnos y sus notas.
2.	Mostrar todas las parejas alumno -> nota.
3.	Pedir por teclado el nombre de un alumno y mostrar su nota.
4.	Indicar qué alumno tiene la nota más alta.
5.	Calcular la media de todas las notas.
6.	Mostrar solo los alumnos que tengan una nota mayor o igual que 5.'''

#alumnos_dict = {{"nombre":"Luis", "nota" : 7.6},{"nombre":"Maria", "nota" : 9.5},{"nombre":"Jorge", "nota" : 5.6},{"nombre":"Carmele", "nota" : 3.6},{"nombre":"Pepa", "nota" : 1.6}}

alumnos_dict = {
    "Luis": 7.6,
    "Maria": 9.5,
    "Jorge": 5.6,
    "Carmele": 3.6,
    "Pepa": 1.6,
    "Carmen": 4.4
}

# 1 Crear y mostrar
for nombre, nota in alumnos_dict.items():
    print(f"Alumno {nombre} tienen nota {nota}.")
    
print("-" * 20)    

    
## 2. Pedir y mostrar su nota
alumno = input("Mirar nota de alumno: ")
if alumno in alumnos_dict:
    print(f"La nota de {alumno} es {alumnos_dict.get(alumno)}")
    print(f"La nota de {alumno} es {alumnos_dict[alumno]}")
else:
    print("No se ha encontrado el alumno")
    