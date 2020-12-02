"""Помогите Алле написать код алгоритма для выбора уроков, которые пройдут в
классе. Дано расписание предметов. Нужно составить расписание,
в соответствии с которым в классе можно будет провести как можно больше
уроков.
Формат ввода В первой строке задано число предметов. Оно не превосходит
1000. Далее для каждого предмета в отдельной строке записано время начала и
окончания урока. Обратите внимание на формат времени. Указываются только
значащие цифры.
Формат вывода Выведите информацию о всех уроках, которые нужно провести в
кабинете, в порядке возрастания времени начала.
Пример
Ввод
5
9 10
9.3 10.3
10 11
10.3 11.3
11 12

Вывод
3
9 10
10 11
11 12
"""


def schedule_maker():
    sort_list = sorted(global_list, key=lambda el: (el[1], el[0]))
    end = sort_list[0][1]
    result = []
    result += [sort_list[0]]
    for lesson in range(1, n):
        if sort_list[lesson][0] >= end or sort_list[lesson][0] == sort_list[lesson][1]:
            result += [sort_list[lesson]]
            end = sort_list[lesson][1]
    return result


if __name__ == "__main__":
    n = int(input())
    global_list = [input().split() for _ in range(n)]
    global_list = [list(map(float, sublist)) for sublist in global_list]
    schedule = schedule_maker()
    print(len(schedule))
    for row in schedule:
        print(*row)
