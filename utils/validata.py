import re

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

def validar_solo_letras(campo: str, nombre_campo: str) -> str:
    """
    Valida que la entrada solo contenga letras y espacios.
    Retorna la cadena válida.
    """
    while True:
        valor = input(f"{nombre_campo}: ").strip()
        if valor != "" and re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", valor):
            return valor
        print(f"❌ {nombre_campo} solo puede contener letras y espacios.")

def validar_valoracion() -> float:
    while True:
        try:
            valor = input("Valoración (1-10): ").strip()
            if valor != "":
                valor = float(valor)
                if 1 <= valor <= 10:
                    return valor
                else:
                    print("❌ La valoración debe estar entre 1 y 10.")
            else:
                print("❌ La valoración no puede estar vacía.")
        except ValueError:
            print("❌ La valoración debe ser un número válido.")