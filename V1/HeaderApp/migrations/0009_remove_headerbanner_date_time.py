# Generated by Django 3.2.7 on 2021-11-26 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HeaderApp', '0008_alter_headerbanner_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerbanner',
            name='date_time',
        ),
    ]