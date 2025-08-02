# Python proyecto: Administrador de Colección de libros/peliculas y musica

Este proyecto esta basado en la interfaz de python algo facil de manejar y administar, para que el usuario no tenga complicaciones a la hora de utilizar el administrador de colecion y puede agregar informacion ya sea a libros , peliculas y musica, para tener mejor claridad de su infromacion.

##  Características Principales

- **Gestión de múltiples tipos de elementos**: Libros, películas y música
- **CRUD completo**: Crear, leer, actualizar y eliminar elementos
- **Búsqueda avanzada**: Por título, autor/director/artista o género
- **Sistema de valoraciones**: Califica tus elementos del 1 al 5
- **Colecciones**: Guarda y carga conjuntos completos de elementos
- **Interfaz intuitiva**: Menús organizados y navegación sencilla Instalación

### Dependencias

```bash
pip install tabulate
```

### Configuración

1. Clona o descarga el repositorio
2. Navega al directorio del proyecto
3. Ejecuta la aplicación:

```bash
python app.py
```

## 📁 Estructura del Proyecto

```
administrador-coleccion/
│
├── app.py                     # Punto de entrada principal
├── config.py                  # Configuración y constantes
├── README.md                  # Este archivo
│
├── controllers/
│   ├── mainmenu.py           # Controladores de menús
│   └── elemento.py           # Lógica de gestión de elementos
│
├── utils/
│   ├── coreFiles.py          # Manejo de archivos JSON
│   ├── screenControllers.py  # Control de pantalla
│   └── validata.py           # Validaciones de entrada
│
└── data/
    ├── libros.json           # Almacenamiento de libros
    ├── peliculas.json        # Almacenamiento de películas
    ├── musica.json           # Almacenamiento de música
    └── colecciones.json      # Colecciones guardadas
```

## Funcionalidades

### 1. 📋 Menú Principal

- **Añadir Nuevo Elemento**: Agregar libros, películas o música
- **Ver Todos los Elementos**: Listar elementos por categoría
- **Buscar Elemento**: Búsqueda por diferentes criterios
- **Editar Elemento**: Modificar información existente
- **Eliminar Elemento**: Remover elementos por ID o título
- **Ver Elementos por Categoría**: Filtrado avanzado
- **Guardar y Cargar Colección**: Gestión de colecciones
- **Salir**: Cierre seguro de la aplicación

### 2. 📚 Gestión de Libros

- **Campos**: Título, Autor, Género, Valoración
- **Funciones**: Agregar, listar, buscar, editar, eliminar

### 3. 🎬 Gestión de Películas

- **Campos**: Título, Director, Género, Valoración
- **Funciones**: Agregar, listar, buscar, editar, eliminar

### 4. 🎵 Gestión de Música

- **Campos**: Título, Artista, Género, Valoración
- **Funciones**: Agregar, listar, buscar, editar, eliminar

### 5. 🔍 Sistema de Búsqueda

- **Por Título**: Búsqueda parcial en títulos
- **Por Persona**: Búsqueda por autor, director o artista
- **Por Género**: Filtrado por categoría

### 6. ✏️ Edición de Elementos

- **Edición selectiva**: Modifica campos específicos
- **Validación**: Mantiene la integridad de los datos
- **Confirmación**: Proceso seguro de actualización

### 7. 🗑️ Eliminación de Elementos

- **Por ID**: Eliminación precisa usando identificador único
- **Por Título**: Eliminación con búsqueda por nombre
- **Confirmación**: Proceso seguro con confirmación del usuario

### 8. 💾 Sistema de Colecciones

- **Guardar Colección**: Crea una instantánea completa de todos los elementos
- **Cargar Colección**: Restaura una colección previamente guardada
- **Listar Colecciones**: Ve todas las colecciones disponibles
- **Sobrescritura**: Gestiona colecciones duplicadas

## 🛡️ Validaciones

- **Solo letras y espacios**: Para nombres, títulos, géneros, etc.
- **Valoraciones numéricas**: Entre 1 y 5 (acepta decimales)
- **Campos obligatorios**: Previene entradas vacías
- **IDs únicos**: Generación automática de identificadores
- **Archivos seguros**: Manejo robusto de archivos JSON

## 📊 Visualización de Datos

El sistema utiliza la librería `tabulate` para mostrar los datos en formato de tabla con:

- Encabezados claros
- Formato de rejilla 
- Información organizada por columnas
- ID únicos para cada elemento

### Estructura de Datos

```json
{
    "titulo": "Ejemplo",
    "autor/director/artista": "Creador",
    "genero": "Categoría",
    "valoracion": 4.5,
    "id": "00001"
}
```

## 🎨 Interfaz de Usuario

- **Mensajes informativos**: Confirmaciones y estados claros
- **Multiplataforma**: Compatible con Windows, Linux y macOS

## 👨‍💻 Autor

Nombre: Tomas Esteban Gonzalez Quintero

Grupo: J-3
