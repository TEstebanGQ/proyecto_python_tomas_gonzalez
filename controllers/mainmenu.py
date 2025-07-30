from utils.screenControllers import limpiarPantalla, pausarPantalla
import controllers.libros as libros
import controllers.peliculas as peliculas
import controllers.musica as musica
from utils.coreFiles import cargarJson, guardarJson
from config import RUTA_LIBROS, RUTA_PELICULAS, RUTA_MUSICA

# ✅ Submenú para añadir nuevo elemento
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
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            libros.agregarLibro()
        elif opcion == "2":
            peliculas.agregarPelicula()
        elif opcion == "3":
            musica.agregarMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# ✅ Submenú para ver todos los elementos
def listarElementos():
    while True:
        limpiarPantalla()
        print("===================================")
        print("       Ver Todos los Elementos     ")
        print("===================================")
        print("1. Libros")
        print("2. Películas")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===================================")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            libros.listarLibros()
        elif opcion == "2":
            peliculas.listarPeliculas()
        elif opcion == "3":
            musica.listarMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# ✅ Submenú para buscar un elemento
def menuBuscarElemento():
    while True:
        limpiarPantalla()
        print("===================================")
        print("          Buscar un Elemento       ")
        print("===================================")
        print("1. Buscar en Libros")
        print("2. Buscar en Películas")
        print("3. Buscar en Música")
        print("4. Regresar al Menú Principal")
        print("===================================")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            libros.buscarLibro()
        elif opcion == "2":
            peliculas.buscarPelicula()
        elif opcion == "3":
            musica.buscarMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# ✅ Submenú para editar un elemento
def menuEditarElemento():
    while True:
        limpiarPantalla()
        print("===================================")
        print("         Editar un Elemento        ")
        print("===================================")
        print("1. Editar Libro")
        print("2. Editar Película")
        print("3. Editar Música")
        print("4. Regresar al Menú Principal")
        print("===================================")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            libros.editarLibro()
        elif opcion == "2":
            peliculas.editarPelicula()
        elif opcion == "3":
            musica.editarMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# ✅ Submenú para eliminar un elemento
def menuEliminarElemento():
    while True:
        limpiarPantalla()
        print("===================================")
        print("        Eliminar un Elemento       ")
        print("===================================")
        print("1. Eliminar Libro")
        print("2. Eliminar Película")
        print("3. Eliminar Música")
        print("4. Regresar al Menú Principal")
        print("===================================")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            libros.eliminarLibro()
        elif opcion == "2":
            peliculas.eliminarPelicula()
        elif opcion == "3":
            musica.eliminarMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# ✅ Submenú para guardar y cargar colección
def menuGuardarCargar():
    while True:
        limpiarPantalla()
        print("===================================")
        print("       Guardar y Cargar Datos      ")
        print("===================================")
        print("1. Guardar colección actual")
        print("2. Cargar colección guardada")
        print("3. Regresar al Menú Principal")
        print("===================================")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            print("Colección guardada automáticamente al agregar/editar/eliminar.")
            pausarPantalla()
        elif opcion == "2":
            print("Los datos se cargan automáticamente al iniciar.")
            pausarPantalla()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuVerCategoria():
    while True:
        limpiarPantalla()
        print("===================================")
        print("     Ver Elementos por Categoría   ")
        print("===================================")
        print("1. Ver Libros")
        print("2. Ver Películas")
        print("3. Ver Música")
        print("4. Regresar al Menú Principal")
        print("===================================")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            libros.listarLibros()
        elif opcion == "2":
            peliculas.listarPeliculas()
        elif opcion == "3":
            musica.listarMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

