# Generated by Django 4.0 on 2021-12-29 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0004_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DailySalary',
        ),
        migrations.DeleteModel(
            name='test',
        ),
        migrations.DeleteModel(
            name='Trip',
        ),
    ]
