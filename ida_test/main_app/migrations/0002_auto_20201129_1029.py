# Generated by Django 3.1.3 on 2020-11-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='image',
            field=models.ImageField(blank=True, upload_to='some_directory/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Название изображения'),
        ),
        migrations.AlterField(
            model_name='file',
            name='url_variable',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
    ]
