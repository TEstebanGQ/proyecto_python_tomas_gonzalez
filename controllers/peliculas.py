import json
import os
from tabulate import tabulate
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from models.elemento import Elemento
from utils.validata import validar_valoracion, obtener_entrada_valida, validar_solo_letras

DATA_PATH = "data/peliculas.json"
os.makedirs("data", exist_ok=True)

def cargar_peliculas():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_peliculas(peliculas):
    with open(DATA_PATH, "w", encoding="utf-8") as archivo:
        json.dump(peliculas, archivo, indent=4, ensure_ascii=False)

def mostrar_peliculas():
    peliculas = cargar_peliculas()
    if not peliculas:
        print("No hay películas registradas.")
    else:
        print(tabulate(peliculas, headers="keys", tablefmt="grid"))

def agregar_pelicula():
    limpiar_pantalla()
    peliculas = cargar_peliculas()

    titulo = input("Título de la película: ").strip()
    while titulo == "":
        print("❌ El título no puede estar vacío.")
        titulo = input("Título de la película: ").strip()

    director = validar_solo_letras("Director")
    genero = validar_solo_letras("Género de la película")
    valoracion = validar_valoracion()

    nueva_pelicula = {
        "titulo": titulo,
        "director": director,
        "genero": genero,
        "valoracion": valoracion
    }
    peliculas.append(nueva_pelicula)
    guardar_peliculas(peliculas)
    print("✅ Película agregada correctamente.")
    pausar_pantalla()

def eliminar_pelicula():
    peliculas = cargar_peliculas()
    if not peliculas:
        print("No hay películas registradas.")
        pausar_pantalla()
        return
        
    mostrar_peliculas()
    
    try:
        indice = int(input("Número de la película a eliminar: ")) - 1
        if 0 <= indice < len(peliculas):
            pelicula_eliminada = peliculas.pop(indice)
            guardar_peliculas(peliculas)
            print(f"✅ Película '{pelicula_eliminada['titulo']}' eliminada.")
        else:
            print("❌ Índice no válido.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")
    
    pausar_pantalla()

# FUNCIONES PARA LA COLECCIÓN UNIFICADA
def listar_peliculas(coleccion):
    """Lista las películas de la colección unificada"""
    peliculas = [elem for elem in coleccion if elem.tipo == 'película']
    
    if not peliculas:
        print("🎬 No hay películas en la colección.")
        pausar_pantalla()
        return
    
    # Preparar datos para tabulate
    datos_tabla = []
    for pelicula in peliculas:
        valoracion_str = f"{pelicula.valoracion}/10" if pelicula.valoracion else "Sin valorar"
        datos_tabla.append({
            'ID': pelicula.id,
            'Título': pelicula.titulo,
            'Director': pelicula.autor_director_artista,
            'Género': pelicula.genero,
            'Valoración': valoracion_str,
            'Fecha': pelicula.fecha_agregado.split()[0]
        })
    
    print(f"🎬 PELÍCULAS EN LA COLECCIÓN ({len(peliculas)})")
    print("=" * 80)
    print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    print(f"\nTotal de películas: {len(peliculas)}")
    pausar_pantalla()

def crear_pelicula(coleccion, gestor_archivos):
    """Crea una nueva película en la colección unificada"""
    limpiar_pantalla()
    print("=== AGREGAR NUEVA PELÍCULA ===")
    print("-" * 40)
    
    # Obtener datos de la película
    titulo = obtener_entrada_valida("Título de la película: ")
    director = obtener_entrada_valida("Director de la película: ")
    genero = obtener_entrada_valida("Género de la película: ")
    
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
    pelicula = Elemento(titulo, director, genero, valoracion, "película")
    coleccion.append(pelicula)
    
    # Guardar la colección
    if gestor_archivos.guardar_coleccion(coleccion):
        print(f"✅ Película '{titulo}' agregada exitosamente.")
        print(f"🎬 ID asignado: {pelicula.id}")
    else:
        print("❌ Error al guardar la película.")
        coleccion.remove(pelicula)
    
    pausar_pantalla()