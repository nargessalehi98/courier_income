# Generated by Django 4.0 on 2021-12-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0020_alter_salarychange_income_raise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='date',
            field=models.DateField(),
        ),
    ]
