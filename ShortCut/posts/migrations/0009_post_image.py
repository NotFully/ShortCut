# Generated by Django 2.2.16 on 2021-09-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210922_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите сюда вашу картинку', upload_to='posts/', verbose_name='Картинка'),
        ),
    ]