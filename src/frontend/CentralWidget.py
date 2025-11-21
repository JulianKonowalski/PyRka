from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog 

from frontend.Controls import Controls
from frontend.TextViewer import TextViewer

from backend.FileReader import FileReader

class CentralWidget(QWidget):

    fileChosen: pyqtSignal = pyqtSignal(str, name="filepath")
    fileOpened: pyqtSignal = pyqtSignal(str, name="file_contents")

    controls: Controls | None = None 
    text_viewer: TextViewer | None = None

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.controls = Controls()
        self.controls.loadFile.connect(self.__chooseFile__)

        self.text_viewer = TextViewer()
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_viewer)
        layout.addWidget(self.controls)
        self.setLayout(layout)

        self.fileChosen.connect(self.__openFile__)

    def __chooseFile__(self) -> None:
        filepath, check = QFileDialog.getOpenFileName(
            None, 
            "Open File", 
            "", 
            self.tr(
                "Supported Files (*.txt *.docx *.pdf);;" \
                "Text Files (*.txt);;" \
                "Microsoft Word Files (*.docx);;" \
                "PDF files (*.pdf)"
            )
        )
        if check: self.fileChosen.emit(filepath)

    def __openFile__(self, filepath: str) -> None:
        text = FileReader(filepath).readAll()
        self.text_viewer.setPlainText(text)
        self.fileOpened.emit(text)