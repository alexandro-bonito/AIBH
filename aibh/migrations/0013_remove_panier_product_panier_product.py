# Generated by Django 5.1 on 2024-08-30 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aibh', '0012_remove_panier_product_panier_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='product',
        ),
        migrations.AddField(
            model_name='panier',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='paniers', to='aibh.product'),
            preserve_default=False,
        ),
    ]
