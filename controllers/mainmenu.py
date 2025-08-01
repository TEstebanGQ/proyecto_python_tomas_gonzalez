from controllers import elemento
from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.coreFiles import cargarJson
from config import RUTA_LIBROS, RUTA_PELICULAS, RUTA_MUSICA

def menuNuevoElemento():
    while True:
        limpiarPantalla()
        print("=====================================")
        print("        Añadir un Nuevo Elemento   ")
        print("=====================================")
        print("¿Que tipo de elemento deseas añadir?")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("=====================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.agregarElemento(RUTA_LIBROS, "libro", ["titulo", "autor", "genero", "valoracion"])
        elif opcion == "2":
            elemento.agregarElemento(RUTA_PELICULAS, "película", ["titulo", "director", "genero", "valoracion"])
        elif opcion == "3":
            elemento.agregarElemento(RUTA_MUSICA, "música", ["titulo", "artista", "genero", "valoracion"])
        elif opcion == "4":
            break
        else:
            print("Opción inválida.   ")
            pausarPantalla()

def listarElementos():
    while True:
        limpiarPantalla()
        print("===================================")
        print("        Ver Todos los Elementos    ")
        print("===================================")
        print("¿Que categoria deseas ver?")
        print("1. Libros")
        print("2. Películas")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.listarElementos(RUTA_LIBROS, "libro")
        elif opcion == "2":
            elemento.listarElementos(RUTA_PELICULAS, "película")
        elif opcion == "3":
            elemento.listarElementos(RUTA_MUSICA, "música")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.  ")
            pausarPantalla()

def menuBuscarElemento():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Buscar un Elemento")
        print("===========================================")
        print("¿Cómo deseas buscar?")
        print("1. Buscar por Título")
        print("2. Buscar por Autor/Director/Artista")
        print("3. Buscar por Género")
        print("4. Regresar al Menú Principal")
        print("===========================================")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            menuBuscarPorTitulo()
        elif opcion == "2":
            menuBuscarPorPersona()
        elif opcion == "3":
            menuBuscarPorGenero()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.  ")
            pausarPantalla()

def menuBuscarPorTitulo():
    while True:
        limpiarPantalla()
        print("===================================")
        print("        Buscar por Título          ")
        print("===================================")
        print("1. Buscar en Libros")
        print("2. Buscar en Películas")
        print("3. Buscar en Música")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.buscarElementoPorCampo(RUTA_LIBROS, "libro", "titulo")
        elif opcion == "2":
            elemento.buscarElementoPorCampo(RUTA_PELICULAS, "película", "titulo")
        elif opcion == "3":
            elemento.buscarElementoPorCampo(RUTA_MUSICA, "música", "titulo")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.   ")
            pausarPantalla()

def menuBuscarPorPersona():
    while True:
        limpiarPantalla()
        print("===================================")
        print("   Buscar por Autor/Director/Artista")
        print("===================================")
        print("1. Buscar en Libros (por Autor)")
        print("2. Buscar en Películas (por Director)")
        print("3. Buscar en Música (por Artista)")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.buscarElementoPorCampo(RUTA_LIBROS, "libro", "autor")
        elif opcion == "2":
            elemento.buscarElementoPorCampo(RUTA_PELICULAS, "película", "director")
        elif opcion == "3":
            elemento.buscarElementoPorCampo(RUTA_MUSICA, "música", "artista")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuBuscarPorGenero():
    while True:
        limpiarPantalla()
        print("===================================")
        print("        Buscar por Género          ")
        print("===================================")
        print("1. Buscar en Libros")
        print("2. Buscar en Películas")
        print("3. Buscar en Música")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.buscarElementoPorCampo(RUTA_LIBROS, "libro", "genero")
        elif opcion == "2":
            elemento.buscarElementoPorCampo(RUTA_PELICULAS, "película", "genero")
        elif opcion == "3":
            elemento.buscarElementoPorCampo(RUTA_MUSICA, "música", "genero")
        elif opcion == "4":
            break
        else:
            print(" Opción inválida.")
            pausarPantalla()

def menuEditarElemento():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Editar un Elemento")
        print("===========================================")
        print("¿Qué tipo de cambio deseas realizar?")
        print("1. Editar Título")
        print("2. Editar Autor/Director/Artista")
        print("3. Editar Género")
        print("4. Editar Valoración")
        print("5. Regresar al Menú Principal")
        print("===========================================")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            menuEditarCampo("titulo")
        elif opcion == "2":
            menuEditarPersona()
        elif opcion == "3":
            menuEditarCampo("genero")
        elif opcion == "4":
            menuEditarCampo("valoracion")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuEditarCampo(campo):
    while True:
        limpiarPantalla()
        campoTexto = {
            "titulo": "Título",
            "genero": "Género", 
            "valoracion": "Valoración"
        }.get(campo, campo)
        
        print(f"===================================")
        print(f"        Editar {campoTexto}")
        print(f"===================================")
        print("1. Editar en Libros")
        print("2. Editar en Películas")
        print("3. Editar en Música")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            if campo == "valoracion":
                elemento.editarElementoCampoEspecifico(RUTA_LIBROS, "libro", ["autor"], campo)
            else:
                elemento.editarElementoCampoEspecifico(RUTA_LIBROS, "libro", ["autor"], campo)
        elif opcion == "2":
            if campo == "valoracion":
                elemento.editarElementoCampoEspecifico(RUTA_PELICULAS, "película", ["director"], campo)
            else:
                elemento.editarElementoCampoEspecifico(RUTA_PELICULAS, "película", ["director"], campo)
        elif opcion == "3":
            if campo == "valoracion":
                elemento.editarElementoCampoEspecifico(RUTA_MUSICA, "música", ["artista"], campo)
            else:
                elemento.editarElementoCampoEspecifico(RUTA_MUSICA, "música", ["artista"], campo)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuEditarPersona():
    while True:
        limpiarPantalla()
        print("===================================")
        print("   Editar Autor/Director/Artista   ")
        print("===================================")
        print("1. Editar Autor (Libros)")
        print("2. Editar Director (Películas)")
        print("3. Editar Artista (Música)")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.editarElementoCampoEspecifico(RUTA_LIBROS, "libro", ["autor"], "autor")
        elif opcion == "2":
            elemento.editarElementoCampoEspecifico(RUTA_PELICULAS, "película", ["director"], "director")
        elif opcion == "3":
            elemento.editarElementoCampoEspecifico(RUTA_MUSICA, "música", ["artista"], "artista")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuEliminarElemento():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Eliminar un Elemento")
        print("===========================================")
        print("¿Cómo deseas eliminar?")
        print("1. Eliminar por Título")
        print("2. Eliminar por Identificador Único")
        print("3. Regresar al Menú Principal")
        print("===========================================")

        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            menuEliminarPorTitulo()
        elif opcion == "2":
            menuEliminarPorId()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuEliminarPorTitulo():
    while True:
        limpiarPantalla()
        print("===================================")
        print("       Eliminar por Título         ")
        print("===================================")
        print("1. Eliminar en Libros")
        print("2. Eliminar en Películas")
        print("3. Eliminar en Música")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.eliminarElementoPorTitulo(RUTA_LIBROS, "libro")
        elif opcion == "2":
            elemento.eliminarElementoPorTitulo(RUTA_PELICULAS, "película")
        elif opcion == "3":
            elemento.eliminarElementoPorTitulo(RUTA_MUSICA, "música")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuEliminarPorId():
    while True:
        limpiarPantalla()
        print("===================================")
        print("    Eliminar por ID")
        print("===================================")
        print("1. Eliminar en Libros")
        print("2. Eliminar en Películas")
        print("3. Eliminar en Música")
        print("4. Regresar")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.eliminarElemento(RUTA_LIBROS, "libro")
        elif opcion == "2":
            elemento.eliminarElemento(RUTA_PELICULAS, "película")
        elif opcion == "3":
            elemento.eliminarElemento(RUTA_MUSICA, "música")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()
# Reemplazar la función menuVerCategoria() en controllers/mainmenu.py por esta:

def menuVerCategoria():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Ver Elementos por Categoría")
        print("===========================================")
        print("¿Qué categoría deseas ver?")
        print("1. Libros")
        print("2. Películas")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===========================================")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            menuVerLibros()
        elif opcion == "2":
            menuVerPeliculas()
        elif opcion == "3":
            menuVerMusica()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# Agregar estas nuevas funciones también en controllers/mainmenu.py:

def menuVerLibros():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Ver Libros")
        print("===========================================")
        print("¿Cómo deseas filtrar los libros?")
        print("1. Filtrar por Título")
        print("2. Filtrar por Autor")
        print("3. Filtrar por Género")
        print("4. Regresar")
        print("===========================================")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            elemento.buscarElementoPorCampo(RUTA_LIBROS, "libro", "titulo")
        elif opcion == "2":
            elemento.buscarElementoPorCampo(RUTA_LIBROS, "libro", "autor")
        elif opcion == "3":
            elemento.filtrarPorGenero(RUTA_LIBROS, "libros")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuVerPeliculas():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Ver Películas")
        print("===========================================")
        print("¿Cómo deseas filtrar las películas?")
        print("1. Filtrar por Título")
        print("2. Filtrar por Director")
        print("3. Filtrar por Género")
        print("4. Regresar")
        print("===========================================")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            elemento.buscarElementoPorCampo(RUTA_PELICULAS, "película", "titulo")
        elif opcion == "2":
            elemento.buscarElementoPorCampo(RUTA_PELICULAS, "película", "director")
        elif opcion == "3":
            elemento.filtrarPorGenero(RUTA_PELICULAS, "películas")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

def menuVerMusica():
    while True:
        limpiarPantalla()
        print("===========================================")
        print("        Ver Música")
        print("===========================================")
        print("¿Cómo deseas filtrar la música?")
        print("1. Filtrar por Título")
        print("2. Filtrar por Artista")
        print("3. Filtrar por Género")
        print("4. Regresar")
        print("===========================================")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            elemento.buscarElementoPorCampo(RUTA_MUSICA, "música", "titulo")
        elif opcion == "2":
            elemento.buscarElementoPorCampo(RUTA_MUSICA, "música", "artista")
        elif opcion == "3":
            elemento.filtrarPorGenero(RUTA_MUSICA, "música")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()

# Reemplazar la función menuGuardarCargar() en controllers/mainmenu.py por esta:

def menuGuardarCargar():
    while True:
        limpiarPantalla()
        print("===================================")
        print("        Guardar y Cargar Datos     ")
        print("===================================")
        print("1. Guardar colección")
        print("2. Cargar colección")
        print("3. Ver colecciones guardadas")
        print("4. Regresar al Menú Principal")
        print("===================================")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            elemento.guardarColeccion()
        elif opcion == "2":
            elemento.cargarColeccion()
        elif opcion == "3":
            elemento.listarColecciones()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausarPantalla()