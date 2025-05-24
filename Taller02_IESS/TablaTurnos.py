class TablaTurnos:
    def __init__(self):
        self.tabla_turnos = []
        for dia in range(1, 31):
            horas = [0] * 23  # 24 horas inicializadas en 0
            self.tabla_turnos.append(horas)
        
    def ver_tabla_turnos(self):
        for dia in self.tabla_turnos:
            print(dia)
            
    def agregar_turno(self, turno):
        dia = turno.dia - 1
        hora = turno.hora
        if self.tabla_turnos[dia][hora] < 5:
            self.tabla_turnos[dia][hora] += 1
            print(f"Turno asignado para el paciente {turno.paciente.nombre} el dia {turno.dia} a las {turno.hora}.")
        else:
            print("El turno ya está ocupado.")
            
    def cantidad_turnos_maximo(self):
        max_turnos = 0
        for dia in self.tabla_turnos:
            for hora in dia:
                if hora == 5:
                    max_turnos += 1
        return max_turnos
    
    