from introducir.cadena import solicitar_introducir_cadena

def doslineas():
    archivo = open("Mayúsculas.txt", 'w', encoding='utf-8')
    archivo.write("")
    archivo.close()
    __texto = solicitar_introducir_cadena("Introduce un texto") #entrada éstandar. Digamos que una línea vale 100 caracteres.
    __caracteres = list(__texto)
    archivo = open("Mayúsculas.txt", 'a', encoding='utf-8')
    for j in range(2):
        if len(__caracteres) < 101:
            archivo.write(str(__texto))
            break
        else:
            for i in range(100):
                letra = __caracteres[i]
                if i == 99:
                    archivo.write(str(letra)+"\n")
                else:
                    archivo.write(letra)
            for k in range(100):
                __caracteres.pop(0) 
    archivo.close()