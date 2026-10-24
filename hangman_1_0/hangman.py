import os

# Obtiene la carpeta exacta donde está guardado este script actual
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
for linea in lineas:
        print(linea.strip())

monigote = cargar_monigote()
segmentos = "".join(monigote).split("=" * 35)

numero_segmento = 5  # Empieza en 0: el primer dibujo
print(segmentos[numero_segmento].strip("\r\n"))


