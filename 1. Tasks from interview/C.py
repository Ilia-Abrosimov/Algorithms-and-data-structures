"""
Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма — это массив его цифр
слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход
подается количество цифр числа Х, списочная форма неотрицательного числа Х и
число K. Числа К и Х не превосходят 10000.
Нужно вернуть списочную форму числа X + K.

Формат ввода В первой строке - длина списочной формы числа X. На следующей
строке - сама списочная форма с цифрами записанными через пробел. В
последней строке записано число K.
Формат вывода
Выведите списочную форму числа X+K.

Пример
Ввод
4
1 2 0 0
34

Вывод
1 2 3 4
"""


def sum_list(number1, number2):
    number = int(''.join(number1))
    total = str(number + number2)
    return total


if __name__ == '__main__':
    long = int(input())
    x = input().split()
    k = int(input())
    result = sum_list(x, k)
    print(*result)
