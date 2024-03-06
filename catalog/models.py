from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.CharField(max_length=200, verbose_name='Описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Наименование - {self.product_name}; Описание - {self.product_description} '

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
