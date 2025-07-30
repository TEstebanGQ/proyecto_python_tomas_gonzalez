from utils.coreFiles import cargarJson, guardarJson
from utils.validata import validarSoloLetras, validarValoracion, generarId
from utils.screenControllers import limpiarPantalla, pausarPantalla
from tabulate import tabulate

# ✅ Añadir elemento genérico
def agregarElemento(ruta, tipoElemento, campos):
    limpiarPantalla()
    elementos = cargarJson(ruta)

    print(f"=== Añadir {tipoElemento} ===")
    datos = {}

    for campo in campos:
        if campo == "valoracion":
            datos[campo] = validarValoracion()  # Obligatoria
        else:
            etiqueta = obtenerEtiquetaCampo(tipoElemento, campo)
            datos[campo] = validarSoloLetras(f"Ingrese {etiqueta}: ")

    datos["id"] = generarId(elementos)
    elementos.append(datos)
    guardarJson(ruta, elementos)
    print(f"✅ {tipoElemento} agregado correctamente.")
    pausarPantalla()

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
        filas = [[e["id"], e["titulo"], e["autor"], e["genero"], e["valoracion"]] for e in elementos]

        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
    pausarPantalla()

# ✅ Buscar elementos
def buscarElemento(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    etiqueta = "título, " + obtenerEtiquetaCampo(tipoElemento, "autor") + " o género"
    criterio = validarSoloLetras(f"Buscar en {tipoElemento} por {etiqueta}: ")

    encontrados = [e for e in elementos if any(criterio.lower() in str(v).lower() for k, v in e.items() if k != "id")]

    if encontrados:
        headers = generarEncabezados(tipoElemento)
        filas = [[e["id"], e["titulo"], e["autor"], e["genero"], e["valoracion"]] for e in encontrados]
        print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"⚠ No se encontraron {tipoElemento} con ese criterio.")
    pausarPantalla()

# ✅ Editar elemento
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
    filas = [[e["id"], e["titulo"], e["autor"], e["genero"], e["valoracion"]] for e in elementos]
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

    # Seleccionar ID a editar
    idEditar = input(f"Ingrese el ID del {tipoElemento} a editar: ").strip()
    elemento = next((e for e in elementos if e["id"] == idEditar), None)

    if elemento:
        for campo in campos:
            etiqueta = obtenerEtiquetaCampo(tipoElemento, campo)
            if campo == "valoracion":
                nuevaVal = validarValoracion()  # Ahora obligatoria
                elemento[campo] = nuevaVal
            else:
                nuevaVal = validarSoloLetras(f"Nuevo {etiqueta} ({elemento[campo]}): ", permitirVacio=True)
                if nuevaVal:
                    elemento[campo] = nuevaVal

        guardarJson(ruta, elementos)
        print(f"✅ {tipoElemento} editado correctamente.")
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
    filas = [[e["id"], e["titulo"], e["autor"], e["genero"], e["valoracion"]] for e in elementos]
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


# ✅ Obtener etiqueta dinámica (Autor/Director/Artista)
def obtenerEtiquetaCampo(tipoElemento, campo):
    if campo == "autor":
        if tipoElemento.lower() == "libro":
            return "Autor"
        elif tipoElemento.lower() == "película":
            return "Director"
        elif tipoElemento.lower() == "música":
            return "Artista"
    elif campo == "genero":
        return "Género"
    elif campo == "titulo":
        return "Título"
    elif campo == "valoracion":
        return "Valoración"
    return campo

# ✅ Generar encabezados dinámicos para la tabla
def generarEncabezados(tipoElemento):
    if tipoElemento.lower() == "libro":
        return ["ID", "Título", "Autor", "Género", "Valoración"]
    elif tipoElemento.lower() == "película":
        return ["ID", "Título", "Director", "Género", "Valoración"]
    elif tipoElemento.lower() == "música":
        return ["ID", "Título", "Artista", "Género", "Valoración"]
