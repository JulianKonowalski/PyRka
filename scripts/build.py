import os
import pathlib

CWD: str = pathlib.Path(__file__).parent.resolve()
ICON_PATH: str = os.path.abspath(os.path.join(CWD, "..", "assets", "icon.ico"))
MAIN_PATH: str = os.path.abspath(os.path.join(CWD, "..", "src", "main.py"))

if __name__ == "__main__":
    os.system(f"pyinstaller --onefile --windowed --name PyRka --icon {ICON_PATH} {MAIN_PATH}")