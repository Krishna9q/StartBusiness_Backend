# Generated by Django 4.1.12 on 2024-04-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_highlight', '0005_producthighlight_update_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='producthighlight',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]