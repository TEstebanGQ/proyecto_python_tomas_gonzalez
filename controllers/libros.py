from models.elemento import Elemento
from utils.validata import obtener_entrada_valida, validar_valoracion, validar_texto_no_vacio
from utils.screenControllers import limpiar_pantalla

def crear_libro(coleccion, gestor_archivos):
    """Crea un nuevo libro"""
    print("=== AÑADIR NUEVO LIBRO ===")
    
    titulo = obtener_entrada_valida("Título del libro: ", 
                                  lambda x: x if validar_texto_no_vacio(x, "título") else None)
    
    autor = obtener_entrada_valida("Autor: ", 
                                 lambda x: x if validar_texto_no_vacio(x, "autor") else None)
    
    genero = obtener_entrada_valida("Género: ", 
                                  lambda x: x if validar_texto_no_vacio(x, "género") else None)
    
    print("Valoración (1-10, opcional - presiona Enter para omitir): ", end="")
    valoracion_input = input()
    valoracion = validar_valoracion(valoracion_input) if valoracion_input else None
    
    libro = Elemento(titulo, autor, genero, valoracion, "libro")
    coleccion.append(libro)
    
    if gestor_archivos.guardar_coleccion(coleccion):
        print(f"✅ Libro '{titulo}' agregado exitosamente con ID: {libro.id}")
    else:
        print("❌ Error al guardar el libro")
    
    input("Presione Enter para continuar...")

def listar_libros(coleccion):
    """Lista todos los libros"""
    libros = [elem for elem in coleccion if elem.tipo == "libro"]
    
    if not libros:
        print("No hay libros en la colección.")
        input("Presione Enter para continuar...")
        return
    
    print("=== LIBROS EN LA COLECCIÓN ===")
    print("-" * 80)
    
    for libro in libros:
        valoracion_str = f"{libro.valoracion}/10" if libro.valoracion else "Sin valorar"
        print(f"ID: {libro.id}")
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor_director_artista}")
        print(f"Género: {libro.genero}")
        print(f"Valoración: {valoracion_str}")
        print(f"Agregado: {libro.fecha_agregado}")
        print("-" * 80)
    
    input("Presione Enter para continuar...")