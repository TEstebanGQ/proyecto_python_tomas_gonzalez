from models.elemento import Elemento
from utils.validata import obtener_entrada_valida, validar_valoracion, validar_texto_no_vacio

def crear_musica(coleccion, gestor_archivos):
    """Crea una nueva entrada de música"""
    print("=== AÑADIR NUEVA MÚSICA ===")
    
    titulo = obtener_entrada_valida("Título del álbum/canción: ", 
                                  lambda x: x if validar_texto_no_vacio(x, "título") else None)
    
    artista = obtener_entrada_valida("Artista: ", 
                                   lambda x: x if validar_texto_no_vacio(x, "artista") else None)
    
    genero = obtener_entrada_valida("Género: ", 
                                  lambda x: x if validar_texto_no_vacio(x, "género") else None)
    
    print("Valoración (1-10, opcional - presiona Enter para omitir): ", end="")
    valoracion_input = input()
    valoracion = validar_valoracion(valoracion_input) if valoracion_input else None
    
    musica = Elemento(titulo, artista, genero, valoracion, "música")
    coleccion.append(musica)
    
    if gestor_archivos.guardar_coleccion(coleccion):
        print(f"✅ Música '{titulo}' agregada exitosamente con ID: {musica.id}")
    else:
        print("❌ Error al guardar la música")
    
    input("Presione Enter para continuar...")

def listar_musica(coleccion):
    """Lista toda la música"""
    musica = [elem for elem in coleccion if elem.tipo == "música"]
    
    if not musica:
        print("No hay música en la colección.")
        input("Presione Enter para continuar...")
        return
    
    print("=== MÚSICA EN LA COLECCIÓN ===")
    print("-" * 80)
    
    for item in musica:
        valoracion_str = f"{item.valoracion}/10" if item.valoracion else "Sin valorar"
        print(f"ID: {item.id}")
        print(f"Título: {item.titulo}")
        print(f"Artista: {item.autor_director_artista}")
        print(f"Género: {item.genero}")
        print(f"Valoración: {valoracion_str}")
        print(f"Agregado: {item.fecha_agregado}")
        print("-" * 80)
    
    input("Presione Enter para continuar...")