"""
B. Любители конференций
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Список студентов представлен в таблице. В колонке «Вуз» записаны числа — id учебного заведения.
Тимофей предложил Саше выяснить, из каких вузов на конференцию пришло больше всего учащихся.
Ребята решили выяснить, из каких k вузов присутствует больше всего гостей.

Формат ввода
В первой строке записан список id вузов длиной не больше 10100. Каждое из чисел находится в диапазоне от 0 до 10000. Во второй строке записано одно число - параметр k.

Формат вывода
Выведите k чисел (id вуза) через пробел, отсортированные по убыванию, начиная от максимального количества гостей от вуза на конференции.

Пример
Ввод
1 2 3 1 2 3 4
3
Вывод
1 2 3
"""


# university_id = [1, 2, 3, 1, 2, 3, 4]
# k = 3


def count_students():
    members_from_university = {}
    for vuz_id in university_id:
        if vuz_id not in members_from_university:
            members_from_university[vuz_id] = 1
        else:
            members_from_university[vuz_id] += 1
    sort_university = list(members_from_university.items())
    sort_university.sort(key=lambda i: i[1], reverse=True)
    i = 0
    top_list = []
    for values in sort_university:
        i += 1
        if i > k:
            break
        top_list.append(values[0])
    return top_list


if __name__ == '__main__':
    university_id = input().split()
    k = int(input())
    result = count_students()
    print(' '.join(str(i) for i in result))
