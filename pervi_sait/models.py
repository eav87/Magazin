from django.db import models

class  BD_auto(models.Model):
    auto = models.CharField('Марка',max_length=200)
    auto_1 = models.CharField('Модель',max_length=200)
    auto_2 = models.TextField('Характеристики')
    auto_3 = models.DateField('Дата публикации')
    def __str__(self):
        return self.auto