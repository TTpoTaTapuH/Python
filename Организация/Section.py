from Worker import Worker

class Section:
    """Класс представляет из себя список отделов
    Имеет такие поля как:
    _name - Название отдела
    _worker - Ссылка на список сотрудников
    __right - Ссылка на следующий отдел
    _download_worker - Ссылка на последнего добавленного сотрудника при загрузке данных из файла
    """

    def __init__(self, name):
        """Инициализация названия отдела
        Ссылки на сотрудников
        Ссылки на следующий объект отдела
        Ссылки для добавления сотрудника при загрузке из файла"""
        self._name = name
        self._worker = None
        self.__right = None
        self._download_worker = None

    def __del__(self):
        """Удаление объекта
        Зануляет ссылку на след объект отдела, название отдела, ссылки
        Через цикл while вызывает деструкторы сотрудников, т.е. удаляет"""
        self._name = None
        self._right = None
        self._download_worker = None
        # Удаление сотрудников из отдела
        while self._worker != None:
            worker = self._worker
            self._worker = self._worker.Get_right()
            del worker

    def Set_right(self, section_right):
        """Установка ссылки на следующий объект для отдела"""
        self.__right = section_right

    def Get_right(self):
        """Возращает ссылку на следующий объект"""
        return self.__right

    def Get_name(self):
        """Возвращает название отдела"""
        return self._name

    def Download_add(self, name, major):
        """Метод добавления сотрудников при загрузке из файла
        Принимает 2 аргумента для создания объекта сотрудника:
        name - фамилия сотрудника
        major - должность сотрудника"""
        new_worker = Worker(name, major)

        # Добавление первого сотрудника
        if self._worker == None:
            self._worker = new_worker
            self._download_worker = self._worker

        # Добавление 2-го и более сотрудника
        else:
            self._download_worker.Set_right(new_worker)
            new_worker.Set_left(self._download_worker)
            self._download_worker = new_worker

    def Save_to_file(self, my_self):
        """Сохранение структуры данных в файл
        Параметры функции:
        my_self - объект отдела
        С этого объекта начинается сохранение в файл"""

        # Открываем файл data.txt
        with open("data.txt", "w") as f:
            loop_section = my_self

            # Выполняем пока не наступит конец списка
            while loop_section != None:
                f.write("Отдел:\n")
                f.write(loop_section.Get_name()+"\n")

                # Проверка на наличие сотрудников в отделе
                if loop_section._worker != None:
                    loop_worker = loop_section._worker

                    # Сохраняем в файл всех сотрудников
                    while loop_worker != None:
                        f.write("Сотрудник:\n")
                        f.write(loop_worker.Get_surname()+"\n")
                        f.write(loop_worker.Get_major()+"\n")
                        loop_worker = loop_worker.Get_right()
                loop_section = loop_section.Get_right()

    def init_worker(self):
        """Метод ввода информационных полей сотрудника
        Возвращает объект нового сотрудника"""
        name = ""
        major = ""

        # Вводим пока не будут только буквы
        while not name.isalpha():
            name = input("Фамилия сотрудника: ")

        # Вводим пока не будут только буквы
        while not major.isalpha():
            major = input("Должность сотрудника: ")
        return Worker(name, major)

    def Show_worker(self):
        """Метод отображения структуры данных на консоль"""
        print("\t\tСотрудники: ")

        # Проверка на наличие сотрудников
        if self._worker != None:
            workers = self._worker

            # Выводим на консоль всех сотрудников
            while workers != None:
                print("  Фамилия: " + workers.Get_surname())
                print("Должность: " + workers.Get_major())
                workers = workers.Get_right()

        # Сотрудников нет
        else:
            print("Пусто")

    def Search_worker_and_return(self):
        choice = 0

        # Выбор порядка поиска
        while choice <= 0 or choice > 2:
            try:
                print("1 - Поиск сотрудника в прямом порядке\n2 - Поиск сотрудника в обратном порядке")
                choice = int(input("Ваш ответ: "))
            except ValueError:
                print("Ошибка! Введите число от 1 до 2!")
        search_name_worker = ""

        # Ввод фамилии сотрудника
        while not search_name_worker.isalpha():
            print("Поиск сотрудника")
            search_name_worker = input("Фамилия сотрудника для поиска: ")
        search_worker = self._worker

        # Поиск в слева направо
        if choice == 1:
            while search_worker != None:
                if search_worker.Get_surname() == search_name_worker:
                    return search_worker
                search_worker = search_worker.Get_right()
            return None

        # Поиск справа налево
        else:

            # Доходим до правого конца
            while search_worker.Get_right() != None:
                search_worker = search_worker.Get_right()

            # Поиск справа налево
            while search_worker != None:
                if search_worker.Get_surname() == search_name_worker:
                    return search_worker
                search_worker = search_worker.Get_left()
            return None

    def Add_worker(self):
        """Добавление сотрудника
        Добавление осуществляется с поиском
        слева направо или справа налево сотрудника
        Возможно добавить до или после заданного сотрудника"""

        # Проверка на наличие сотрудников
        # Добавляем первого сотрудника
        if self._worker == None:
            new_worker = self.init_worker()
            self._worker = new_worker

        # Добавляем 2-й и более сотрудника
        else:
            search_worker = self.Search_worker_and_return()
            # Сотрудник не найден
            if search_worker == None:
                print("Сотрудник не найден!")

            # Сотрудник найден
            else:
                ask = 0

                # Выбор добавления до или после
                while ask <= 0 or ask > 2:
                    try:
                        ask = int(input("1 - Добавить до заданного сотрудника\n2 - Добавить после заданного сотрудника\nТвой ответ: "))
                    except ValueError:
                        print("Введите число от 1 до 2")

                # Инициализация сотрудника
                new_worker = self.init_worker()

                # Добавление сотрудника до заданного сотрудника
                if ask == 1:
                    new_worker.Set_right(search_worker)

                    # Если крайний левый в списке сотрудник
                    if search_worker.Get_left() == None:
                        search_worker.Set_left(new_worker)
                        self._worker = new_worker

                    # Не крайний в списке сотрудник
                    else:
                        new_worker.Set_left(search_worker.Get_left())
                        search_worker.Get_left().Set_right(new_worker)
                        search_worker.Set_left(new_worker)

                # Добавление сотрудника после заданного сотрудника
                else:
                    new_worker.Set_left(search_worker)

                    # Самый краний правый в списке сотрудник
                    if search_worker.Get_right() == None:
                        search_worker.Set_right(new_worker)

                    # Не крайний сотрудник
                    else:
                        new_worker.Set_right(search_worker.Get_right())
                        search_worker.Get_right().Set_left(new_worker)
                        search_worker.Set_right(new_worker)

    def Delete_worker(self):
        """Метод удаления сотрудника"""

        # Проверка на наличие сотрудников
        # Сотрудников нет
        if self._worker == None:
            print("Сотрудников нет!")

        # Сотрудники имеются в отделе
        else:
            search_worker = self.Search_worker_and_return()

            # Поиск не нашёл сотрудника
            if search_worker == None:
                print("Сотрудник не найден!")

            # Сотрудник найден
            else:

                # Если сотрудник самый первый
                if search_worker.Get_left() == None:
                    self._worker = search_worker.Get_right()

                    # Не последний сотрудник
                    if search_worker.Get_right() != None:
                        search_worker.Get_right().Set_left(None)
                    del search_worker

                # Если сотрудник самый последний
                elif search_worker.Get_right() == None:
                    search_worker.Get_left().Set_right(search_worker.Get_right())
                    del search_worker

                # Сотрудник в середине - имеет левого и правого соседа
                else:
                    search_worker.Get_left().Set_right(search_worker.Get_right())
                    search_worker.Get_right().Set_left(search_worker.Get_left())
                    del search_worker

    def Search_worker(self):
        """Метод поиска сотрудника
        В случае нахождения сотрудника выводит на консоль информацию о сотруднике
        Если поиск не находит сотрудника - соответствующее сообщение"""

        # Проверка на наличие сотрудников в отделе
        # Сотрудников нет
        if self._worker == None:
            print("Сотрудников нет!")

        #Сотрудники имеются в отделе
        else:
            search_worker = self.Search_worker_and_return()

            # Сотрудник не найден
            if search_worker == None:
                print("Сотрудник не найден!")

            # Сотрудник найден
            else:
                print("Сотрудник найден!")
                print("Фамилия: " + search_worker.Get_surname())
                print("Должность: " + search_worker.Get_major())

