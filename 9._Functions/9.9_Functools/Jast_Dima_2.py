"""Просто Дима 🙃
Дима любит учиться, но не любит получать низкие оценки, больше всего его огорчают двойки.
Поэтому, когда Дима добирается до квартиры по лестнице, он поднимается исключительно на одну,
три или четыре ступени, но не на две.
Реализуйте функцию ways(), которая принимает один аргумент:
n — натуральное число (n ≤ 100)
Функция должна возвращать единственное число — количество способов, которыми можно забраться на n-ую ступень.
Путь начинается с первой ступени, подниматься можно исключительно на одну, три или четыре ступени.
Примечание 1. Рассмотрим первый тест. На пятую ступень можно забраться следующими четырьмя способами:
1→2→3→4→5
1→4→5
1→2→5
1→5
"""
from functools import lru_cache


@lru_cache
def ways(n: int):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)


print(ways(100))
