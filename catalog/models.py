import datetime
from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    version_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.TextField(verbose_name='описание')
    product_preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    product_cost = models.FloatField(verbose_name='цена')
    product_data_created = models.DateField(verbose_name='создан', default=datetime.date.today)
    product_last_data_change = models.DateField(verbose_name='последнее изменение', default=datetime.date.today)

    def __str__(self):
        return f"{self.product_name} * {self.product_cost}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Version(models.Model):
    version_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    version_is_active = models.BooleanField(default=False, verbose_name='активная версия')

    def __str__(self):
        return f"{self.version_name} v.{self.version_number}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('version_product',)
