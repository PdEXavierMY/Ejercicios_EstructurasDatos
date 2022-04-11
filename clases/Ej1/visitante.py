

bloqueif = bloque_alternativa.instrucciones[0]
elemento = bloqueif.condicion.split()
while bucle.condicion:
    if bloqueif.condicion:
        print(bloqueif.entonces.mensaje)
    else:
        print(bloqueif.si_no.mensaje)
    break