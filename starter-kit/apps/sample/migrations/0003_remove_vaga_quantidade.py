# Generated by Django 5.0.6 on 2024-08-22 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_vaga_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaga',
            name='quantidade',
        ),
    ]
