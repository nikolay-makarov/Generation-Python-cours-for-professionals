"""Функция flip_dict()
Рассмотрим следующий словарь:
{'a': [1, 2], 'b': [3, 1], 'c': [2]}
«Перевернем» его, представив ключи в виде значений, а значения — в виде ключей:
{1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
Реализуйте функцию flip_dict(), которая принимает один аргумент:
dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк
Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию),
который представляет собой «перевернутый» словарь dict_of_lists.
Примечание 1. Ключи в возвращаемом функцией словаре, а также элементы в списках
должны располагаться в своем исходном порядке."""
from collections import defaultdict


def flip_dict(dict_of_lists: dict) -> defaultdict:
    result = defaultdict(list)
    for key, value in dict_of_lists.items():
        for elem in value:
            result[elem].append(key)
    return result


# data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
#
# for key, values in flip_dict(data).items():
#     print(f'{key}: {", ".join(values)}')
