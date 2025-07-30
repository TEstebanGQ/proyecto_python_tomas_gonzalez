
import uuid

class Elemento:
    def __init__(self, titulo, autor_director_artista, genero, valoracion=None, tipo=""):
        self.id = str(uuid.uuid4())[:8]  # ID único corto
        self.titulo = titulo
        self.autor_director_artista = autor_director_artista
        self.genero = genero
        self.valoracion = valoracion
        self.tipo = tipo  # libro, película, música
        
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor_director_artista': self.autor_director_artista,
            'genero': self.genero,
            'valoracion': self.valoracion,
            'tipo': self.tipo,
            
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
        return elemento
