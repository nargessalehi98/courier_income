# Generated by Django 4.0 on 2021-12-29 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salarychange',
            name='trip',
        ),
        migrations.DeleteModel(
            name='WeeklySalary',
        ),
        migrations.DeleteModel(
            name='SalaryChange',
        ),
    ]
