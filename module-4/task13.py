"""
Напишите функцию parse_folder, она принимает единственный параметр path, который является объектом Path.
Функция должна просканировать директорию path и вернуть кортеж из двух списков.
Первый — это список файлов внутри директории, второй — список директорий.
"""

from pathlib import Path


def parse_folder(path):
    files = []
    folders = []

    for i in path.iterdir():
        if i.is_file():
            files.append(i.name)
        else:
            folders.append(i.name)

    return files, folders