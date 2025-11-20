from PyQt6.QtWidgets import QMainWindow

from frontend.CentralWidget import CentralWidget

class MainWindow(QMainWindow):

    central_widget: CentralWidget | None = None

    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 400)
        self.setWindowTitle("PyRka")
        
        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)