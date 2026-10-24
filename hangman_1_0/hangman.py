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


# =========================================VALIDACIONES===============================
def validaciones(letras_usadas):
    n = True
    while n:
        letra = ingreso_letra()
        if letra in letras_usadas:
            print("¡LA LETRA YA AH SIDO USADA!")
        elif len(letra) == 1 and 'A' <= letra <= 'Z':
            n = False
        elif len(letra) == 0:
            print("¡NO PUEDES ENTREGAR EL CARACTER VACIO!")
        elif len(letra) > 1:
            print("!SOLO SE PERMITE UNA SOLA LETRA POR INTENTO¡")
        else:
            print("EL CARACTER DEBE ESTAR ENTRE [A-Z]")
    return letra
#=====================================================================================

#===============DIBUJOS DEL AHORCADO=============
def monigotes(vidas):
    segmentos = "".join(monigote).split("=" * 35)
    numero_segmento = 6 - vidas
    print(segmentos[numero_segmento].strip("\r\n")) 
#================================================


#=============LOGICA DEL JUEGO===================
def jugabilidad():

    vidas = 6
    letras_usadas = []
    palabra_oculta = palabra_random()
    list_palabra_oculta = list(palabra_oculta)
    progreso_jugador = ['_'] * len(palabra_oculta)
    while vidas > 0:
        print("\n")
        monigotes(vidas)
        print("TIENES " + str(vidas) + " VIDAS")
        print("Palabra: " + " ".join(progreso_jugador))
        letra = validaciones(letras_usadas) 
        letras_usadas.append(letra)
        for i in range(len(list_palabra_oculta)):
            if list_palabra_oculta[i] == letra:
                progreso_jugador[i] = letra
                
        if letra not in list_palabra_oculta:
            vidas -= 1

        if '_' not in progreso_jugador:
            print(" ".join(progreso_jugador))
            print("FELICIDADES, GANASTE EL JUEGO")
            break

        if vidas == 0:
            print("\n")
            monigotes(0)
            print("\n")
            print("LO SENETIMOS, HAS PERDIDO.\nLA PALABRA OCULTA ES: " + palabra_oculta)
#================================================

#================================================
def menu_principal():
    jugando = True
    while jugando:
        print("\n")
        print("╔═════════════════════════════════════╗")
        print("║                                     ║")
        print("║               HangMan               ║")
        print("║                                     ║")
        print("╠═════════════════════════════════════╣")
        print("║                                     ║")
        print("║      [ 1 ] Iniciar partida          ║")
        print("║      [ 2 ] Salir del juego          ║")
        print("║                                     ║")
        print("╚═════════════════════════════════════╝")
        
        opcion = input("\nSelecciona una opción (1 o 2): ")
        
        if opcion == '1':
            jugabilidad()
            pass 
            
        elif opcion == '2':
            
            print("\n¡Gracias por jugar! Cerrando consola...")
            jugando = False 
            
        else:
            print("\nOpción no válida. Por favor, ingresa 1 o 2.")
#================================================


menu_principal()




