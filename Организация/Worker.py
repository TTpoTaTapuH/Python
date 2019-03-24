class Worker:
    """Класс реализует двунаправленный динамический список
    Свoйства:
        _right - ссылка на правого сотрудника
        _left - ссылка на левого сотрудника
        _surname - фамилия сотрудника
        _major - должность сотрудника
    Реализованы функции для инициализации и возвращения
    правого и левого сотрудника, фамилии и должности"""

    def __init__(self, surname, major):
        """Инициализация сотрудника
        Параметры функции:
            - surname - фамилия сотрудника
            - major - должность сотрудника"""
        self._right = None
        self._left = None
        self._surname = surname
        self._major = major

    def __del__(self):
        """Деструктор
        Зануляет ссылки на другие объекты и свои поля
        Вызывается при удалении объекта"""
        self._right = None
        self._left = None
        self._surname = None
        self._major = None

    def Get_surname(self):
        """Возврашает фамилию сотрудника"""
        return self._surname

    def Get_major(self):
        """Возвращает должность сотрудника"""
        return self._major

    def Get_left(self):
        """Возвращет объект левого сотрудника"""
        return self._left

    def Get_right(self):
        """Возвращает объект правого сотрудника"""
        return self._right

    def Set_surname(self, name):
        """Инициализирует фамилия сотрудника
        name - фамилия сотрудника"""
        self._surname = name

    def Set_major(self, major):
        """Инициализирует должность сотрудника
        major - должность сотрудника"""
        self._major = major

    def Set_right(self, right):
        """Инициализирует ссылку на правого сотрудника
        right - объект Worker"""
        self._right = right

    def Set_left(self, left):
        """Инициализирует ссылку на левого сотрудника
        left - объект Worker"""
        self._left = left