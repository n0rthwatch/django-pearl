import os
import uuid

from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


def upload_to(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f'{instance._meta.model_name}_{uuid.uuid4()}.{extension}'
    return os.path.join('rooms/', instance._meta.model_name, new_filename)


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=255, verbose_name='URL-адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Room(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Полное описание')
    short_description = models.TextField(max_length=100, verbose_name='Короткое описание')
    main_image = models.ImageField(upload_to=upload_to, verbose_name='Превью')
    services = models.ManyToManyField(Service, verbose_name='Услуги номера')
    slider_images = models.ManyToManyField('RoomImage', related_name='room_slider', verbose_name='Изображения слайдера',
                                           blank=True)
    is_available = models.BooleanField(default=True, verbose_name='Свободен')
    max_adults = models.IntegerField(default=2, verbose_name='Макс. взрослых')
    max_children = models.IntegerField(default=0, verbose_name='Макс. детей')
    slug = models.SlugField(unique=True, max_length=255, verbose_name='URL-адрес')
    check_in = models.DateField(verbose_name='Дата заезда', blank=True, null=True)
    check_out = models.DateField(verbose_name='Дата выезда', blank=True, null=True)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Забронировал')
    price = models.IntegerField(default=1, verbose_name='Стоимость за ночь')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Room.objects.filter(slug=self.slug).exists():
                self.slug = slugify(f'{self.title} {uuid.uuid4()}')
        super().save(*args, **kwargs)

    def is_booked(self):
        return self.check_in is not None and self.check_out is not None and self.check_out >= timezone.localdate()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class RoomImage(models.Model):
    image = models.ImageField(upload_to=upload_to, verbose_name='Ссылка')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images', null=True, blank=True,
                             verbose_name='Номер')

    def __str__(self):
        return f'{self.room} | {os.path.basename(self.image.name)}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="max-height:200px;"/>')
        else:
            return ''

    image_tag.short_description = 'Изображение'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения слайдера'


class Staff(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    position = models.CharField(verbose_name='Должность', max_length=50)
    picture = models.ImageField(verbose_name='Изображение', upload_to=upload_to)
    s_link_vk = models.CharField(verbose_name='Ссылка: ВКонтакте', max_length=255, default='#', blank=True)
    s_link_tg = models.CharField(verbose_name='Ссылка: Telegram', max_length=255, default='#', blank=True)
    s_link_yt = models.CharField(verbose_name='Ссылка: YouTube', max_length=255, default='#', blank=True)
    s_link_ph = models.CharField(verbose_name='Телефон', max_length=255, default='#', blank=True)
    main = models.BooleanField(verbose_name='Отображать на главной странице', default=False)

    def __str__(self):
        return f'{self.position}: {self.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Номер')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    date_booked = models.DateTimeField(verbose_name='Дата и время бронирования', auto_now_add=True)
    child_count = models.IntegerField(verbose_name='Кол-во детей', blank=True, null=True)
    adult_count = models.IntegerField(verbose_name='Кол-во взрослых')
    check_in = models.DateField(verbose_name='Дата заезда')
    check_out = models.DateField(verbose_name='Дата выезда')
    guest_name = models.CharField(max_length=255, verbose_name='Имя гостя', blank=True)
    guest_email = models.EmailField(max_length=255, verbose_name='Электронная почта', blank=True, null=True)
    guest_phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    price = models.IntegerField(verbose_name='Стоимость проживания', blank=True, null=True)

    def __str__(self):
        return f'{self.guest_name} забронировал номер "{self.room.title}" {self.date_booked.strftime("%d.%m.%Y")}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
