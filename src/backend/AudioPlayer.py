import io
import time
import typing

import pyglet

class AudioPlayer:

    data_callback: typing.Callable[[None], io.BytesIO | None] | None = None

    def __init__(self, data_callback: typing.Callable[[None], io.BytesIO | None]) -> None:
        self.data_callback = data_callback

    def run(self) -> None:
        while data := self.data_callback():
            audio = pyglet.media.load(".mp3", data, streaming=False)
            audio.play()
            time.sleep(audio.duration)