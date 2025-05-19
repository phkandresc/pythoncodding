# controlador.py

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_input("Elige una opción: ")

            if choice == "1":
                task = self.view.get_input("Escribe la tarea: ")
                self.model.add_task(task)
                self.view.show_message("Tarea agregada.")
            elif choice == "2":
                tasks = self.model.list_tasks()
                self.view.show_tasks(tasks)
            elif choice == "3":
                self.view.show_message("¡Hasta luego!")
                break
            else:
                self.view.show_message("Opción inválida.")
