# Generated by Django 3.0.4 on 2020-04-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200423_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Student',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='info',
            name='Teacher',
            field=models.BooleanField(default=1),
        ),
    ]
