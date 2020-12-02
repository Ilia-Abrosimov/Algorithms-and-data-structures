"""На вход подается строка. Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.
Формат ввода
Одна строка, состоящая из латинских букв. Длина строки не превосходит 10000.

Формат вывода
Одно число - ответ на задачу.

Пример
Ввод
abcabcbb

Вывод
3
"""


def max_list_len(string):
    max_count = 0
    substring = []
    for i in range(len(string)):
        if string[i] in substring:
            k = substring.index(string[i])
            substring = substring[k + 1:]
        substring.append(string[i])
        if len(substring) > max_count:
            max_count = len(substring)
    return max_count


if __name__ == '__main__':
    row = input()
    print(max_list_len(row))
