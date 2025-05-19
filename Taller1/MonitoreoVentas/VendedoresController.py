from DicVendedores import DicVendedores
from MonitoreoView import MonitoreoView
class VendedoresController:
    def __init__(self, usuario):
        self.vista = MonitoreoView(usuario)
        self.vendedores = DicVendedores()


    def registrar_vendedor(self):
        nombre = input("Ingrese nombre del vendedor: ")
        self.vendedores.agregar_vendedor(nombre)

    def ver_vendedores(self):
        self.vendedores.ver_vendedores()

    def ingresar_opcion(self):
        try: 
            opcion = int(input("Ingrese una opcion del menu"))
            return opcion
        except:
            print("ERROR")
        
    
    def iniciar(self):
        while True:
            self.vista.mostrar_menu();
            opcion = self.ingresar_opcion()
            match opcion:
                case 1:
                    self.registrar_vendedor();
                case 2:
                    self.ver_vendedores();
    