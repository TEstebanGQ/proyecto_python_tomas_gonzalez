from utils.validata import validar_solo_letras, validar_valoracion, generar_id
from utils.corefiles import cargar_json, guardar_json
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from tabulate import tabulate

RUTA = "data/musica.json"

def mostrar_tabla(lista):
    if not lista:
        print("📭 No hay registros disponibles.")
    else:
        print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))

def agregar_musica():
    limpiar_pantalla()
    canciones = cargar_json(RUTA)
    nueva_cancion = {
        "id": generar_id(RUTA),
        "titulo": input("Título de la canción: ").strip(),
        "artista": validar_solo_letras("Artista"),
        "genero": validar_solo_letras("Género musical"),
        "valoracion": validar_valoracion()
    }
    canciones.append(nueva_cancion)
    guardar_json(RUTA, canciones)
    print("✅ Canción agregada correctamente.")
    pausar_pantalla()

def listar_musica():
    limpiar_pantalla()
    canciones = cargar_json(RUTA)
    mostrar_tabla(canciones)
    pausar_pantalla()

def buscar_musica():
    limpiar_pantalla()
    canciones = cargar_json(RUTA)
    criterio = input("Buscar por título, artista o género: ").strip().lower()
    encontrados = [c for c in canciones if criterio in c["titulo"].lower() or criterio in c["artista"].lower() or criterio in c["genero"].lower()]
    mostrar_tabla(encontrados)
    pausar_pantalla()

def editar_musica():
    limpiar_pantalla()
    canciones = cargar_json(RUTA)
    mostrar_tabla(canciones)
    id_cancion = input("\nIngrese el ID de la canción a editar: ").strip()

    cancion = next((c for c in canciones if c["id"] == id_cancion), None)
    if cancion:
        cancion["titulo"] = input(f"Nuevo título [{cancion['titulo']}]: ").strip() or cancion["titulo"]
        cancion["artista"] = validar_solo_letras("Nuevo artista")
        cancion["genero"] = validar_solo_letras("Nuevo género")
        cancion["valoracion"] = validar_valoracion()
        guardar_json(RUTA, canciones)
        print("✅ Canción editada correctamente.")
    else:
        print("❌ No se encontró una canción con ese ID.")
    pausar_pantalla()

def eliminar_musica():
    limpiar_pantalla()
    canciones = cargar_json(RUTA)
    mostrar_tabla(canciones)
    id_cancion = input("\nIngrese el ID de la canción a eliminar: ").strip()

    canciones_filtradas = [c for c in canciones if c["id"] != id_cancion]
    if len(canciones_filtradas) != len(canciones):
        guardar_json(RUTA, canciones_filtradas)
        print("✅ Canción eliminada correctamente.")
    else:
        print("❌ No se encontró una canción con ese ID.")
    pausar_pantalla()
