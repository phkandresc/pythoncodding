from model.model import TaskModel
from view.view import ConsoleView
from controller.controller import TaskController

if __name__ == "__main__":
    model = TaskModel()
    view = ConsoleView()
    controller = TaskController(model, view)
    controller.run()