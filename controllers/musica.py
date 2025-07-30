import json
import os
from tabulate import tabulate
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from models.elemento import Elemento
from utils.validata import validar_valoracion, obtener_entrada_valida, validar_solo_letras

DATA_PATH = "data/musica.json"
os.makedirs("data", exist_ok=True)

def cargar_musica():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_musica(musica):
    with open(DATA_PATH, "w", encoding="utf-8") as archivo:
        json.dump(musica, archivo, indent=4, ensure_ascii=False)

def mostrar_musica():
    musica = cargar_musica()
    if not musica:
        print("No hay canciones registradas.")
    else:
        print(tabulate(musica, headers="keys", tablefmt="grid"))

def agregar_musica():
    limpiar_pantalla()
    musica = cargar_musica()

    titulo = input("Título de la canción: ").strip()
    while titulo == "":
        print("❌ El título no puede estar vacío.")
        titulo = input("Título de la canción: ").strip()

    artista = validar_solo_letras("Artista")
    genero = validar_solo_letras("Género musical")
    valoracion = validar_valoracion()

    nueva_cancion = {
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "valoracion": valoracion
    }
    musica.append(nueva_cancion)
    guardar_musica(musica)
    print("✅ Canción agregada correctamente.")
    pausar_pantalla()

def eliminar_musica():
    musica = cargar_musica()
    if not musica:
        print("No hay canciones registradas.")
        pausar_pantalla()
        return
        
    mostrar_musica()
    
    try:
        indice = int(input("Número de la canción a eliminar: ")) - 1
        if 0 <= indice < len(musica):
            cancion_eliminada = musica.pop(indice)
            guardar_musica(musica)
            print(f"✅ Canción '{cancion_eliminada['titulo']}' eliminada.")
        else:
            print("❌ Índice no válido.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")
    
    pausar_pantalla()

# FUNCIONES PARA LA COLECCIÓN UNIFICADA
def listar_musica(coleccion):
    """Lista la música de la colección unificada"""
    musica = [elem for elem in coleccion if elem.tipo == 'música']
    
    if not musica:
        print("🎵 No hay música en la colección.")
        pausar_pantalla()
        return
    
    # Preparar datos para tabulate
    datos_tabla = []
    for cancion in musica:
        valoracion_str = f"{cancion.valoracion}/10" if cancion.valoracion else "Sin valorar"
        datos_tabla.append({
            'ID': cancion.id,
            'Título': cancion.titulo,
            'Artista': cancion.autor_director_artista,
            'Género': cancion.genero,
            'Valoración': valoracion_str,
            'Fecha': cancion.fecha_agregado.split()[0]
        })
    
    print(f"🎵 MÚSICA EN LA COLECCIÓN ({len(musica)})")
    print("=" * 80)
    print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    print(f"\nTotal de canciones: {len(musica)}")
    pausar_pantalla()

def crear_musica(coleccion, gestor_archivos):
    """Crea una nueva canción en la colección unificada"""
    limpiar_pantalla()
    print("=== AGREGAR NUEVA CANCIÓN ===")
    print("-" * 40)
    
    # Obtener datos de la canción
    titulo = obtener_entrada_valida("Título de la canción: ")
    artista = obtener_entrada_valida("Artista: ")
    genero = obtener_entrada_valida("Género musical: ")
    
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
    cancion = Elemento(titulo, artista, genero, valoracion, "música")
    coleccion.append(cancion)
    
    # Guardar la colección
    if gestor_archivos.guardar_coleccion(coleccion):
        print(f"✅ Canción '{titulo}' agregada exitosamente.")
        print(f"🎵 ID asignado: {cancion.id}")
    else:
        print("❌ Error al guardar la canción.")
        coleccion.remove(cancion)
    
    pausar_pantalla()