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
            datos[campo] = validarValoracion(permitirVacio=False)
        else:
            datos[campo] = validarSoloLetras(f"Ingrese {campo}: ")

    datos["id"] = generarId(elementos)
    elementos.append(datos)
    guardarJson(ruta, elementos)
    print(f"✅ {tipoElemento} agregado correctamente.")
    pausarPantalla()

# ✅ Listar elementos
def listarElementos(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    if not elementos:
        print(f"⚠ No hay {tipoElemento} registrados.")
    else:
        print(f"=== Lista de {tipoElemento} ===")
        print(tabulate(elementos, headers="keys", tablefmt="fancy_grid"))
    pausarPantalla()

# ✅ Buscar elementos
def buscarElemento(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    criterio = validarSoloLetras(f"Buscar en {tipoElemento} por título, autor/director/artista o género: ")

    encontrados = [e for e in elementos if any(criterio.lower() in str(v).lower() for k, v in e.items() if k != "id")]

    if encontrados:
        print(tabulate(encontrados, headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"⚠ No se encontraron {tipoElemento} con ese criterio.")
    pausarPantalla()

# ✅ Editar elemento
def editarElemento(ruta, tipoElemento, campos):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    listarElementos(ruta, tipoElemento)
    idEditar = input(f"Ingrese el ID del {tipoElemento} a editar: ").strip()

    elemento = next((e for e in elementos if e["id"] == idEditar), None)
    if elemento:
        for campo in campos:
            if campo == "valoracion":
                nuevaVal = validarValoracion(permitirVacio=True)
                if nuevaVal is not None:
                    elemento[campo] = nuevaVal
            else:
                nuevaVal = validarSoloLetras(f"Nuevo {campo} ({elemento[campo]}): ", permitirVacio=True)
                if nuevaVal:
                    elemento[campo] = nuevaVal

        guardarJson(ruta, elementos)
        print(f"✅ {tipoElemento} editado correctamente.")
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")
    pausarPantalla()

# ✅ Eliminar elemento
def eliminarElemento(ruta, tipoElemento):
    limpiarPantalla()
    elementos = cargarJson(ruta)
    listarElementos(ruta, tipoElemento)
    idEliminar = input(f"Ingrese el ID del {tipoElemento} a eliminar: ").strip()

    elementosFiltrados = [e for e in elementos if e["id"] != idEliminar]
    if len(elementosFiltrados) < len(elementos):
        guardarJson(ruta, elementosFiltrados)
        print(f"✅ {tipoElemento} eliminado correctamente.")
    else:
        print(f"⚠ ID no encontrado en {tipoElemento}.")
    pausarPantalla()
