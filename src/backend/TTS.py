import io
import threading

import gtts

from backend.AudioPlayer import AudioPlayer 

class TTS:

    audio_player: AudioPlayer | None = None
    data: list[io.BytesIO | None] = []
    is_running: bool = False

    def __init__(self, text: str) -> None:
        mp3_fp = io.BytesIO()
        gtts.gTTS(text, lang="en").write_to_fp(mp3_fp)
        self.data.append(mp3_fp)
        self.audio_player = AudioPlayer(self.getDataChunk)

    def getDataChunk(self) -> io.BytesIO | None:
        return None if len(self.data) == 0 else self.data.pop(0)

    def run(self) -> None:
        audio_thread = threading.Thread(target=self.audio_player.run)
        self.is_running = True
        audio_thread.start()