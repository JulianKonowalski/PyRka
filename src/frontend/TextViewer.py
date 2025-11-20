from PyQt6.QtWidgets import QWidget, QTextEdit

class TextViewer(QTextEdit):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setReadOnly(True)