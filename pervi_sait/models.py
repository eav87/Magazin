from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# класс автомобилей
class Auto(models.Model):
    marka = models.CharField('Марка',max_length=200)
    model = models.CharField('Модель',max_length=200)
    harakteristika = models.TextField('Характеристики',blank=True)
    create_date = models.DateTimeField('Дата публикации', default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True)
    foto = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False)


    def __str__(self):
        return self.marka

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'автомобили'
        verbose_name_plural = 'автомобили'
        ordering = ['create_date']


# Класс автозапчастей
class Part(models.Model):
    name = models.CharField(max_length=50)
    opisanie = models.TextField('Описание товара',blank=True)
    price = models.DecimalField('Цена',max_digits=10,decimal_places=2,null=False)
    foto = models.ImageField('Фото',upload_to='%Y/%m/%d', blank=True)
    date = models.DateTimeField('Дата',default=timezone.now)

    def __str__(self):
        return self.name


# класс запись на то
class ZapisTo(models.Model):
    name = models.CharField(max_length=50)
    name_auto = models.CharField(max_length=200)
    nomer_auto = models.CharField(max_length=10)
    date = models.DateTimeField('Выбрать дату и время для записи')
    create_date = models.DateTimeField('Дата',default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.name



# элемент корзины
class CartItem(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    part = models.OneToOneField(Part,on_delete=models.PROTECT)
    count = models.IntegerField('количество')
    date = models.DateTimeField('дата',default=timezone.now)


class Wheels(models.Model):
    name = models.CharField(max_length=200)
    opisanie = models.TextField('Описание колес',blank=True)
    date  = models.DateTimeField('Дата',default=timezone.now)
    part = models.ManyToManyField(Part)


