class ListaPacientes:
    def __init__(self):
        self.lista_pacientes = []
        
    def registrar_paciente(self, paciente):
        self.lista_pacientes.append(paciente)
        
    def ver_lista_pacientes(self):
        for paciente in self.lista_pacientes:
            print(paciente)
    
    def buscar_paciente(self, cedula):
        for paciente in self.lista_pacientes:
            if paciente.cedula == cedula:
                return paciente
        return None