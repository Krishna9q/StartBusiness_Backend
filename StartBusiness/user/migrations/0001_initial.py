# Generated by Django 4.1.12 on 2024-03-16 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=225, unique=True)),
                ('user_mobile_number', models.CharField(max_length=225, unique=True)),
                ('user_name', models.CharField(max_length=225)),
                ('user_password', models.CharField(max_length=225)),
                ('is_verify', models.BooleanField(default=False)),
                ('user_role', models.CharField(default='customer', max_length=225)),
                ('otp_key', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
