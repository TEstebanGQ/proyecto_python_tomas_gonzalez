from utils.coreFiles import cargarJson, guardarJson
from utils.validata import validarSoloLetras, validarValoracion, generarId
from utils.screenControllers import limpiarPantalla, pausarPantalla
from config import TIPOS_ELEMENTOS, ETIQUETAS_CAMPOS, RUTA_COLECCIONES
from tabulate import tabulate

def obtenerConfigTipo(tipoElemento):
    return TIPOS_ELEMENTOS.get(tipoElemento.lower(), TIPOS_ELEMENTOS['libro'])

def obtenerEtiquetaCampo(campo):
    return ETIQUETAS_CAMPOS.get(campo, campo.capitalize())

def generarEncabezados(tipoElemento):
    config = obtenerConfigTipo(tipoElemento)
    return ["ID", "Título", config['etiqueta_persona'], "Género", "Valoración"]

def crearFilaTabla(elemento, tipoElemento):
    config = obtenerConfigTipo(tipoElemento)
    campo_persona = config['campo_persona']
    return [
        elemento["id"], 
        elemento["titulo"], 
        elemento.get(campo_persona, "N/A"), 
        elemento["genero"], 
        elemento["valoracion"]
    ]

def mostrarTabla(elementos, tipoElemento, titulo=""):
    if not elementos:
        print(f"No hay {tipoElemento} registrados.")
        return
    
    if titulo:
        print(f"=== {titulo} ===")
    
    headers = generarEncabezados(tipoElemento)
    filas = [crearFilaTabla(e, tipoElemento) for e in elementos]
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

def agregarElemento(tipoElemento):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])

    print(f"=== Añadir {config['nombre']} ===")
    datos = {}

    for campo in config['campos']:
        if campo == "valoracion":
            datos[campo] = validarValoracion()
        else:
            etiqueta = obtenerEtiquetaCampo(campo)
            datos[campo] = validarSoloLetras(f"Ingrese {etiqueta}: ")

    datos["id"] = generarId(elementos)
    elementos.append(datos)
    guardarJson(config['ruta'], elementos)
    print(f"{config['nombre']} agregado correctamente.")
    pausarPantalla()

def listarElementos(tipoElemento):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])
    mostrarTabla(elementos, tipoElemento, f"Lista de {config['plural']}")
    pausarPantalla()

def buscarElementoPorCampo(tipoElemento, campo):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])
    
    if not elementos:
        print(f"No hay {config['plural']} registrados.")
        pausarPantalla()
        return

    etiqueta = obtenerEtiquetaCampo(campo)
    criterio = validarSoloLetras(f"Buscar {config['plural']} por {etiqueta}: ")
    
    encontrados = [e for e in elementos if criterio.lower() in str(e.get(campo, "")).lower()]
    
    if encontrados:
        mostrarTabla(encontrados, tipoElemento, f"{config['plural']} encontrados por {etiqueta}")
    else:
        print(f"No se encontraron {config['plural']} que contengan '{criterio}' en {etiqueta}.")
    pausarPantalla()

def editarElementoCampoEspecifico(tipoElemento, campoAEditar):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])

    if not elementos:
        print(f"No hay {config['plural']} registrados.")
        pausarPantalla()
        return

    mostrarTabla(elementos, tipoElemento, f"{config['plural']} disponibles para editar")

    idEditar = input(f"Ingrese el ID del {config['nombre']} a editar: ").strip()
    elemento = next((e for e in elementos if e["id"] == idEditar), None)

    if not elemento:
        print(f"ID no encontrado en {config['plural']}.")
        pausarPantalla()
        return

    etiqueta = obtenerEtiquetaCampo(campoAEditar)
    valor_actual = elemento.get(campoAEditar, "N/A")
    
    if campoAEditar == "valoracion":
        print(f"Valoración actual: {valor_actual}")
        nuevaVal = validarValoracion(permitirVacio=True)
        if nuevaVal is not None:
            elemento[campoAEditar] = nuevaVal
            print(f"{etiqueta} actualizada correctamente.")
        else:
            print("No se realizaron cambios.")
    else:
        nuevaVal = validarSoloLetras(f"Nuevo {etiqueta} ({valor_actual}): ", permitirVacio=True)
        if nuevaVal:
            elemento[campoAEditar] = nuevaVal
            print(f"{etiqueta} actualizado correctamente.")
        else:
            print("No se realizaron cambios.")

    guardarJson(config['ruta'], elementos)
    pausarPantalla()

def eliminarElemento(tipoElemento):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])

    if not elementos:
        print(f"No hay {config['plural']} registrados para eliminar.")
        pausarPantalla()
        return

    mostrarTabla(elementos, tipoElemento, f"{config['plural']} disponibles para eliminar")

    idEliminar = input(f"Ingrese el ID del {config['nombre']} a eliminar: ").strip()
    elementosFiltrados = [e for e in elementos if e["id"] != idEliminar]
    
    if len(elementosFiltrados) < len(elementos):
        guardarJson(config['ruta'], elementosFiltrados)
        print(f"{config['nombre']} eliminado correctamente.")
    else:
        print(f"ID no encontrado en {config['plural']}.")
    pausarPantalla()


def mostrarTablaSinId(elementos, tipoElemento, titulo=""):
    """Muestra tabla sin la columna ID para eliminación por título"""
    if not elementos:
        print(f"No hay {tipoElemento} registrados.")
        return
    
    if titulo:
        print(f"=== {titulo} ===")
    
    config = obtenerConfigTipo(tipoElemento)
    campo_persona = config['campo_persona']
    headers = ["Título", config['etiqueta_persona'], "Género", "Valoración"]

    filas = []
    for elemento in elementos:
        fila = [
            elemento["titulo"], 
            elemento.get(campo_persona, "N/A"), 
            elemento["genero"], 
            elemento["valoracion"]
        ]
        filas.append(fila)
    
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))



def eliminarElementoPorTitulo(tipoElemento):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])

    if not elementos:
        print(f"No hay {config['plural']} registrados para eliminar.")
        pausarPantalla()
        return

    mostrarTablaSinId(elementos, tipoElemento, f"{config['plural']} disponibles para eliminar")

    titulo_buscar = validarSoloLetras(f"Ingrese el título del {config['nombre']} a eliminar: ")
    coincidencias = [e for e in elementos if titulo_buscar.lower() in e["titulo"].lower()]
    
    if not coincidencias:
        print(f"No se encontró ningún {config['nombre']} con el título '{titulo_buscar}'.")
        pausarPantalla()
        return
    
    if len(coincidencias) == 1:
        elemento_eliminar = coincidencias[0]
        confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (si/no): ").strip().lower()
        if confirmacion == 'si':
            elementos.remove(elemento_eliminar)
            guardarJson(config['ruta'], elementos)
            print(f"{config['nombre']} '{elemento_eliminar['titulo']}' eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:

        print(f"Se encontraron {len(coincidencias)} {config['plural']} con ese título:")
        mostrarTablaSinId(coincidencias, tipoElemento)
        
        print("Seleccione cuál eliminar:")
        for i, elemento in enumerate(coincidencias, 1):
            print(f"{i}. {elemento['titulo']} - {elemento.get(config['campo_persona'], 'N/A')} ({elemento['genero']})")
        
        try:
            seleccion = int(input("Ingrese el número del elemento a eliminar: ")) - 1
            if 0 <= seleccion < len(coincidencias):
                elemento_eliminar = coincidencias[seleccion]
                confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (s/n): ").strip().lower()
                if confirmacion == 's':
                    elementos.remove(elemento_eliminar)
                    guardarJson(config['ruta'], elementos)
                    print(f"{config['nombre']} eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("Selección inválida.")
        except ValueError:
            print("Debe ingresar un número válido.")
    
    pausarPantalla()


def guardarColeccion():
    limpiarPantalla()
    print("=== Guardar Colección ===")
    
    libros = cargarJson(TIPOS_ELEMENTOS['libro']['ruta'])
    peliculas = cargarJson(TIPOS_ELEMENTOS['película']['ruta'])
    musica = cargarJson(TIPOS_ELEMENTOS['música']['ruta'])
    
    total_elementos = len(libros) + len(peliculas) + len(musica)
    if total_elementos == 0:
        print("No hay elementos para guardar. La colección está vacía.")
        pausarPantalla()
        return
    
    nombre_coleccion = validarSoloLetras("Ingrese el nombre de la colección: ")
    
    coleccion = {
        "nombre": nombre_coleccion,
        "libros": libros,
        "peliculas": peliculas,
        "musica": musica
    }
    
    colecciones_existentes = cargarJson(RUTA_COLECCIONES)
    

    for i, col in enumerate(colecciones_existentes):
        if col.get("nombre", "").lower() == nombre_coleccion.lower():
            respuesta = input(f"Ya existe una colección llamada '{nombre_coleccion}'. ¿Desea sobrescribirla? (s/n): ").strip().lower()
            if respuesta == 's':
                colecciones_existentes[i] = coleccion
                print(f"Colección '{nombre_coleccion}' sobrescrita correctamente.")
            else:
                print("Guardado cancelado.")
                pausarPantalla()
                return
            break
    else:
        colecciones_existentes.append(coleccion)
        print(f"Colección '{nombre_coleccion}' guardada correctamente.")
    
    guardarJson(RUTA_COLECCIONES, colecciones_existentes)
    
    print(f"Total de elementos guardados: {total_elementos}")
    print(f"- Libros: {len(libros)}")
    print(f"- Películas: {len(peliculas)}")  
    print(f"- Música: {len(musica)}")
    pausarPantalla()

def cargarColeccion():
    limpiarPantalla()
    print("=== Cargar Colección ===")
    
    coleccionesExistentes = cargarJson(RUTA_COLECCIONES)
    
    if not coleccionesExistentes:
        print(" No hay colecciones guardadas.")
        pausarPantalla()
        return
    
    print("Colecciones disponibles:")
    for i, coleccion in enumerate(coleccionesExistentes, 1):
        nombre = coleccion.get("nombre", f"Colección {i}")
        libros_count = len(coleccion.get("libros", []))
        peliculas_count = len(coleccion.get("peliculas", []))
        musica_count = len(coleccion.get("musica", []))
        total = libros_count + peliculas_count + musica_count
        print(f"{i}. {nombre} ({total} elementos)")
    
    try:
        seleccion = int(input("Ingrese el número de la colección a cargar: "))
        if seleccion < 1 or seleccion > len(coleccionesExistentes):
            raise ValueError
    except ValueError:
        print("Selección inválida.")
        pausarPantalla()
        return
    
    coleccionSeleccionada = coleccionesExistentes[seleccion - 1]
    nombreColeccion = coleccionSeleccionada.get("nombre", f"Colección {seleccion}")
    
    respuesta = input("Esto sobrescribirá todos los datos actuales. ¿Continuar? (s/n): ").strip().lower()
    if respuesta != 's':
        print("Carga cancelada.")
        pausarPantalla()
        return
    
    libros = coleccionSeleccionada.get("libros", [])
    peliculas = coleccionSeleccionada.get("peliculas", [])
    musica = coleccionSeleccionada.get("musica", [])
    
    guardarJson(TIPOS_ELEMENTOS['libro']['ruta'], libros)
    guardarJson(TIPOS_ELEMENTOS['película']['ruta'], peliculas)
    guardarJson(TIPOS_ELEMENTOS['música']['ruta'], musica)
    
    print(f"Colección '{nombreColeccion}' cargada correctamente.")
    print(f"- Libros cargados: {len(libros)}")
    print(f"- Películas cargadas: {len(peliculas)}")
    print(f"- Música cargada: {len(musica)}")
    pausarPantalla()

def listarColecciones():
    """Lista todas las colecciones guardadas"""
    limpiarPantalla()
    print("=== Colecciones Guardadas ===")
    
    colecciones_existentes = cargarJson(RUTA_COLECCIONES)
    
    if not colecciones_existentes:
        print("No hay colecciones guardadas.")
        pausarPantalla()
        return
    
    for i, coleccion in enumerate(colecciones_existentes, 1):
        nombre = coleccion.get("nombre", f"Colección {i}")
        libros = len(coleccion.get("libros", []))
        peliculas = len(coleccion.get("peliculas", []))
        musica = len(coleccion.get("musica", []))
        total = libros + peliculas + musica
        
        print(f"{i}. {nombre}")
        print(f"   - Libros: {libros}")
        print(f"   - Películas: {peliculas}")
        print(f"   - Música: {musica}")
        print(f"   - Total: {total} elementos")
        print("-" * 30)
    
    pausarPantalla()