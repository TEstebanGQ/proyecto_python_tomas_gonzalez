from utils.screenControllers import limpiar_pantalla
import controllers.libros as libros
import controllers.peliculas as peliculas 
import controllers.musica as musica
from utils.corefiles import GestorArchivos

# Variables globales para la colección
coleccion = []
gestorArchivos = GestorArchivos()

def inicializar_coleccion():
    """Inicializa la colección cargando datos del archivo"""
    global coleccion
    coleccion = gestorArchivos.cargar_coleccion()
    print(f"🔄 Colección inicializada: {len(coleccion)} elementos cargados.")

def menuNuevoElemento():
    nuevoElemento = [
        'Libro',
        'Película', 
        'Música',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('       Añadir nuevo elemento      ')
        print('==================================')
        for a, item in enumerate(nuevoElemento, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-4): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(nuevoElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {nuevoElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    libros.crear_libro(coleccion, gestorArchivos)  # CORREGIDO
                case 2:
                    peliculas.crear_pelicula(coleccion, gestorArchivos)
                case 3:
                    musica.crear_musica(coleccion, gestorArchivos)
                case 4:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

def ListarElementos():
    TodosElementos = [
        'Ver todos los libros',
        'Ver todas las películas',
        'Ver toda la música',
        'Ver todos los elementos',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('      Ver todos los elementos     ')
        print('==================================')
        for a, item in enumerate(TodosElementos, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-5): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(TodosElementos):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {TodosElementos[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    libros.listar_libros(coleccion)
                case 2:
                    peliculas.listar_peliculas(coleccion)
                case 3:
                    musica.listar_musica(coleccion)
                case 4:
                    listar_todos_elementos()
                case 5:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

def listar_todos_elementos():
    """Lista todos los elementos de la colección usando tabulate"""
    from tabulate import tabulate
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("📋 La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    # Preparar datos para tabulate
    datos_tabla = []
    for elemento in coleccion:
        valoracion_str = f"{elemento.valoracion}/10" if elemento.valoracion else "Sin valorar"
        tipo_emoji = {"libro": "📚", "película": "🎬", "música": "🎵"}.get(elemento.tipo, "📄")
        
        datos_tabla.append({
            'ID': elemento.id,
            'Tipo': f"{tipo_emoji} {elemento.tipo.title()}",
            'Título': elemento.titulo,
            'Autor/Director/Artista': elemento.autor_director_artista,
            'Género': elemento.genero,
            'Valoración': valoracion_str,
            'Fecha': elemento.fecha_agregado.split()[0]
        })
    
    print(f"📋 TODOS LOS ELEMENTOS DE LA COLECCIÓN ({len(coleccion)})")
    print("=" * 120)
    print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    
    # Estadísticas por tipo
    tipos_count = {}
    for elem in coleccion:
        tipos_count[elem.tipo] = tipos_count.get(elem.tipo, 0) + 1
    
    print(f"\n📊 RESUMEN:")
    for tipo, cantidad in tipos_count.items():
        emoji = {"libro": "📚", "película": "🎬", "música": "🎵"}.get(tipo, "📄")
        print(f"  {emoji} {tipo.title()}: {cantidad}")
    print(f"  📋 Total: {len(coleccion)}")
    
    pausar_pantalla()

def buscar_por_titulo():
    """Busca elementos por título"""
    from tabulate import tabulate
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    titulo_buscar = input("Ingrese el título a buscar: ").strip().lower()
    if not titulo_buscar:
        print("Debe ingresar un título.")
        input("Presione Enter para continuar...")
        return
    
    resultados = [elem for elem in coleccion if titulo_buscar in elem.titulo.lower()]
    
    if not resultados:
        print(f"❌ No se encontraron elementos con el título '{titulo_buscar}'")
    else:
        # Preparar datos para tabulate
        datos_tabla = []
        for elem in resultados:
            valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
            tipo_emoji = {"libro": "📚", "película": "🎬", "música": "🎵"}.get(elem.tipo, "📄")
            
            datos_tabla.append({
                'ID': elem.id,
                'Tipo': f"{tipo_emoji} {elem.tipo.title()}",
                'Título': elem.titulo,
                'Autor/Director/Artista': elem.autor_director_artista,
                'Género': elem.genero,
                'Valoración': valoracion_str
            })
        
        print(f"🔍 RESULTADOS PARA '{titulo_buscar}' ({len(resultados)} encontrados)")
        print("=" * 100)
        print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    
    pausar_pantalla()

def buscar_por_autor():
    """Busca elementos por autor/director/artista"""
    from tabulate import tabulate
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    autor_buscar = input("Ingrese el nombre del autor/director/artista: ").strip().lower()
    if not autor_buscar:
        print("Debe ingresar un nombre.")
        input("Presione Enter para continuar...")
        return
    
    resultados = [elem for elem in coleccion if autor_buscar in elem.autor_director_artista.lower()]
    
    if not resultados:
        print(f"❌ No se encontraron elementos del autor/director/artista '{autor_buscar}'")
    else:
        # Preparar datos para tabulate
        datos_tabla = []
        for elem in resultados:
            valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
            tipo_emoji = {"libro": "📚", "película": "🎬", "música": "🎵"}.get(elem.tipo, "📄")
            
            datos_tabla.append({
                'ID': elem.id,
                'Tipo': f"{tipo_emoji} {elem.tipo.title()}",
                'Título': elem.titulo,
                'Autor/Director/Artista': elem.autor_director_artista,
                'Género': elem.genero,
                'Valoración': valoracion_str
            })
        
        print(f"🔍 RESULTADOS PARA '{autor_buscar}' ({len(resultados)} encontrados)")
        print("=" * 100)
        print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    
    pausar_pantalla()

def buscar_por_genero():
    """Busca elementos por género"""
    from tabulate import tabulate
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    genero_buscar = input("Ingrese el género a buscar: ").strip().lower()
    if not genero_buscar:
        print("Debe ingresar un género.")
        input("Presione Enter para continuar...")
        return
    
    resultados = [elem for elem in coleccion if genero_buscar in elem.genero.lower()]
    
    if not resultados:
        print(f"❌ No se encontraron elementos del género '{genero_buscar}'")
    else:
        # Preparar datos para tabulate
        datos_tabla = []
        for elem in resultados:
            valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
            tipo_emoji = {"libro": "📚", "película": "🎬", "música": "🎵"}.get(elem.tipo, "📄")
            
            datos_tabla.append({
                'ID': elem.id,
                'Tipo': f"{tipo_emoji} {elem.tipo.title()}",
                'Título': elem.titulo,
                'Autor/Director/Artista': elem.autor_director_artista,
                'Género': elem.genero,
                'Valoración': valoracion_str
            })
        
        print(f"🔍 RESULTADOS PARA GÉNERO '{genero_buscar}' ({len(resultados)} encontrados)")
        print("=" * 100)
        print(tabulate(datos_tabla, headers="keys", tablefmt="grid"))
    
    pausar_pantalla()

def menuBuscarElemento():
    BuscarElemento = [
        'Buscar por Título',
        'Buscar por Autor/Director/Artista',
        'Buscar por Género',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Buscar elemento          ')
        print('==================================')
        for a, item in enumerate(BuscarElemento, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-4): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(BuscarElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {BuscarElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    buscar_por_titulo()
                case 2:
                    buscar_por_autor()
                case 3:
                    buscar_por_genero()
                case 4:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

def encontrar_elemento_por_id(id_elemento):
    """Encuentra un elemento por su ID"""
    for elemento in coleccion:
        if elemento.id == id_elemento:
            return elemento
    return None

def editar_titulo():
    """Edita el título de un elemento"""
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar elementos disponibles
    print("📋 ELEMENTOS DISPONIBLES:")
    for elem in coleccion:
        print(f"ID: {elem.id} - {elem.titulo} ({elem.tipo})")
    print("-" * 40)
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"❌ No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"📝 Título actual: {elemento.titulo}")
    nuevo_titulo = input("Nuevo título: ").strip()
    
    if nuevo_titulo:
        elemento.titulo = nuevo_titulo
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Título actualizado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("❌ El título no puede estar vacío.")
    
    pausar_pantalla()

def editar_autor():
    """Edita el autor/director/artista de un elemento"""
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
        
    # Mostrar elementos disponibles
    print("📋 ELEMENTOS DISPONIBLES:")
    for elem in coleccion:
        print(f"ID: {elem.id} - {elem.titulo} ({elem.tipo})")
    print("-" * 40)
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"❌ No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"👤 Autor/Director/Artista actual: {elemento.autor_director_artista}")
    nuevo_autor = input("Nuevo autor/director/artista: ").strip()
    
    if nuevo_autor:
        elemento.autor_director_artista = nuevo_autor
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Autor/Director/Artista actualizado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("❌ El autor/director/artista no puede estar vacío.")
    
    pausar_pantalla()

def editar_genero():
    """Edita el género de un elemento"""
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar elementos disponibles
    print("📋 ELEMENTOS DISPONIBLES:")
    for elem in coleccion:
        print(f"ID: {elem.id} - {elem.titulo} ({elem.tipo})")
    print("-" * 40)
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"❌ No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"🏷️ Género actual: {elemento.genero}")
    nuevo_genero = input("Nuevo género: ").strip()
    
    if nuevo_genero:
        elemento.genero = nuevo_genero
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Género actualizado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("❌ El género no puede estar vacío.")
    
    pausar_pantalla()

def editar_valoracion():
    """Edita la valoración de un elemento"""
    from utils.screenControllers import pausar_pantalla
    from utils.validata import validar_valoracion
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar elementos disponibles
    print("📋 ELEMENTOS DISPONIBLES:")
    for elem in coleccion:
        valoracion_actual = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
        print(f"ID: {elem.id} - {elem.titulo} ({valoracion_actual})")
    print("-" * 40)
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"❌ No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    valoracion_actual = f"{elemento.valoracion}/10" if elemento.valoracion else "Sin valorar"
    print(f"⭐ Valoración actual: {valoracion_actual}")
    print("Nueva valoración (1-10, Enter para quitar valoración): ", end="")
    valoracion_input = input()
    
    if not valoracion_input.strip():
        elemento.valoracion = None
        print("✅ Valoración eliminada.")
    else:
        nueva_valoracion = validar_valoracion(valoracion_input)
        if nueva_valoracion is not False:
            elemento.valoracion = nueva_valoracion
            print("✅ Valoración actualizada exitosamente.")
        else:
            pausar_pantalla()
            return
    
    if gestorArchivos.guardar_coleccion(coleccion):
        print("✅ Cambios guardados exitosamente.")
    else:
        print("❌ Error al guardar los cambios.")
    
    pausar_pantalla()

def menuEditarElemento():
    EditarElemento = [
        'Editar Título',
        'Editar Autor/Director/Artista',
        'Editar Género',
        'Editar Valoración',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Editar elemento          ')
        print('==================================')
        for a, item in enumerate(EditarElemento, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-5): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(EditarElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {EditarElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    editar_titulo()
                case 2:
                    editar_autor()
                case 3:
                    editar_genero()
                case 4:
                    editar_valoracion()
                case 5:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

def eliminar_por_titulo():
    """Elimina un elemento por título"""
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    titulo_eliminar = input("Ingrese el título del elemento a eliminar: ").strip()
    if not titulo_eliminar:
        print("Debe ingresar un título.")
        input("Presione Enter para continuar...")
        return
    
    elementos_encontrados = [elem for elem in coleccion if titulo_eliminar.lower() in elem.titulo.lower()]
    
    if not elementos_encontrados:
        print(f"❌ No se encontraron elementos con el título '{titulo_eliminar}'")
        pausar_pantalla()
        return
    
    if len(elementos_encontrados) == 1:
        elemento = elementos_encontrados[0]
        print(f"📋 Elemento encontrado:")
        print(f"  Título: {elemento.titulo}")
        print(f"  Tipo: {elemento.tipo}")
        print(f"  Autor/Director/Artista: {elemento.autor_director_artista}")
        
        confirmacion = input("¿Está seguro de que desea eliminar este elemento? (s/N): ").strip().lower()
        if confirmacion == 's':
            coleccion.remove(elemento)
            if gestorArchivos.guardar_coleccion(coleccion):
                print("✅ Elemento eliminado exitosamente.")
            else:
                print("❌ Error al guardar los cambios.")
        else:
            print("❌ Operación cancelada.")
    else:
        print(f"🔍 Se encontraron {len(elementos_encontrados)} elementos:")
        for i, elem in enumerate(elementos_encontrados, 1):
            print(f"{i}. {elem.titulo} ({elem.tipo}) - ID: {elem.id}")
        
        try:
            seleccion = int(input("Seleccione el número del elemento a eliminar (0 para cancelar): "))
            if seleccion == 0:
                print("❌ Operación cancelada.")
                pausar_pantalla()
                return
            
            if 1 <= seleccion <= len(elementos_encontrados):
                elemento = elementos_encontrados[seleccion - 1]
                confirmacion = input(f"¿Está seguro de que desea eliminar '{elemento.titulo}'? (s/N): ").strip().lower()
                if confirmacion == 's':
                    coleccion.remove(elemento)
                    if gestorArchivos.guardar_coleccion(coleccion):
                        print("✅ Elemento eliminado exitosamente.")
                    else:
                        print("❌ Error al guardar los cambios.")
                else:
                    print("❌ Operación cancelada.")
            else:
                print("❌ Selección inválida.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")
    
    pausar_pantalla()

def eliminar_por_id():
    """Elimina un elemento por ID"""
    from utils.screenControllers import pausar_pantalla
    
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar elementos disponibles
    print("📋 ELEMENTOS DISPONIBLES:")
    for elem in coleccion:
        print(f"ID: {elem.id} - {elem.titulo} ({elem.tipo})")
    print("-" * 40)
    
    id_eliminar = input("Ingrese el ID del elemento a eliminar: ").strip()
    elemento = encontrar_elemento_por_id(id_eliminar)
    
    if not elemento:
        print(f"❌ No se encontró un elemento con ID '{id_eliminar}'")
        pausar_pantalla()
        return
    
    print(f"📋 Elemento encontrado:")
    print(f"  ID: {elemento.id}")
    print(f"  Título: {elemento.titulo}")
    print(f"  Tipo: {elemento.tipo}")
    print(f"  Autor/Director/Artista: {elemento.autor_director_artista}")
    
    confirmacion = input("¿Está seguro de que desea eliminar este elemento? (s/N): ").strip().lower()
    if confirmacion == 's':
        coleccion.remove(elemento)
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Elemento eliminado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("❌ Operación cancelada.")
    
    pausar_pantalla()

def menuEliminarElemento():
    EliminarElemento = [
        'Eliminar por Título',
        'Eliminar por Identificador Único',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Eliminar elemento        ')
        print('==================================')
        for a, item in enumerate(EliminarElemento, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-3): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(EliminarElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {EliminarElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    eliminar_por_titulo()
                case 2:
                    eliminar_por_id()
                case 3:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

def menuVerCategoria():
    VerCategoria = [
        'Ver libros',
        'Ver películas',
        'Ver música',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Ver por categoría        ')
        print('==================================')
        for a, item in enumerate(VerCategoria, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-4): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(VerCategoria):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {VerCategoria[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    libros.listar_libros(coleccion)
                case 2:
                    peliculas.listar_peliculas(coleccion)
                case 3:
                    musica.listar_musica(coleccion)
                case 4:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

def guardar_coleccion_manual():
    """Guarda manualmente la colección"""
    from utils.screenControllers import pausar_pantalla
    
    if gestorArchivos.guardar_coleccion(coleccion):
        print(f"✅ Colección guardada exitosamente en '{gestorArchivos.archivo}'")
        print(f"📊 Total de elementos guardados: {len(coleccion)}")
    else:
        print("❌ Error al guardar la colección")
    
    pausar_pantalla()

def cargar_coleccion_manual():
    """Carga manualmente una colección"""
    from utils.screenControllers import pausar_pantalla
    global coleccion
    
    archivo_personalizado = input(f"Ingrese el nombre del archivo (Enter para usar '{gestorArchivos.archivo}'): ").strip()
    
    if archivo_personalizado:
        gestor_temp = GestorArchivos(archivo_personalizado)
        coleccion_temp = gestor_temp.cargar_coleccion()
    else:
        coleccion_temp = gestorArchivos.cargar_coleccion()
    
    if coleccion_temp is not None:  # Incluir lista vacía como válida
        confirmacion = input(f"¿Desea reemplazar la colección actual? Esto eliminará {len(coleccion)} elementos actuales (s/N): ").strip().lower()
        
        if confirmacion == 's':
            coleccion = coleccion_temp
            if archivo_personalizado:
                gestorArchivos.archivo = archivo_personalizado
            print(f"✅ Colección cargada exitosamente")
            print(f"📊 Total de elementos cargados: {len(coleccion)}")
        else:
            print("❌ Operación cancelada.")
    else:
        print("❌ No se pudo cargar la colección o el archivo no existe.")
    
    pausar_pantalla()

def menuGuardarCargar():
    GuardarCargar = [
        'Guardar colección actual',
        'Cargar una colección guardada',
        'Regresar al menú principal'
    ]
    
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Guardar y cargar         ')
        print('==================================')
        for a, item in enumerate(GuardarCargar, start=1):
            print(f'{a}. {item}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción (1-3): "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(GuardarCargar):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {GuardarCargar[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    guardar_coleccion_manual()
                case 2:
                    cargar_coleccion_manual()
                case 3:
                    return
                    
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")