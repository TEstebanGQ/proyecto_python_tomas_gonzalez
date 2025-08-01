from controllers import elemento
from utils.screenControllers import limpiarPantalla, pausarPantalla
from config import TIPOS_ELEMENTOS

def mostrarMenuGenerico(titulo, opciones, accion_callback):
    while True:
        limpiarPantalla()
        print("=" * 35)
        print(titulo)
        print("=" * 35)
        
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        print(f"{len(opciones) + 1}. Regresar al menu anterior")
        print("=" * 35)

        try:
            seleccion = int(input(f"Seleccione una opción (1-{len(opciones) + 1}): ").strip())
            if seleccion == len(opciones) + 1:
                break
            elif 1 <= seleccion <= len(opciones):
                accion_callback(seleccion - 1)
            else:
                raise ValueError
        except ValueError:
            print("Opción inválida.")
            pausarPantalla()

def menuNuevoElemento():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [TIPOS_ELEMENTOS[tipo]['nombre'] for tipo in tipos]
    
    def accion(indice):
        elemento.agregarElemento(tipos[indice])
    
    mostrarMenuGenerico("Añadir un Nuevo Elemento", opciones, accion)

def listarElementos():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [TIPOS_ELEMENTOS[tipo]['plural'] for tipo in tipos]
    
    def accion(indice):
        elemento.listarElementos(tipos[indice])
    
    mostrarMenuGenerico("Ver Todos los Elementos", opciones, accion)

def menuBuscarElemento():
    opciones = ["Buscar por Título", "Buscar por Autor/Director/Artista", "Buscar por Género"]
    
    def accion(indice):
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
        campo = TIPOS_ELEMENTOS[tipo]['campo_persona']
        elemento.buscarElementoPorCampo(tipo, campo)
    
    mostrarMenuGenerico("Buscar por Autor/Director/Artista", opciones, accion)

def menuBuscarPorGenero():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [f"Buscar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
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
        elemento.eliminarElementoPorTitulo(tipos[indice])
    
    mostrarMenuGenerico("Eliminar por Título", opciones, accion)

def menuEliminarPorId():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [f"Eliminar en {TIPOS_ELEMENTOS[tipo]['plural']}" for tipo in tipos]
    
    def accion(indice):
        elemento.eliminarElemento(tipos[indice])
    
    mostrarMenuGenerico("Eliminar por ID", opciones, accion)

def menuVerCategoria():
    tipos = list(TIPOS_ELEMENTOS.keys())
    opciones = [TIPOS_ELEMENTOS[tipo]['plural'] for tipo in tipos]
    
    def accion(indice):
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
        elemento.buscarElementoPorCampo(tipoElemento, campos[indice])
    
    mostrarMenuGenerico(f"Ver {config['plural']}", opciones, accion)

def menuGuardarCargar():
    opciones = ["Guardar colección", "Cargar colección", "Ver colecciones guardadas"]
    
    def accion(indice):
        acciones = [elemento.guardarColeccion, elemento.cargarColeccion, elemento.listarColecciones]
        acciones[indice]()
    
    mostrarMenuGenerico("Guardar y Cargar Datos", opciones, accion)