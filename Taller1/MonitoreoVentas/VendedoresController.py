from ListaVendedores import ListaVendedores
from ListaProductos import ListaProductos
from ListaVentas import ListaVentas
from Venta import Venta
from Vendedor import Vendedor
from Producto import Producto
from MonitoreoView import MonitoreoView
class VendedoresController:
    def __init__(self, usuario):
        self.vista = MonitoreoView(usuario)
        self.lista_vendedores = ListaVendedores()
        self.lista_vendedores.agregar_vendedor(Vendedor("Juan"))
        self.lista_vendedores.agregar_vendedor(Vendedor("Ana"))
        self.lista_vendedores.agregar_vendedor(Vendedor("Luis"))
        
        self.lista_productos = ListaProductos()
        self.lista_productos.agregar_producto(Producto("Laptop", 3500.0))
        self.lista_productos.agregar_producto(Producto("Mouse", 150.0))
        self.lista_productos.agregar_producto(Producto("Teclado", 250.0))
        self.lista_productos.agregar_producto(Producto("Monitor", 1200.0))
        
        self.lista_ventas = ListaVentas();
        # Datos de ejemplo para ventas
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Juan"), self.lista_productos.buscar_producto("Laptop"), 2))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Ana"), self.lista_productos.buscar_producto("Mouse"), 5))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Luis"), self.lista_productos.buscar_producto("Teclado"), 3))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Juan"), self.lista_productos.buscar_producto("Monitor"), 1))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Ana"), self.lista_productos.buscar_producto("Laptop"), 1))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Luis"), self.lista_productos.buscar_producto("Mouse"), 2))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Juan"), self.lista_productos.buscar_producto("Teclado"), 4))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Ana"), self.lista_productos.buscar_producto("Monitor"), 2))
        self.lista_ventas.agregar_venta(Venta(self.lista_vendedores.buscar_vendedor("Luis"), self.lista_productos.buscar_producto("Laptop"), 1))


    def registrar_vendedor(self):
        nombre = input("Ingrese nombre del vendedor: ")
        vendedor = Vendedor(nombre.title())
        self.lista_vendedores.agregar_vendedor(vendedor)

    def ver_vendedores(self):
        self.lista_vendedores.ver_vendedores()
    
    def registrar_producto(self):
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input(f"Ingrese precio para {nombre}: "))
        self.lista_productos.agregar_producto(Producto(nombre, precio))

    def ver_lista_precios(self):
        self.lista_productos.ver_productos()

    def registrar_venta(self):
        vendedor = input("Ingrese nombre del vendedor: ")
        vendedor = self.lista_vendedores.buscar_vendedor(vendedor)
        producto = input("Ingrese nombre del producto: ")
        producto = self.lista_productos.buscar_producto(producto)
        cantidad = int(input("Ingrese cantidad vendida: "))
        self.lista_ventas.agregar_venta(Venta(vendedor, producto, cantidad))
        
    def ver_ventas(self):
        self.lista_ventas.ver_ventas()
        
    def ingresar_opcion(self):
        try: 
            opcion = int(input("Ingrese una opcion del menu: "))
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
                case 3:
                    self.registrar_producto();
                case 4:
                    self.lista_productos.ver_productos();
                case 5:
                    self.registrar_venta();
                case 6: 
                    self.ver_ventas();
                case 7:
                    producto = self.lista_productos.buscar_producto(input("Ingrese nombre del producto: "))
                    print(producto)
                    lista = self.lista_ventas.mejor_vendedor_producto(producto.nombre)
                    print(lista)