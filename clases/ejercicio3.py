#producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
#precio_neto = FactoryFactura.crear(producto).facturar() 
#print(precio_neto) 
## 105.5 
 
#producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
#precio_neto = FactoryFactura.crear(producto).facturar() ==> int
#print(precio_neto) 
## 120

class Naturaleza:
    SERVICIO = 0.2
    ALIMENTARIA = 0.055
class FactoryFactura:
    def crear(tipo_producto):
        if tipo_producto == 0.2 or 0.05:
            precio = 100
            return precio
        else:
            print("El programa solo factura productos alimentarios o servicios")
def Producto(iva):
    return iva