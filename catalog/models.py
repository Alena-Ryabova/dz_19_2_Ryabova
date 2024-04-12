from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return f'{self.id} {self.category_name} '

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.CharField(max_length=200, verbose_name='Описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.id} {self.product_name} {self.purchase_price} {self.category} '

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='versions')
    version_num = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='наименование версии')
    version_indicator = models.BooleanField(default=True, verbose_name='признак версии')

    def __str__(self):
        return f'{self.id} {self.version_name} {self.version_num} '

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
