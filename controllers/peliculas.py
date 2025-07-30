import json
import os
from tabulate import tabulate
from utils.screenControllers import limpiar_pantalla

DATA_PATH = "data/peliculas.json"
os.makedirs("data", exist_ok=True)

def cargar_peliculas():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_peliculas(peliculas):
    with open(DATA_PATH, "w", encoding="utf-8") as archivo:
        json.dump(peliculas, archivo, indent=4)

def mostrar_peliculas():
    peliculas = cargar_peliculas()
    if not peliculas:
        print("No hay películas registradas.")
    else:
        print(tabulate(peliculas, headers="keys", tablefmt="grid"))

def agregar_pelicula():
    limpiar_pantalla()
    peliculas = cargar_peliculas()

    titulo = input("Título de la película: ")
    director = input("Director: ")

    nueva_pelicula = {
        "titulo": titulo,
        "director": director
    }
    peliculas.append(nueva_pelicula)
    guardar_peliculas(peliculas)
    print("✅ Película agregada correctamente.")

def eliminar_pelicula():
    peliculas = cargar_peliculas()
    mostrar_peliculas()

    indice = int(input("Número de la película a eliminar: ")) - 1
    if 0 <= indice < len(peliculas):
        peliculas.pop(indice)
        guardar_peliculas(peliculas)
        print("✅ Película eliminada.")
    else:
        print("❌ Índice no válido.")
