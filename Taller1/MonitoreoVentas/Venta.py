class Venta:
    def __init__(self, vendedor, producto, cantidad):
        self.vendedor = vendedor
        self.producto = producto
        self.cantidad = cantidad
        
    def __str__(self):
        return f"Vendedor: {self.vendedor.nombre}, Producto: {self.producto.nombre}, Cantidad: {self.cantidad}"