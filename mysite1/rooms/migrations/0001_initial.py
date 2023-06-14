# Generated by Django 4.2.1 on 2023-06-03 20:29

from django.db import migrations, models
import django.db.models.deletion
import rooms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Полное описание')),
                ('short_description', models.TextField(max_length=100, verbose_name='Короткое описание')),
                ('main_image', models.ImageField(upload_to=rooms.models.upload_to, verbose_name='Превью')),
                ('is_available', models.BooleanField(default=True, verbose_name='Свободен')),
                ('max_adults', models.IntegerField(default=2, verbose_name='Макс. взрослых')),
                ('max_children', models.IntegerField(default=0, verbose_name='Макс. детей')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL-адрес')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=rooms.models.upload_to)),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('picture', models.ImageField(upload_to=rooms.models.upload_to, verbose_name='Изображение')),
                ('s_link_vk', models.CharField(blank=True, default='#', max_length=255, verbose_name='Ссылка: ВКонтакте')),
                ('s_link_tg', models.CharField(blank=True, default='#', max_length=255, verbose_name='Ссылка: Telegram')),
                ('s_link_yt', models.CharField(blank=True, default='#', max_length=255, verbose_name='Ссылка: YouTube')),
                ('s_link_ph', models.CharField(blank=True, default='#', max_length=255, verbose_name='Телефон')),
                ('main', models.BooleanField(default=False, verbose_name='Отображать на главной странице')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=rooms.models.upload_to, verbose_name='Ссылка')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.room', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения слайдера',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='services',
            field=models.ManyToManyField(to='rooms.service', verbose_name='Услуги номера'),
        ),
        migrations.AddField(
            model_name='room',
            name='slider_images',
            field=models.ManyToManyField(blank=True, related_name='room_slider', to='rooms.roomimage', verbose_name='Изображения слайдера'),
        ),
    ]
