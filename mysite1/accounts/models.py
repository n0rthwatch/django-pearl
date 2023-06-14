from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    name = models.CharField(verbose_name='Имя', max_length=255, default='Безымянный')
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    username = models.CharField(verbose_name='Имя пользователя', max_length=255, blank=True, unique=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

