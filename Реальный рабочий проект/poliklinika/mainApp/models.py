from django.db import models
from django.contrib.auth.models import User

class WorkGrafic(models.Model): #График работы
    time_work = (
        ('1', 'Выходной'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
    )
    monday_start = models.CharField(max_length=20, verbose_name='Понедельник начало работы', choices=time_work, default='8')
    monday_stop = models.CharField(max_length=20, verbose_name='Понедельник конец работы', choices=time_work, default='17')
    tuesday_start = models.CharField(max_length=20, verbose_name='Вторник начало работы', choices=time_work, default='8')
    tuesday_stop = models.CharField(max_length=20, verbose_name='Вторник конец работы', choices=time_work, default='17')
    wednesday_start = models.CharField(max_length=20, verbose_name='Среда начало работы', choices=time_work, default='8')
    wednesday_stop = models.CharField(max_length=20, verbose_name='Среда конец работы', choices=time_work, default='17')
    thursday_start = models.CharField(max_length=20, verbose_name='Четверг начало работы', choices=time_work, default='8')
    thursday_stop = models.CharField(max_length=20, verbose_name='Четверг конец работы', choices=time_work, default='17')
    friday_start = models.CharField(max_length=20, verbose_name='Пятница начало работы', choices=time_work, default='8')
    friday_stop = models.CharField(max_length=20, verbose_name='Пятница конец работы', choices=time_work, default='17')
    saturday_start = models.CharField(max_length=20, verbose_name='Суббота начало работы', choices=time_work, default='8')
    saturday_stop = models.CharField(max_length=20, verbose_name='Суббота конец работы', choices=time_work, default='17')
    weekend_one_people_start = models.TextField(verbose_name='Отпуск начало (дд.мм.гг)', default='07.08.2019')
    weekend_one_people_stop = models.TextField(verbose_name='Отпуск конец (дд.мм.гг)', default='08.09.2019')
    weekend = models.TextField(verbose_name='Выходные дни (дд.мм)', default='8.03, 31.12, 23.02')
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

class Medicina(models.Model):
    name = models.CharField(max_length = 100, unique=True, null=False, verbose_name='Название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Медицина'
        verbose_name_plural = 'Медицины'
        ordering = ['name']

class Service(models.Model):
    name = models.CharField(max_length = 400, unique=True, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.CharField(max_length = 100, verbose_name='Ссылка на фото')
    text = models.TextField(verbose_name='Описание', null=True, blank=True)
    medicina = models.ForeignKey(Medicina, on_delete=models.SET_NULL, verbose_name='Услуги', related_name='services', null=True, blank=True)
    def __str__(self):
        return '('+self.medicina.__str__()+') '+self.name+' '+str(self.price)+' Руб'
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['medicina','name']

class Doctor(models.Model): #Доктор
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    father_name = models.CharField(max_length = 50, verbose_name='Отчество')
    photo = models.CharField(max_length = 200, null=True)
    medicina = models.ForeignKey(Medicina, on_delete=models.SET_NULL, verbose_name='Медицина', related_name='doctors', null=True, blank=True)
    major = models.CharField(max_length=100, verbose_name='Специальность', default='Терапевт')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, blank=True, verbose_name='График работы')
    def __str__(self):
        fio = '('+self.medicina.__str__()+') '+ self.surname+' '+self.name+' '+self.father_name
        return fio
    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['medicina','name']

class Patient(models.Model): #Пациент
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь',null=True, blank=True, related_name='patient')
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    gender = models.CharField(max_length=5, choices=(('муж','Муж'),('жен','Жен')), verbose_name='Пол')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')
    birthday = models.DateField()
    blood_group = models.CharField(max_length=5, verbose_name='Группа крови',choices=(('-1','-1'),('-2','-2'),('-3','-3'),('-4','-4'),('+1','+1'),('+2','+2'),('+3','+3'),('+4','+4')))
    def __str__(self):
        return self.surname+' '+self.name+' '+self.second_name 
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['surname']

class Analysis(models.Model): #Анализы
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    name = models.CharField(max_length=200, verbose_name='Наименование')
    laboratory = models.CharField(max_length=200, verbose_name='Лаборатория')
    result = models.TextField(verbose_name='Резултат')
    priority = models.TextField(verbose_name='Приоритет')
    out_patient_card = models.ForeignKey('OutPatientCard', on_delete=models.PROTECT, verbose_name='Амбулаторная карта', related_name='analyse')
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.PROTECT, blank=True, verbose_name='Врач', related_name='analyse')
    assistent = models.ForeignKey('Assistent', null=True, on_delete=models.PROTECT, blank=True, verbose_name='Лаборант', related_name='analyse')
    def __str__(self):
        return self.date.strftime('%d-%m-%Y')+ ' (' + self.out_patient_card.__str__()+')'
    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ['name']

class Assistent(models.Model): #Лаборант
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, blank=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+' '+self.second_name 
        return namea
    class Meta:
        verbose_name = 'Лаборант'
        verbose_name_plural = 'Лаборанты'
        ordering = ['surname']

class Zavhoz(models.Model): #Договор
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, blank=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+' '+self.second_name 
        return namea
    class Meta:
        verbose_name = 'Завхоз'
        verbose_name_plural = 'Завхозы'
        ordering = ['surname']

class Accountant(models.Model): #Бухгалтер
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, blank=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+' '+self.second_name 
        return namea
    class Meta:
        verbose_name = 'Бухгалтер'
        verbose_name_plural = 'Бухгалтеры'
        ordering = ['surname']

class Report(models.Model): #Отчет
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(verbose_name='Описание')
    zavhoz = models.ForeignKey(Zavhoz, on_delete=models.CASCADE, verbose_name='Завхоз', null=True, blank=True, related_name='zavhoz')
    medsister = models.ForeignKey(Accountant, on_delete=models.CASCADE, verbose_name='Бухгалтер', null=True, blank=True, related_name='accountant')
    def __str__(self):
        return self.date.strftime('%d-%m-%Y')+ ' ' + self.description[:30]+'...'
    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
        ordering = ['-date']
    

class Contract(models.Model): #Договор
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(verbose_name='Описание', default="Первичный приём")
    price = models.IntegerField(verbose_name='Стоимость')
    status = models.CharField(max_length=100, verbose_name='Статус')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, verbose_name='Пациент')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач', null=True, blank=True)
    assistant = models.ForeignKey(Assistent, on_delete=models.PROTECT, verbose_name='Лаборант', null=True, blank=True)
    cashier = models.ForeignKey("Cashier", on_delete=models.PROTECT, verbose_name='Кассир',blank=True, null=True)
    def __str__(self):
        return self.date.strftime("%d-%b-%Y")+' '+str(self.price)+' Руб'
    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'
        ordering = ['-date','price']

class OutPatientCard(models.Model): #Амбулаторная карта
    number_police = models.CharField(unique=True, max_length=30, verbose_name='Номер страх. полиса')
    passport = models.TextField(unique=True, verbose_name='Паспортные данные')
    company = models.CharField(max_length=50, verbose_name='Страх. компания')
    record = models.TextField(verbose_name='Записи')
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name='Пациент', related_name='out_patient_card')
    def __str__(self):
        return self.patient.__str__()
    class Meta:
        verbose_name = 'Амбулаторная карта'
        verbose_name_plural = 'Амбулаторные карты'
        ordering = ['patient']

class Cashier(models.Model): #Кассир
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, blank=True, verbose_name='График работы')
    def __str__(self):
        namea = self.surname+' '+self.name+' '+self.second_name
        return namea
    class Meta:
        verbose_name = 'Кассир'
        verbose_name_plural = 'Кассиры'
        ordering = ['surname']

class MedRequest(models.Model): #Заявка
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=50, verbose_name='Статус')
    assistent = models.ForeignKey(Assistent, on_delete=models.CASCADE, verbose_name='Лаборант', null=True, blank=True, related_name='med_request')
    medsister = models.ForeignKey('MedSister', on_delete=models.CASCADE, verbose_name='Медсестра', null=True, blank=True, related_name='med_request')
    zavhoz = models.ForeignKey(Zavhoz, on_delete=models.CASCADE, verbose_name='Завхоз', null=True, blank=True, related_name='med_request')
    def __str__(self):
        return self.date.strftime("%d-%b-%Y") + ' ('+self.status+')'
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']

class Reception(models.Model): #Прием
    date = models.DateField(verbose_name='Дата приема', null=True, blank=True)
    time = models.TimeField(verbose_name='Время приема', null=True, blank=True)
    status = models.CharField(max_length=50, verbose_name='Статус')
    registrator = models.ForeignKey("RegistryClerk",on_delete=models.PROTECT, verbose_name='Регистратор',blank=True, null=True)
    patient = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь',related_name='reception')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач', related_name='reception')
    def __str__(self):
        return self.doctor.__str__()+' '+ self.date.strftime("(%d-%b-%Y")+' '+self.time.strftime("%H:%M)")
    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'  
        ordering = ['-date','-time']

class RegistryClerk(models.Model): #Регистратура
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы',blank=True)
    def __str__(self):
        namea = self.surname+' '+self.name+' '+self.second_name
        return namea
    class Meta:
        verbose_name = 'Ригистратор'
        verbose_name_plural = 'Ригистраторы'
        ordering = ['surname']

class MedSister(models.Model): #Мед сестра
    name = models.CharField(max_length = 50, verbose_name='Имя')
    surname = models.CharField(max_length = 50, verbose_name='Фамилия')
    second_name = models.CharField(max_length = 50, verbose_name='Отчество')
    passport = models.TextField(unique=True,verbose_name='Паспортные данные')
    telephone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    work_plan = models.OneToOneField(WorkGrafic, on_delete=models.PROTECT, null=True, verbose_name='График работы', blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач', null=True, blank=True)
    def __str__(self):
        namea = self.surname+' '+self.name+' '+self.second_name
        return namea
    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'
        ordering = ['surname']

class Treatment(models.Model): #Посещение
    date = models.DateField(verbose_name='Дата')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач',related_name='treatment')
    patient_card = models.ForeignKey(OutPatientCard, on_delete=models.PROTECT, verbose_name='Амбулаторная карта', related_name='treatment')
    diagnose = models.TextField(verbose_name='Диагноз')
    medication = models.TextField(verbose_name='Лечение')
    def __str__(self):
        return self.date.strftime("%d-%b-%Y")+' ('+self.patient_card.__str__()+')'
    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
        ordering = ['-date']

class Draft(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', related_name='draft')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='draft')
    def __str__(self):
        return self.date.strftime("%d-%b-%Y")+' ( '+self.user.username+' )'
    class Meta:
        verbose_name = 'Черновик'
        verbose_name_plural = 'Черновики'
        ordering = ['-date','user']

class TimeReception(models.Model): #Информация о приеме
    list_status=(
        ("Free","Свободен"),
        ("Busy","Занят"),
    )
    status = models.CharField(max_length=5, choices=list_status, verbose_name='Статус', default='Free')
    time = models.TimeField(verbose_name='Время')
    work_day = models.DateField(verbose_name='День',null=True,blank=True)
    doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Врач', related_name='time_reception')
    def __str__(self):
        a = self.doctor.__str__()+' '+self.work_day.strftime("(%d-%b-%Y")+' '+self.time.strftime("%H:%M)")
        return a
    class Meta:
        verbose_name = 'Время приема'
        verbose_name_plural = 'Время приемов'
        ordering = ['doctor','-work_day','-time']
