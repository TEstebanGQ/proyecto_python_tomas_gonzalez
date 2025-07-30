import json
import os
from models.elemento import Elemento

class GestorArchivos:
    def __init__(self, archivo='coleccion.json'):
        self.archivo = archivo
    
    def cargar_coleccion(self):
        """Carga la colección desde el archivo JSON"""
        if not os.path.exists(self.archivo):
            return []
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                return [Elemento.from_dict(item) for item in datos]
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def guardar_coleccion(self, coleccion):
        """Guarda la colección en el archivo JSON"""
        try:
            datos = [elemento.to_dict() for elemento in coleccion]
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False