import io
import threading

import gtts

from backend.AudioPlayer import AudioPlayer 

class TTS:
    
    chunk_size: int = 10
    raw_data: list[str] = []
    processed_data: list[io.BytesIO] = []
    audio_player: AudioPlayer | None = None

    def __init__(self, text: str, chunk_size: int = 10) -> None:
        self.chunk_size = chunk_size 
        self.raw_data = text.split()
        self.audio_player = AudioPlayer(self.__getDataChunk__)

    def run(self):
        process_thread = threading.Thread(target=self.__processData__)
        audio_thread = threading.Thread(target=self.audio_player.run)
        process_thread.start()
        audio_thread.start()

    def __processData__(self) -> None:
        while len(self.raw_data) > 0:
            chunk_size: int = min(len(self.raw_data), self.chunk_size)
            mp3_fp = io.BytesIO()
            gtts.gTTS("".join(self.raw_data[:chunk_size]), lang="en").write_to_fp(mp3_fp)
            self.processed_data.append(mp3_fp)
            del self.raw_data[:chunk_size]

    def __getDataChunk__(self) -> io.BytesIO | None:
        if len(self.processed_data) == 0:
            if len(self.raw_data) == 0: return None
            while len(self.processed_data) == 0: pass
        return self.processed_data.pop(0)