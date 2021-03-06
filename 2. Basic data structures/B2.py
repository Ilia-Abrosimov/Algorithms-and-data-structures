"""Алла получила задание, связанное с мониторингом работы различных
серверов. Требуется понять, сколько времени обрабатываются определённые
запросы на конкретных серверах. Эту информацию нужно хранить в матрице,
где номер столбца соответствуют идентификатору запроса, а номер строки —
идентификатору сервера. Алла перепутала строки и столбцы местами. С каждым
бывает. Помогите ей исправить баг. Есть матрица размера m × n. Нужно
написать функцию, которая её транспонирует. Транспонированная матрица
получается из исходной заменой строк на столбцы.

Формат ввода В первой строке задано число n — количество строк матрицы. Во
второй строке задано m — число столбцов, m и n не превосходят 1000. В
следующих n строках задана матрица. Числа в матрице не превосходят по модулю
1000.

Формат вывода Напечатайте транспонированную матрицу в том же формате,
который задан во входных данных. Каждая строка матрицы печатается на
отдельной строке, элементы разделяются пробелами.

Пример
Ввод
4
3
1 2 3
0 2 6
7 4 1
2 7 0

Вывод
1 0 7 2
2 2 4 7
3 6 1 0
"""


def transport_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append(input().split())
    result = []
    for i in range(column):
        boost = []
        for row in matrix:
            boost.append(row[i])
        result.append(boost)
    return result


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    new_matrix = transport_matrix(n, m)
    for string in new_matrix:
        print(*string)
