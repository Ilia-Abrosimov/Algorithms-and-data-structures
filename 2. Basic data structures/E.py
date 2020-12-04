"""Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите
функцию, которая печатает все его дела. Известно, что дел у Васи не больше 5
000. Внимание: в этой задаче не нужно считывать входные данные. Нужно
написать только функцию, которая принимает на вход голову списка и печатает
его элементы. Ниже дано описание структуры, которая задаёт вершину списка. В
качестве ответа сдайте только код функции, которая печатает элементы списка.
Длина списка не превосходит 5000 элементов. Список не бывает пустым. Python:
Если вы пишете на Python, функция должна принимать на вход вершину node и
иметь сигнатуру

solution(node) -> None
Узел списка описывается следующим классом:

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node):
    print(node)
    tmp = node.next_item
    while tmp is not None:
        print(tmp)
        tmp = tmp.next_item


n5 = Node('5')
n4 = Node('4', n5)
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('1', n2)

solution(n1)
