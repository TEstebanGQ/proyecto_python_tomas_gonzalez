import json
import os
from tabulate import tabulate
from utils.screenControllers import limpiar_pantalla

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

# Guardar libros en JSON (sin hora)
def guardar_libros(libros):
    with open(DATA_PATH, "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4)

# Mostrar libros usando tabulate
def mostrar_libros():
    libros = cargar_libros()
    if not libros:
        print("No hay libros registrados.")
    else:
        print(tabulate(libros, headers="keys", tablefmt="grid"))

# Agregar un nuevo libro
def agregar_libro():
    limpiar_pantalla()
    libros = cargar_libros()

    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor
        # Se eliminó cualquier referencia a 'hora'
    }
    libros.append(nuevo_libro)
    guardar_libros(libros)
    print("✅ Libro agregado correctamente.")

# Eliminar un libro
def eliminar_libro():
    libros = cargar_libros()
    mostrar_libros()

    indice = int(input("Número del libro a eliminar: ")) - 1
    if 0 <= indice < len(libros):
        libros.pop(indice)
        guardar_libros(libros)
        print("✅ Libro eliminado.")
    else:
        print("❌ Índice no válido.")
