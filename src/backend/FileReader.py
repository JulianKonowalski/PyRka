import os
import io

class FileReader:

    file: io.TextIOWrapper | None = None
    filesize: int = 0

    def __init__(self, filepath: str) -> None:
        self.file = open(filepath, "r")
        self.filesize = os.fstat(self.file.fileno()).st_size

    def readLine(self) -> str:
        data = ""
        while data == "" and self.file.tell() < self.filesize:
            data = self.file.readline().strip("\n")
        return data