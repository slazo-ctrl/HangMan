
import os

# Obtiene la carpeta exacta donde está guardado este script actual
hangman_1_0 = os.path.dirname(__file__)

# Une esa carpeta con el nombre de tu archivo txt de forma segura
PALABRAS = os.path.join(hangman_1_0, "palabras.txt")


def cargar_datos():
    try:
        with open(PALABRAS, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except:
        return []


lineas = cargar_datos()
for linea in lineas:
        print(linea.strip())
