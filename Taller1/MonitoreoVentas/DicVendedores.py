class DicVendedores:
    def __init__(self):
        self.dic_vendedores = {}

    def agregar_vendedor(self,  nombre):
        self.dic_vendedores["nombre"] = nombre

    def ver_vendedores(self):
        print(self.dic_vendedores.values())
    