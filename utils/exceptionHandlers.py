from utils.screenControllers import limpiarPantalla

def manejarInterrupcion():
    limpiarPantalla()
    print("===================================")
    print("    Operación cancelada           ")
    print("    Regresando al menú anterior... ")
    print("===================================")
    return True

def inputSeguro(mensaje, permitirVacio=False):
    try:
        valor = input(mensaje).strip()
        return valor
    except (KeyboardInterrupt, EOFError):
        # Usuario presionó Ctrl+C o Ctrl+D 
        if manejarInterrupcion():
            return None
    except Exception as e:
        # Cualquier otro error inesperado 
        limpiarPantalla()
        print("===================================")
        print("    Error inesperado               ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return None

def ejecutarConManejo(funcion, *args, **kwargs):

    try:
        return funcion(*args, **kwargs)
    except (KeyboardInterrupt, EOFError):
        # Usuario interrumpió 
        return manejarInterrupcion()
    except Exception as e:
        # Error inesperado - informo al usuario sin detalles técnicos
        limpiarPantalla()
        print("===================================")
        print("    Error inesperado               ")
        print("    Regresando al menú anterior... ")
        print("===================================")
        return False
