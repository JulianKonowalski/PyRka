import io
import threading

import gtts

from backend.AudioPlayer import AudioPlayer 

class TTS:
    
    chunk_size: int = 10
    chunk_start: int = 0
    is_playing: bool = False
    raw_data: list[str] = []
    audio_player: AudioPlayer | None = None
    mutex: threading.Lock = threading.Lock()

    def __init__(self, text: str, chunk_size: int = 10) -> None:
        self.chunk_size = chunk_size 
        self.raw_data = text.split()
        self.audio_player = AudioPlayer(self.__getDataChunk__)
        self.__startAudioThread__()       

    def playPause(self):
        with self.mutex:
            if self.is_playing: self.audio_player.pause()
            else: self.audio_player.play()
            self.is_playing = False if self.is_playing else True

    def reset(self):
        with self.mutex:
            self.audio_player.reset()
            self.chunk_start = 0
            self.__startAudioThread__()

    def __processChunk__(self) -> io.BytesIO | None:
        chunk_size: int = min(len(self.raw_data), self.chunk_size)
        text = "".join(self.raw_data[self.chunk_start:self.chunk_start + chunk_size])
        if text == "": return None
        
        mp3_fp = io.BytesIO()
        gtts.gTTS(text, lang="en").write_to_fp(mp3_fp)
        self.chunk_start += chunk_size
        return mp3_fp

    def __getDataChunk__(self) -> io.BytesIO | None:
        with self.mutex:
            if (len(self.raw_data) - self.chunk_start) == 0: return None
            return self.__processChunk__()
        
    def __startAudioThread__(self) -> None:
        audio_thread = threading.Thread(target=self.audio_player.run)
        audio_thread.start()       