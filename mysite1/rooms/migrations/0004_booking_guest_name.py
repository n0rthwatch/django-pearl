# Generated by Django 4.2.1 on 2023-06-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_booking_adult_count_booking_check_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guest_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя гостя'),
        ),
    ]
