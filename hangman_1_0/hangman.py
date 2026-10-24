import os
import random

# =================================EXTRACCION DE PALABRAS Y MONIGOTES=================================

'''
Obtiene la carpeta exacta donde está guardada la instancia del juego, 
para poder acceder a los archivos de palabras y monigote.
''' 
hangman_1_0 = os.path.dirname(__file__)

PALABRAS = os.path.join(hangman_1_0, "palabras.txt")
MONIGOTE = os.path.join(hangman_1_0, "monigote.txt")

def cargar_palabras():
    try:
        with open(PALABRAS, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return []

def cargar_monigote():
    try:
        with open(MONIGOTE, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
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
def validaciones(letras_usadas):
    n = True
    while n:
        letra = ingreso_letra()
        if letra in letras_usadas:
            print("la letra ya ah sido usada")
        elif len(letra) == 1 and 'A' <= letra <= 'Z':
            n = False
        elif len(letra) == 0:
            print("No puedes entregar el caracter vacio")
        elif len(letra) > 1:
            print("solo es permitido un caracter por intento")
        else:
            print("El caracter debe estar entre [A-Z]")
    return letra



#bloque de codigo de prueba de funcionamiento
letras_usadas = []
for g in range(5):
    letra = validaciones(letras_usadas)
    letras_usadas.append(letra)
    print(letra)
print(letras_usadas)
#===========================================







#print("Primera palabra de la lista: ", lineas[0].strip())

'''
segmentos = "".join(monigote).split("=" * 35)

numero_segmento = 5  # Empieza en 0: el primer dibujo
print(segmentos[numero_segmento].strip("\r\n"))

'''
