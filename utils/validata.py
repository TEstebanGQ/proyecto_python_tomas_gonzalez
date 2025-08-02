import re
from config import VALORACION_MIN, VALORACION_MAX
from utils.screenControllers import limpiarPantalla

def manejarInterrupcion():
    limpiarPantalla()
    print("===================================")
    print("    Operación cancelada           ")
    print("    Regresando al menú anterior... ")
    print("===================================")
    return True

def validarSoloLetras(mensaje, permitirVacio=False):
    while True:
        try:
            # Solicito la entrada y limpio espacios extras
            valor = input(mensaje).strip()
            
            # Si permito vacío y no ingresó nada, acepto
            if permitirVacio and valor == "":
                return ""
            
            # Mi patrón de validación: solo letras (incluye acentos y ñ) y espacios
            if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", valor):
                return valor
            
            # Explico claramente qué acepto
            print("Entrada inválida. Solo se permiten letras y espacios.")
            
        except (KeyboardInterrupt, EOFError):
            # Manejo interrupciones elegantemente - nunca muestro errores técnicos
            if manejarInterrupcion():
                return None  # Señalo que el usuario canceló
        except Exception:
            # Capturo cualquier error inesperado
            limpiarPantalla()
            print("Error inesperado. Regresando al menú anterior...")
            return None

def validarValoracion(permitirVacio=False):
    while True:
        try:
            # Muestro claramente el rango que acepto
            valor = input(f"Ingrese la valoración ({VALORACION_MIN}-{VALORACION_MAX}): ").strip()
            
            # Si permito vacío y no ingresó nada, retorno None para señalar "sin cambios"
            if permitirVacio and valor == "":
                return None
                
            # No acepto entradas vacías cuando la valoración es obligatoria
            if valor == "":
                print(f"La valoración es obligatoria. Ingrese un número entre {VALORACION_MIN} y {VALORACION_MAX}.")
                continue
            try:
                # Intento convertir a número decimal
                valor_float = float(valor)
                
                # Valido que esté en mi rango permitido
                if VALORACION_MIN <= valor_float <= VALORACION_MAX:
                    return valor_float  
                else:
                    print(f"La valoración debe ser un número entre {VALORACION_MIN} y {VALORACION_MAX}.")
            except ValueError:
                # El usuario ingresó algo que no es un número
                print(f"La valoración debe ser un número entre {VALORACION_MIN} y {VALORACION_MAX}.")
                
        except (KeyboardInterrupt, EOFError):
            # Manejo interrupciones sin mostrar errores técnicos
            if manejarInterrupcion():
                return None  
        except Exception:
            limpiarPantalla()
            print("Error inesperado. Regresando al menú anterior...")
            return None

def generarId(lista):
    # Si la lista está vacía, empiezo desde el principio
    if not lista:
        return "00001"
    
    # Busco el ID más alto existente y le sumo 1
    ultimo_id = max(int(item["id"]) for item in lista)
    nuevo_id = ultimo_id + 1
    
    # Formato con 5 dígitos 
    return str(nuevo_id).zfill(5)