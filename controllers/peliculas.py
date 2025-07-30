from utils.validata import validar_solo_letras, validar_valoracion, generar_id
from utils.corefiles import cargar_json, guardar_json
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from tabulate import tabulate

RUTA = "data/peliculas.json"

def mostrar_tabla(lista):
    if not lista:
        print("📭 No hay registros disponibles.")
    else:
        print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))

def agregar_pelicula():
    limpiar_pantalla()
    peliculas = cargar_json(RUTA)
    nueva_pelicula = {
        "id": generar_id(RUTA),
        "titulo": input("Título de la película: ").strip(),
        "director": validar_solo_letras("Director"),
        "genero": validar_solo_letras("Género"),
        "valoracion": validar_valoracion()
    }
    peliculas.append(nueva_pelicula)
    guardar_json(RUTA, peliculas)
    print("✅ Película agregada correctamente.")
    pausar_pantalla()

def listar_peliculas():
    limpiar_pantalla()
    peliculas = cargar_json(RUTA)
    mostrar_tabla(peliculas)
    pausar_pantalla()

def buscar_pelicula():
    limpiar_pantalla()
    peliculas = cargar_json(RUTA)
    criterio = input("Buscar por título, director o género: ").strip().lower()
    encontrados = [p for p in peliculas if criterio in p["titulo"].lower() or criterio in p["director"].lower() or criterio in p["genero"].lower()]
    mostrar_tabla(encontrados)
    pausar_pantalla()

def editar_pelicula():
    limpiar_pantalla()
    peliculas = cargar_json(RUTA)
    mostrar_tabla(peliculas)
    id_pelicula = input("\nIngrese el ID de la película a editar: ").strip()

    pelicula = next((p for p in peliculas if p["id"] == id_pelicula), None)
    if pelicula:
        pelicula["titulo"] = input(f"Nuevo título [{pelicula['titulo']}]: ").strip() or pelicula["titulo"]
        pelicula["director"] = validar_solo_letras("Nuevo director")
        pelicula["genero"] = validar_solo_letras("Nuevo género")
        pelicula["valoracion"] = validar_valoracion()
        guardar_json(RUTA, peliculas)
        print("✅ Película editada correctamente.")
    else:
        print("❌ No se encontró una película con ese ID.")
    pausar_pantalla()

def eliminar_pelicula():
    limpiar_pantalla()
    peliculas = cargar_json(RUTA)
    mostrar_tabla(peliculas)
    id_pelicula = input("\nIngrese el ID de la película a eliminar: ").strip()

    peliculas_filtradas = [p for p in peliculas if p["id"] != id_pelicula]
    if len(peliculas_filtradas) != len(peliculas):
        guardar_json(RUTA, peliculas_filtradas)
        print("✅ Película eliminada correctamente.")
    else:
        print("❌ No se encontró una película con ese ID.")
    pausar_pantalla()
