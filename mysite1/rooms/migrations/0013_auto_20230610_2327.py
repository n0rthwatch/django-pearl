# Generated by Django 3.2.19 on 2023-06-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_auto_20230610_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость проживания'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
    ]
