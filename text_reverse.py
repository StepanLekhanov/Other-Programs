""" Программа для вывода текста наоборот """

from typing import NoReturn


def _text_reverse(lang: str) -> NoReturn:
    """ Изменение текста """

    if lang.lower() == "ru":
        name: str = input("Введите свое имя: ")
        print(f'Привет, {name}. Добро пожаловать в программу "Текст наоборот".')
        question: str = input("Желаете ознакомиться с инструкцией по использованию программы(да/нет)?: ")

        if question.lower() == "да":
            print("Введите текст и программа выведет его наоборот.")

        text_input: str = input("Введите текст: ")
        _output_text(text_input, lang, name)

    elif lang.lower() == "en":
        name: str = input("Enter your name: ")
        print(f'Hi, {name}. Welcome to the program "Text in reverse".')
        question: str = input("Would you like to read the instructions for using the program(yes/no)?: ")

        if question.lower() == "yes":
            print("Enter the text and the program will output it the other way around.")

        text_input: str = input("Enter the text: ")
        _output_text(text_input, lang, name)


def _output_text(text: str, lang: str, name: str) -> NoReturn:
    """ Вывод текста """

    if lang.lower() == "ru":
        print(f'{name}, Ваш изначально введенный текст: {text}')
        print(f'{name}, Ваш текст наоборот: {text[::-1]}')

    elif lang.lower() == "en":
        print(f'{name}, Your originally entered text: {text}')
        print(f'{name}, Your text is the opposite: {text[::-1]}')


def main() -> NoReturn:
    language: str = input("Select language(ru/en): ")
    _text_reverse(lang=language)


if __name__ == '__main__':
    main()
