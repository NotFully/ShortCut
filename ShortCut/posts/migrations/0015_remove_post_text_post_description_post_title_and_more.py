# Generated by Django 4.1.7 on 2023-03-17 09:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='default description', help_text='Текст длиной до 500 символов', verbose_name='Описание вашего фильма'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default='default title', help_text='Текст длиной до 500 символов', verbose_name='Название фильма'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]