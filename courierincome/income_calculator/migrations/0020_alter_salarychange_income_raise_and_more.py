# Generated by Django 4.0 on 2021-12-29 14:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0019_alter_dailysalary_date_alter_trip_date_salarychange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarychange',
            name='income_raise',
            field=models.PositiveIntegerField(default=0, verbose_name='افزایش درآمد'),
        ),
        migrations.AlterField(
            model_name='salarychange',
            name='income_reduce',
            field=models.PositiveIntegerField(default=0, verbose_name='کسر از درآمد'),
        ),
        migrations.AlterField(
            model_name='salarychange',
            name='trip',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='income_calculator.trip', verbose_name='اطلاعات سفر'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
