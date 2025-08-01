
import os

RUTA_LIBROS = "data/libros.json"
RUTA_PELICULAS = "data/peliculas.json"
RUTA_MUSICA = "data/musica.json"
RUTA_COLECCIONES = "data/colecciones.json"

TIPOS_ELEMENTOS = {
    'libro': {
        'nombre': 'Libro',
        'plural': 'Libros', 
        'ruta': RUTA_LIBROS,
        'campos': ['titulo', 'autor', 'genero', 'valoracion'],
        'campo_persona': 'autor',
        'etiqueta_persona': 'Autor'
    },
    'película': {
        'nombre': 'Película',
        'plural': 'Películas',
        'ruta': RUTA_PELICULAS, 
        'campos': ['titulo', 'director', 'genero', 'valoracion'],
        'campo_persona': 'director',
        'etiqueta_persona': 'Director'
    },
    'música': {
        'nombre': 'Música',
        'plural': 'Música',
        'ruta': RUTA_MUSICA,
        'campos': ['titulo', 'artista', 'genero', 'valoracion'], 
        'campo_persona': 'artista',
        'etiqueta_persona': 'Artista'
    }
}

VALORACION_MIN = 1
VALORACION_MAX = 5

ETIQUETAS_CAMPOS = {
    'titulo': 'Título',
    'autor': 'Autor', 
    'director': 'Director',
    'artista': 'Artista',
    'genero': 'Género',
    'valoracion': 'Valoración'
}



def crearDirectorios():
    os.makedirs("data", exist_ok=True)
crearDirectorios()