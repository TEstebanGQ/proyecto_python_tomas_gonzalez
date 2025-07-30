def validar_valoracion(valoracion_str):
    """Valida que la valoración esté entre 1 y 10"""
    if not valoracion_str.strip():
        return None
    
    try:
        valoracion = float(valoracion_str)
        if 1 <= valoracion <= 10:
            return valoracion
        else:
            print("La valoración debe estar entre 1 y 10")
            return False
    except ValueError:
        print("La valoración debe ser un número")
        return False

def validar_texto_no_vacio(texto, campo):
    """Valida que el texto no esté vacío"""
    if not texto.strip():
        print(f"El {campo} no puede estar vacío.")
        return False
    return True

def obtener_entrada_valida(prompt, validador=None):
    """Obtiene entrada válida del usuario"""
    while True:
        entrada = input(prompt)
        if validador:
            resultado = validador(entrada)
            if resultado is not False:
                return resultado
        else:
            if entrada.strip():
                return entrada.strip()
            else:
                print("La entrada no puede estar vacía.")