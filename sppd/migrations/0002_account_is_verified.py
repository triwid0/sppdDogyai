# Generated by Django 4.2.5 on 2023-09-27 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sppd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
