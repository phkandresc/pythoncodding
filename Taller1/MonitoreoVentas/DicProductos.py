class DicProductos:
    def __init__(self):
        self.dic_productos = {}
    
    def agregar_producto(self, nombre, precio):
        self.dic_productos[nombre] = precio
    
    def eliminar_producto(self, nombre):
        if nombre in self.dic_productos:
            del self.dic_productos[nombre]
    
    def ver_productos(self):
        return self.dic_productos.values()
    
    def obtener_producto(self, nombre):
        if nombre in self.dic_productos:
            return self.dic_productos.get(nombre)
        return None