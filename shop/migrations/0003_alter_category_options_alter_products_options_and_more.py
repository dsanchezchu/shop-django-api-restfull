# Generated by Django 5.1.4 on 2024-12-20 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_precio_products_price_products_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='descripcion',
            new_name='description',
        ),
    ]
