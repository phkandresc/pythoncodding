class Turno: 
    def __init__(self, paciente, dia, hora):
        self.paciente = paciente
        self.dia = dia
        self.hora = hora
        
    def __str__(self):
        return f"Turno(paciente={self.paciente.nombre}, dia={self.dia}, hora={self.hora})"