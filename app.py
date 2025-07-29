from utils.screenControllers import limpiar_pantalla
if __name__ == '__main__':

 
    menuPrincipal = [

        "Gestionar Equipos",
        "Gestionar Jugadores",
        "Transferencias de Jugadores",
        "Gestionar Ligas",
        "Gestionar Torneos",
        "Ver Estadísticas",
        "Gestionar Dirigentes",
        "Gestionar Partidos",
        "Salir del Sistema"
    ]


    while True:
        limpiar_pantalla()
        print('=============================')
        print('          Actividad          ')
        print('=============================')
        for a, item in enumerate(menuPrincipal, start=1):
                print(f'{a}, {item}')
        print('=============================')
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
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    limpiar_pantalla()
                    print("=" * 60)
                    print("Gracias .")
                    print("=" * 60)
                    break
        except ValueError:
            limpiar_pantalla()
            print("Debe ingresar un número válido.")
            input("Presione Enter para continuar...")