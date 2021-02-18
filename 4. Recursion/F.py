"""Евлампия не смогла разобраться с рекурсией! Напишите реализацию алгоритма
определения факториала числа с использованием цикла.
Формат ввода
На вход подается n - целое число в диапазоне от 0 до 22
Формат вывода
Нужно вывести число - факториал для n

Пример
Ввод
3
Вывод
2
"""


def fact(number):
    multiplication = 1
    i = 1
    while i <= number:
        multiplication = multiplication * i
        i += 1
    return multiplication


if __name__ == "__main__":
    n = int(input())
    print(fact(n))
