import os

# Estas son las rutas donde almaceno los datos JSON de cada tipo de elemento
RUTA_LIBROS = "data/libros.json"        # Aquí guardo todos los libros
RUTA_PELICULAS = "data/peliculas.json"  # Aquí almaceno las películas
RUTA_MUSICA = "data/musica.json"        # Aquí conservo la música
RUTA_COLECCIONES = "data/colecciones.json"  # Aquí guardo los respaldos completos



TIPOS_ELEMENTOS = {
    # Configuración para libros
    'libro': {
        'nombre': 'Libro',             
        'plural': 'Libros',            
        'ruta': RUTA_LIBROS,            # Dónde guardo estos elementos
        'campos': ['titulo', 'autor', 'genero', 'valoracion'],  # Qué información almaceno
        'campo_persona': 'autor',       # El campo que identifica a la persona responsable
        'etiqueta_persona': 'Autor'     # Cómo etiqueto ese campo para el usuario
    },
    # Configuración para películas
    'película': {
        'nombre': 'Película',
        'plural': 'Películas',
        'ruta': RUTA_PELICULAS, 
        'campos': ['titulo', 'director', 'genero', 'valoracion'],
        'campo_persona': 'director',    # Para películas, la persona es el director
        'etiqueta_persona': 'Director'
    },
    # Configuración para música
    'música': {
        'nombre': 'Música',
        'plural': 'Música',             # La música no cambia en plural
        'ruta': RUTA_MUSICA,
        'campos': ['titulo', 'artista', 'genero', 'valoracion'], 
        'campo_persona': 'artista',     # Para música, la persona es el artista
        'etiqueta_persona': 'Artista'
    }
}

# Defino el rango de valoraciones que permito (1 a 5 estrellas)
VALORACION_MIN = 1  
VALORACION_MAX = 5  

ETIQUETAS_CAMPOS = {
    'titulo': 'Título',       
    'autor': 'Autor', 
    'director': 'Director',
    'artista': 'Artista',
    'genero': 'Género',        
}

def crearDirectorios():
    """
    Mi función de inicialización automática
    
    Me aseguro de que el directorio 'data' exista antes de que el sistema
    trate de guardar archivos. Si no existe, lo creo automáticamente.
    Uso exist_ok=True para evitar errores si ya existe.
    """
    os.makedirs("data", exist_ok=True)
# Ejecuto mi inicialización automáticamente cuando me importan
crearDirectorios()