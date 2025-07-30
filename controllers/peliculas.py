from models.elemento import Elemento
from utils.validata import obtener_entrada_valida, validar_valoracion, validar_texto_no_vacio

def crear_pelicula(coleccion, gestor_archivos):
    """Crea una nueva película"""
    print("=== AÑADIR NUEVA PELÍCULA ===")
    
    titulo = obtener_entrada_valida("Título de la película: ", 
                                  lambda x: x if validar_texto_no_vacio(x, "título") else None)
    
    director = obtener_entrada_valida("Director: ", 
                                    lambda x: x if validar_texto_no_vacio(x, "director") else None)
    
    genero = obtener_entrada_valida("Género: ", 
                                  lambda x: x if validar_texto_no_vacio(x, "género") else None)
    
    print("Valoración (1-10, opcional - presiona Enter para omitir): ", end="")
    valoracion_input = input()
    valoracion = validar_valoracion(valoracion_input) if valoracion_input else None
    
    pelicula = Elemento(titulo, director, genero, valoracion, "película")
    coleccion.append(pelicula)
    
    if gestor_archivos.guardar_coleccion(coleccion):
        print(f"✅ Película '{titulo}' agregada exitosamente con ID: {pelicula.id}")
    else:
        print("❌ Error al guardar la película")
    
    input("Presione Enter para continuar...")

def listar_peliculas(coleccion):
    """Lista todas las películas"""
    peliculas = [elem for elem in coleccion if elem.tipo == "película"]
    
    if not peliculas:
        print("No hay películas en la colección.")
        input("Presione Enter para continuar...")
        return
    
    print("=== PELÍCULAS EN LA COLECCIÓN ===")
    print("-" * 80)
    
    for pelicula in peliculas:
        valoracion_str = f"{pelicula.valoracion}/10" if pelicula.valoracion else "Sin valorar"
        print(f"ID: {pelicula.id}")
        print(f"Título: {pelicula.titulo}")
        print(f"Director: {pelicula.autor_director_artista}")
        print(f"Género: {pelicula.genero}")
        print(f"Valoración: {valoracion_str}")
        print(f"Agregado: {pelicula.fecha_agregado}")
        print("-" * 80)
    
    input("Presione Enter para continuar...")