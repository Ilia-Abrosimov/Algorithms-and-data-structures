"""Рита захотела оптимизировать алгоритм быстрой сортировки. Алгоритму не
должно требоваться O(n) дополнительной памяти. А у вас получится?
Формат ввода В первой строке на вход подается число n - длина массива. n не
превосходит 1000. Во второй строке через пробел записаны n чисел. Каждое из
чисел по модулю не превосходит 1000.
Формат вывода
Нужно вывести через пробел числа в отсортированном по возрастанию порядке.

Пример
Ввод
15
5 3 7 2 8 5 20 -19 -17 22 19 -16 6 11 -1

Вывод
19 -17 -16 -1 2 3 5 5 6 7 8 11 19 20 22
"""


def quicksort(arr, low, high):
    if low >= high:
        return
    i = low
    j = high
    pivot = arr[(low + high) // 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1
    quicksort(arr, low, j)
    quicksort(arr, i, high)
    return arr


if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    print(*quicksort(array, 0, len(array) - 1))
