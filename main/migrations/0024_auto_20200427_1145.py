# Generated by Django 3.0.4 on 2020-04-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200427_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='grkey',
            field=models.TextField(default=5500649, unique=True),
        ),
    ]
