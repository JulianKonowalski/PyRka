import io
import threading

import gtts

from backend.FileReader import FileReader
from backend.AudioPlayer import AudioPlayer 

class TTS:

    file_reader: FileReader | None = None
    audio_player: AudioPlayer | None = None
    data: list[io.BytesIO | None] = []
    is_running: bool = False

    def __init__(self, filepath: str) -> None:
        self.file_reader = FileReader(filepath)
        self.audio_player = AudioPlayer(self.getDataChunk)
        self.data.append(self.__parseLine__())

    def __parseLine__(self) -> io.BytesIO | None:
        data = self.file_reader.readLine()
        if data == "": return None
        mp3_fp = io.BytesIO()
        gtts.gTTS(data, lang="en").write_to_fp(mp3_fp)
        return mp3_fp

    def __parseFile__(self) -> None:
        while True:
            parsed = self.__parseLine__()
            while len(self.data) >= 5: pass
            self.data.append(parsed)
            if parsed == None: break
    
    def getDataChunk(self) -> io.BytesIO | None:
        return self.data.pop(0)

    def run(self) -> None:
        audio_thread = threading.Thread(target=self.audio_player.run)
        self.is_running = True
        audio_thread.start()
        self.__parseFile__()

    def stop(self) -> None:
        self.is_running = False