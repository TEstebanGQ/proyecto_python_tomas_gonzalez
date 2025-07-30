from config import RUTA_LIBROS
from controllers.elemento import agregarElemento, listarElementos, buscarElemento, editarElemento, eliminarElemento

# ✅ Agregar un nuevo libro
def agregarLibro():
    agregarElemento(
        RUTA_LIBROS,               # Ruta del archivo JSON
        "Libro",                   # Nombre del tipo de elemento
        ["titulo", "autor", "genero", "valoracion"]  # Campos requeridos
    )

# ✅ Listar todos los libros
def listarLibros():
    listarElementos(
        RUTA_LIBROS,
        "Libros"
    )

# ✅ Buscar libros (por título, autor o género)
def buscarLibro():
    buscarElemento(
        RUTA_LIBROS,
        "Libros"
    )

# ✅ Editar datos de un libro existente
def editarLibro():
    editarElemento(
        RUTA_LIBROS,
        "Libro",
        ["titulo", "autor", "genero", "valoracion"]
    )

# ✅ Eliminar un libro por ID
def eliminarLibro():
    eliminarElemento(
        RUTA_LIBROS,
        "Libro"
    )
