import io
import typing
import threading

import pyglet

class AudioPlayer:

    player: pyglet.media.Player | None = None
    data_callback: typing.Callable[[None], io.BytesIO | None] | None = None
    is_running: bool = False
    mutex: threading.Lock = threading.Lock()

    def __init__(self, data_callback: typing.Callable[[None], io.BytesIO | None]) -> None:
        self.data_callback = data_callback
        self.player = pyglet.media.Player()

    def run(self) -> None:
        self.is_running = True
        while data := self.data_callback():
            with self.mutex:
                if not self.is_running: break
                self.player.queue(pyglet.media.load(".mp3", data, streaming=False))

    def play(self) -> None:
        with self.mutex:
            self.player.play()

    def pause(self) -> None:
        with self.mutex:
            self.player.pause()

    def reset(self) -> None:
        with self.mutex:
            self.is_running = False
            self.player.pause()
            self.player.delete()
            self.player = pyglet.media.Player()