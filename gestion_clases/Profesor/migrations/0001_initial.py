# Generated by Django 5.1.1 on 2024-12-20 01:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('clases_impartidas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clase.clase')),
            ],
        ),
    ]
