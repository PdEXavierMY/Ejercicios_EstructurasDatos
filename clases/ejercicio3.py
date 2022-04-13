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
    class crear():
        def __init__(self, tipo_producto):
            self.tipo_producto = tipo_producto
        def facturar(self):
            if self.tipo_producto == 0.2 or 0.05:
                self.precio = 100
                return self.precio+(self.precio*self.tipo_producto)
            else:
                print("El programa solo factura productos alimentarios o servicios.")
def Producto(iva):
    return iva

producto = Producto(Naturaleza.ALIMENTARIA)
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)

producto = Producto(Naturaleza.SERVICIO)
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)