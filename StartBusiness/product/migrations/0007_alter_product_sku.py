# Generated by Django 4.1.12 on 2024-03-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='NKQ26892', max_length=8),
        ),
    ]
