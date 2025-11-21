import io
import threading

import gtts

from backend.AudioPlayer import AudioPlayer 

class TTS:
    
    chunk_size: int = 10
    raw_data: list[str] = []
    audio_player: AudioPlayer | None = None
    is_playing: bool = False

    def __init__(self, text: str, chunk_size: int = 10) -> None:
        self.chunk_size = chunk_size 
        self.raw_data = text.split()
        self.audio_player = AudioPlayer(self.__getDataChunk__)
        
        audio_thread = threading.Thread(target=self.audio_player.run)
        audio_thread.start()

    def playPause(self):
        if self.is_playing: self.audio_player.pause()
        else: self.audio_player.play()
        self.is_playing = False if self.is_playing else True

    def __processChunk__(self) -> io.BytesIO:
        chunk_size: int = min(len(self.raw_data), self.chunk_size)
        mp3_fp = io.BytesIO()
        gtts.gTTS("".join(self.raw_data[:chunk_size]), lang="en").write_to_fp(mp3_fp)
        del self.raw_data[:chunk_size]
        return mp3_fp

    def __getDataChunk__(self) -> io.BytesIO | None:
        if len(self.raw_data) == 0: return None
        return self.__processChunk__()