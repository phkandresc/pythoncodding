class MonitoreoView:
    def __init__(self, usuario):
        self.usuario = usuario

    def mostrar_menu(self):
        print(f"Bienvenido {self.usuario}")
        print("1. Agregar un vendedor.")
        print("2. Ver vendedores.")
        print("3. Registrar un producto.")
        print("4. Ver lista de precios.")
        print("5. Registrar una venta.")
        print("6. Ver ventas.")
        print("7. Mejores vendedores por producto: ")