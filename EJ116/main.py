from view.vector_view import VectorView
from controller.vector_controller import VectorController

if __name__ == "__main__":
    view = VectorView()
    controller = VectorController(view)
    controller.ejecutar()