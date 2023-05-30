from django.db import models


class Auto(models.Model):
    marka = models.CharField('Марка',max_length=200)
    model = models.CharField('Модель',max_length=200)
    harakteristika = models.TextField('Характеристики')
    data = models.DateField('Дата публикации')

    def __str__(self):
        return self.marka
    class Metta:
        verbose_name='автомобили'
        verbose_name_plural='автомобили'
        ordering = ['data','title']