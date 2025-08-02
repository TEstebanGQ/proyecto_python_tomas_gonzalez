"""
Autor: Tomas Esteban Gonzalez Quintero
Grupo: J-3
Fecha: 01/0882025
descripcion: Aqui se implemta todo lo relacionado con el administrador de coleccion para que el sisteme
guaede, edite y elimine informacion.
"""

from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.exceptionHandlers import ejecutarConManejo
import controllers.mainmenu as mainmenu

def menu():
    menuPrincipal = [
        "Añadir Nuevo Elemento",          # Permito agregar libros, películas, música
        "Ver Todos los Elementos",        # Muestro todo el contenido por categorías
        "Buscar Elemento",                # Busco por título, autor/director/artista, género
        "Editar Elemento",                # Modifico información existente
        "Eliminar Elemento",              # Remuevo elementos del sistema
        "Ver Elementos por Categoría",    # Filtro y muestro por tipo específico
        "Guardar y Cargar Colección",     # Manejo respaldos completos del sistema
        "Salir"                          # Cierro la aplicación de manera segura
    ]

    
    while True:
        # Limpio la pantalla para mantener una interfaz ordenada
        limpiarPantalla()
        print("===================================")
        print("    Administrador de Colección     ")
        print("===================================")
        
        # Enumero todas mis opciones para que el usuario sepa qué puede hacer
        for indice, item in enumerate(menuPrincipal, start=1):
            print(f"{indice}. {item}")
        print("===================================")

        try:
            # Solicito la selección del usuario - solo acepto números
            opcion = int(input("Ingrese una opción (1-8): ").strip())
            limpiarPantalla()

            # Valido que la opción esté en mi rango permitido
            if opcion < 1 or opcion > len(menuPrincipal):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            # Confirmo al usuario qué opción seleccionó
            print(f"Has seleccionado: {menuPrincipal[opcion - 1]}")
            print("-----------------------------------")

            # Mi sistema de enrutamiento - dirijo cada opción a su función correspondiente
            match opcion:
                case 1:
                    # Ejecuto con manejo de excepciones para evitar cierres inesperados
                    ejecutarConManejo(mainmenu.menuNuevoElemento)
                case 2:
                    ejecutarConManejo(mainmenu.listarElementos)
                case 3:
                    ejecutarConManejo(mainmenu.menuBuscarElemento)
                case 4:
                    ejecutarConManejo(mainmenu.menuEditarElemento)
                case 5:
                    ejecutarConManejo(mainmenu.menuEliminarElemento)
                case 6:
                    ejecutarConManejo(mainmenu.menuVerCategoria)
                case 7:
                    ejecutarConManejo(mainmenu.menuGuardarCargar)
                case 8:
                    # Salida elegante del sistema
                    limpiarPantalla()
                    print("===================================")
                    print(" Gracias por usar el sistema     ")
                    print("===================================")
                    break
                    
        except (KeyboardInterrupt, EOFError):
            # Manejo interrupciones de teclado (Ctrl+C, Ctrl+D) 
            limpiarPantalla()
            print("===================================")
            print("  ¿Desea salir del programa?      ")
            print("===================================")
            try:
                respuesta = input("Presione 's' para salir o Enter para continuar: ").strip().lower()
                if respuesta == 's':
                    limpiarPantalla()
                    print("===================================")
                    print(" Gracias por usar el sistema     ")
                    print("===================================")
                    break
            except (KeyboardInterrupt, EOFError):
                limpiarPantalla()
                print("===================================")
                print(" Saliendo del sistema...          ")
                print("===================================")
                break
        except ValueError:
            limpiarPantalla()
            print("Debe ingresar un número válido.")
            try:
                input("Presione Enter para continuar...")
            except (KeyboardInterrupt, EOFError):
                continue


if __name__ == "__main__":
    menu()