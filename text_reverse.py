language = input("Select language(ru/en): ")

if language == "ru":
    name_ru = input("Введите свое имя: ")
    print(f'Привет, {name_ru}. Добро пожаловать в программу "Текст наоборот".')
    question_ru = input("Желаете ознакомиться с инструкцией по использованию программы(да/нет)?: ")

    if question_ru == "да":
        print("Введите текст и программа выведет его наоборот.")
        text_input = input("Введите текст: ")
        print(f'{name_ru}, Ваш изначально введенный текст: {text_input}')
        print(f'{name_ru}, Ваш текст наоборот: {text_input[::-1]}')

    elif question_ru == "нет":
        text_input = input("Введите текст: ")
        print(f'{name_ru}, Ваш изначально введенный текст: {text_input}')
        print(f'{name_ru}, Ваш текст наоборот: {text_input[::-1]}')

elif language == "en":
    name_en = input("Enter your name: ")
    print(f'Hi, {name_en}. Welcome to the program "Text in reverse".')
    question_en = input("Would you like to read the instructions for using the program(yes/no)?: ")

    if question_en == "yes":
        print("Enter the text and the program will output it the other way around.")
        text_input = input("Enter the text: ")
        print(f'{name_en}, Your originally entered text: {text_input}')
        print(f'{name_en}, Your text is the opposite: {text_input[::-1]}')

    elif question_en == "no":
        text_input = input("Enter the text: ")
        print(f'{name_en}, Your originally entered text: {text_input}')
        print(f'{name_en}, Your text is the opposite: {text_input[::-1]}')