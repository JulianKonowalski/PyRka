from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class Controls(QWidget):

    loadFile: pyqtSignal = pyqtSignal()
    resetPlayback: pyqtSignal = pyqtSignal()
    startStopPlayback: pyqtSignal = pyqtSignal()

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        layout = QHBoxLayout(self)

        upload_btn = QPushButton("Load File")
        upload_btn.clicked.connect(lambda: self.loadFile.emit())

        play_btn = QPushButton("Play/Pause")
        play_btn.clicked.connect(lambda: self.startStopPlayback.emit())
        
        reset_btn = QPushButton("Reset")
        reset_btn.clicked.connect(lambda: self.resetPlayback.emit())

        layout.addWidget(upload_btn)
        layout.addWidget(play_btn)
        layout.addWidget(reset_btn)