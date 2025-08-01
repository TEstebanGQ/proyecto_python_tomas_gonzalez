### 📋 Menú Principal (`mainMenu()`)

Desde aquí puedes:

1. **📚 Libros** – Ir al submenú de libros.
2. **🎬 Películas** – Ir al submenú de películas.
3. **🎵 Música** – Ir al submenú de música.
4. **💾 Guardar colección** – Guarda todos los elementos actuales (libros, películas y música) como una colección completa en `colecciones.json`.
5. **📂 Cargar colección** – Muestra una lista de colecciones guardadas para cargar una de ellas. Reemplaza los datos actuales.
6. **🚪 Salir** – Cierra el programa.

------

### 📚 Submenú Libros (`menuLibros()`)

Este menú permite gestionar los libros:

1. **➕ Agregar libro** – Pide al usuario los datos de un nuevo libro (nombre, autor, género, etc.) y lo guarda en `libros.json`.
2. **📋 Mostrar libros** – Muestra en pantalla todos los libros que se han guardado.
3. **⬅ Volver** – Retorna al menú principal.

------

### 🎬 Submenú Películas (`menuPeliculas()`)

Este menú es igual al de libros, pero enfocado en películas:

1. **➕ Agregar película** – Pide al usuario nombre, director, género, año, etc.
2. **📋 Mostrar películas** – Muestra todas las películas registradas en el sistema.
3. **⬅ Volver** – Regresa al menú principal.

------

### 🎵 Submenú Música (`menuMusica()`)

También similar al anterior, para gestionar canciones o álbumes musicales:

1. **➕ Agregar música** – Solicita título, artista, género, duración, etc.
2. **📋 Mostrar música** – Lista todas las canciones o registros musicales.
3. **⬅ Volver** – Vuelve al menú principal.

------

### 💾 Submenú Guardar Colección (`guardarColeccion()`)

- Este menú guarda todos los elementos actuales (libros, películas y música) en un archivo llamado `colecciones.json`.
- Se solicita un **nombre para la colección**, por ejemplo: "Favoritos2025".
- Guarda la colección completa con ese nombre.

------

### 📂 Submenú Cargar Colección (`cargarColeccion()`)

- Muestra todas las colecciones guardadas en `colecciones.json` (cada una con un número).
- El usuario elige una colección por **número**.
- Carga los datos de esa colección y sobrescribe los archivos individuales (`libros.json`, `peliculas.json`, `musica.json`) con esa información.

------

### 🔐 Validaciones

- El sistema valida que los nombres no estén vacíos, que los números sean correctos y que no se repitan entradas innecesariamente.
- Si introduces algo incorrecto, te vuelve a pedir el dato.
