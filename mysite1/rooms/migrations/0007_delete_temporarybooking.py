# Generated by Django 4.2.1 on 2023-06-06 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_temporarybooking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TemporaryBooking',
        ),
    ]
