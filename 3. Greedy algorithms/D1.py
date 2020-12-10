"""
Реализуйте код алгоритма заполнения рюкзака, рассмотренного в лекции:
Взять наиболее ценный предмет, который поместится в рюкзак. Выбрать
следующий по стоимости товар с учётом того, что для него осталось место в
рюкзаке. Формат ввода В первой строке записано целое число с в диапазоне от
0 до 1000 — вместимость рюкзака. Во второй — число n — количество предметов.
Оно не больше 10000.
В следующих n строках записано по 2 числа, разделенные пробелом: стоимость
предмета и его вес. Оба числа не превосходят 1000
Формат вывода Нужно в строке вывести в отсортированном порядке номера
предметов, которые будут выбраны. Номер предмета - это порядковый номер его
появления во входных данных. (Индексация начинается с нуля)

Пример
Ввод
36
4
25 50
30 40
10 80
2 3

Вывод
3
"""


class Thing:
    def __init__(self, price, weight, index):
        self.price = price
        self.weight = weight
        self.index = index


def collect_backpack(capacity, global_list):
    global_list.sort(key=lambda thing: (-thing.price, thing.weight,
                                        thing.index))
    result = []
    for item in global_list:
        if item.weight <= capacity:
            capacity -= item.weight
            result.append(item.index)
    result.sort()
    return result


if __name__ == "__main__":
    size = int(input())
    n = int(input())
    array = []
    for i in range(n):
        price, weight = input().split()
        array.append(Thing(int(price), int(weight), i))
    indexs = collect_backpack(size, array)
    print(*indexs)
