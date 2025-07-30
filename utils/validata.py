import re

# ✅ Validar que solo contenga letras y espacios
def validarSoloLetras(mensaje, permitirVacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitirVacio and valor == "":
            return ""  # Retorna vacío si se permite omitir

        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", valor):
            return valor
        print("❌ Entrada inválida. Solo se permiten letras y espacios.")

# ✅ Validar que solo contenga números
def validarSoloNumeros(mensaje, permitirVacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitirVacio and valor == "":
            return ""  
        if valor.isdigit():
            return valor
        print("❌ Entrada inválida. Solo se permiten números.")

# ✅ Validar valoración (obligatoria u opcional según parámetro)
def validarValoracion(permitirVacio=False):
    while True:
        valor = input("Ingrese la valoración (1-10): ").strip()

        # Si se permite vacío (solo en edición)
        if permitirVacio and valor == "":
            return None  

        # Si no se permite vacío (en agregar), forzar ingreso
        if valor == "":
            print("❌ La valoración es obligatoria. Ingrese un número entre 1 y 10.")
            continue

        if valor.replace('.', '', 1).isdigit():  
            valor = float(valor)
            if 1 <= valor <= 10:
                return valor
        print("❌ La valoración debe ser un número entre 1 y 10.")

# ✅ Generar IDs automáticos de 5 dígitos
def generarId(lista):
    if not lista:
        return "00001"  # Primer ID
    else:
        ultimoId = max(int(item["id"]) for item in lista)
        nuevoId = str(ultimoId + 1).zfill(5)  # Rellenar con ceros
        return nuevoId
