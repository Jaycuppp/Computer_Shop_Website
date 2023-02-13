from django.db import models


# Create your models here.

class Store(models.Model):
    Street = models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Opens = models.TimeField()
    Closes = models.TimeField()
