from django.db import models

# Create your models here.
class Events(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    time_start = models.TimeField()
    city = models.CharField()

class ContryCity(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField