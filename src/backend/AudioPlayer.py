import io
import time
import typing

import pyglet

class AudioPlayer:

    player: pyglet.media.Player | None = None
    data_callback: typing.Callable[[None], io.BytesIO | None] | None = None

    def __init__(self, data_callback: typing.Callable[[None], io.BytesIO | None]) -> None:
        self.data_callback = data_callback
        self.player = pyglet.media.Player()

    def run(self) -> None:
        while data := self.data_callback():
            self.player.queue(pyglet.media.load(".mp3", data, streaming=False))

    def play(self) -> None:
        self.player.play()

    def pause(self) -> None:
        self.player.pause()