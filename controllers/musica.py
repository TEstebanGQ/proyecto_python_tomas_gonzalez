import json
import os
from tabulate import tabulate
from utils.screenControllers import limpiar_pantalla

DATA_PATH = "data/musica.json"
os.makedirs("data", exist_ok=True)

def cargar_musica():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_musica(musica):
    with open(DATA_PATH, "w", encoding="utf-8") as archivo:
        json.dump(musica, archivo, indent=4)

def mostrar_musica():
    musica = cargar_musica()
    if not musica:
        print("No hay canciones registradas.")
    else:
        print(tabulate(musica, headers="keys", tablefmt="grid"))

def agregar_musica():
    limpiar_pantalla()
    musica = cargar_musica()

    titulo = input("Título de la canción: ")
    artista = input("Artista: ")

    nueva_cancion = {
        "titulo": titulo,
        "artista": artista
    }
    musica.append(nueva_cancion)
    guardar_musica(musica)
    print("✅ Canción agregada correctamente.")

def eliminar_musica():
    musica = cargar_musica()
    mostrar_musica()

    indice = int(input("Número de la canción a eliminar: ")) - 1
    if 0 <= indice < len(musica):
        musica.pop(indice)
        guardar_musica(musica)
        print("✅ Canción eliminada.")
    else:
        print("❌ Índice no válido.")
