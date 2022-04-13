from introducir import solicitar_introducir_cadena

__texto = solicitar_introducir_cadena("Introduce un texto") #entrada éstandar. Digamos que una línea vale 100 caracteres.
archivo = open("Mayúsculas.txt", 'w', encoding='utf-8')
archivo.close()