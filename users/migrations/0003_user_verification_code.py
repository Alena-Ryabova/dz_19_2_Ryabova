# Generated by Django 4.2.10 on 2024-04-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Код для верификации'),
        ),
    ]