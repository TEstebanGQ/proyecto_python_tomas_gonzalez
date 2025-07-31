import re


def validarSoloLetras(mensaje, permitirVacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitirVacio and valor == "":
            return ""  

        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", valor):
            return valor
        print("Entrada inválida. Solo se permiten letras y espacios.")


def validarSoloNumeros(mensaje, permitirVacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitirVacio and valor == "":
            return ""  
        if valor.isdigit():
            return valor
        print("Entrada inválida. Solo se permiten números.")


def validarValoracion(permitirVacio=False):
    while True:
        valor = input("Ingrese la valoración (1-5): ").strip()


        if permitirVacio and valor == "":
            return None  
        if valor == "":
            print("La valoración es obligatoria. Ingrese un número entre 1 y 5.")
            continue

        if valor.replace('.', '', 1).isdigit():  
            valor = float(valor)
            if 1 <= valor <= 5:
                return valor
        print(" La valoración debe ser un número entre 1 y 5.")

def generarId(lista):
    if not lista:
        return "00001"  
    else:
        ultimoId = max(int(item["id"]) for item in lista)
        nuevoId = str(ultimoId + 1).zfill(5)  
        return nuevoId
