# Generated by Django 4.0 on 2021-12-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0023_weeklysalary'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklysalary',
            name='salary',
            field=models.IntegerField(default=0, verbose_name='حقوق ماه'),
        ),
    ]
