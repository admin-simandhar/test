# Generated by Django 3.2.7 on 2021-11-25 08:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HeaderApp', '0003_alter_headerbanner_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerbanner',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 8, 0, 10, 566996, tzinfo=utc)),
        ),
    ]
