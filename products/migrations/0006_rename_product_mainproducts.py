# Generated by Django 4.1.5 on 2023-01-26 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_newproducts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='MainProducts',
        ),
    ]
