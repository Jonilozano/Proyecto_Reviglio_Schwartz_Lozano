# Generated by Django 4.2 on 2023-08-14 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0004_delete_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
