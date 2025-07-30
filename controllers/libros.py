from utils.validata import validar_solo_letras, validar_valoracion, generar_id
from utils.corefiles import cargar_json, guardar_json
from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from tabulate import tabulate

RUTA = "data/libros.json"

# Mostrar tabla de elementos
def mostrar_tabla(lista):
    if not lista:
        print("📭 No hay registros disponibles.")
    else:
        print(tabulate(lista, headers="keys", tablefmt="fancy_grid"))

# Añadir libro
def agregar_libro():
    limpiar_pantalla()
    libros = cargar_json(RUTA)
    nuevo_libro = {
        "id": generar_id(RUTA),
        "titulo": input("Título del libro: ").strip(),
        "autor": validar_solo_letras("Autor"),
        "genero": validar_solo_letras("Género"),
        "valoracion": validar_valoracion()
    }
    libros.append(nuevo_libro)
    guardar_json(RUTA, libros)
    print("✅ Libro agregado correctamente.")
    pausar_pantalla()

# Listar libros
def listar_libros():
    limpiar_pantalla()
    libros = cargar_json(RUTA)
    mostrar_tabla(libros)
    pausar_pantalla()

# Buscar libro por título, autor o género
def buscar_libro():
    limpiar_pantalla()
    libros = cargar_json(RUTA)
    criterio = input("Buscar por título, autor o género: ").strip().lower()
    encontrados = [l for l in libros if criterio in l["titulo"].lower() or criterio in l["autor"].lower() or criterio in l["genero"].lower()]
    mostrar_tabla(encontrados)
    pausar_pantalla()

# Editar libro
def editar_libro():
    limpiar_pantalla()
    libros = cargar_json(RUTA)
    mostrar_tabla(libros)
    id_libro = input("\nIngrese el ID del libro a editar: ").strip()

    libro = next((l for l in libros if l["id"] == id_libro), None)
    if libro:
        libro["titulo"] = input(f"Nuevo título [{libro['titulo']}]: ").strip() or libro["titulo"]
        libro["autor"] = validar_solo_letras("Nuevo autor")
        libro["genero"] = validar_solo_letras("Nuevo género")
        libro["valoracion"] = validar_valoracion()
        guardar_json(RUTA, libros)
        print("✅ Libro editado correctamente.")
    else:
        print("❌ No se encontró un libro con ese ID.")
    pausar_pantalla()

# Eliminar libro
def eliminar_libro():
    limpiar_pantalla()
    libros = cargar_json(RUTA)
    mostrar_tabla(libros)
    id_libro = input("\nIngrese el ID del libro a eliminar: ").strip()

    libros_filtrados = [l for l in libros if l["id"] != id_libro]
    if len(libros_filtrados) != len(libros):
        guardar_json(RUTA, libros_filtrados)
        print("✅ Libro eliminado correctamente.")
    else:
        print("❌ No se encontró un libro con ese ID.")
    pausar_pantalla()
