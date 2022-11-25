from django.db import models

# Create your models here.

class Products(models.Model):
    name    = models.CharField(max_length=75, verbose_name='Название букета')
    price   = models.IntegerField(verbose_name='Цена товара')
    rubric  = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Тип букета')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name        = 'Товар'

    def __str__(self):
        return self.name

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Тип букета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы букетов'
        verbose_name        = 'Тип букета'
        ordering            = ['name']