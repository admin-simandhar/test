# Generated by Django 3.2.7 on 2021-11-25 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeaderApp', '0007_alter_headerbanner_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerbanner',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
