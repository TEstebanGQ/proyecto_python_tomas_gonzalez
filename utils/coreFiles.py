import json
import os

def cargarJson(ruta):
    # Verifico si el archivo existe antes de intentar leerlo
    if not os.path.exists(ruta):
        # simplemente el archivo aún no se ha creado
        return [] 
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)  # Cargo y retorno el contenido JSON
            
    except (json.JSONDecodeError, FileNotFoundError):
        # Si el archivo está corrupto o hay problemas de acceso
        print(f" Archivo {ruta} corrupto o vacío. Se reiniciará.")
        return []  # Retorno lista vacía para permitir que el sistema continúe
    
def guardarJson(ruta, datos):
    # Me aseguro de que el directorio padre exista
    os.makedirs(os.path.dirname(ruta), exist_ok=True)  

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        