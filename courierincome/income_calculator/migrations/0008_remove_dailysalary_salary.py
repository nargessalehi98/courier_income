# Generated by Django 4.0 on 2021-12-29 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0007_dailysalary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailysalary',
            name='salary',
        ),
    ]
