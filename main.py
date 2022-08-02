import random

mainhelp = """
добавить — добавить задачу в список (название задачи запрашиваем у пользователя).
показать — напечатать все добавленные задачи.
рандом — добавить случайную задачу на сегодня.
помощь — напечатать справку по программе.
выйти — выйти из программы.
"""

random_tasks = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]
bye_phrases = ["До свидания!", "Увидимся;)", "Заходите ещё)", "Не прощаемся)", "Как, уже? Ну ок...", "Бай бай)"]


tasks = {

}

# Переменная для цикла while
run = True


# Функция добавления задачи в список задач
def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет
        # Создаем запись с ключом date
        tasks[date] = []
        tasks[date].append(task)
    print("Задача", task, "добавлена на", date)


# основной цикл программы
while run:
    command = input("Введите команду: ")
    if command == "помощь":
        print(mainhelp)
    elif command == "показать":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == "добавить":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "рандом":
        task = random.choice(random_tasks)
        add_todo("Сегодня", task)
    elif command == "выйти":
        print(random.choice(bye_phrases))
        break
    else:
        print("Неизвестная команда. Пожалуйста, используйте только зарезервированные слова.")
        print("Для просмотра доступных команд напечатайте 'помощь'.")
