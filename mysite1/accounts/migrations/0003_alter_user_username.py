# Generated by Django 4.2.1 on 2023-06-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_name_alter_user_email_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя пользователя'),
        ),
    ]
