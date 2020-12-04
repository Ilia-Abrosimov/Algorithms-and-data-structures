"""Гоша решил убрать из статистики дни, когда ничего в «Черепашеньке» не
заработал и не проиграл. Дан список заработанных очков. Нужно удалить из
него нули. Дополнительную память больше O(1) использовать нельзя.
Формат ввода
В первой строке - одно число n. Во второй - n целых чисел через пробел.
Формат вывода
Напечатайте очки за все дни, где выигрыш был отличен от нуля.

Пример
Ввод
8
-1 0 0 1 2 -1 -4 0

Вывод
-1 1 2 -1 -4
"""


def statistics(arr):
    print(' '.join(str(i) for i in arr if int(i) != 0))


if __name__ == '__main__':
    n = int(input())
    array = input().split()
    statistics(array)