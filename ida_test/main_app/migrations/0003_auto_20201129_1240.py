# Generated by Django 3.1.3 on 2020-11-29 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201129_1029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='UserFile',
        ),
    ]