import os
from pathlib import Path


#print(os.path.abspath(os.path.dirname(__file__))) # абсолютный путь до папки с файлом (без названия файла в конце пути)
#print(os.path.abspath(__file__))  # абсолютный путь до папки с файлом (с названием файла в конце пути)
#parent_dir = os.path.dirname(os.path.abspath(__file__))
#print(parent_dir)
#print(os.path.join(parent_dir, 'path', 'file.txt'))
print(Path(__file__).absolute().parent.parent.parent)
print(Path(__file__).resolve().parent.parent.parent)
