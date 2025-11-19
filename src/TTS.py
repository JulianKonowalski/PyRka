import io
import time
import typing

import gtts
import pyglet

class TTS:

    data_callback: typing.Callable[[None], str] | None = None

    def __init__(self, data_callback: typing.Callable[[None], list[str]]) -> None:
        self.data_callback = data_callback

    def run(self) -> None:
        while data := self.data_callback():
            mp3_fp = io.BytesIO()
            gtts.gTTS(data, lang="en").write_to_fp(mp3_fp)
            audio = pyglet.media.load(".mp3", mp3_fp, streaming=False)
            audio.play()
            time.sleep(audio.duration)