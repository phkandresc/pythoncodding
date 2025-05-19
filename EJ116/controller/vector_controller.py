from model.vector import Vector

class VectorController:
    def __init__(self, view):
        self.view = view
        self.vector1 = None
        self.vector2 = None

    def introducir_vector(self):
        try:
            x = float(self.view.obtener_texto("Ingrese coordenada en x"))
            y = float(self.view.obtener_texto("Ingrese coordenada en y"))
            z = float(self.view.obtener_texto("Ingrese coordenada en z"))
            return Vector(x, y, z)
        except ValueError:
            self.view.mostrar_mensaje("Entrada inválida. Debe ser un número.")
            return None

    def ejecutar(self):
        while True:
            self.view.mostrar_menu()
            opcion = self.view.obtener_texto("Elige una opción")

            if opcion == "1":
                v = self.introducir_vector()
                if v:
                    self.vector1 = v
                    self.view.mostrar_mensaje("Primer vector guardado.")
                    self.view.mostrar_vector(v)

            elif opcion == "2":
                v = self.introducir_vector()
                if v:
                    self.vector2 = v
                    self.view.mostrar_mensaje("Segundo vector guardado.")
                    self.view.mostrar_vector(v)

            elif opcion == "3":
                if self.vector1 and self.vector2:
                    resultado = self.vector1 + self.vector2
                    self.view.mostrar_mensaje("Suma:")
                    self.view.mostrar_vector(resultado)
                else:
                    self.view.mostrar_mensaje("Debe ingresar ambos vectores primero.")

            elif opcion == "4":
                if self.vector1 and self.vector2:
                    resultado = self.vector1 - self.vector2
                    self.view.mostrar_mensaje("Diferencia:")
                    self.view.mostrar_vector(resultado)
                else:
                    self.view.mostrar_mensaje("Debe ingresar ambos vectores primero.")

            elif opcion == "5":
                if self.vector1 and self.vector2:
                    resultado = self.vector1 * self.vector2
                    self.view.mostrar_mensaje(f"Producto escalar: {resultado}")
                else:
                    self.view.mostrar_mensaje("Debe ingresar ambos vectores primero.")

            elif opcion == "6":
                if self.vector1 and self.vector2:
                    resultado = self.vector1.producto_vectorial(self.vector2)
                    self.view.mostrar_mensaje("Producto vectorial:")
                    self.view.mostrar_vector(resultado)
                else:
                    self.view.mostrar_mensaje("Debe ingresar ambos vectores primero.")

            elif opcion == "7":
                self.view.mostrar_mensaje("¡Hasta luego!")
                break

            else:
                self.view.mostrar_mensaje("Opción inválida.")