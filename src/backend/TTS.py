import io

import gtts

from backend.FileReader import FileReader
from backend.AudioPlayer import AudioPlayer 

class TTS:

    file_reader: FileReader | None = None
    audio_player: AudioPlayer | None = None

    def __init__(self, filepath: str) -> None:
        self.file_reader = FileReader(filepath)
        self.audio_player = AudioPlayer(self.__parseLine__)

    def __parseLine__(self) -> io.BytesIO:
        data = self.file_reader.readLine()
        if data == "": return None
        
        mp3_fp = io.BytesIO()
        gtts.gTTS(data, lang="en").write_to_fp(mp3_fp)
        return mp3_fp
    
    def run(self):
        self.audio_player.run()