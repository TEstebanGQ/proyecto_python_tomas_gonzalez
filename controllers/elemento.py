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

# ✅ Obtener el campo correcto según el tipo (autor/director/artista)
def obtenerCampoPersona(tipoElemento):
    if tipoElemento.lower() == "libro":
        return "autor"
    elif tipoElemento.lower() == "película":
        return "director"  
    elif tipoElemento.lower() == "música":
        return "artista"
    return "autor"  # Por defecto

# ✅ Obtener etiqueta dinámica (Autor/Director/Artista)
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
    return ["ID", "Título", "Persona", "Género", "Valoración"]  # Por defecto

# ✅ Listar elementos con encabezados personalizados
def listarElementos(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
    else:
        print(f"=== Lista de {tipoElemento} ===")

        # Encabezados personalizados según tipo
        headers = generarEncabezados(tipoElemento)
        
        # Convertir datos a lista de filas en el orden correcto
        filas = []
        for e in elementos:
            # Obtener el campo correcto (autor/director/artista)
            campo_persona = obtenerCampoPersona(tipoElemento)
            fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
            filas.append(fila)

        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
    pausarPantalla()

# ✅ Buscar elementos
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

# ✅ Nueva función: Buscar por campo específico
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

# ✅ Editar elemento (con encabezados correctos antes de editar)
def editarElemento(ruta, tipoElemento, campos):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    # Mostrar lista con encabezados dinámicos
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

    # Seleccionar ID a editar
    idEditar = input(f"Ingrese el ID del {tipoElemento} a editar: ").strip()
    elemento = next((e for e in elementos if e["id"] == idEditar), None)

    if elemento:
        for campo in campos:
            etiqueta = obtenerEtiquetaCampo(tipoElemento, campo)
            if campo == "valoracion":
                nuevaVal = validarValoracion(permitirVacio=True)  # Permitir vacío en edición
                if nuevaVal is not None:
                    elemento[campo] = nuevaVal
            else:
                valor_actual = elemento.get(campo, "N/A")
                nuevaVal = validarSoloLetras(f"Nuevo {etiqueta} ({valor_actual}): ", permitirVacio=True)
                if nuevaVal:
                    elemento[campo] = nuevaVal

        guardarJson(ruta, elementos)
        print(f"✅ {tipoElemento} editado correctamente.")
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")
    pausarPantalla()

# ✅ Nueva función: Editar campo específico
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

    # Seleccionar ID a editar
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
                print(f"✅ {etiqueta} actualizada correctamente.")
            else:
                print("No se realizaron cambios.")
        else:
            nuevaVal = validarSoloLetras(f"Nuevo {etiqueta} ({valor_actual}): ", permitirVacio=True)
            if nuevaVal:
                elemento[campoAEditar] = nuevaVal
                print(f"✅ {etiqueta} actualizado correctamente.")
            else:
                print("No se realizaron cambios.")

        guardarJson(ruta, elementos)
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")
    pausarPantalla()

# ✅ Eliminar elemento (con encabezados correctos antes de eliminar)
def eliminarElemento(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    # Verificar si hay elementos
    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados para eliminar.")
        pausarPantalla()
        return

    # Mostrar lista con encabezados dinámicos
    print(f"=== {tipoElemento} disponibles para eliminar ===")
    headers = generarEncabezados(tipoElemento)
    filas = []
    for e in elementos:
        campo_persona = obtenerCampoPersona(tipoElemento)
        fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
        filas.append(fila)
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    # Solicitar ID para eliminar
    idEliminar = input(f"Ingrese el ID del {tipoElemento} a eliminar: ").strip()

    # Filtrar elementos
    elementosFiltrados = [e for e in elementos if e["id"] != idEliminar]
    if len(elementosFiltrados) < len(elementos):
        guardarJson(ruta, elementosFiltrados)
        print(f"✅ {tipoElemento} eliminado correctamente.")
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")
    pausarPantalla()

# ✅ Nueva función: Eliminar por título
def eliminarElementoPorTitulo(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados para eliminar.")
        pausarPantalla()
        return

    # Mostrar lista
    print(f"=== {tipoElemento} disponibles para eliminar ===")
    headers = generarEncabezados(tipoElemento)
    filas = []
    for e in elementos:
        campo_persona = obtenerCampoPersona(tipoElemento)
        fila = [e["id"], e["titulo"], e.get(campo_persona, "N/A"), e["genero"], e["valoracion"]]
        filas.append(fila)
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    # Buscar por título
    titulo_buscar = validarSoloLetras(f"Ingrese el título del {tipoElemento} a eliminar: ")
    
    # Buscar elementos que coincidan
    coincidencias = [e for e in elementos if titulo_buscar.lower() in e["titulo"].lower()]
    
    if not coincidencias:
        print(f"⚠ No se encontró ningún {tipoElemento} con el título '{titulo_buscar}'.")
        pausarPantalla()
        return
    
    if len(coincidencias) == 1:
        # Solo una coincidencia, eliminar directamente
        elemento_eliminar = coincidencias[0]
        confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (s/n): ").strip().lower()
        if confirmacion == 's':
            elementos.remove(elemento_eliminar)
            guardarJson(ruta, elementos)
            print(f"✅ {tipoElemento} '{elemento_eliminar['titulo']}' eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        # Múltiples coincidencias, mostrar opciones
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
                print(f"✅ {tipoElemento} eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("⚠ ID no válido.")
    
    pausarPantalla()