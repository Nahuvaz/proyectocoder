# Generated by Django 4.2.7 on 2023-12-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderapp', '0003_albumespendiente_alter_artista_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumesescuchados',
            name='album',
        ),
        migrations.AddField(
            model_name='albumesescuchados',
            name='nombre',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
    ]