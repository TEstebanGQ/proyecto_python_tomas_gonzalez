from config import RUTA_MUSICA
from controllers.elemento import agregarElemento, listarElementos, buscarElemento, editarElemento, eliminarElemento
def agregarMusica():
    agregarElemento(
        RUTA_MUSICA,                 # Ruta del archivo JSON
        "Música",                    # Tipo de elemento
        ["titulo", "artista", "genero", "valoracion"]  # Campos requeridos
    )
def listarMusica():
    listarElementos(
        RUTA_MUSICA,
        "Música"
    )

def buscarMusica():
    buscarElemento(
        RUTA_MUSICA,
        "Música"
    )

def editarMusica():
    editarElemento(
        RUTA_MUSICA,
        "Música",
        ["titulo", "artista", "genero", "valoracion"]
    )

def eliminarMusica():
    eliminarElemento(
        RUTA_MUSICA,
        "Música"
    )
