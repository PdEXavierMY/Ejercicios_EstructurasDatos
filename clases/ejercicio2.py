def solicitar_introducir_cadena(invite): #no soy capaz de importear, seguiré intentando
    """
    Esta función verifica que hay un dato introducido
    de al menos un carácter
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        if len(datoIntroducido) > 0:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido
        else:
            print("¡¡La cadena introducida debe tener al menos 1 elemento!!")

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