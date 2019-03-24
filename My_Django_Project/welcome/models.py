from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    telephone = models.CharField(unique=True, max_length=20)
    gender = models.CharField(choices=(('1', 'Муж'),('2', 'Жен')), max_length=10)
    date_birthday = models.DateField()