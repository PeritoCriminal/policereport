# Generated by Django 5.2.4 on 2025-07-25 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationalunit',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
