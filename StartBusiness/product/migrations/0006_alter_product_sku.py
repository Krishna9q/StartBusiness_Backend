# Generated by Django 4.1.12 on 2024-03-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_sku_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='UDY65623', max_length=8),
        ),
    ]