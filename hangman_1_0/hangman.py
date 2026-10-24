import os
import random

# =================================EXTRACCION DE PALABRAS Y MONIGOTES=================================

# Obtiene la carpeta exacta donde está guardada la instancia del juego, para poder acceder a los archivos de palabras y monigote.
hangman_1_0 = os.path.dirname(__file__)

PALABRAS = os.path.join(hangman_1_0, "palabras.txt")
MONIGOTE = os.path.join(hangman_1_0, "monigote.txt")

def cargar_palabras():
    try:
        with open(PALABRAS, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except:
        return []

def cargar_monigote():
    try:
        with open(MONIGOTE, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except:
        return []

lineas = cargar_palabras()
monigote = cargar_monigote()
#===================================================================================================

# ==================SE ESCOGE UNA PALABRA RANDOM=======================
def palabra_random():
    palabra = random.choice(lineas)

    return palabra.strip()
#======================================================================

# ==================SE INGRESA UNA LETRA POR TECLADO=======================
def ingreso_letra():
    letra = input("Escribe una letra: ")
    return letra.upper()
#==========================================================================


# =========================================VALIDACIONES==============================================
def una_letre():
    n = True
    while n:
        letra = ingreso_letra()
        if len(letra) == 1:
            n = False
            return letra
        elif len(letra) == 0:
            print("No puedes entregar el caracter vacio")
        else:
            print("solo es permitido un caracter por intento")
    return letra



una_letre()







#print("Primera palabra de la lista: ", lineas[0].strip())

'''
segmentos = "".join(monigote).split("=" * 35)

numero_segmento = 5  # Empieza en 0: el primer dibujo
print(segmentos[numero_segmento].strip("\r\n"))

'''
