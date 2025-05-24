from GestionTurnosView import GestionTurnosView
from TablaTurnos import TablaTurnos
from Turno import Turno
from ListaPacientes import ListaPacientes
from Paciente import Paciente
class GestionTurnosController:
    
    def __init__(self, usuario):
        self.vista = GestionTurnosView(usuario)
        self.tabla_turnos = TablaTurnos()
        self.lista_pacientes = ListaPacientes()
        self.lista_pacientes.registrar_paciente(Paciente("0105627806", "Juan Perez"))
        
        self.tabla_turnos.agregar_turno(Turno(self.lista_pacientes.buscar_paciente("0105627806"), 1, 10))
        self.tabla_turnos.agregar_turno(Turno(self.lista_pacientes.buscar_paciente("0105627806"), 1, 10))
        self.tabla_turnos.agregar_turno(Turno(self.lista_pacientes.buscar_paciente("0105627806"), 1, 10))
        self.tabla_turnos.agregar_turno(Turno(self.lista_pacientes.buscar_paciente("0105627806"), 1, 10))
        self.tabla_turnos.agregar_turno(Turno(self.lista_pacientes.buscar_paciente("0105627806"), 1, 10))
        
    
    def registrar_paciente(self):
        cedula = input("Ingrese la cédula del paciente: ")
        nombre = input("Ingrese el nombre del paciente: ")
        paciente = Paciente(cedula, nombre)
        self.lista_pacientes.registrar_paciente(paciente)
        print("Paciente registrado exitosamente.")
    
    def ingresar_opcion(self):
        try: 
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except:
            print("ERROR")
    
    def asignar_turno(self):
        cedula = input("Ingrese la cédula del paciente: ")
        paciente = self.lista_pacientes.buscar_paciente(cedula)
        if paciente is None:
            print("Paciente no encontrado.")
            return
        dia = int(input("Ingrese el dia del mes: "))
        hora = int(input("Ingrese la hora: "))
        turno = Turno(paciente, dia, hora)
        self.tabla_turnos.agregar_turno(turno)

    def run(self):
        while True:
            self.vista.mostrar_menu();
            opcion = self.ingresar_opcion()
            match opcion:
                case 1:
                    self.registrar_paciente()
                case 2:
                    self.lista_pacientes.ver_lista_pacientes()
                case 3:
                    self.tabla_turnos.ver_tabla_turnos()
                case 4:
                    self.asignar_turno()
                case 5:
                    max = self.tabla_turnos.cantidad_turnos_maximo()
                    print(f"La cantidad de turnos a máxima capacidad en el mes es: {max}")
                case 6:
                    print("Saliendo del programa.")
                    break