
archivo = open("Mayúsculas.txt", 'w', encoding='utf-8')
archivo.close()
__texto = input("Introduce un texto") #entrada éstandar. Digamos que una línea vale 100 caracteres.
__caracteres = list(__texto)
archivo = open("Mayúsculas.txt", 'a', encoding='utf-8')
n=1
while n<3:
    if len(__caracteres) < 101:
        archivo.write(str(__texto)+"\n")
        break
    else:
        for i in range(100):
            letra = __caracteres[i]
            archivo.write(letra)
        archivo.write("\n")
        for i in range(100):
            __caracteres.pop(0)
    n+=1    
archivo.close()