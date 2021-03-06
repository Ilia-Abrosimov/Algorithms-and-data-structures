"""Тимофей спросил у студента Саши, умеет ли тот работать с числами в
двоичной системе счисления. Он ответил, что проходил это на одной из первых
лекций по информатике. Тимофей предложил Саше решить задачку. Два числа
записаны в двоичной системе счисления. Нужно вывести их сумму, также в
двоичной системе. Встроенную в язык программирования возможность сложения
двоичных чисел применять нельзя.
Решение должно работать за O(N) , где N - количество разрядов максимального
числа на входе.

Формат ввода Два числа в двоичной системе счисления, каждое на отдельной
строке. Длина каждого числа не превосходит 10000 цифр.

Формат вывода
Одно число в двоичной системе счисления.

Пример
Ввод
1010
1011

Вывод
10101
"""


def bin_to_dec(number):
    number_dec = int(number, 2)
    return number_dec


def dec_to_bin(number):
    if number == 0:
        return 0
    binary = bin(number)[2:]
    return binary


if __name__ == '__main__':
    first_number = input()
    second_number = input()
    addition = bin_to_dec(first_number) + bin_to_dec(second_number)
    print(dec_to_bin(addition))
