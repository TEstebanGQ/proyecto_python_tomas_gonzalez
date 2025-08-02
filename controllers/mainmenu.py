

from controllers import elemento
from utils.screenControllers import limpiarPantalla, pausarPantalla
from config import TIPOS_ELEMENTOS

def mostrarMenuGenerico(titulo, opciones, accion_callback):
    while True:
        try:
            limpiarPantalla()
            print("=" * 35)
            print(titulo)
            print("=" * 35)
            
            # Enumero todas las opciones disponibles para el usuario
            for i, opcion in enumerate(opciones, 1):
                print(f"{i}. {opcion}")
            print(f"{len(opciones) + 1}. Regresar al menu anterior")
            print("=" * 35)

            # Solicito la selección del usuario con validación de rango
            seleccion = int(input(f"Seleccione una opción (1-{len(opciones) + 1}): ").strip())
            
            if seleccion == len(opciones) + 1:
                break
            elif 1 <= seleccion <= len(opciones):
                # Ejecuto la acción seleccionada con manejo de excepciones
                try:
                    accion_callback(seleccion - 1)  # Ajusto el índice (base 0)
                except (KeyboardInterrupt, EOFError):
                    limpiarPantalla()
                    print("===================================")
                    print("    Operación cancelada           ")
                    print("    Regresando al menú anterior... ")
                    print("===================================")
                    try:
                        input("Presione Enter para continuar...")
                    except (KeyboardInterrupt, EOFError):
                        pass
                    continue
            else:
                raise ValueError  # Opción fuera de rango
                
        except (KeyboardInterrupt, EOFError):
            # Manejo interrupciones de teclado a nivel de menú
            limpiarPantalla()
            print("===================================")
            print("    Operación cancelada           ")
            print("    Regresando al menú anterior... ")
            print("===================================")
            break
        except ValueError:
            print("Opción inválida.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                continue


def menuNuevoElemento():
    tipos = list(TIPOS_ELEMENTOS.keys())  # Obtengo todos los tipos disponibles
    opciones = [TIPOS_ELEMENTOS[tipo]['nombre'] for tipo in tipos]  # Sus nombres amigables
    
    def accion(indice):
        # Ejecuto la función de agregar elemento del tipo seleccionado
        elemento.agregarElemento(tipos[indice])
    
    mostrarMenuGenerico("Añadir un Nuevo Elemento", opciones, accion)

def listarElementos():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [TIPOS_ELEMENTOS[tipo]['plural'] for tipo in tipos]  # Uso plurales para claridad
    
    def accion(indice):
        # Muestro todos los elementos del tipo seleccionado
        elemento.listarElementos(tipos[indice])
    
    mostrarMenuGenerico("Ver Todos los Elementos", opciones, accion)


def menuBuscarElemento():
    opciones = ["Buscar por Título", "Buscar por Autor/Director/Artista", "Buscar por Género"]
    
    def accion(indice):
        # Dirijo a los submenús de búsqueda específicos
        if indice == 0:
            menuBuscarPorTitulo()
        elif indice == 1:
            menuBuscarPorPersona()
        elif indice == 2:
            menuBuscarPorGenero()
    
    mostrarMenuGenerico("Buscar un Elemento", opciones, accion)

def menuBuscarPorTitulo():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [f"Buscar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
        # Ejecuto búsqueda por título en el tipo seleccionado
        elemento.buscarElementoPorCampo(tipos[indice], "titulo")
    
    mostrarMenuGenerico("Buscar por Título", opciones, accion)

def menuBuscarPorPersona():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [
        f"Buscar en {TIPOS_ELEMENTOS[tipo]['plural']} (por {TIPOS_ELEMENTOS[tipo]['etiqueta_persona']})"
        for tipo in tipos
    ]
    
    def accion(indice):
        tipo = tipos[indice]
        campo = TIPOS_ELEMENTOS[tipo]['campo_persona']  # Campo específico para cada tipo
        elemento.buscarElementoPorCampo(tipo, campo)
    
    mostrarMenuGenerico("Buscar por Autor/Director/Artista", opciones, accion)

def menuBuscarPorGenero():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [f"Buscar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
        # Ejecuto búsqueda por género en el tipo seleccionado
        elemento.buscarElementoPorCampo(tipos[indice], "genero")
    
    mostrarMenuGenerico("Buscar por Género", opciones, accion)

def menuEditarElemento():
    opciones = ["Editar Título", "Editar Autor/Director/Artista", "Editar Género", "Editar Valoración"]
    
    def accion(indice):
        campos = ["titulo", None, "genero", "valoracion"]  
        if indice == 1:
            menuEditarPersona()  
        else:
            menuEditarCampo(campos[indice])
    
    mostrarMenuGenerico("Editar un Elemento", opciones, accion)

def menuEditarCampo(campo):
    tipos = list(TIPOS_ELEMENTOS.keys())
    etiquetas_campos = {"titulo": "Título", "genero": "Género", "valoracion": "Valoración"}
    campo_texto = etiquetas_campos.get(campo, campo)
    opciones = [f"Editar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
        # Ejecuto edición del campo específico en el tipo seleccionado
        elemento.editarElementoCampoEspecifico(tipos[indice], campo)
    
    mostrarMenuGenerico(f"Editar {campo_texto}", opciones, accion)

def menuEditarPersona():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [
        f"Editar {TIPOS_ELEMENTOS[tipo]['etiqueta_persona']} ({TIPOS_ELEMENTOS[tipo]['plural']})"
        for tipo in tipos
    ]
    
    def accion(indice):
        tipo = tipos[indice]
        campo = TIPOS_ELEMENTOS[tipo]['campo_persona']  
        elemento.editarElementoCampoEspecifico(tipo, campo)
    
    mostrarMenuGenerico("Editar Autor/Director/Artista", opciones, accion)

def menuEliminarElemento():
    opciones = ["Eliminar por Título", "Eliminar por Identificador Único"]
    
    def accion(indice):
        if indice == 0:
            menuEliminarPorTitulo()
        elif indice == 1:
            menuEliminarPorId()
    
    mostrarMenuGenerico("Eliminar un Elemento", opciones, accion)

def menuEliminarPorTitulo():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [f"Eliminar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
        # Ejecuto eliminación por título con búsqueda flexible
        elemento.eliminarElementoPorTitulo(tipos[indice])
    
    mostrarMenuGenerico("Eliminar por Título", opciones, accion)

def menuEliminarPorId():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [f"Eliminar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
        # Ejecuto eliminación por ID específico
        elemento.eliminarElemento(tipos[indice])
    
    mostrarMenuGenerico("Eliminar por ID", opciones, accion)

def menuVerCategoria():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [TIPOS_ELEMENTOS[tipo]['plural'] for tipo in tipos]
    
    def accion(indice):
        # Abro submenú específico para el tipo seleccionado
        menuVerTipo(tipos[indice])
    
    mostrarMenuGenerico("Ver Elementos por Categoría", opciones, accion)

def menuVerTipo(tipoElemento):
    config = TIPOS_ELEMENTOS[tipoElemento]
    opciones = [
        f"Filtrar por Título",
        f"Filtrar por {config['etiqueta_persona']}", 
        f"Filtrar por Género"
    ]
    
    def accion(indice):
        campos = ["titulo", config['campo_persona'], "genero"]
        # Ejecuto búsqueda/filtro en el campo seleccionado
        elemento.buscarElementoPorCampo(tipoElemento, campos[indice])
    
    mostrarMenuGenerico(f"Ver {config['plural']}", opciones, accion)

def menuGuardarCargar():
    opciones = ["Guardar colección", "Cargar colección", "Ver colecciones guardadas"]
    
    def accion(indice):
        # Mapeo directo a las funciones de gestión de colecciones
        acciones = [elemento.guardarColeccion, elemento.cargarColeccion, elemento.listarColecciones]
        acciones[indice]()
    
    mostrarMenuGenerico("Guardar y Cargar Datos", opciones, accion)