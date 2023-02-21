# Generated by Django 4.1.5 on 2023-01-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couponcode', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=50)),
                ('discountpercentage', models.FloatField()),
            ],
        ),
    ]