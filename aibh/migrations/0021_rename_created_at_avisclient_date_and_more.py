# Generated by Django 5.1 on 2024-08-31 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aibh', '0020_avisclient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avisclient',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='avisclient',
            name='product',
        ),
        migrations.RemoveField(
            model_name='avisclient',
            name='user',
        ),
        migrations.AddField(
            model_name='avisclient',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aibh.profile'),
            preserve_default=False,
        ),
    ]
