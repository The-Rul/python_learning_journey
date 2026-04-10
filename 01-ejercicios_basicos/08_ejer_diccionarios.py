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
    
    
    
'''-------------------------------------------------------------------------------------------------------------------
Ejercicio 3: diccionarios, listas, objetos, herencia y excepciones
Enunciado

Crea un sistema de gestión de biblioteca en Python.
Requisitos de clases

    Crea una clase base llamada Material con:

    titulo
    autor
    método mostrar_info()

    Crea dos clases hijas:

    Libro, que además tenga num_paginas
    Revista, que además tenga numero_edicion

    Redefine el método mostrar_info() en las clases hijas.


'''

class Material():
  def __init__(self, titulo:str ="na", autor:str="na") -> None:
    self.titulo = titulo
    self.autor = autor

  def mostrar_info(self):
    return f"{type(self).__name__}: {self.titulo} | Autor: {self.autor} "

    #podriamos cambiar el nombre a mostrar_info por __str__ de la clase objeto que usa por defecto


        
# ############################ CLASES "Libro" , "Revista" ###############3333
class Libro(Material):
  def __init__(self, titulo: str = "na", autor: str = "na", num_paginas:int = 0) -> None:
    super().__init__(titulo, autor) #El super se encarga de pasarle ya el self no es necesario.
    # Material.__init_(self, titulo, autor) # Si que sería necesario en este caso pasarle el self.  
    self.num_paginas = num_paginas

  def mostrar_info(self):
    return super().mostrar_info() + f"| Paginas: {self.num_paginas}"

class Revista(Material):
  def __init__(self, titulo: str = "na", autor: str = "na", numero_edicion:int =0) -> None:
    super().__init__(titulo, autor)
    self.numero_edicion = numero_edicion

  def mostrar_info(self):
    return super().mostrar_info() + f"| Numero edicion: {self.numero_edicion}"


'''Estructura de datos

Crea un diccionario llamado biblioteca donde:

• la clave sea una categoría, por ejemplo "novela", "ciencia", "historia"

• el valor sea una lista de objetos (Libro o Revista)

Ejemplo conceptual:

biblioteca = {
    "novela": [objeto1, objeto2],
    "ciencia": [objeto3]
}
'''


biblioteca = {
    "novela": [
        Libro("Cien Años de Soledad", "Gabriel García Márquez", 417),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863),
        Libro("La Sombra del Viento", "Carlos Ruiz Zafón", 565)  # Libro extra
    ],
    "ciencia": [
        Libro("Breve Historia del Tiempo", "Stephen Hawking", 256),
        Revista("Investigación y Ciencia", 150, "Abril 2026"),     # Revista 1
        Revista("National Geographic", 202, "Mayo 2026")          # Revista 2
    ],
    "historia": [
        Libro("Sapiens: De Animales a Dioses", "Yuval Noah Harari", 498),
        Revista("Historia Hoy", 34, "Marzo 2026")
    ],
    "ciencia ficción": [
        Libro("Dune", "Frank Herbert", 412)
    ]
}

# Añadir material de otra manera 

libro1 = Libro("El principito", "Antoine", 100)
libro2 = Libro("Don quijote", "Cervantes", 1200)
revista1 = Revista("elMundo", "Anonymous", 3)
revista2 = Revista("el pais", "Anonymous", 30)

#Añadir en la categoria historia
biblioteca["historia"] = [libro1, revista1] # Es una lista a la que añadirmos objeto
biblioteca["novela"] = [libro2,revista2]



'''
### Funcionalidades que debe tener el programa

1. Añadir materiales a la biblioteca dentro de una categoría.

2. Mostrar todos los materiales agrupados por categoría.

3. Buscar un material por título.

4. Mostrar cuántos materiales hay en cada categoría.

5. Crear una función que recorra toda la biblioteca y devuelva una lista con todos los títulos.

6. Controlar errores con excepciones:

    * si se intenta buscar una categoría que no existe

    * si se introduce un dato incorrecto, por ejemplo páginas con texto en vez de número

    * si se busca un título que no está en la biblioteca

7. Usar try, except, else y finally al menos una vez.

8. Crear un menú sencillo para ejecutar las opciones.

'''
    
# ################### METODOS PARA EL MENÚ ###########################

# Clase expcecion par acontrolar que es numero
class LibroException(Exception):
    pass

# 1 Metodo para añadir materiales

def anadir_material(biblioteca):
  print(f"Nuevo libro.", end = f"\n {"-"*20} \n")
  # Preguntar si es libro o revista
  tipo = input(f"Tipo de material (libro/revista): ").strip().lower() # Pedir tipo
  genero = input(f"Generao: ").strip().lower()  #Pedir genero
  titulo = input("Titulo del libro: ").strip().lower() #Pedir titulo
  autor = input("Autor: ").strip().lower() #Pedir autor
  
  # Creamos el libro o revista dependiendo
  if tipo == "libro":
    # Controlar que usuario introduce un numero.
    if num_paginas.isdigit:   # Comprobar que es digito. 
        num_paginas = int(input("Nº paginas del libro: "))
    else:
        raise ValueError
    
    # Metodo uso del tryexcept para controlar intro num_paginas. .
    try :
        if num_paginas < 0:
            raise LibroException("Esto es una excepccion personalizada. Num no puede ser negativo")
        
    except (LibroException, TypeError) as e: 
            print(e)
    except:
        print("Error desconocido")
    
    item = Libro(titulo, autor, num_paginas)
  elif tipo == "revista":
    numero_edicion = int(input("Nº edicion es: "))
    item = Revista(titulo, autor, numero_edicion)
  else:
    print("Tipo material no valido.")

  #biblioteca[genero].append(item)
  biblioteca.setdefault(genero, []).append(item) # Comprueba si existe el genero si no lo crea
  print(f"El material {item.titulo} se ha añadido correctamente.")

# 2. Metodo par mostrar los materiales agrupados por categoria
def mostrar_biblioteca(biblioteca:dict):
  for categoria, items in biblioteca.items():
    print(f"\nCategoría: {categoria}")
    for item in items:
        print(f"  - {item.mostrar_info()}")

# 3.Busqueda por titulo.
def buscar_por_titulo():
  titulo_a_buscar = "El principito"
  # biblioteca.values devuelve lista de listas con valores. 
  
  lista_listas_materiales = biblioteca.values()
  for lista_materiales in lista_listas_materiales:
    for material in lista_materiales:
        if material.titulo == titulo_a_buscar:
            print(material.mostrar_info())
            
## Controlar si no esta la kety. Diferencia entre get y biblioteca["key"]
print(biblioteca.get("Musica")) # Devuelve none
print(biblioteca["musica"]) # Devuelve excepcion "KeyError"

 # Lo mejor para comprobar seria si la categoria esta en la lista de categoria con un if
# if "musica" in biblioteca:
# Controlar con try except:
try:
    print(biblioteca["musica"])
except: # Si no expecificamos excepcion coge la primera de la clase excepcion
    print("No existe la categoria")
    
        

# 4.Contar material por catergoria
def contar_por_categoria():
  for categoria, materiales in biblioteca.items():
      print(f"Categoria: {categoria}")
      print(f"Numero d ematerialse : {len(materiales)}")
 
    # otra manera de hacero
   #for categoria in biblioteca: #Esto es lo mismo que biblioteca.keys
    #    print(f"CAtegoria: {categoria}")
     #   print(f"Numero de materiales: {len(biblioteca[categoria])}")    

# 5.Lista con todos los titulos
def lista_todos_titulos():
  titulos = []
  for categoria in biblioteca:
    for material in biblioteca[categoria]:
        titulos.append(material .titulo)
    return titulos


 # ################################ MENÚ PRINCIPAL #############################
 # Menú principal
def menu_biblioteca():
    texto_menu = """
============================================================
                  Menú Biblioteca
============================================================

  1. Añadir material
  2. Mostrar todos los materiales
  3. Buscar material por título
  4. Contar materiales por categoría
  5. Listar todos los títulos
  0. Salir
"""
    while True: #Es peligrosoo hacerlo en app real. Mejor variable que se le cambie el valor. 
        print(texto_menu)
        opcion = input("Elige una opción: ").strip()
        if opcion == "0": # Mejor un match - case
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            anadir_material(biblioteca)
        elif opcion == "2":
            mostrar_biblioteca(biblioteca)
        elif opcion == "3":
            buscar_por_titulo()
        elif opcion == "4":
            contar_por_categoria()
        elif opcion == "5":
            lista_todos_titulos()
        else:
            print("Opción no válida")

        input("\nPulsa Enter para continuar...")

menu_biblioteca()   
    

### ############ Extra: Clase Usuario

'''

Extra opcional Añade una clase Usuario con:

• nombre

• materiales_prestados → lista de objetos

Y crea métodos para:

• prestar un material

• devolver un material

Controla con excepciones que:

• no se pueda prestar un material que no exista

• no se pueda devolver un material no prestado
'''

class Usuario: 
  def __init__(self,nombre):
    self.nombre = nombre 
    self.materiales_prestados = []
  
  def prestar_material(self,material):
    #try:
    self.materiales_prestados.append(material)
    #except:  
        
def devolver_material(self, material):
        self.materiales_presatdos.remove(material)

usuario1 = Usuario("usuario1")
usuario1.prestar_material(biblioteca["novela"][1])

print(usuario1.material_presatado[0].titulo)