class ListaVendedores:
    def __init__(self):
        self.listaVendedores = []

    def agregar_vendedor(self, vendedor):
        if self.existe_vendedor(vendedor):
            self.listaVendedores.append(vendedor)
        else:
            print(f"El vendedor '{vendedor.nombre}' ya existe en la lista.")
    
    def existe_vendedor(self, vendedor):
        return vendedor.nombre not in [v.nombre for v in self.listaVendedores]
        
    def buscar_vendedor(self, nombre):
        for vendedor in self.listaVendedores:
            if vendedor.nombre == nombre:
                return vendedor
        return None
    
    def ver_vendedores(self):
        for vendedor in self.listaVendedores:
            print(vendedor)