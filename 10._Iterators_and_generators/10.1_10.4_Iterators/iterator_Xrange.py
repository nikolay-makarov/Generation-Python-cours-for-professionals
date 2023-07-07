"""Итератор Xrange 🌶️
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
start — целое или вещественное число
end — целое или вещественное число
step — целое или вещественное число, по умолчанию имеет значение 1
Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end,
включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.
"""


class Xrange:
    def __init__(self, start: int | float, end: int | float, step: int | float = 1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self) -> 'Xrange':
        return self

    def __next__(self) -> int | float:
        self.start += self.step
        if (self.start >= self.end and self.step > 0) or (self.start <= self.end and self.step < 0):
            raise StopIteration
        return self.start


xrange = list(Xrange(3, 0, -0.5))
print(xrange)
