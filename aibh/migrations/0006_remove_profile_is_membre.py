# Generated by Django 5.1 on 2024-08-28 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aibh', '0005_panier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_membre',
        ),
    ]
