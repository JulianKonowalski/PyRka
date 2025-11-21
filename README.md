# PyRka
This is a __text-to-speech__ app that reads `.txt`, `.docx` and `.pdf` files to
the user. You can load any file you want and listen to what is has to say!

## Usage
The app comes with 3 buttons:
* load file
* play/pause
* reset

It's quite simple, really.

## Installation & Building

To build the application run:
```
# cd to destination folder here <<<

git clone https://github.com/JulianKonowalski/PyRka.git
cd PyRka

# create and activate python venv here <<<

pip install -r requirements.txt
python scripts/build.py
```

## Additional info about the app
As stated earlier the application only supports 3 file formats written in english.
Reading and processing other languages is possible by modifying the source code,
but changing them dynamically is not supported as of today.