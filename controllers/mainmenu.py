from utils.screenControllers import limpiar_pantalla
nuevoElemento = [
    'libro',
    'película',
    'musica',
    'Regresar al menú principal'
]

def menuNuevoElemento():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('       Añador nuevo elemento      ')
        print('==================================')
        for a, itrm in enumerate(nuevoElemento, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-4): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(nuevoElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {nuevoElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

TodosElementos = [
    'Ver todos los libros',
    'Ver Todas las películas',
    'Ver toda la música',
    'Regresar al menú principal'
]

def ListarElementos():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('    Ver todos los elemento      ')
        print('==================================')
        for a, itrm in enumerate(TodosElementos, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-4): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(TodosElementos):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {TodosElementos[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

BuscarElemento = [
    'Buscar por Titulo',
    'Buscar por Autor/Director/Artista',
    'Buscar por Género',
    'Regresar al menú principal'
]

def menuBuscarElemento():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Buscar elemento      ')
        print('==================================')
        for a, itrm in enumerate(BuscarElemento, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-4): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(BuscarElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {BuscarElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

EditarElemento = [
    'Editar Titulo',
    'Editar Autor/Director/Artista',
    'Editar Género',
    'Editar valoración',
    'Regresar al menú principal'
]
def menuEditarElemento():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Editar elemento      ')
        print('==================================')
        for a, itrm in enumerate(EditarElemento, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-5): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(EditarElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {EditarElemento[opcion - 1]}")
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
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
EliminarElemento = [
    'Eliminar por Titulo',
    'Eliminar por identificador unico',
    'Regresar al menú principal'
]
def menuEliminarElemento():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Eliminar elemento      ')
        print('==================================')
        for a, itrm in enumerate(EliminarElemento, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-3): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(EliminarElemento):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {EliminarElemento[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
        
VerCategoria = [
    'Ver libros ',
    'Ver películas',
    'Ver música',
    'Regresar al menú principal'
]
def menuVerCategoria():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Ver por categoría      ')
        print('==================================')
        for a, itrm in enumerate(VerCategoria, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-4): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(VerCategoria):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {VerCategoria[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")

GuardarCargar = [
    'Guardar colección Actual',
    'Cargar una colección Guardada',
    'Regresar al menú principal'
]
def menuGuardarCargar():
    while True:
        limpiar_pantalla()
        print('==================================')
        print('         Guardar y cargar      ')
        print('==================================')
        for a, itrm in enumerate(GuardarCargar, start = 1):
            print(f'{a}, {itrm}')
        print('==================================')
        try:
            opcion = int(input("Ingrese una opción(1-3): "))
            limpiar_pantalla()
            if opcion < 1 or opcion > len(GuardarCargar):
                print("Opción fuera de rango.")
                input("Presione Enter para continuar...")
                continue

            print(f"Ha seleccionado: {GuardarCargar[opcion - 1]}")
            print("-" * 60)

            match opcion:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    return  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")



