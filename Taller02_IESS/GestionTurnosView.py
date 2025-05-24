class GestionTurnosView:
    def __init__(self, usuario):
        self.usuario = usuario

    def mostrar_menu(self):
        print(f"Bienvenido {self.usuario}")
        print("1. Registro de datos del paciente.")
        print("2. Ver lista de pacientes")
        print("3. Consultar tabla mensual de turnos.")
        print("4. Asignacion de citas.")
        print("5. Cantidad de turnos a maxima capacidad en el mes")
        print("6. Salir.")