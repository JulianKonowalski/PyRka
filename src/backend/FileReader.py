import os

import docx 
import pypdf

class FileReader:

    filepath: str = ""

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def readAll(self) -> str:
        _, extension = os.path.splitext(self.filepath)
        match extension.lower():
            case ".txt": return self.__readTxt__()
            case ".docx": return self.__readDocx__()
            case ".pdf": return self.__readPdf__()
            case _: return ""

    def __readTxt__(self) -> str:
        return open(self.filepath).read()

    def __readDocx__(self) -> str:
        document = docx.Document(self.filepath)
        return "".join([paragraph.text + " " for paragraph in document.paragraphs])

    def __readPdf__(self) -> str:
        reader = pypdf.PdfReader(self.filepath)
        return "".join([page.extract_text() + " " for page in reader.pages])