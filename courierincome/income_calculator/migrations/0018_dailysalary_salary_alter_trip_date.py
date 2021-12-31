# Generated by Django 4.0 on 2021-12-29 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0017_alter_trip_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailysalary',
            name='salary',
            field=models.IntegerField(default=0, verbose_name='حقوق روز'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 29, 12, 45, 18, 622343)),
        ),
    ]
