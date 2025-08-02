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
    
    # Muestro título si se proporciona
    if titulo:
        print(f"=== {titulo} ===")
    
    # Genero encabezados dinámicos y creo filas
    headers = generarEncabezados(tipoElemento)
    filas = [crearFilaTabla(e, tipoElemento) for e in elementos]
    
    # Muestro la tabla con formato elegante
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

def mostrarTablaSinId(elementos, tipoElemento, titulo=""):
    if not elementos:
        print(f"No hay {tipoElemento} registrados.")
        return
    
    if titulo:
        print(f"=== {titulo} ===")
    
    # Encabezados sin ID para mayor claridad visual
    config = obtenerConfigTipo(tipoElemento)
    campo_persona = config['campo_persona']
    headers = ["Título", config['etiqueta_persona'], "Género", "Valoración"]

    # Creo filas sin incluir el ID
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

def agregarElemento(tipoElemento):
    try:
        limpiarPantalla()
        config = obtenerConfigTipo(tipoElemento)
        elementos = cargarJson(config['ruta'])

        print(f"=== Añadir {config['nombre']} ===")
        datos = {}
        # Solicito cada campo con validación específica
        for campo in config['campos']:
            if campo == "valoracion":
                # Validación especial para valoraciones numéricas
                resultado = validarValoracion()
                if resultado is None:  
                    return
                datos[campo] = resultado
            else:
                # Validación de texto para otros campos
                etiqueta = obtenerEtiquetaCampo(campo)
                resultado = validarSoloLetras(f"Ingrese {etiqueta}: ")
                if resultado is None:  #
                    return
                datos[campo] = resultado

        # Genero ID único y guardo
        datos["id"] = generarId(elementos)
        elementos.append(datos)
        guardarJson(config['ruta'], elementos)
        
        print(f"{config['nombre']} agregado correctamente.")
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass  
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return

def listarElementos(tipoElemento):
    limpiarPantalla()
    config = obtenerConfigTipo(tipoElemento)
    elementos = cargarJson(config['ruta'])
    mostrarTabla(elementos, tipoElemento, f"Lista de {config['plural']}")
    pausarPantalla()


def buscarElementoPorCampo(tipoElemento, campo):
    try:
        limpiarPantalla()
        config = obtenerConfigTipo(tipoElemento)
        elementos = cargarJson(config['ruta'])
        
        # Verifico que haya elementos para buscar
        if not elementos:
            print(f"No hay {config['plural']} registrados.")
            pausarPantalla()
            return

        # Solicito el criterio de búsqueda
        etiqueta = obtenerEtiquetaCampo(campo)
        criterio = validarSoloLetras(f"Buscar {config['plural']} por {etiqueta}: ")
        
        if criterio is None:  # Usuario canceló
            return
            
        encontrados = [e for e in elementos 
        if criterio.lower() in str(e.get(campo, "")).lower()]
        
        # Muestro resultados
        if encontrados:
            mostrarTabla(encontrados, tipoElemento, 
                        f"{config['plural']} encontrados por {etiqueta}")
        else:
            print(f"No se encontraron {config['plural']} que contengan '{criterio}' en {etiqueta}.")
        
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return


def editarElementoCampoEspecifico(tipoElemento, campoAEditar):
    try:
        limpiarPantalla()
        config = obtenerConfigTipo(tipoElemento)
        elementos = cargarJson(config['ruta'])

        # Verifico que haya elementos para editar
        if not elementos:
            print(f"No hay {config['plural']} registrados.")
            pausarPantalla()
            return

        # Muestro elementos disponibles para que el usuario elija
        mostrarTabla(elementos, tipoElemento, f"{config['plural']} disponibles para editar")

        try:
            idEditar = input(f"Ingrese el ID del {config['nombre']} a editar: ").strip()
        except (KeyboardInterrupt, EOFError):
            return
            
        # Busco el elemento por ID
        elemento = next((e for e in elementos if e["id"] == idEditar), None)

        if not elemento:
            print(f"ID no encontrado en {config['plural']}.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return
        # Proceso de edición específico por tipo de campo
        etiqueta = obtenerEtiquetaCampo(campoAEditar)
        valor_actual = elemento.get(campoAEditar, "N/A")
        
        if campoAEditar == "valoracion":
            # Manejo especial para valoraciones numéricas
            print(f"Valoración actual: {valor_actual}")
            nuevaVal = validarValoracion(permitirVacio=True)
            if nuevaVal is None and valor_actual == "N/A":  
                return
            if nuevaVal is not None:
                elemento[campoAEditar] = nuevaVal
                print(f"{etiqueta} actualizada correctamente.")
            else:
                print("No se realizaron cambios.")
        else:
            # Manejo para campos de texto
            nuevaVal = validarSoloLetras(f"Nuevo {etiqueta} ({valor_actual}): ", permitirVacio=True)
            if nuevaVal is None:  # Cancelado
                return
            if nuevaVal:  # Solo actualizo si ingresó algo nuevo
                elemento[campoAEditar] = nuevaVal
                print(f"{etiqueta} actualizado correctamente.")
            else:
                print("No se realizaron cambios.")

        # Guardo cambios solo si llegué hasta aquí
        guardarJson(config['ruta'], elementos)
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return

def eliminarElemento(tipoElemento):
    try:
        limpiarPantalla()
        config = obtenerConfigTipo(tipoElemento)
        elementos = cargarJson(config['ruta'])

        if not elementos:
            print(f"No hay {config['plural']} registrados para eliminar.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return

        # Muestro elementos disponibles para eliminación
        mostrarTabla(elementos, tipoElemento, f"{config['plural']} disponibles para eliminar")

        try:
            idEliminar = input(f"Ingrese el ID del {config['nombre']} a eliminar: ").strip()
        except (KeyboardInterrupt, EOFError):
            return
            
        # Filtro elementos manteniendo todos excepto el seleccionado
        elementosFiltrados = [e for e in elementos if e["id"] != idEliminar]
        
        # Verifico si realmente eliminé algo
        if len(elementosFiltrados) < len(elementos):
            guardarJson(config['ruta'], elementosFiltrados)
            print(f"{config['nombre']} eliminado correctamente.")
        else:
            print(f"ID no encontrado en {config['plural']}.")
        
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return

def eliminarElementoPorTitulo(tipoElemento):
    try:
        limpiarPantalla()
        config = obtenerConfigTipo(tipoElemento)
        elementos = cargarJson(config['ruta'])

        if not elementos:
            print(f"No hay {config['plural']} registrados para eliminar.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return

        # Muestro sin IDs 
        mostrarTablaSinId(elementos, tipoElemento, f"{config['plural']} disponibles para eliminar")

        titulo_buscar = validarSoloLetras(f"Ingrese el título del {config['nombre']} a eliminar: ")
        if titulo_buscar is None:  # Usuario canceló
            return
            
        # Busco coincidencias parciales
        coincidencias = [e for e in elementos if titulo_buscar.lower() in e["titulo"].lower()]
        
        if not coincidencias:
            print(f"No se encontró ningún {config['nombre']} con el título '{titulo_buscar}'.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return
        
        if len(coincidencias) == 1:
            # Una sola coincidencia 
            elemento_eliminar = coincidencias[0]
            try:
                confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (si/no): ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                return
                
            if confirmacion == 'si':
                elementos.remove(elemento_eliminar)
                guardarJson(config['ruta'], elementos)
                print(f"{config['nombre']} '{elemento_eliminar['titulo']}' eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            # Múltiples coincidencias - necesito que el usuario especifique
            print(f"Se encontraron {len(coincidencias)} {config['plural']} con ese título:")
            mostrarTablaSinId(coincidencias, tipoElemento)
            
            print("Seleccione cuál eliminar:")
            for i, elemento in enumerate(coincidencias, 1):
                print(f"{i}. {elemento['titulo']} - {elemento.get(config['campo_persona'], 'N/A')} ({elemento['genero']})")
            
            try:
                seleccion = int(input("Ingrese el número del elemento a eliminar: ")) - 1
                if 0 <= seleccion < len(coincidencias):
                    elemento_eliminar = coincidencias[seleccion]
                    try:
                        confirmacion = input(f"¿Está seguro de eliminar '{elemento_eliminar['titulo']}'? (s/n): ").strip().lower()
                    except (KeyboardInterrupt, EOFError):
                        return
                        
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
            except (KeyboardInterrupt, EOFError):
                return
        
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return


def guardarColeccion():
    try:
        limpiarPantalla()
        print("=== Guardar Colección ===")
        # Recopilo todos los datos del sistema
        libros = cargarJson(TIPOS_ELEMENTOS['libro']['ruta'])
        peliculas = cargarJson(TIPOS_ELEMENTOS['película']['ruta'])
        musica = cargarJson(TIPOS_ELEMENTOS['música']['ruta'])
        # Verifico que haya algo que respaldar
        total_elementos = len(libros) + len(peliculas) + len(musica)
        if total_elementos == 0:
            print("No hay elementos para guardar. La colección está vacía.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return
        # Solicito nombre para la colección
        nombre_coleccion = validarSoloLetras("Ingrese el nombre de la colección: ")
        if nombre_coleccion is None:  
            return
        # Creo el paquete de respaldo completo
        coleccion = {
            "nombre": nombre_coleccion,
            "libros": libros,
            "peliculas": peliculas,
            "musica": musica
        }
        
        # Cargo colecciones existentes para verificar duplicados
        colecciones_existentes = cargarJson(RUTA_COLECCIONES)
        
        # Manejo sobrescritura de colecciones existentes
        for i, col in enumerate(colecciones_existentes):
            if col.get("nombre", "").lower() == nombre_coleccion.lower():
                try:
                    respuesta = input(f"Ya existe una colección llamada '{nombre_coleccion}'. ¿Desea sobrescribirla? (s/n): ").strip().lower()
                except (KeyboardInterrupt, EOFError):
                    return
                    
                if respuesta == 's':
                    colecciones_existentes[i] = coleccion
                    print(f"Colección '{nombre_coleccion}' sobrescrita correctamente.")
                else:
                    print("Guardado cancelado.")
                    try:
                        pausarPantalla()
                    except (KeyboardInterrupt, EOFError):
                        pass
                    return
                break
        else:
            # No hay duplicado - agrego nueva colección
            colecciones_existentes.append(coleccion)
            print(f"Colección '{nombre_coleccion}' guardada correctamente.")
        
        # Guardo y muestro estadísticas
        guardarJson(RUTA_COLECCIONES, colecciones_existentes)
        
        print(f"Total de elementos guardados: {total_elementos}")
        print(f"- Libros: {len(libros)}")
        print(f"- Películas: {len(peliculas)}")  
        print(f"- Música: {len(musica)}")
        
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return

def cargarColeccion():
    try:
        limpiarPantalla()
        print("=== Cargar Colección ===")
        
        coleccionesExistentes = cargarJson(RUTA_COLECCIONES)
        
        if not coleccionesExistentes:
            print(" No hay colecciones guardadas.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return
        
        # Muestro colecciones disponibles con estadísticas
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
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return
        except (KeyboardInterrupt, EOFError):
            return
        
        coleccionSeleccionada = coleccionesExistentes[seleccion - 1]
        nombreColeccion = coleccionSeleccionada.get("nombre", f"Colección {seleccion}")
        
        # Advertencia crítica sobre sobrescritura
        try:
            respuesta = input("Esto sobrescribirá todos los datos actuales. ¿Continuar? (s/n): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            return
            
        if respuesta != 's':
            print("Carga cancelada.")
            try:
                pausarPantalla()
            except (KeyboardInterrupt, EOFError):
                pass
            return
        # Extraigo datos de la colección
        libros = coleccionSeleccionada.get("libros", [])
        peliculas = coleccionSeleccionada.get("peliculas", [])
        musica = coleccionSeleccionada.get("musica", [])
        
        # Sobrescribo TODOS los archivos de datos
        guardarJson(TIPOS_ELEMENTOS['libro']['ruta'], libros)
        guardarJson(TIPOS_ELEMENTOS['película']['ruta'], peliculas)
        guardarJson(TIPOS_ELEMENTOS['música']['ruta'], musica)
        
        # Confirmo operación exitosa con estadísticas
        print(f"Colección '{nombreColeccion}' cargada correctamente.")
        print(f"- Libros cargados: {len(libros)}")
        print(f"- Películas cargadas: {len(peliculas)}")
        print(f"- Música cargada: {len(musica)}")
        
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
            
    except (KeyboardInterrupt, EOFError):
        limpiarPantalla()
        print("===================================")
        print("    Operación cancelada           ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return

def listarColecciones():
    limpiarPantalla()
    print("=== Colecciones Guardadas ===")
    
    colecciones_existentes = cargarJson(RUTA_COLECCIONES)
    
    if not colecciones_existentes:
        print("No hay colecciones guardadas.")
        try:
            pausarPantalla()
        except (KeyboardInterrupt, EOFError):
            pass
        return
    # Muestro cada colección con desglose detallado
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
    
    try:
        pausarPantalla()
    except (KeyboardInterrupt, EOFError):
        pass



