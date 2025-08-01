import re
from config import VALORACION_MIN, VALORACION_MAX

def validarSoloLetras(mensaje, permitirVacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitirVacio and valor == "":
            return ""
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", valor):
            return valor
        print("Entrada inválida. Solo se permiten letras y espacios.")

def validarValoracion(permitirVacio=False):
    while True:
        valor = input(f"Ingrese la valoración ({VALORACION_MIN}-{VALORACION_MAX}): ").strip()
        
        if permitirVacio and valor == "":
            return None
        if valor == "":
            print(f"La valoración es obligatoria. Ingrese un número entre {VALORACION_MIN} y {VALORACION_MAX}.")
            continue

        try:
            valor_float = float(valor)
            if VALORACION_MIN <= valor_float <= VALORACION_MAX:
                return valor_float
            else:
                print(f"La valoración debe ser un número entre {VALORACION_MIN} y {VALORACION_MAX}.")
        except ValueError:
            print(f"La valoración debe ser un número entre {VALORACION_MIN} y {VALORACION_MAX}.")

def generarId(lista):
    if not lista:
        return "00001"
    ultimo_id = max(int(item["id"]) for item in lista)
    return str(ultimo_id + 1).zfill(5)