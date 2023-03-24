"""
Без комментариев
Дан блок кода на языке Python. Напишите программу, которая удаляет все строки в данном коде,
которые содержат в себе только комментарии. Если в строке помимо комментария имеется что-то еще,
то такую строку учитывать не нужно.
Формат входных данных
На вход программе подается произвольное количество строк,
в совокупности представляющих блок кода на языке Python.
Формат выходных данных
Программа должна вывести введенный блок кода, предварительно удалив из него все строки,
которые содержат в себе только комментарии.
Примечание 1. Порядок вывода строк кода должен совпадать с порядком их ввода.
"""
import sys
for line in sys.stdin:
    if line.strip().startswith('#'):
        continue
    print(line.rstrip('\n'))
