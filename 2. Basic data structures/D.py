"""Дана матрица. Нужно написать функцию, которая для элемента возвращает
всех его соседей. Соседним считается элемент, находящийся от текущего на
одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними
не считаются.
Формат ввода
В первой строке задано n - количество строк
матрицы. Во второй - m - количество столбцов. Числа m и n не превосходят
1000. В следующих n строках задана матрица. Элементы матрицы - целые числа,
по модулю не превосходящие 1000. В последних двух строках записаны
координаты элемента (индексация начинается с нуля), соседей которого нужно
найти.
Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
Пример
Ввод
4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
Вывод
7 7
"""


def find_neighbors(matr, string, pillar):
    neighbors = []
    if string - 1 > - 1:
        neighbors.append(int(matr[string - 1][pillar]))
    if string + 1 < n:
        neighbors.append(int(matr[string + 1][pillar]))
    if column - 1 > -1:
        neighbors.append(int(matr[string][pillar - 1]))
    if column + 1 < m:
        neighbors.append(int(matr[string][pillar + 1]))
    neighbors = sorted(neighbors)
    return neighbors


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    matrix = [input().split() for _ in range(n)]
    row = int(input())
    column = int(input())
    result = find_neighbors(matrix, row, column)
    print(*result)
