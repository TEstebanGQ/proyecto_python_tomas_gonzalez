from utils.coreFiles import cargarJson, guardarJson
from utils.validata import validarSoloLetras, validarValoracion, generarId
from utils.screenControllers import limpiarPantalla, pausarPantalla
from tabulate import tabulate
import data as data


def agregarElemento(ruta, tipoElemento, campos):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    print(f"=== Añadir {tipoElemento} ===")
    datos = {}

    for campo in campos:
        if campo == "valoracion":
            datos[campo] = validarValoracion()  # 
        else:
            etiqueta = obtenerEtiquetaCampo(tipoElemento, campo)
            datos[campo] = validarSoloLetras(f"Ingrese {etiqueta}: ")

    datos["id"] = generarId(elementos)
    elementos.append(datos)
    guardarJson(ruta, elementos)
    print(f"{tipoElemento} agregado correctamente.")
    pausarPantalla()

#Obtener el campo correcto según el tipo (autor/director/artista)
def obtenerCampoPersona(tipoElemento):
    if tipoElemento.lower() == "libro":
        return "autor"
    elif tipoElemento.lower() == "película":
        return "director"  
    elif tipoElemento.lower() == "música":
        return "artista"
    return "autor"  

def obtenerEtiquetaCampo(tipoElemento, campo):
    if campo == "autor":
        return "Autor"
    elif campo == "director":
        return "Director"
    elif campo == "artista":
        return "Artista"
    elif campo == "genero":
        return "Género"
    elif campo == "titulo":
        return "Título"
    elif campo == "valoracion":
        return "Valoración"
    return campo


def generarEncabezados(tipoElemento):
    if tipoElemento.lower() == "libro":
        return ["ID", "Título", "Autor", "Género", "Valoración"]
    elif tipoElemento.lower() == "película":
        return ["ID", "Título", "Director", "Género", "Valoración"]
    elif tipoElemento.lower() == "música":
        return ["ID", "Título", "Artista", "Género", "Valoración"]
    return ["ID", "Título", "Persona", "Género", "Valoración"]  

def listarElementos(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
    else:
        print(f"=== Lista de {tipoElemento} ===")

        headers = generarEncabezados(tipoElemento)
        filas = []
        for e in elementos:
            
            campo_persona = obtenerCampoPersona(tipoElemento)
            fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
            filas.append(fila)

        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
    pausarPantalla()


def buscarElemento(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    etiqueta = "título, " + obtenerEtiquetaCampo(tipoElemento, obtenerCampoPersona(tipoElemento)) + " o género"
    criterio = validarSoloLetras(f"Buscar en {tipoElemento} por {etiqueta}: ")

    encontrados = [e for e in elementos if any(criterio.lower() in str(v).lower() for k, v in e.items() if k != "id")]

    if encontrados:
        headers = generarEncabezados(tipoElemento)
        filas = []
        for e in encontrados:
            campo_persona = obtenerCampoPersona(tipoElemento)
            fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
            filas.append(fila)
        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"⚠ No se encontraron {tipoElemento} con ese criterio.")
    pausarPantalla()

def buscarElementoPorCampo(ruta, tipoElemento, campo):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    
    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
        pausarPantalla()
        return

    etiqueta = obtenerEtiquetaCampo(tipoElemento, campo)
    criterio = validarSoloLetras(f"Buscar {tipoElemento} por {etiqueta}: ")

    encontrados = [e for e in elementos if criterio.lower() in str(e.get(campo, "")).lower()]

    if encontrados:
        print(f"=== {tipoElemento} encontrados por {etiqueta} ===")
        headers = generarEncabezados(tipoElemento)
        filas = []
        for e in encontrados:
            campo_persona = obtenerCampoPersona(tipoElemento)
            fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
            filas.append(fila)
        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"⚠ No se encontraron {tipoElemento} que contengan '{criterio}' en {etiqueta}.")
    pausarPantalla()

def editarElemento(ruta, tipoElemento, campos):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
        pausarPantalla()
        return

    print(f"=== {tipoElemento} disponibles para editar ===")
    headers = generarEncabezados(tipoElemento)
    filas = []
    for e in elementos:
        campo_persona = obtenerCampoPersona(tipoElemento)
        fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
        filas.append(fila)
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    idEditar = input(f"Ingrese el ID del {tipoElemento} a editar: ").strip()
    elemento = next((e for e in elementos if e["id"] == idEditar), None)

    if elemento:
        for campo in campos:
            etiqueta = obtenerEtiquetaCampo(tipoElemento, campo)
            if campo == "valoracion":
                nuevaVal = validarValoracion(permitirVacio=True)  
                if nuevaVal is not None:
                    elemento[campo] = nuevaVal
            else:
                valor_actual = elemento.get(campo, "N/A")
                nuevaVal = validarSoloLetras(f"Nuevo {etiqueta} ({valor_actual}): ", permitirVacio=True)
                if nuevaVal:
                    elemento[campo] = nuevaVal

        guardarJson(ruta, elementos)
        print(f"{tipoElemento} editado correctamente.")
    else:
        print(f"ID no encontrado en {tipoElemento}.")
    pausarPantalla()

def editarElementoCampoEspecifico(ruta, tipoElemento, camposPersona, campoAEditar):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
        pausarPantalla()
        return

    print(f"=== {tipoElemento} disponibles para editar ===")
    headers = generarEncabezados(tipoElemento)
    filas = []
    for e in elementos:
        campo_persona = obtenerCampoPersona(tipoElemento)
        fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
        filas.append(fila)
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    idEditar = input(f"Ingrese el ID del {tipoElemento} a editar: ").strip()
    elemento = next((e for e in elementos if e["id"] == idEditar), None)

    if elemento:
        etiqueta = obtenerEtiquetaCampo(tipoElemento, campoAEditar)
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

        guardarJson(ruta, elementos)
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")
    pausarPantalla()

def eliminarElemento(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)


    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados para eliminar.")
        pausarPantalla()
        return

    print(f"=== {tipoElemento} disponibles para eliminar ===")
    headers = generarEncabezados(tipoElemento)
    filas = []
    for e in elementos:
        campo_persona = obtenerCampoPersona(tipoElemento)
        fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
        filas.append(fila)
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    idEliminar = input(f"Ingrese el ID del {tipoElemento} a eliminar: ").strip()

    elementosFiltrados = [e for e in elementos if e["id"] != idEliminar]
    if len(elementosFiltrados) < len(elementos):
        guardarJson(ruta, elementosFiltrados)
        print(f"{tipoElemento} eliminado correctamente.")
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")



def eliminarElementoPorTitulo(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados para eliminar.")
        pausarPantalla()

    print(f"=== {tipoElemento} disponibles para eliminar ===")
    headers = generarEncabezados(tipoElemento)
    filas = []
    for e in elementos:
        campo_persona = obtenerCampoPersona(tipoElemento)
        fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
        filas.append(fila)
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    titulo_buscar = validarSoloLetras(f"Ingrese el título del {tipoElemento} a eliminar: ")
    

    coincidencias = [e for e in elementos if titulo_buscar.lower() in e["titulo"].lower()]
    
    if not coincidencias:
        print(f"⚠ No se encontró ningún {tipoElemento} con el título '{titulo_buscar}'.")
        pausarPantalla()
        return
    
    if len(coincidencias) == 1:
        elemento_eliminar = coincidencias[0]
        confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (s/n): ").strip().lower()
        if confirmacion == 's':
            elementos.remove(elemento_eliminar)
            guardarJson(ruta, elementos)
            print(f"{tipoElemento} '{elemento_eliminar['titulo']}' eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"\nSe encontraron {len(coincidencias)} {tipoElemento} con ese título:")
        filas_coincidencias = []
        for e in coincidencias:
            campo_persona = obtenerCampoPersona(tipoElemento)
            fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
            filas_coincidencias.append(fila)
        print(tabulate(filas_coincidencias, headers=headers, tablefmt="fancy_grid"))
        
        id_eliminar = input("Ingrese el ID específico a eliminar: ").strip()
        elemento_eliminar = next((e for e in coincidencias if e["id"] == id_eliminar), None)
        
        if elemento_eliminar:
            confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                elementos.remove(elemento_eliminar)
                guardarJson(ruta, elementos)
                print(f"{tipoElemento} eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("⚠ ID no válido.")
    
    pausarPantalla()

# Agregar esta función al final del archivo controllers/elemento.py

def filtrarPorGenero(ruta, tipoElemento):
    """Busca y filtra elementos por género - igual que la función buscar pero específica para géneros"""
    limpiarPantalla()
    elementos = cargarJson(ruta)
    
    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
        pausarPantalla()
        return
    # Pedir al usuario que ingrese el género (igual que buscar)
    etiqueta = obtenerEtiquetaCampo(tipoElemento, "genero")
    criterio = validarSoloLetras(f"Buscar {tipoElemento} por {etiqueta}: ")

    # Buscar elementos que coincidan con el género ingresado
    encontrados = [e for e in elementos if criterio.lower() in str(e.get("genero", "")).lower()]

    if encontrados:
        print(f"=== {tipoElemento} encontrados por {etiqueta} ===")
        headers = generarEncabezados(tipoElemento)
        filas = []
        for e in encontrados:
            campo_persona = obtenerCampoPersona(tipoElemento)
            fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
            filas.append(fila)
        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
        
    else:
        print(f"No se encontraron {tipoElemento} que contengan '{criterio}' en {etiqueta}.")
    pausarPantalla()
# Agregar estas funciones al final del archivo controllers/elemento.py

def guardarColeccion():
    """Guarda toda la colección (libros, películas, música) en un archivo de colecciones"""
    from config import RUTA_LIBROS, RUTA_PELICULAS, RUTA_MUSICA
    from utils.validata import validarSoloLetras
    import os
    
    limpiarPantalla()
    print("=== Guardar Colección ===")
    
    # Cargar todos los datos actuales
    libros = cargarJson(RUTA_LIBROS)
    peliculas = cargarJson(RUTA_PELICULAS)
    musica = cargarJson(RUTA_MUSICA)
    
    # Verificar si hay datos para guardar
    total_elementos = len(libros) + len(peliculas) + len(musica)
    if total_elementos == 0:
        print("⚠ No hay elementos para guardar. La colección está vacía.")
        pausarPantalla()
        return
    
    # Pedir nombre de la colección
    nombre_coleccion = validarSoloLetras("Ingrese el nombre de la colección: ")
    
    # Crear la estructura de datos para guardar
    coleccion = {
        "nombre": nombre_coleccion,
        "libros": libros,
        "peliculas": peliculas,
        "musica": musica
    }
    
    # Cargar colecciones existentes
    ruta_colecciones = "data/colecciones.json"
    colecciones_existentes = cargarJson(ruta_colecciones)
    
    # Buscar si ya existe una colección con ese nombre
    coleccion_existente = None
    for i, col in enumerate(colecciones_existentes):
        if col.get("nombre", "").lower() == nombre_coleccion.lower():
            coleccion_existente = i
            break
    
    # Si existe, preguntar si desea sobrescribir
    if coleccion_existente is not None:
        respuesta = input(f"Ya existe una colección llamada '{nombre_coleccion}'. ¿Desea sobrescribirla? (s/n): ").strip().lower()
        if respuesta == 's':
            colecciones_existentes[coleccion_existente] = coleccion
            print(f"Colección '{nombre_coleccion}' sobrescrita correctamente.")
        else:
            print("Guardado cancelado.")
            pausarPantalla()
            return
    else:
        # Agregar nueva colección
        colecciones_existentes.append(coleccion)
        print(f"Colección '{nombre_coleccion}' guardada correctamente.")
    
    # Guardar en el archivo de colecciones
    guardarJson(ruta_colecciones, colecciones_existentes)
    
    print(f"Total de elementos guardados: {total_elementos}")
    print(f"- Libros: {len(libros)}")
    print(f"- Películas: {len(peliculas)}")  
    print(f"- Música: {len(musica)}")
    pausarPantalla()

def cargarColeccion():
    """Carga una colección específica y restaura los datos en los archivos individuales"""
    from config import RUTA_LIBROS, RUTA_PELICULAS, RUTA_MUSICA
    from utils.validata import validarSoloLetras
    
    limpiarPantalla()
    print("=== Cargar Colección ===")
    
    # Cargar colecciones existentes
    ruta_colecciones = "data/colecciones.json"
    colecciones_existentes = cargarJson(ruta_colecciones)
    
    if not colecciones_existentes:
        print("⚠ No hay colecciones guardadas.")
        pausarPantalla()
        return
    
    # Mostrar colecciones disponibles
    print("Colecciones disponibles:")
    for i, coleccion in enumerate(colecciones_existentes, 1):
        nombre = coleccion.get("nombre", f"Colección {i}")
        libros_count = len(coleccion.get("libros", []))
        peliculas_count = len(coleccion.get("peliculas", []))
        musica_count = len(coleccion.get("musica", []))
        total = libros_count + peliculas_count + musica_count
        print(f"{i}. {nombre} ({total} elementos)")
    print("=" * 40)
    
    # Pedir nombre de la colección a cargar
    nombre_coleccion = validarSoloLetras("Ingrese el nombre de la colección a cargar: ")
    
    # Buscar la colección
    coleccion_encontrada = None
    for coleccion in colecciones_existentes:
        if coleccion.get("nombre", "").lower() == nombre_coleccion.lower():
            coleccion_encontrada = coleccion
            break
    
    if not coleccion_encontrada:
        print(f"⚠ No se encontró una colección llamada '{nombre_coleccion}'.")
        pausarPantalla()
        return
    
    # Confirmar carga (esto sobrescribirá los datos actuales)
    respuesta = input("⚠ Esto sobrescribirá todos los datos actuales. ¿Continuar? (s/n): ").strip().lower()
    if respuesta != 's':
        print("Carga cancelada.")
        pausarPantalla()
        return
    
    # Cargar los datos de la colección
    libros = coleccion_encontrada.get("libros", [])
    peliculas = coleccion_encontrada.get("peliculas", [])
    musica = coleccion_encontrada.get("musica", [])
    
    # Guardar en los archivos individuales
    guardarJson(RUTA_LIBROS, libros)
    guardarJson(RUTA_PELICULAS, peliculas)
    guardarJson(RUTA_MUSICA, musica)
    
    print(f"Colección '{nombre_coleccion}' cargada correctamente.")
    print(f"- Libros cargados: {len(libros)}")
    print(f"- Películas cargadas: {len(peliculas)}")
    print(f"- Música cargada: {len(musica)}")
    pausarPantalla()

def listarColecciones():
    """Lista todas las colecciones guardadas con detalles"""
    limpiarPantalla()
    print("=== Colecciones Guardadas ===")
    
    ruta_colecciones = "data/colecciones.json"
    colecciones_existentes = cargarJson(ruta_colecciones)
    
    if not colecciones_existentes:
        print("⚠ No hay colecciones guardadas.")
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