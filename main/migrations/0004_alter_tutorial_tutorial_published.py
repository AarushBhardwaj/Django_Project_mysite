# Generated by Django 4.1.5 on 2023-01-26 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 20, 28, 1, 13956), verbose_name='date published'),
        ),
    ]