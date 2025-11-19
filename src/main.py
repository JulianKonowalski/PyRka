import os
import pathlib

from backend.TTS import TTS
from backend.FileReader import FileReader

CWD: str = pathlib.Path(__file__).parent.resolve()
FILEPATH: str = os.path.join(CWD, "..", "test.txt")

if __name__ == "__main__":
    fr = FileReader(FILEPATH)
    tts = TTS(fr.readLine)
    tts.run()