from config import RUTA_PELICULAS
from models.elemento import agregarElemento, listarElementos, buscarElemento, editarElemento, eliminarElemento

# ✅ Agregar una nueva película
def agregarPelicula():
    agregarElemento(
        RUTA_PELICULAS,                # Ruta del archivo JSON
        "Película",                    # Tipo de elemento
        ["titulo", "director", "genero", "valoracion"]  # Campos requeridos
    )

# ✅ Listar todas las películas
def listarPeliculas():
    listarElementos(
        RUTA_PELICULAS,
        "Películas"
    )

# ✅ Buscar películas (por título, director o género)
def buscarPelicula():
    buscarElemento(
        RUTA_PELICULAS,
        "Películas"
    )

# ✅ Editar datos de una película
def editarPelicula():
    editarElemento(
        RUTA_PELICULAS,
        "Película",
        ["titulo", "director", "genero", "valoracion"]
    )

# ✅ Eliminar una película por ID
def eliminarPelicula():
    eliminarElemento(
        RUTA_PELICULAS,
        "Película"
    )
