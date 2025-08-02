import os
import sys

def pausarPantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        input('Presiona Enter para continuar .....')
    else:
        os.system('pause')
        
def limpiarPantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system('clear')
    else:
        os.system('cls')


