# vista.py

class ConsoleView:
    def show_menu(self):
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")

    def get_input(self, prompt):
        return input(prompt)

    def show_tasks(self, tasks):
        if not tasks:
            print("No hay tareas.")
        else:
            print("\nLista de tareas:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    def show_message(self, message):
        print(message)
