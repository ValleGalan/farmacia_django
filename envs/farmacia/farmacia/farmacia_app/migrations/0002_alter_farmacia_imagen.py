# Generated by Django 4.1.2 on 2022-10-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacia',
            name='imagen',
            field=models.ImageField(upload_to='farmacia'),
        ),
    ]
