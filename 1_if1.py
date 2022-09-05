"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def get_occupation_by_age(age: int):
    if 3 <= age < 7:
        return "kindergarden"
    if 7 <= age <= 17:
        return "school"
    if 18 <= age <=22:
        return "university"
    if 70 > age > 23:
        return "work"
    return "Provided nuber is incorrect or the occupation is not defined for your age"


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
        age = int(input("How old are you? (Full years) "))
        occupation = get_occupation_by_age(age)
        print(occupation)
    except ValueError:
        print("Please enter the integer number")


if __name__ == "__main__":
    main()
