class MonitoreoView:
    def __init__(self, usuario):
        self.usuario = usuario

    def mostrar_menu(self):
        print(f"Bienvenido {self.usuario}")
        print("1. Agregar un vendedor")
        print("2. Ver vendedores")