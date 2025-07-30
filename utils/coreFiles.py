import json
import os

# ✅ Cargar datos desde un archivo JSON
def cargarJson(ruta):
    if not os.path.exists(ruta):
        return [] 
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        print(f"⚠ Archivo {ruta} corrupto o vacío. Se reiniciará.")
        return []  
    
def guardarJson(ruta, datos):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)  # Crear carpeta si no existe
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
