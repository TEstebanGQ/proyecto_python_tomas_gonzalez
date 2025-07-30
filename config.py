# config.py - Configuraciones del Administrador de Colección
"""
Archivo de configuración centralizada para el Administrador de Colección.
Aquí se definen todas las constantes y configuraciones del sistema.
"""

import os
from datetime import datetime
# 📂 config.py

# ✅ Rutas de archivos JSON
RUTA_LIBROS = "data/libros.json"
RUTA_PELICULAS = "data/peliculas.json"
RUTA_MUSICA = "data/musica.json"

# ✅ Configuración general
TITULO_APP = "Administrador de Colección"
VERSION_APP = "1.0"

# ================================
# INFORMACIÓN DE LA APLICACIÓN
# ================================
VERSION = "1.0.0"
NOMBRE_APP = "Administrador de Colección"
DESCRIPCION = "Sistema de gestión de colecciones personales de libros, películas y música"
AUTOR = "Tu Nombre"
FECHA_CREACION = "2024"

# ================================
# CONFIGURACIÓN DE ARCHIVOS
# ================================
# Archivo principal donde se guarda la colección
ARCHIVO_COLECCION_DEFAULT = 'coleccion.json'

# Carpeta para backups automáticos
CARPETA_BACKUPS = 'backups'

# Carpeta para archivos temporales
CARPETA_TEMP = 'temp'

# Extensión de archivos de backup
EXTENSION_BACKUP = '.backup.json'

# Codificación de archivos
ENCODING = 'utf-8'

# ================================
# TIPOS DE ELEMENTOS VÁLIDOS
# ================================
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

# ================================
# CONFIGURACIÓN DE VALORACIONES
# ================================
VALORACION_MIN = 1
VALORACION_MAX = 10
VALORACION_DECIMALES = 1  # Número de decimales permitidos

# Mensajes para valoraciones
VALORACION_MESSAGES = {
    'prompt': f"Valoración ({VALORACION_MIN}-{VALORACION_MAX}, opcional - presiona Enter para omitir): ",
    'error_rango': f"La valoración debe estar entre {VALORACION_MIN} y {VALORACION_MAX}",
    'error_formato': "La valoración debe ser un número"
}

# ================================
# CONFIGURACIÓN DE INTERFAZ
# ================================
# Caracteres para decoración de menús
SEPARADOR_MENU = '='
SEPARADOR_SECCION = '-'
ANCHO_MENU = 40
ANCHO_SEPARADOR = 80

# Colores de consola (códigos ANSI)
COLORES = {
    'RESET': '\033[0m',
    'ROJO': '\033[91m',
    'VERDE': '\033[92m',
    'AMARILLO': '\033[93m',
    'AZUL': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'BLANCO': '\033[97m'
}

# Emojis para mensajes
EMOJIS = {
    'exito': '✅',
    'error': '❌',
    'info': 'ℹ️',
    'advertencia': '⚠️',
    'pregunta': '❓',
    'buscar': '🔍',
    'editar': '✏️',
    'eliminar': '🗑️',
    'guardar': '💾',
    'cargar': '📂',
    'estadisticas': '📊'
}

# ================================
# CONFIGURACIÓN DE VALIDACIONES
# ================================
# Longitudes mínimas y máximas para campos
LONGITUD_CAMPOS = {
    'titulo': {'min': 1, 'max': 200},
    'autor_director_artista': {'min': 1, 'max': 100},
    'genero': {'min': 1, 'max': 50}
}

# Caracteres no permitidos en títulos
CARACTERES_PROHIBIDOS = ['<', '>', ':', '"', '|', '?', '*', '\\', '/']

# ================================
# CONFIGURACIÓN DE BÚSQUEDA
# ================================
# Número máximo de resultados a mostrar
MAX_RESULTADOS_BUSQUEDA = 50

# Búsqueda insensible a mayúsculas/minúsculas
BUSQUEDA_INSENSIBLE = True

# ================================
# CONFIGURACIÓN DE BACKUPS
# ================================
# Número máximo de backups a mantener
MAX_BACKUPS = 10

# Crear backup automático al guardar
BACKUP_AUTOMATICO = True

# Formato de fecha para nombres de backup
FORMATO_FECHA_BACKUP = "%Y%m%d_%H%M%S"

# ================================
# MENSAJES DEL SISTEMA
# ================================
MENSAJES = {
    'bienvenida': f"""
{SEPARADOR_MENU * ANCHO_MENU}
    {NOMBRE_APP}    
{SEPARADOR_MENU * ANCHO_MENU}
    Versión: {VERSION}
    Gestiona tu colección personal
{SEPARADOR_MENU * ANCHO_MENU}
""",
    
    'despedida': f"""
{SEPARADOR_MENU * 70}
Gracias por usar {NOMBRE_APP}.
Su colección ha sido guardada automáticamente.
{SEPARADOR_MENU * 70}
""",
    
    'coleccion_vacia': "La colección está vacía. ¡Añade algunos elementos!",
    'elemento_no_encontrado': "No se encontró el elemento especificado.",
    'operacion_cancelada': "Operación cancelada por el usuario.",
    'guardado_exitoso': "Colección guardada exitosamente.",
    'carga_exitosa': "Colección cargada exitosamente.",
    'error_archivo': "Error al acceder al archivo de datos.",
    'entrada_invalida': "Entrada inválida. Intente nuevamente."
}

# ================================
# CONFIGURACIÓN DE DESARROLLO
# ================================
# Modo debug (muestra información adicional)
DEBUG = False

# Logging activado
LOGGING_ACTIVO = False

# Archivo de log
ARCHIVO_LOG = 'app.log'

# ================================
# FUNCIONES DE CONFIGURACIÓN
# ================================

def crear_directorios():
    """Crea los directorios necesarios si no existen"""
    directorios = [CARPETA_BACKUPS, CARPETA_TEMP]
    
    for directorio in directorios:
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                if DEBUG:
                    print(f"Directorio '{directorio}' creado.")
            except OSError as e:
                print(f"Error al crear directorio '{directorio}': {e}")

def obtener_configuracion_tipo(tipo):
    """
    Obtiene la configuración específica para un tipo de elemento
    
    Args:
        tipo (str): El tipo de elemento ('libro', 'película', 'música')
    
    Returns:
        dict: Configuración del tipo o None si no existe
    """
    return TIPOS_ELEMENTOS.get(tipo.lower())

def validar_configuracion():
    """Valida que la configuración sea coherente"""
    errores = []
    
    # Validar rangos de valoración
    if VALORACION_MIN >= VALORACION_MAX:
        errores.append("VALORACION_MIN debe ser menor que VALORACION_MAX")
    
    # Validar tipos de elementos
    if not TIPOS_ELEMENTOS:
        errores.append("Debe haber al menos un tipo de elemento definido")
    
    # Validar longitudes de campos
    for campo, config in LONGITUD_CAMPOS.items():
        if config['min'] >= config['max']:
            errores.append(f"Longitud mínima de '{campo}' debe ser menor que la máxima")
    
    if errores:
        print("⚠️ Errores en configuración:")
        for error in errores:
            print(f"  - {error}")
        return False
    
    return True

def mostrar_configuracion():
    """Muestra la configuración actual (útil para debug)"""
    if not DEBUG:
        return
    
    print("\n📋 CONFIGURACIÓN ACTUAL:")
    print(f"  Aplicación: {NOMBRE_APP} v{VERSION}")
    print(f"  Archivo de datos: {ARCHIVO_COLECCION_DEFAULT}")
    print(f"  Tipos soportados: {list(TIPOS_ELEMENTOS.keys())}")
    print(f"  Rango valoración: {VALORACION_MIN}-{VALORACION_MAX}")
    print(f"  Backup automático: {'Sí' if BACKUP_AUTOMATICO else 'No'}")
    print(f"  Max resultados búsqueda: {MAX_RESULTADOS_BUSQUEDA}")

def obtener_info_version():
    """Retorna información de la versión"""
    return {
        'version': VERSION,
        'nombre': NOMBRE_APP,
        'descripcion': DESCRIPCION,
        'autor': AUTOR,
        'fecha': FECHA_CREACION
    }

# ================================
# INICIALIZACIÓN
# ================================

# Crear directorios al importar el módulo
crear_directorios()

# Validar configuración al importar
if not validar_configuracion():
    print("❌ Hay errores en la configuración. Revise config.py")

# Mostrar configuración si está en modo debug
mostrar_configuracion()

# ================================
# CONFIGURACIONES ESPECÍFICAS DEL SISTEMA
# ================================

# Detectar sistema operativo para comandos específicos
import platform
SISTEMA_OPERATIVO = platform.system().lower()

# Configuración específica por OS
if SISTEMA_OPERATIVO == 'windows':
    COMANDO_LIMPIAR = 'cls'
    COMANDO_PAUSA = 'pause'
else:  # Linux, macOS, etc.
    COMANDO_LIMPIAR = 'clear'
    COMANDO_PAUSA = 'read -p "Presione Enter para continuar..."'

# ================================
# CONFIGURACIÓN DE EXPORTACIÓN
# ================================
FORMATOS_EXPORTACION = {
    'json': {'extension': '.json', 'nombre': 'JSON'},
    'csv': {'extension': '.csv', 'nombre': 'CSV'},
    'txt': {'extension': '.txt', 'nombre': 'Texto plano'}
}

# ================================
# CONFIGURACIÓN DE GÉNEROS PREDEFINIDOS
# ================================
GENEROS_PREDEFINIDOS = {
    'libro': [
        'Ficción', 'No ficción', 'Fantasía', 'Ciencia ficción', 'Misterio',
        'Romance', 'Thriller', 'Historia', 'Biografía', 'Autoayuda',
        'Poesía', 'Drama', 'Aventura', 'Terror', 'Humor'
    ],
    'película': [
        'Acción', 'Aventura', 'Comedia', 'Drama', 'Terror', 'Ciencia ficción',
        'Fantasía', 'Romance', 'Thriller', 'Misterio', 'Animación',
        'Documental', 'Musical', 'Guerra', 'Western'
    ],
    'música': [
        'Rock', 'Pop', 'Jazz', 'Blues', 'Country', 'Hip-hop', 'Electrónica',
        'Clásica', 'Folk', 'Reggae', 'Metal', 'Punk', 'R&B', 'Soul', 'Funk'
    ]
}

# ================================
# FIN DE CONFIGURACIÓN
# ================================

if __name__ == "__main__":
    # Si se ejecuta directamente, mostrar información de configuración
    print(f"📋 {NOMBRE_APP} - Configuración")
    print(f"Versión: {VERSION}")
    print(f"Sistema: {SISTEMA_OPERATIVO.title()}")
    print(f"Archivo de datos: {ARCHIVO_COLECCION_DEFAULT}")
    print(f"Tipos soportados: {len(TIPOS_ELEMENTOS)}")
    print("\n✅ Configuración cargada correctamente.")