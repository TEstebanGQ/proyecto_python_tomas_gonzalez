from utils.screenControllers import limpiarPantalla
import controllers.mainmenu as mainmenu

def menu():
    menuPrincipal = [
        "Añadir Nuevo Elemento",
        "Ver Todos los Elementos",
        "Buscar Elemento",
        "Editar Elemento",
        "Eliminar Elemento",
        "Ver Elementos por Categoría",
        "Guardar y Cargar Colección",
        "Salir"
    ]

    while True:
        limpiarPantalla()
        print("===================================")
        print("    Administrador de Colección     ")
        print("===================================")
        for indice, item in enumerate(menuPrincipal, start=1):
            print(f"{indice}. {item}")
        print("===================================")

        try:
            opcion = int(input("Ingrese una opción (1-8): ").strip())
            limpiarPantalla()

            if opcion < 1 or opcion > len(menuPrincipal):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Has seleccionado: {menuPrincipal[opcion - 1]}")
            print("-----------------------------------")

            match opcion:
                case 1:
                    mainmenu.menuNuevoElemento()
                case 2:
                    mainmenu.listarElementos()
                case 3:
                    mainmenu.menuBuscarElemento()
                case 4:
                    mainmenu.menuEditarElemento()
                case 5:
                    mainmenu.menuEliminarElemento()
                case 6:
                    mainmenu.menuVerCategoria()
                case 7:
                    mainmenu.menuGuardarCargar()
                case 8:
                    limpiarPantalla()
                    print("===================================")
                    print(" Gracias . ")
                    print("===================================")
                    break
        except ValueError:
            limpiarPantalla()
            print("Debe ingresar un número válido.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()
