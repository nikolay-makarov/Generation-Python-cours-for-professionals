"""Функция count_iterable()
Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.
Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является конечным.
"""


def count_iterable(iterable):
    return sum(1 for _ in iterable)


data = tuple(range(432, 3845, 17))

print(count_iterable(data))
