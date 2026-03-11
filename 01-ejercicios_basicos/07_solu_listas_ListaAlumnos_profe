# Solucion de manera sencilla centrandonos en uso de listas. 
class Alumno:
    def __init__(self, nombre, dni, asignaturas):
        self.nombre = nombre
        self.dni = dni
        self.asignaturas = asignaturas
        
    def __str__(self):
        return f"Alumno: {self.nombre}, DNI: {self.dni}, Asignaturas: {', '.join(self.asignaturas)}"
        
    
num_alumnos = int(input("Intro duce el numero de alumnso: "))
listado_alumnos = []

for i in range(num_alumnos):
    # Pedimos datos alumno
    nombre = input("Introduce el nombre:")
    dni = input("Introduce el dni: ")
    asignaturas = []
    especialidad = input("Introduce la especialidad (Ciencias / Letras): ")
    especialidad = especialidad.lower()
    if especialidad == "ciencias":
        asignaturas = ["Matematicas", "Fisica", "Quimica"]
    else:
        asignaturas = ["Lengua", "Latin", "Historia"]
    #Generamos objeto alumno
    alumno = Alumno(nombre, dni, asignaturas)
    
    # Añadimos el objeto a la lista 
    listado_alumnos.append(alumno)
    
alumno1 = Alumno("Pepe", "12345678A", ["Matematicas", "Fisica", "Quimica"])
alumno2 = Alumno("Maria", "87654321B", ["Lengua", "Latin", "Historia"])
alumno3 = Alumno("Juan", "11223344C", ["Matematicas", "Fisica", "Quimica"])
listado_alumnos.append(alumno1)
listado_alumnos.append(alumno2)
listado_alumnos.append(alumno3) 
    
# Chequeamos la lista de alumnos
for alumno in listado_alumnos:
    print("-" * 20)
    print(alumno) # Al definir el metodo __str__ en la clase alumno, al imprimir la lista de alumnos se muestra la info de cada alumno.

# Sacar el nombre de alumnos que estudian  qumica.
print("*"*40)
print("Alumnos que estudian quimica:")

for alumno in listado_alumnos:
    # Accedo a las asignaturas del alumno
    listado_asignaturas = alumno.asignaturas
    # Miro si quimica esta en la lista de asignaturas
    if "Quimica" in listado_asignaturas:
        print(f"{alumno.nombre} estudia quimica")

## Solicitar dni y sacar de la linea mostrar el alumno eliminiado
# En listas para buscar un elemento concreto, lo mas eficiente es usar un bucle for con un if.
print("*" *20)
dni_buscado = input("Introduce el dni: ")

for alumno in listado_alumnos:
    if alumno.dni == dni_buscado:
        listado_alumnos.remove(alumno) # Lo eliminamos de la lista
        # Todavia el objeto alumno exite en memoria ya no en la lista podemos acceder a el.
        print(f"Alumno eliminado: {alumno.nombre} eliminado con dni {alumno.dni}")
        break # Salir del bucle para ahorrar recursos a la app
'''
### Eliminarlo usando pop y posiciones
dni_buscado = input("introduce el dni: ")
for i in range(len(listado_alumnos)):
    if listado_alumnos[i].dni == dni:
        a = listado_alumnos.pop(i)
        print(f"El alumno {a.nombre} se ha elminado. ")
        break 
'''
'''   
## Diferencia entre el continue y el break en un bucle

for i in range(10):
    if i % 2 == 0:
        continue # Vuelve al inicio
    if i % 3 == 0:
        break # Sale del bucle
    print(i) # ¿Que numero/s imprimiria. 
    
# Imprimiria 1 el continuo vuelve al inicio del bucle el break '''