# Generated by Django 5.0.6 on 2024-08-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='status',
            field=models.CharField(choices=[('aberta', 'Aberta'), ('fechada', 'Fechada')], default='aberta', max_length=20),
        ),
    ]