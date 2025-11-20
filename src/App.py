from PyQt6.QtWidgets import QApplication

from backend.TTS import TTS
from frontend.MainWindow import MainWindow

class App(QApplication):

    main_window: MainWindow | None = None

    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)
        self.main_window = MainWindow()
        self.main_window.show()

    def __tts__(self, filepath: str) -> None:
        self.tts = TTS(filepath)
        self.tts.run()