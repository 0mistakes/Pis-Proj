# Generated by Django 4.2.1 on 2023-05-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_apart_price_alter_apart_quantityroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='apart',
            name='city',
            field=models.TextField(default='city'),
        ),
    ]
