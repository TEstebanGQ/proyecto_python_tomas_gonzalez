from config import RUTA_LIBROS
from controllers.elemento import agregarElemento, listarElementos, buscarElemento, editarElemento, eliminarElemento


def agregarLibro():
    agregarElemento(
        RUTA_LIBROS,               # Ruta del archivo JSON
        "Libro",                   # Nombre del tipo de elemento
        ["titulo", "autor", "genero", "valoracion"]  # Campos requeridos
    )

def listarLibros():
    listarElementos(
        RUTA_LIBROS,
        "Libros"
    )

def buscarLibro():
    buscarElemento(
        RUTA_LIBROS,
        "Libros"
    )

def editarLibro():
    editarElemento(
        RUTA_LIBROS,
        "Libro",
        ["titulo", "autor", "genero", "valoracion"]
    )

def eliminarLibro():
    eliminarElemento(
        RUTA_LIBROS,
        "Libro"
    )
