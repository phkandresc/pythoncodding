class VectorView:
    def mostrar_menu(self):
        print("1. Introducir el primer vector")
        print("2. Introducir el segundo vector")
        print("3. Calcular la suma")
        print("4. Calcular la diferencia")
        print("5. Salir")

    def obtener_texto(self, prompt):
            return input(prompt)
    
    def mostrar_mensaje(self, mensaje):
         print(mensaje)
    
    def mostrar_vector(self, vector):
        print(f"Vector: {vector}")