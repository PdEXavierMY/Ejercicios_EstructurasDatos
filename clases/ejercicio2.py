from introducir import solicitar_introducir_cadena

archivo = open("Mayúsculas.txt", 'w', encoding='utf-8')
__texto = solicitar_introducir_cadena("Introduce un texto")
archivo.write(__texto)
archivo.close()
archivo = open("Mayúsculas.txt", 'r', encoding='utf-8')
n = 1
linea1 = ""
linea2 = ""
for linea in archivo:
    if n > 2:
        break
    else:
        if n==1:
            linea1 = linea
        elif n==2:
            linea2 = linea
    n+=1
print(linea1)
print(linea2)