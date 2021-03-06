"""Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша взялся
изучать разные сортировки. На очереди - сортировка пузырьком.
Алгоритм следующий (сортируем по возрастанию):
На каждом шаге проходим по массиву поочередно сравниваем пары соседних
элементов. Если элемент на позиции i больше элемента на позиции i+1, меняем
их местами. После первой итерации самый большой элемент окажется в конце
массива.
Проходим по массиву, выполняя указанные действия n - 1 раз, или до тех пор,
пока на очередной итерации не окажется, что обмены больше не нужны, то есть
массив уже отсортирован.
Помогите Гоше написать код алгоритма.

Формат ввода
В первой строке на вход подается число n - длина массива. n не
превосходит 1000. Во второй строке через пробел записаны n чисел. Каждое из
чисел по модулю не превосходит 1000.
Формат вывода
Нужно вывести через пробел числа в отсортированном порядке.

Пример
Ввод
14
5 3 7 2 8 26 -12 -30 -10 27 13 -20 -30 18

Вывод
30 -30 -20 -12 -10 2 3 5 7 8 13 18 26 27
"""


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                buff = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = buff
    return arr


if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    print(*bubble_sort(array))
