import json
import os
from tabulate import tabulate
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from models.elemento import Elemento
from utils.validata import validar_valoracion, obtener_entrada_valida, validar_solo_letras


# Ruta fija en la carpeta data
DATA_PATH = "data/libros.json"

# Crear carpeta data si no existe
os.makedirs("data", exist_ok=True)

# Cargar libros desde JSON
def cargar_libros():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

# Guardar libros en JSON
def guardar_libros(libros):
    with open(DATA_PATH, "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)

# Mostrar libros usando tabulate
def mostrar_libros():
    libros = cargar_libros()
    if not libros:
        print("No hay libros registrados.")
    else:
        print(tabulate(libros, headers="keys", tablefmt="grid"))

# Para validar solo letras
def agregar_libro():
    limpiar_pantalla()
    libros = cargar_libros()

    titulo = input("Título del libro: ").strip()
    while titulo == "":
        print("❌ El título no puede estar vacío.")
        titulo = input("Título del libro: ").strip()

    autor = validar_solo_letras("Autor del libro")
    genero = validar_solo_letras("Género del libro")
    valoracion = validar_valoracion()

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    libros.append(nuevo_libro)
    guardar_libros(libros)
    print("✅ Libro agregado correctamente.")
    pausar_pantalla()




# Eliminar un libro
def eliminar_libro():
    libros = cargar_libros()
    if not libros:
        print("No hay libros registrados.")
        pausar_pantalla()
        return
        
    mostrar_libros()
    
    try:
        indice = int(input("Número del libro a eliminar: ")) - 1
        if 0 <= indice < len(libros):
            libro_eliminado = libros.pop(indice)
            guardar_libros(libros)
            print(f"✅ Libro '{libro_eliminado['titulo']}' eliminado.")
        else:
            print("❌ Índice no válido.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")
    
    pausar_pantalla()

# FUNCIONES PARA LA COLECCIÓN UNIFICADA
def listar_libros(coleccion):
    """Lista los libros de la colección unificada"""
    libros = [elem for elem in coleccion if elem.tipo == 'libro']
    
    if not libros:
        print("📚 No hay libros en la colección.")
        pausar_pantalla()
        return
    
    # Preparar datos para tabulate
    datos_tabla = []
    for libro in libros:
        valoracion_str = f"{libro.valoracion}/10" if libro.valoracion else "Sin valorar"
        datos_tabla.append({
            'ID': libro.id,
            'Título': libro.titulo,
            'Autor': libro.autor_director_artista,
            'Género': libro.genero,
            'Valoración': valoracion_str,
            'Fecha': libro.fecha_agregado.split()[0]  # Solo la fecha, sin hora
        })
    
    print(f"📚 LIBROS EN LA COLECCIÓN ({len(libros)})")
    print("=" * 80)
    print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    print(f"\nTotal de libros: {len(libros)}")
    pausar_pantalla()

def crear_libro(coleccion, gestor_archivos):
    """Crea un nuevo libro en la colección unificada"""
    limpiar_pantalla()
    print("=== AGREGAR NUEVO LIBRO ===")
    print("-" * 40)
    
    # Obtener datos del libro
    titulo = obtener_entrada_valida("Título del libro: ")
    autor = obtener_entrada_valida("Autor del libro: ")
    genero = obtener_entrada_valida("Género del libro: ")
    
    # Solicitar valoración
    while True:
        valoracion_input = input("Valoración (1-10, opcional - presiona Enter para omitir): ")
        if not valoracion_input.strip():
            valoracion = None
            break
        
        valoracion = validar_valoracion(valoracion_input)
        if valoracion is not False:
            break
    
    # Crear el elemento
    libro = Elemento(titulo, autor, genero, valoracion, "libro")
    coleccion.append(libro)
    
    # Guardar la colección
    if gestor_archivos.guardar_coleccion(coleccion):
        print(f"✅ Libro '{titulo}' agregado exitosamente.")
        print(f"📚 ID asignado: {libro.id}")
    else:
        print("❌ Error al guardar el libro.")
        coleccion.remove(libro)  # Revertir si no se pudo guardar
    
    pausar_pantalla()