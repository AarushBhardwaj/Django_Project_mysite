# Generated by Django 4.1.5 on 2023-01-26 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 0, 34, 47, 577185), verbose_name='date published'),
        ),
    ]
