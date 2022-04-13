from introducir import solicitar_introducir_numero_extremo
from clases import *

if __name__ == '__main__':
    ejercicio = solicitar_introducir_numero_extremo("Introduzca un número para ejecutar un ejercicio(1 para el ej1, 2 para el ej2 y 3 paar el ej3)", 1, 3)
    if ejercicio == 1:
        visitante()
    elif ejercicio == 2:
        doslineas()
    elif ejercicio ==3:
        from clases import ejercicio3