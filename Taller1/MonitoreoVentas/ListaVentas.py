class ListaVentas:
    def __init__(self):
        self.listaVentas = []
        
    def agregar_venta(self, venta):
        self.listaVentas.append(venta)
        
    def ver_ventas(self):
        for venta in self.listaVentas:
            print(venta)
            
    def mejor_vendedor_producto(self, producto):
        # monto = unidades vendidas x precio
        lista_mejores_vendedores = []
        for venta in self.listaVentas:
            if venta.producto.nombre == producto:
                monto = venta.cantidad * venta.producto.precio
                lista_mejores_vendedores.append([venta.vendedor.nombre, monto])
        lista_mejores_vendedores.sort(key=lambda x: x[1], reverse=True)
        return lista_mejores_vendedores