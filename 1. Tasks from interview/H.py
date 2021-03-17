"""А теперь помогите Васе понять, будет ли фраза палиндромом. Учитываются
только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N - длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут
быть только латинские.

Формат вывода
Выведите True, если фраза является палиндромом и False, если не является.

Пример
Ввод
A man, a plan, a canal: Panama

Вывод
True
"""


def search_palindrome(word):
    array = []
    for symbol in word.lower():
        if symbol.isalpha():
            array.append(symbol)
    if array != array[::-1]:
        return False
    return True


if __name__ == '__main__':
    phrase = input()
    print(search_palindrome(phrase))
