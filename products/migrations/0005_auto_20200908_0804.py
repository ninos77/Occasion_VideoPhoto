# Generated by Django 3.1 on 2020-09-08 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_things_include'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
