# Generated by Django 2.2.7 on 2019-11-14 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20191114_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name_ru',
        ),
    ]
