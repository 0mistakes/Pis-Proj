# Generated by Django 4.2.1 on 2023-05-14 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_apart_lcdors_apart_apartplan_apart_mebel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantityRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='apart',
            name='quantityRoom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.quantityroom'),
        ),
    ]
