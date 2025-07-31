from config import RUTA_PELICULAS
from controllers.elemento import agregarElemento, listarElementos, buscarElemento, editarElemento, eliminarElemento

def agregarPelicula():
    agregarElemento(
        RUTA_PELICULAS,                # Ruta del archivo JSON
        "Película",                    # Tipo de elemento
        ["titulo", "director", "genero", "valoracion"]  # Campos requeridos
    )


def listarPeliculas():
    listarElementos(
        RUTA_PELICULAS,
        "Películas"
    )


def buscarPelicula():
    buscarElemento(
        RUTA_PELICULAS,
        "Películas"
    )

def editarPelicula():
    editarElemento(
        RUTA_PELICULAS,
        "Película",
        ["titulo", "director", "genero", "valoracion"]
    )

def eliminarPelicula():
    eliminarElemento(
        RUTA_PELICULAS,
        "Película"
    )
