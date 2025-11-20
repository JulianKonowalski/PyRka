from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QFileDialog 

class CentralWidget(QWidget):

    fileChosen: pyqtSignal = pyqtSignal(str, name="filepath")
    fileOpened: pyqtSignal = pyqtSignal(str, name="file_contents")
    text_edit: QTextEdit | None = None

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.text_edit = QTextEdit()
        button = QPushButton("Open File")
        button.clicked.connect(self.__chooseFile__)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(button)
        self.setLayout(layout)

        self.fileChosen.connect(self.__openFile__)

    def __chooseFile__(self) -> None:
        filepath, check = QFileDialog.getOpenFileName(
            None, 
            "Open File", 
            "", 
            self.tr("Text Files (*.txt);;MS Word Files (*.docx)")
        )
        if check: self.fileChosen.emit(filepath)

    def __openFile__(self, filepath: str) -> None:
        text = open(filepath).read()
        self.text_edit.setPlainText(text)
        self.fileOpened.emit(text)