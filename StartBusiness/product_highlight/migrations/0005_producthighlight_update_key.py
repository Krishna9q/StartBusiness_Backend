# Generated by Django 4.1.12 on 2024-03-28 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_highlight', '0004_alter_producthighlight_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='producthighlight',
            name='update_key',
            field=models.BooleanField(default=True),
        ),
    ]