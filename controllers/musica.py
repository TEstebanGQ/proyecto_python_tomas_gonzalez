from config import RUTA_MUSICA
from models.elemento import agregarElemento, listarElementos, buscarElemento, editarElemento, eliminarElemento

# ✅ Agregar una nueva canción
def agregarMusica():
    agregarElemento(
        RUTA_MUSICA,                 # Ruta del archivo JSON
        "Música",                    # Tipo de elemento
        ["titulo", "artista", "genero", "valoracion"]  # Campos requeridos
    )

# ✅ Listar todas las canciones
def listarMusica():
    listarElementos(
        RUTA_MUSICA,
        "Música"
    )

# ✅ Buscar música (por título, artista o género)
def buscarMusica():
    buscarElemento(
        RUTA_MUSICA,
        "Música"
    )

# ✅ Editar datos de una canción
def editarMusica():
    editarElemento(
        RUTA_MUSICA,
        "Música",
        ["titulo", "artista", "genero", "valoracion"]
    )

# ✅ Eliminar una canción por ID
def eliminarMusica():
    eliminarElemento(
        RUTA_MUSICA,
        "Música"
    )
