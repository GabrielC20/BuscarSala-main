# Generated by Django 5.1.3 on 2024-12-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0007_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('area', models.CharField(choices=[('saude', 'Área da Saúde'), ('pavilhao', 'Pavilhão')], max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
