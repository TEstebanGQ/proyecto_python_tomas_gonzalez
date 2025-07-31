# config.py - Configuraciones del Administrador de Colección
"""
Archivo de configuración centralizada para el Administrador de Colección.
Define rutas, constantes y validaciones principales del sistema.
"""

import os
import platform


RUTA_LIBROS = "data/libros.json"
RUTA_PELICULAS = "data/peliculas.json"
RUTA_MUSICA = "data/musica.json"

TIPOS_ELEMENTOS = {
    'libro': {
        'nombre': 'Libro',
        'plural': 'Libros',
        'emoji': '📚',
        'campos': {
            'autor_director_artista': 'Autor',
            'genero': 'Género literario'
        }
    },
    'película': {
        'nombre': 'Película',
        'plural': 'Películas',
        'emoji': '🎬',
        'campos': {
            'autor_director_artista': 'Director',
            'genero': 'Género cinematográfico'
        }
    },
    'música': {
        'nombre': 'Música',
        'plural': 'Música',
        'emoji': '🎵',
        'campos': {
            'autor_director_artista': 'Artista',
            'genero': 'Género musical'
        }
    }
}


VALORACION_MIN = 1
VALORACION_MAX = 10


LONGITUD_CAMPOS = {
    'titulo': {'min': 1, 'max': 200},
    'autor_director_artista': {'min': 1, 'max': 100},
    'genero': {'min': 1, 'max': 50}
}

SISTEMA_OPERATIVO = platform.system().lower()
if SISTEMA_OPERATIVO == 'windows':
    COMANDO_LIMPIAR = 'cls'
    COMANDO_PAUSA = 'pause'
else:  
    COMANDO_LIMPIAR = 'clear'
    COMANDO_PAUSA = 'read -p \"Presione Enter para continuar...\"'

def crearDirectorios():
    """Crea la carpeta data si no existe"""
    if not os.path.exists("data"):
        os.makedirs("data")


crearDirectorios()
