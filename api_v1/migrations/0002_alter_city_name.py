# Generated by Django 4.2.8 on 2024-02-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Город'),
        ),
    ]
