# Generated by Django 4.2.10 on 2024-03-31 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
    ]
