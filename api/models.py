from statistics import mode
from traceback import print_exception
from django.db import models

# Create your models here.

class Products(models.Model):
    name    = models.CharField("Name of product", max_length=75)
    price   = models.IntegerField("Price of product")

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name        = 'Товар'

    def __str__(self):
        return self.name