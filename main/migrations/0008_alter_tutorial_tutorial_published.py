# Generated by Django 4.1.5 on 2023-02-12 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 1, 57, 41, 652411), verbose_name='date published'),
        ),
    ]
