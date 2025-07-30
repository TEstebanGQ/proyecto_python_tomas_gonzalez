from utils.screenControllers import limpiar_pantalla
import controllers.mainmenu as mainmenu
if __name__ == '__main__':

 
    menuPrincipal = [

        "Añadir Nuevo Elemento",
        "Ver Todos los Elementos",
        "Buscar Elemento",
        "Editar Elemento",
        "Eliminar Elemento",
        "Ver Elementos por Categoría",
        "Guadar y cargar Colección",
        "Salir"
    ]


    while True:
        limpiar_pantalla()
        print('==================================')
        print('    Administrador de Colección    ')   
        print('==================================')
        for a, item in enumerate(menuPrincipal, start=1):
                print(f'{a}, {item}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción: "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(menuPrincipal):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {menuPrincipal[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    mainmenu.menuNuevoElemento()
                case 2:
                    mainmenu.ListarElementos()
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
                    limpiar_pantalla()
                    print("=" * 70)
                    print("Gracias por usar Administrador de Colección de Libros/Películas/Música.")
                    print("=" * 70)
                    break
        except ValueError:
            limpiar_pantalla()
            print("Debe ingresar un número válido.")
            input("Presione Enter para continuar...")