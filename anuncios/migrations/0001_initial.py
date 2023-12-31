# Generated by Django 3.2.8 on 2021-10-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('texto', models.TextField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('inactivo', 'Inactivo'), ('activo', 'Activo')], default='inactivo', max_length=10)),
            ],
            options={
                'ordering': ('-fechaCreacion',),
            },
        ),
    ]
