import os
from Section import Section

class Content:
    """
    Класс представляет из себя организацию
    В классе реализован однонаправленный статический список отделов
    Размер списка задаётся при заупске программы
    Методы вызываются из главного меню
    """

    def __init__(self, name, size):
        """Инициализация Организации
        Параметры функции:
            - name - название организации
            - size - количество отделов
        Свойства:
            _name - название организации
            _size - максимальное количество отделов
            _section - ссылка на список отделов
            _count - количество добавленных отделов"""
        self._name = name
        self._size = size
        self._section = Section("start")
        self._count = 0

    def __del__(self):
        """Деструктор
        Удаляет все отделы и зануляет инф. поля объекта"""
        self._name = None
        # Проход по всем отделам и их удаление
        while self._section != None:
            section = self._section
            self._section = self._section.Get_right()
            del section
        self._count = None
        self._size = None

    def Search_section(self):
        """Поиск отдела"""
        # Проверка на наличие отделов
        # Отделы существуют
        if self._count > 0:
            search = ""
            # Ввод названия отдела для поиска
            while not search.isalpha():
                print("Поиск отдела")
                search = input("Название отдела: ")
            find_section = self.Check_add_section(search, 2)
            # Проверка на наличие нахождения отдела
            if find_section != False:
                print("Отдел с таким названием найден!")
                print("\t"+find_section.Get_name())
            # Отдел не найден
            else:
                print("Отдел не найден!")
        # Список отделов пуст
        else:
            print("Отделы не добавлены!")

    def Search_worker(self):
        """Поиск сотрудника в отделе"""
        worker_section = ""
        # Ввод названия отдела в котором ищется сотрудник
        while not worker_section.isalpha():
            print("Поиск сотрудника в Отделе")
            worker_section = input("Название отдела: ")
        find_section = self.Check_add_section(worker_section, 2)
        # Отдел найден, вызывается функция поиска сотрудника внутри отдела
        if find_section != False:
            find_section.Search_worker()
        # Отдел не найден
        else:
            print("Отдел не найден!")


    def Save_to_file(self):
        """Сохранение в файл
        Вызывает метод сохранения в файл"""
        self._section.Get_right().Save_to_file(self._section.Get_right())

    def All_dell(self):
        """Удаление всех отделов и сотрудников"""
        section = self._section.Get_right()
        # Проход по всем отделам и их удаление
        while section != None:
            deleting_section = section
            section = section.Get_right()
            del deleting_section
        self._count = 0

    def Download_from_file(self):
        """Загрузка из файла"""
        self.All_dell()
        section = self._section
        # Обработчик исключений
        try:
            new_line = ""
            # Открытие файла data.txt на чтение
            with open("data.txt", "r") as f:
                # Проход по строкам файла
                while True:
                    new_line = f.readline()
                    new_line = new_line.strip(" \n")
                    # Если строка пуста, то завершается загрузка из файла
                    if len(new_line) == 0:
                        break
                    # Строка содержит метку отдела
                    if new_line == "Отдел:":
                        new_line = f.readline()
                        new_line = new_line.strip(" \n")
                        # проверка на наличие ошибок в названии отдела
                        if not new_line.isalpha():
                            print("Ошибка в названии отдела в файле!")
                            break
                        # Добавление отдела, если список не заполнен
                        if self._count < self._size:
                            new_section = Section(new_line)
                            section.Set_right(new_section)
                            section = new_section
                            self._count += 1
                        # Максимальное количество отделов заполнено
                        else:
                            print("Ошибка! Число отдедов превышено.")
                            break
                    # Строка содержит метку сотрудника
                    elif new_line == "Сотрудник:":
                        new_line = f.readline()
                        new_line = new_line.strip(" \n")
                        major_line = f.readline()
                        major_line = major_line.strip(" \n")
                        # Данные полей сотрудника имеют ошибки
                        if not new_line.isalpha() or not major_line.isalpha():
                            print("Ошибка в файле!В полях сотрудника должны быть только буквы!")
                            break
                        section.Download_add(new_line, major_line)
                    # Строка не равна ни одной метке
                    else:
                        print("Ошибка!")
        except FileNotFoundError:
            print("Файл не найден в данной директории!")

    def Delete_worker(self):
        """Метод удаление сотрудника из отдела"""
        worker_section = ""
        # Поиск отдела для удаления сотрудника
        while not worker_section.isalpha():
            print("Удаление сотрудника из Отдела")
            worker_section = input("Название отдела: ")
        find_section = self.Check_add_section(worker_section, 2)
        # Отдел найден
        if find_section != False:
            find_section.Delete_worker()
        # Отдел не найден
        else:
            print("Отдел не найден!")

    def Delete_section(self):
        """Метод удаления отдела"""
        os.system("clear")
        # Проверка на наличие отделов
        if self._count > 0:
            delete_name = ""
            # Ввод названия отдела
            while not delete_name.isalpha():
                print("Удаление отдела")
                delete_name = input("Название отдела: ")
            delete_section = self.Check_add_section(delete_name, 1)
            # Отдел найден
            if delete_section != False:
                remove_section = delete_section.Get_right()
                # Последний отдел в списке
                if remove_section == None:
                    delete_section.Set_right(None)
                    del remove_section
                    self._count -= 1
                # Не последний отдел
                else:
                    delete_section.Set_right(remove_section.Get_right())
                    del remove_section
                    self._count -= 1
            # Отдел не найден
            else:
                print("Отдел не найден!")

    def Add_section(self):
        """Метод добавления нового отдела"""
        os.system("clear")
        # Проверка на заполненность списка отделов
        if self._count < self._size:
            # Добавление первого отдела
            if self._count == 0:
                section_name = ""
                # Ввод названия отдела
                while not section_name.isalpha():
                    os.system("clear")
                    section_name = input("Введите название отдела: ")
                new_section = Section(section_name)
                self._section.Set_right(new_section)
                self._count += 1
            # Добавление 2-го и более отдела
            else:
                search = ""
                # Поиск отдела
                while not search.isalpha():
                    os.system("clear")
                    print("Поиск отдела до или после которого хотите добавить")
                    search = input("Название отдела: ")
                choice = 0
                # Выбор добавления до или после
                while choice != 1 and choice != 2:
                    # Защита от ввода букв
                    try:
                        print("1 - добавить до\n2 - добавить после")
                        choice = int(input("Ваш ответ: "))
                    except ValueError:
                        os.system("clear")
                        print("Ошибка! Введите число 1 или 2")
                finded_section = self.Check_add_section(search, choice)
                # Отдел найден
                if finded_section != False:
                    new_name = ""
                    # Ввод названия нового отдела
                    while not new_name.isalpha():
                        new_name = input("Введите название отдела: ")
                    new_section = Section(new_name)
                    new_section.Set_right(finded_section.Get_right())
                    finded_section.Set_right(new_section)
                    self._count += 1
                # Отдел не найден
                else:
                    print("Отдел не найден!")
        # Список заполнен
        else:
            print("Количество отделов заполнено")

    def Check_add_section(self, name, choice):
        """Метод проверки наличия отдела в списке
        В случае нахождения отдела возращает данный отдел или предыдущий отдел
        name - название отдела для поиска
        choice - выбор"""
        search_section = self._section.Get_right()
        # Добавление до
        if choice == 1:
            last_section = self._section
            # Проход по списку отделов
            while search_section != None:
                # Поиск нашел соответсвие
                # Возвращает предыдущий отдел
                if search_section.Get_name() == name:
                    return last_section
                last_section = last_section.Get_right()
                search_section = search_section.Get_right()
        # Добавление после
        if choice == 2:
            # Проход по списку отделов
            while search_section != None:
                # Поиск нашел соответсвие
                # Возвращает найденный отдел
                if search_section.Get_name() == name:
                    return search_section
                search_section = search_section.Get_right()
        # Отдел не найден
        # Возвращается False
        return False

    def Add_worker(self):
        """Метод добавления сотрудника"""
        worker_section = ""
        # Ввод названия отдела для поиска
        while not worker_section.isalpha():
            print("Добавление сотрудника в Отдел")
            worker_section = input("Название отдела: ")
        find_section = self.Check_add_section(worker_section, 2)
        # Отдел найден - добавления сотрудника
        if find_section != False:
            find_section.Add_worker()
        # Отдел не найден
        else:
            print("Отдел не найден!")

    def Show(self):
        """Метод вывода на консоль всей структуры данных"""
        print("\t\t\t\tОрганизация: "+self._name)
        # Проверка на наличие отделов
        if self._count > 0:
            show_section = self._section.Get_right()
            # Вывод на консоль всех отделов и сотрудников
            while show_section != None:
                print("\t\t\tОтдел: "+show_section.Get_name())
                show_section.Show_worker()
                show_section = show_section.Get_right()
        input("Для продолжения нажмите enter...")
        os.system("clear")