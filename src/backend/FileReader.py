import io

class FileReader:
    file: io.TextIOWrapper | None = None

    def __init__(self, filepath: str) -> None:
        self.file = open(filepath, "r")

    def readLine(self) -> str | None:
        return self.file.readline()