
# models/elemento.py
from datetime import datetime
import uuid

class Elemento:
    def __init__(self, titulo, autor_director_artista, genero, valoracion=None, tipo=""):
        self.id = str(uuid.uuid4())[:8]  # ID único corto
        self.titulo = titulo
        self.autor_director_artista = autor_director_artista
        self.genero = genero
        self.valoracion = valoracion
        self.tipo = tipo  # libro, película, música
        self.fecha_agregado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor_director_artista': self.autor_director_artista,
            'genero': self.genero,
            'valoracion': self.valoracion,
            'tipo': self.tipo,
            'fecha_agregado': self.fecha_agregado
        }
    
    @classmethod
    def from_dict(cls, data):
        elemento = cls(
            data['titulo'],
            data['autor_director_artista'],
            data['genero'],
            data.get('valoracion'),
            data['tipo']
        )
        elemento.id = data['id']
        elemento.fecha_agregado = data.get('fecha_agregado', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return elemento