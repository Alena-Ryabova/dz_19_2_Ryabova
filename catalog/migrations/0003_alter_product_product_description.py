# Generated by Django 4.2.10 on 2024-03-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
    ]
