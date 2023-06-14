# Generated by Django 4.2.1 on 2023-06-05 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Забронировал'),
        ),
        migrations.AddField(
            model_name='room',
            name='check_in',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата заезда'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='check_out',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата выезда'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateTimeField(verbose_name='Дата и время бронирования')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room', verbose_name='Номер')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]
