# Generated by Django 5.0.6 on 2024-06-05 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavilhao', models.CharField(choices=[(1, 'Pavilhão 01'), (2, 'Pavilhão 02')], max_length=1)),
                ('numero', models.IntegerField()),
                ('url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField()),
                ('turno', models.CharField(max_length=5)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.curso')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.sala')),
            ],
        ),
    ]
