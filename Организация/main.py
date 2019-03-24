from Content import Content
import os

def start(content):
    """Основое меню при запуске программы
    Отображает выбор функционала
    Вызывает соответствующий метод"""
    choice = 0
    os.system("clear")
    # Выбор действия
    # 11 - выход из программы
    while choice != 11:
        try:
            print("1 - Добавить отдел \n2 - Добавить сотрудников \n3 - Удалить отдел \n4 - Удалить сотрудника "
                  "\n5 - Поиск отдела \n6 - Поиск сотрудника \n7 - Вывод на экран "
                "\n8 - Сохранить в файл \n9 - Загрузить из файла\n10 - Удаление всей структуры \n11 - Выход из программы")
            choice = int(input("Ваш ответ: "))
            if choice == 1:
                os.system("clear")
                content.Add_section()
            elif choice == 2:
                os.system("clear")
                content.Add_worker()
            elif choice == 3:
                os.system("clear")
                content.Delete_section()
            elif choice == 4:
                os.system("clear")
                content.Delete_worker()
            elif choice == 5:
                os.system("clear")
                content.Search_section()
            elif choice == 6:
                os.system("clear")
                content.Search_worker()
            elif choice == 7:
                os.system("clear")
                content.Show()
            elif choice == 8:
                os.system("clear")
                content.Save_to_file()
            elif choice == 9:
                os.system("clear")
                content.Download_from_file()
            elif choice == 10:
                os.system("clear")
                content.All_dell()
            elif choice == 11:
                del content
                break
            else:
                print("нет такого выбора")
        except ValueError:
            os.system("clear")
            print("Некорректное значение!")

if __name__ == '__main__':
    name = ""
    size = 0
    # Ввод названия организаации
    while not name.isalpha():
        os.system("clear")
        name = input("Название организации: ")
    # Ввод количества отделов
    while size <= 0 or size > 1000:
        try:
            size = int(input("Введите количество отделов: "))
        except ValueError:
            print("Введите число от 0 до 1000")
    content = Content(name, size)
    start(content)