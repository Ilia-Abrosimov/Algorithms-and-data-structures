"""Вася любит играть в игру Подпоследовательность. Даны 2 строки, и нужно
понять, является ли первая из них подпоследовательностью второй. Когда
строки достаточно длинные, иногда очень трудно получить ответ на этот
вопрос, просто посмотрев на них. Помогите Васе, напишите функцию, которая
решает эту задачу.
Формат ввода
В первой строке записана строка s.
Во второй — строка t.
Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000.
Формат вывода
Выведите True, если s является подпоследовательностью t, иначе — False.

Пример
Ввод
abc
ahbgdcu

Вывод
True
"""


def find_substr(substring, row):
    i = 0
    j = 0
    while i < len(substring) and j < len(row):
        if substring[i] != row[j]:
            j += 1
        else:
            i += 1
            j += 1
    if i == len(substring):
        return True
    if j == len(row):
        return False


if __name__ == "__main__":
    sub = input()
    string = input()
    print(find_substr(sub, string))
