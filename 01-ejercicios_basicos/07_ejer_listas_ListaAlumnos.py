'''Ejercicio Alumnos con listas
================================================
Crear la clase Alumno con los atributos nombre, dni y una lista de asignaturas

1. Preguntar cuantos alumnos hay en el curso. 
2. Nos pide los datos de cada uno de los alumno y para las asignaturas se pregunta 
    si es de ciencias o letras, si es de ciencias se le asigna una lista de 
    3 asignaturas (física, química, matemáticas) ya creada y si es de letras otra lista con latín , lengua, historia. 
    Cada alumno creado se añade a una lista.
4. Sacar el nombre de los alumnos que están estudiando química.
5. Solicitar un DNI, sacar al alumno con ese dni de la lista y mostrar "se ha eliminiado al {nombre.alumno} de la lista de alumnos"
'''


ASIGNATURAS_CIENCIAS = ["Matematicas","Fisica","Quimica"]
ASIGNATURAS_LETRAS = ["Lengua","Latin","Historia"]
class Alumno():
    def __init__ (self, nombre:str, dni:str, ciencias=False, letras=False):
        self.nombre = nombre
        self.dni = dni
        if ciencias:
            self.asignaturas = ASIGNATURAS_CIENCIAS #Probar si luego se cambia a la lista del alumno
        if letras:
            self.asignaturas = list(ASIGNATURAS_LETRAS)
    
    def __str__(self):
        return f"Alumno: {self.nombre}, DNI: {self.dni}, Asignaturas: {', '.join(self.asignaturas)}"
    
            

# ----------------------------  METODOS PARA EL PROGRAMA-----------------------

def chequear_digito(var) -> bool :
    es_digito = False
    if var.isdigit():
        var = int(var)
        es_digito = True
    else:
            print("El numero intro no es un digito. Vuelve a intentarlo. ")
    return es_digito, var
            
print(f"-------------LISTA DE ALUMNOS ----------")
print("-" * 40)

# 1. Pedimos el total de alumnos
es_digito = False 
while(es_digito == False):
    total_alumnos = input("¿Cuantos alumnos hay en el curso?: ")
    es_digito,total_alumnos = chequear_digito(total_alumnos)

##############################################33333    
# 2. Rellenar datos

print(f"Rellana la lista con la info de alumnos:")

lista_alumnos = []

for i in range(total_alumnos):
    print("-"*20)
    print(f"Alumno nº {i+1}")
    nombre = input("Nombre del alumno: ")
    dni = input("Dni: ")
    rama = input("¿Que rama de estudios? (Ciencias / Letras): ")
    rama = rama.lower()
    match rama:
        case "ciencias":
            alumno = Alumno(nombre, dni, ciencias=True)
        case "letras":
            alumno = Alumno(nombre, dni, letras=True) 
    lista_alumnos.append(alumno)

################################
## Alumnos de prueba
alumno1 = Alumno("Pepe", "12345678A", ciencias=True)
alumno2 = Alumno("Maria", "87654321B", letras=True)
alumno3 = Alumno("Juan", "11223344C", ciencias=True)
lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)   
##############################################33333        
#3. Chequear lista alumnos
print("#" *40)
print(f"{"#"*10} LISTA ALUMNOS {"#"*10}")
print("#" *40)

for alumno in lista_alumnos:
    print("-" * 20)
    print(lista_alumnos) # Al definir el metodo __str__ en la clase alumno, al imprimir la lista de alumnos se muestra la info de cada alumno.


################################################
# 3. Alumnos estudiando qumica. 
estudiantes_quimica = [alumno.nombre for alumno in lista_alumnos if "Quimica" in alumno.asignaturas]

print(estudiantes_quimica)

    