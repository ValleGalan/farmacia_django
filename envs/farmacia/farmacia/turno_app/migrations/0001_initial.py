# Generated by Django 4.1.2 on 2022-10-31 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmacia_app', '0002_alter_farmacia_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacion', models.CharField(max_length=255)),
                ('turno_date', models.DateField()),
                ('turno_time', models.TimeField()),
                ('farmacia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farmacia_app.farmacia')),
            ],
        ),
    ]
