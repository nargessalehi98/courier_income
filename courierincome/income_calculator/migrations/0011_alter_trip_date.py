# Generated by Django 4.0 on 2021-12-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0010_alter_dailysalary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]