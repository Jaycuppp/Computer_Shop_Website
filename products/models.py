from django.db import models


# Create your models here.
class MainProducts(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.FloatField()
    Stock = models.IntegerField()
    Image_url = models.CharField(max_length=2083)

class NewProducts(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.FloatField()
    Stock = models.IntegerField()
    Image_url = models.CharField(max_length=2083)

class SpecialSale(models.Model):
    CouponCode = models.CharField(max_length=15)
    Description = models.CharField(max_length=50)
    Discount = models.FloatField()