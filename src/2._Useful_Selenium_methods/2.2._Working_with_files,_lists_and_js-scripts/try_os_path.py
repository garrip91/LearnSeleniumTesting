import os


print(os.path.abspath(os.path.dirname(__file__))) # абсолютный путь до папки с файлом (без названия файла в конце пути)
print(os.path.abspath(__file__))  # абсолютный путь до папки с файлом (с названием файла в конце пути)
