# Generated by Django 4.1.12 on 2024-03-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='AHU05694', max_length=8, unique=True),
        ),
    ]
