"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def compare_strings(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return 0
    if s1 == s2:
        return 1
    elif len(s1) > len(s2):
        return 2
    elif s2 == 'learn':
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(compare_strings(1, 'dkgodgko'))
    print(compare_strings("same", "same"))
    assert compare_strings(1, 'dkgodgko') == 0
    assert compare_strings("same", "same") == 1
    assert compare_strings("same_", "same") == 2
    assert compare_strings("same", "learn") == 3
    assert compare_strings("l", 'aknkjnjnjn') is None


if __name__ == "__main__":
    main()
