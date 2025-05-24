class Paciente:
    
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        
    def __str__(self):
        return f"Paciente[cedula={self.cedula}, nombre={self.nombre}]"