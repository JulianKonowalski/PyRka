from PyQt6.QtWidgets import QApplication

from backend.TTS import TTS
from frontend.MainWindow import MainWindow

class App(QApplication):

    main_window: MainWindow | None = None
    tts: TTS | None = None

    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)
        self.main_window = MainWindow()
        # self.main_window.central_widget.fileOpened.connect(self.__ttsInit__)
        self.main_window.show()

    def __ttsInit__(self, text: str) -> None:
        self.tts = TTS(text)

    def __ttsRun___(self) -> None:
        if self.tts == None: return
        self.tts.run()