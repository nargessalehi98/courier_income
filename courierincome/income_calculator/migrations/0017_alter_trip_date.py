# Generated by Django 4.0 on 2021-12-29 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0016_alter_trip_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 29, 12, 44, 57, 855389)),
        ),
    ]