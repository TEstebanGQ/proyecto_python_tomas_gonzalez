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
                    libros.agregar_libro()  # Cambiado de crear_libro a agregar_libro
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
    """Lista todos los elementos de la colección"""
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    print("=== TODOS LOS ELEMENTOS ===")
    print("-" * 80)
    
    # Agrupar por tipo
    tipos = {'libro': [], 'película': [], 'música': []}
    for elemento in coleccion:
        if elemento.tipo in tipos:
            tipos[elemento.tipo].append(elemento)
    
    for tipo, elementos in tipos.items():
        if elementos:
            print(f"\n📚 {tipo.upper()}S ({len(elementos)})")
            print("=" * 40)
            for elem in elementos:
                valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
                print(f"• {elem.titulo} - {elem.autor_director_artista} ({valoracion_str})")
    
    print(f"\nTotal de elementos: {len(coleccion)}")
    input("\nPresione Enter para continuar...")

def buscar_por_titulo():
    """Busca elementos por título"""
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
        print(f"No se encontraron elementos con el título '{titulo_buscar}'")
    else:
        print(f"=== RESULTADOS PARA '{titulo_buscar}' ===")
        print("-" * 80)
        for elem in resultados:
            valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
            print(f"ID: {elem.id}")
            print(f"Título: {elem.titulo}")
            print(f"Tipo: {elem.tipo}")
            print(f"Autor/Director/Artista: {elem.autor_director_artista}")
            print(f"Género: {elem.genero}")
            print(f"Valoración: {valoracion_str}")
            print("-" * 80)
    
    input("Presione Enter para continuar...")

def buscar_por_autor():
    """Busca elementos por autor/director/artista"""
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
        print(f"No se encontraron elementos del autor/director/artista '{autor_buscar}'")
    else:
        print(f"=== RESULTADOS PARA '{autor_buscar}' ===")
        print("-" * 80)
        for elem in resultados:
            valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
            print(f"ID: {elem.id}")
            print(f"Título: {elem.titulo}")
            print(f"Tipo: {elem.tipo}")
            print(f"Autor/Director/Artista: {elem.autor_director_artista}")
            print(f"Género: {elem.genero}")
            print(f"Valoración: {valoracion_str}")
            print("-" * 80)
    
    input("Presione Enter para continuar...")

def buscar_por_genero():
    """Busca elementos por género"""
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
        print(f"No se encontraron elementos del género '{genero_buscar}'")
    else:
        print(f"=== RESULTADOS PARA GÉNERO '{genero_buscar}' ===")
        print("-" * 80)
        for elem in resultados:
            valoracion_str = f"{elem.valoracion}/10" if elem.valoracion else "Sin valorar"
            print(f"ID: {elem.id}")
            print(f"Título: {elem.titulo}")
            print(f"Tipo: {elem.tipo}")
            print(f"Autor/Director/Artista: {elem.autor_director_artista}")
            print(f"Género: {elem.genero}")
            print(f"Valoración: {valoracion_str}")
            print("-" * 80)
    
    input("Presione Enter para continuar...")

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
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"Título actual: {elemento.titulo}")
    nuevo_titulo = input("Nuevo título: ").strip()
    
    if nuevo_titulo:
        elemento.titulo = nuevo_titulo
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Título actualizado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("El título no puede estar vacío.")
    
    input("Presione Enter para continuar...")

def editar_autor():
    """Edita el autor/director/artista de un elemento"""
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"Autor/Director/Artista actual: {elemento.autor_director_artista}")
    nuevo_autor = input("Nuevo autor/director/artista: ").strip()
    
    if nuevo_autor:
        elemento.autor_director_artista = nuevo_autor
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Autor/Director/Artista actualizado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("El autor/director/artista no puede estar vacío.")
    
    input("Presione Enter para continuar...")

def editar_genero():
    """Edita el género de un elemento"""
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"Género actual: {elemento.genero}")
    nuevo_genero = input("Nuevo género: ").strip()
    
    if nuevo_genero:
        elemento.genero = nuevo_genero
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Género actualizado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("El género no puede estar vacío.")
    
    input("Presione Enter para continuar...")

def editar_valoracion():
    """Edita la valoración de un elemento"""
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    id_elemento = input("Ingrese el ID del elemento a editar: ").strip()
    elemento = encontrar_elemento_por_id(id_elemento)
    
    if not elemento:
        print(f"No se encontró un elemento con ID '{id_elemento}'")
        input("Presione Enter para continuar...")
        return
    
    valoracion_actual = f"{elemento.valoracion}/10" if elemento.valoracion else "Sin valorar"
    print(f"Valoración actual: {valoracion_actual}")
    print("Nueva valoración (1-10, Enter para quitar valoración): ", end="")
    valoracion_input = input()
    
    if not valoracion_input.strip():
        elemento.valoracion = None
        print("✅ Valoración eliminada.")
    else:
        from utils.validata import validar_valoracion
        nueva_valoracion = validar_valoracion(valoracion_input)
        if nueva_valoracion is not False:
            elemento.valoracion = nueva_valoracion
            print("✅ Valoración actualizada exitosamente.")
        else:
            input("Presione Enter para continuar...")
            return
    
    if gestorArchivos.guardar_coleccion(coleccion):
        print("✅ Cambios guardados exitosamente.")
    else:
        print("❌ Error al guardar los cambios.")
    
    input("Presione Enter para continuar...")

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
        print(f"No se encontraron elementos con el título '{titulo_eliminar}'")
        input("Presione Enter para continuar...")
        return
    
    if len(elementos_encontrados) == 1:
        elemento = elementos_encontrados[0]
        print(f"Elemento encontrado:")
        print(f"Título: {elemento.titulo}")
        print(f"Tipo: {elemento.tipo}")
        print(f"Autor/Director/Artista: {elemento.autor_director_artista}")
        
        confirmacion = input("¿Está seguro de que desea eliminar este elemento? (s/N): ").strip().lower()
        if confirmacion == 's':
            coleccion.remove(elemento)
            if gestorArchivos.guardar_coleccion(coleccion):
                print("✅ Elemento eliminado exitosamente.")
            else:
                print("❌ Error al guardar los cambios.")
        else:
            print("Operación cancelada.")
    else:
        print(f"Se encontraron {len(elementos_encontrados)} elementos:")
        for i, elem in enumerate(elementos_encontrados, 1):
            print(f"{i}. {elem.titulo} ({elem.tipo}) - ID: {elem.id}")
        
        try:
            seleccion = int(input("Seleccione el número del elemento a eliminar (0 para cancelar): "))
            if seleccion == 0:
                print("Operación cancelada.")
                input("Presione Enter para continuar...")
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
                    print("Operación cancelada.")
            else:
                print("Selección inválida.")
        except ValueError:
            print("Debe ingresar un número válido.")
    
    input("Presione Enter para continuar...")

def eliminar_por_id():
    """Elimina un elemento por ID"""
    if not coleccion:
        print("La colección está vacía.")
        input("Presione Enter para continuar...")
        return
    
    id_eliminar = input("Ingrese el ID del elemento a eliminar: ").strip()
    elemento = encontrar_elemento_por_id(id_eliminar)
    
    if not elemento:
        print(f"No se encontró un elemento con ID '{id_eliminar}'")
        input("Presione Enter para continuar...")
        return
    
    print(f"Elemento encontrado:")
    print(f"ID: {elemento.id}")
    print(f"Título: {elemento.titulo}")
    print(f"Tipo: {elemento.tipo}")
    print(f"Autor/Director/Artista: {elemento.autor_director_artista}")
    
    confirmacion = input("¿Está seguro de que desea eliminar este elemento? (s/N): ").strip().lower()
    if confirmacion == 's':
        coleccion.remove(elemento)
        if gestorArchivos.guardar_coleccion(coleccion):
            print("✅ Elemento eliminado exitosamente.")
        else:
            print("❌ Error al guardar los cambios.")
    else:
        print("Operación cancelada.")
    
    input("Presione Enter para continuar...")

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
    if gestorArchivos.guardar_coleccion(coleccion):
        print(f"✅ Colección guardada exitosamente en '{gestorArchivos.archivo}'")
        print(f"📊 Total de elementos guardados: {len(coleccion)}")
    else:
        print("❌ Error al guardar la colección")
    
    input("Presione Enter para continuar...")

def cargar_coleccion_manual():
    """Carga manualmente una colección"""
    global coleccion
    
    archivo_personalizado = input(f"Ingrese el nombre del archivo (Enter para usar '{gestorArchivos.archivo}'): ").strip()
    
    if archivo_personalizado:
        gestor_temp = GestorArchivos(archivo_personalizado)
        coleccion_temp = gestor_temp.cargar_coleccion()
    else:
        coleccion_temp = gestorArchivos.cargar_coleccion()
    
    if coleccion_temp or coleccion_temp == []:  # Incluir lista vacía como válida
        confirmacion = input(f"¿Desea reemplazar la colección actual? Esto eliminará {len(coleccion)} elementos actuales (s/N): ").strip().lower()
        
        if confirmacion == 's':
            coleccion = coleccion_temp
            if archivo_personalizado:
                gestorArchivos.archivo = archivo_personalizado
            print(f"✅ Colección cargada exitosamente")
            print(f"📊 Total de elementos cargados: {len(coleccion)}")
        else:
            print("Operación cancelada.")
    else:
        print("No se pudo cargar la colección o el archivo no existe.")
    
    input("Presione Enter para continuar...")

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

# app.py - Versión actualizada
from utils.screenControllers import limpiar_pantalla
import controllers.mainmenu as mainmenu

if __name__ == '__main__':
    # Inicializar la colección al comenzar
    mainmenu.inicializar_coleccion()
    
    menuPrincipal = [
        "Añadir Nuevo Elemento",
        "Ver Todos los Elementos", 
        "Buscar Elemento",
        "Editar Elemento",
        "Eliminar Elemento",
        "Ver Elementos por Categoría",
        "Guardar y Cargar Colección",
        "Salir"
    ]

    while True:
        limpiar_pantalla()
        print('==================================')
        print('    Administrador de Colección    ')
        print('==================================')
        for a, item in enumerate(menuPrincipal, start=1):
            print(f'{a}. {item}')
        print('==================================')
        print(f'📚 Elementos en colección: {len(mainmenu.coleccion)}')
        print('==================================')
        
        try:
            opcion = int(input("Ingrese una opción: "))
            limpiar_pantalla()
            
            if opcion < 1 or opcion > len(menuPrincipal):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {menuPrincipal[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    mainmenu.menuNuevoElemento()
                case 2:
                    mainmenu.ListarElementos()
                case 3:
                    mainmenu.menuBuscarElemento()
                case 4:
                    mainmenu.menuEditarElemento()
                case 5:
                    mainmenu.menuEliminarElemento()
                case 6:
                    mainmenu.menuVerCategoria()
                case 7:
                    mainmenu.menuGuardarCargar()
                case 8:
                    # Guardar automáticamente al salir
                    mainmenu.gestorArchivos.guardar_coleccion(mainmenu.coleccion)
                    limpiar_pantalla()
                    print("=" * 70)
                    print("Gracias por usar Administrador de Colección de Libros/Películas/Música.")
                    print("Su colección ha sido guardada automáticamente.")
                    print("=" * 70)
                    break
                    
        except ValueError:
            limpiar_pantalla()
            print("Debe ingresar un número válido.")
            input("Presione Enter para continuar...")
