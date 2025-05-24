class ListaProductos:
    def __init__(self):
        self.listaProductos = []
    
    def agregar_producto(self, producto):
        self.listaProductos.append(producto)
    
    def existe_producto(self, producto):
        return producto.nombre not in [p.nombre for p in self.listaProductos]
    
    def buscar_producto(self, nombre_producto):
        for producto in self.listaProductos:
            if producto.nombre == nombre_producto:
                return producto
        return None
    
    def ver_productos(self):
        for producto in self.listaProductos:
            print(producto)

    