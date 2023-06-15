from django.contrib.auth.models import User
from django.db import models


class Auto(models.Model):
    marka = models.CharField('Марка',max_length=200)
    model = models.CharField('Модель',max_length=200)
    harakteristika = models.TextField('Характеристики')
    data = models.DateField('Дата публикации')
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.marka

    def get_absolute_url(self):
        return f'/{self.id}'

    class Metta:
        verbose_name = 'автомобили'
        verbose_name_plural = 'автомобили'
        ordering = ['data']