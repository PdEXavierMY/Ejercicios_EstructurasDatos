from introducir import solicitar_introducir_cadena

archivo = open("Mayúsculas.txt", 'w', encoding='utf-8')
texto = solicitar_introducir_cadena("Introduce un texto")
archivo.close()