# Generated by Django 4.1.12 on 2024-04-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_description_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_use',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='OAQ14504', max_length=8),
        ),
    ]
