"""Шахматы были лучше 🌶️
Вам доступен архив data.zip, содержащий различные папки и файлы.
Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:
{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:
    first_name — имя
    last_name — фамилия
    team — название футбольного клуба
    position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
выступающих за футбольный клуб Arsenal.
Футболисты должны быть расположены в лексикографическом порядке имен,
а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует,
что он является корректным текстовым файлом в формате JSON.
"""
import json
from pathlib import Path
from zipfile import ZipFile


result = []

with ZipFile('files/data.zip') as zip_file:
    file_names = zip_file.namelist()
    for file_name in file_names:
        if Path(file_name).suffix == '.json':
            with zip_file.open(file_name) as json_file:
                try:
                    content = json_file.read().decode('utf-8')
                    info = json.loads(content)
                    if info['team'] == 'Arsenal':
                        result.append(f"{info['first_name']} {info['last_name']}")
                except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                    continue

print(*sorted(result, key=lambda x: x.split()), sep='\n')
