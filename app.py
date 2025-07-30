from utils.screenControllers import limpiarPantalla
import controllers.mainmenu as mainmenu
from config import TITULO_APP

def ejecutarAplicacion():
    menuPrincipal = [
        "Añadir un Nuevo Elemento",
        "Ver Todos los Elementos",
        "Buscar un Elemento",
        "Editar un Elemento",
        "Eliminar un Elemento",
        "Ver elementos por categoria",
        "Guardar y Cargar Colección",
        "Salir"
    ]

    while True:
        limpiarPantalla()
        print("===================================")
        print(f"     {TITULO_APP}        ")
        print("===================================")
        for i, item in enumerate(menuPrincipal, start=1):
            print(f"{i}. {item}")
        print("===================================")

        try:
            opcion = int(input("Selecciona una opción (1-8): "))
            limpiarPantalla()

            if opcion < 1 or opcion > len(menuPrincipal):
                print("Opción fuera de rango.")
                input("Presiona Enter para continuar...")
                continue

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
                    print(" Gracias por usar la aplicación.  ")
                    print("===================================")
                    break
        except ValueError:
            print("Debes ingresar un número válido.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    ejecutarAplicacion()
