# Generated by Django 5.1 on 2024-08-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('telefono', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
