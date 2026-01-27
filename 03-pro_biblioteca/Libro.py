class Libro():
    def __init__(self, isbn, titulo, autor,copias_disponibles):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles
       
    def obtener_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}, Género: {self.genero}"