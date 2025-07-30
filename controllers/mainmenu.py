from controllers.libros import agregar_libro, listar_libros, buscar_libro, editar_libro, eliminar_libro
from controllers.peliculas import agregar_pelicula, listar_peliculas, buscar_pelicula, editar_pelicula, eliminar_pelicula
from controllers.musica import agregar_musica, listar_musica, buscar_musica, editar_musica, eliminar_musica
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from utils.corefiles import cargar_json
import os

# Rutas de los archivos JSON
RUTA_LIBROS = "data/libros.json"
RUTA_PELICULAS = "data/peliculas.json"
RUTA_MUSICA = "data/musica.json"

# ---------------- MENÚ: AÑADIR ELEMENTO ---------------- #
def menuNuevoElemento():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("        Añadir un Nuevo Elemento   ")
        print("===================================")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()
        match opcion:
            case "1":
                agregar_libro()
            case "2":
                agregar_pelicula()
            case "3":
                agregar_musica()
            case "4":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()

# ---------------- MENÚ: LISTAR ELEMENTOS ---------------- #
def ListarElementos():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("         Ver Todos los Elementos    ")
        print("===================================")
        print("1. Libros")
        print("2. Películas")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()
        match opcion:
            case "1":
                listar_libros()
            case "2":
                listar_peliculas()
            case "3":
                listar_musica()
            case "4":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()

# ---------------- MENÚ: BUSCAR ELEMENTO ---------------- #
def menuBuscarElemento():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("         Buscar un Elemento         ")
        print("===================================")
        print("1. Buscar en Libros")
        print("2. Buscar en Películas")
        print("3. Buscar en Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()
        match opcion:
            case "1":
                buscar_libro()
            case "2":
                buscar_pelicula()
            case "3":
                buscar_musica()
            case "4":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()

# ---------------- MENÚ: EDITAR ELEMENTO ---------------- #
def menuEditarElemento():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("         Editar un Elemento         ")
        print("===================================")
        print("1. Editar Libro")
        print("2. Editar Película")
        print("3. Editar Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()
        match opcion:
            case "1":
                editar_libro()
            case "2":
                editar_pelicula()
            case "3":
                editar_musica()
            case "4":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()

# ---------------- MENÚ: ELIMINAR ELEMENTO ---------------- #
def menuEliminarElemento():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("         Eliminar un Elemento       ")
        print("===================================")
        print("1. Eliminar Libro")
        print("2. Eliminar Película")
        print("3. Eliminar Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()
        match opcion:
            case "1":
                eliminar_libro()
            case "2":
                eliminar_pelicula()
            case "3":
                eliminar_musica()
            case "4":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()

# ---------------- MENÚ: VER POR CATEGORÍA ---------------- #
def menuVerCategoria():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("     Ver Elementos por Categoría    ")
        print("===================================")
        print("1. Ver Libros")
        print("2. Ver Películas")
        print("3. Ver Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()
        match opcion:
            case "1":
                listar_libros()
            case "2":
                listar_peliculas()
            case "3":
                listar_musica()
            case "4":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()

# ---------------- MENÚ: GUARDAR Y CARGAR ---------------- #
def menuGuardarCargar():
    while True:
        limpiar_pantalla()
        print("===================================")
        print("     Guardar y Cargar Colección     ")
        print("===================================")
        print("1. Guardar Colección Actual")
        print("2. Cargar Colección Guardada")
        print("3. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-3): ").strip()
        match opcion:
            case "1":
                print("💾 Guardando colecciones en JSON...")
                pausar_pantalla()
            case "2":
                print("📂 Cargando colecciones...")
                cargar_json(RUTA_LIBROS)
                cargar_json(RUTA_PELICULAS)
                cargar_json(RUTA_MUSICA)
                pausar_pantalla()
            case "3":
                break
            case _:
                print("❌ Opción inválida.")
                pausar_pantalla()
