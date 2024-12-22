# Generated by Django 5.1.4 on 2024-12-19 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='precio',
            new_name='price',
        ),
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productsAll', to='shop.category'),
        ),
    ]
