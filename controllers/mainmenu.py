from controllers import elemento
from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.coreFiles import cargarJson
from config import RUTA_LIBROS, RUTA_PELICULAS, RUTA_MUSICA

def menuNuevoElemento():
    while True:
        limpiarPantalla()
        print("===================================")
        print("        Añadir un Nuevo Elemento   ")
        print("===================================")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.agregarElemento(RUTA_LIBROS, "Libro", ["titulo", "autor", "genero", "valoracion"])
        elif opcion == "2":
            elemento.agregarElemento(RUTA_PELICULAS, "Película", ["titulo", "director", "genero", "valoracion"])
        elif opcion == "3":
            elemento.agregarElemento(RUTA_MUSICA, "Música", ["titulo", "artista", "genero", "valoracion"])
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida.")
            pausarPantalla()

def listarElementos():
    limpiarPantalla()
    print("===================================")
    print("        Ver Todos los Elementos    ")
    print("===================================")
    print("1. Libros")
    print("2. Películas")
    print("3. Música")
    print("4. Regresar al Menú Principal")
    print("===================================")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        elemento.listarElementos(RUTA_LIBROS, "Libros")
    elif opcion == "2":
        elemento.listarElementos(RUTA_PELICULAS, "Películas")
    elif opcion == "3":
        elemento.listarElementos(RUTA_MUSICA, "Música")

def menuBuscarElemento():
    limpiarPantalla()
    print("===================================")
    print("          Buscar un Elemento       ")
    print("===================================")
    print("1. Buscar en Libros")
    print("2. Buscar en Películas")
    print("3. Buscar en Música")
    print("4. Regresar al Menú Principal")
    print("===================================")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        elemento.buscarElemento(RUTA_LIBROS, "Libros")
    elif opcion == "2":
        elemento.buscarElemento(RUTA_PELICULAS, "Películas")
    elif opcion == "3":
        elemento.buscarElemento(RUTA_MUSICA, "Música")


def menuEditarElemento():
    limpiarPantalla()
    print("===================================")
    print("          Editar un Elemento       ")
    print("===================================")
    print("1. Editar en Libros")
    print("2. Editar en Películas")
    print("3. Editar en Música")
    print("4. Regresar al Menú Principal")
    print("===================================")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        elemento.editarElemento(RUTA_LIBROS, "Libro", ["titulo", "autor", "genero", "valoracion"])
    elif opcion == "2":
        elemento.editarElemento(RUTA_PELICULAS, "Película", ["titulo", "director", "genero", "valoracion"])
    elif opcion == "3":
        elemento.editarElemento(RUTA_MUSICA, "Música", ["titulo", "artista", "genero", "valoracion"])


def menuEliminarElemento():
    limpiarPantalla()
    print("===================================")
    print("          Eliminar un Elemento     ")
    print("===================================")
    print("1. Eliminar en Libros")
    print("2. Eliminar en Películas")
    print("3. Eliminar en Música")
    print("4. Regresar al Menú Principal")
    print("===================================")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        elemento.eliminarElemento(RUTA_LIBROS, "Libro")
    elif opcion == "2":
        elemento.eliminarElemento(RUTA_PELICULAS, "Película")
    elif opcion == "3":
        elemento.eliminarElemento(RUTA_MUSICA, "Música")


def menuVerCategoria():
    limpiarPantalla()
    print("===================================")
    print("      Ver Elementos por Categoría  ")
    print("===================================")
    print("1. Libros")
    print("2. Películas")
    print("3. Música")
    print("4. Regresar al Menú Principal")
    print("===================================")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        elemento.listarElementos(RUTA_LIBROS, "Libros")
    elif opcion == "2":
        elemento.listarElementos(RUTA_PELICULAS, "Películas")
    elif opcion == "3":
        elemento.listarElementos(RUTA_MUSICA, "Música")


def menuGuardarCargar():
    limpiarPantalla()
    print("===================================")
    print("        Guardar y Cargar Datos     ")
    print("===================================")
    print("1. Guardar colección")
    print("2. Cargar colección")
    print("3. Regresar al Menú Principal")
    print("===================================")

    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
        print("💾 Colección guardada automáticamente al modificar datos.")
        pausarPantalla()
    elif opcion == "2":
        cargarJson(RUTA_LIBROS)
        cargarJson(RUTA_PELICULAS)
        cargarJson(RUTA_MUSICA)
        print("📂 Colección cargada correctamente.")
        pausarPantalla()
