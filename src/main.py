import os
import pathlib

from backend.TTS import TTS

CWD: str = pathlib.Path(__file__).parent.resolve()
FILEPATH: str = os.path.join(CWD, "..", "test.txt")

if __name__ == "__main__":
    tts = TTS(FILEPATH)
    tts.run()