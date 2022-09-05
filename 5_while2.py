"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {"Hey": "Hey!", "What are you doing?": "Programming", "How are you?": "All good"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    question_from_user = input(f"Ask me something. Available questions are {list(questions_and_answers.keys())}")
    while question_from_user in questions_and_answers.keys():
        print(questions_and_answers[question_from_user])
        question_from_user = input(f"Ask me something. Available questions are {questions_and_answers.keys()}")
    print("This question is not supported. Start over!")


if __name__ == "__main__":
    ask_user(questions_and_answers)
