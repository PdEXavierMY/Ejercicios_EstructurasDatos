from introducir.cadena import solicitar_introducir_cadena

class Modelo:
    def __init__(self, texto):
        self.texto = texto
class Vista:
    def __init__(self):
        self.modelo = Modelo(solicitar_introducir_cadena("Introduce un texto") #entrada éstandar. Digamos que una línea vale 100 caracteres.
)
    def doslineas(self):
        archivo = open("Mayúsculas.txt", 'w', encoding='utf-8')
        archivo.write("")
        archivo.close()
        __caracteres = list(self.modelo)
        archivo = open("Mayúsculas.txt", 'a', encoding='utf-8')
        for j in range(2):
            if len(__caracteres) < 101:
                archivo.write(str(self.modelo).upper())
                break
            else:
                for i in range(100):
                    letra = __caracteres[i]
                    if i == 99:
                        archivo.write(str(letra).upper()+"\n")
                    else:
                        archivo.write(letra.upper())
                for k in range(100):
                    __caracteres.pop(0) 
        archivo.close()
class Controlador:
    def __init__(self):
        self.vista = Vista()
    
    def conseguirtexto(self):
        self.vista.doslineas()