import Libro
import Usuario
import Prestamo

class Biblioteca():
    def __init__(self, libros=[]):
        
        self.libros = []
        self.prestamos = []
        self.usuarios = []

    def resgistrar_libro(self, libro):
        self.libros.append(libro)

    def resgistrar_ejemplar(self, isbn, titulo, autor):
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.copias_disponibles += 1
                return True
        self.libros.append(Libro(isbn, titulo, autor, 1))

    def registrar_usuario(self, nombre):
        self.usuarios.append(Usuario(len(self.usuarios) + 1, nombre))
        
    def mostrar_disponibles(self, isbn):
        salida = "Nuestros libros disponibles son:\n"
        for libro in self.libros:
            if libro.copias_disponibles > 0:
                salida += f"{libro.titulo} de {libro.autor} - Copias disponibles: {libro.copias_disponibles}\n"    
        print(salida)
        
    def prestar_libro(self,usuario,libro):
        if libro in self.libros and usuario in self.usuarios:
            prestamo = Prestamo(usuario,libro)
            self.prestamos.append(prestamo)
            return prestamo
        return False
    
    def devolver_libro(self,prestamo):
        if prestamo in self.prestamos:
            self.prestamos.remove(prestamo)

    def listar_libros(self):
        for libro in self.libros:
            print(libro.obtener_informacion())