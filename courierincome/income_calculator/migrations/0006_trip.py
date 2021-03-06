# Generated by Django 4.0 on 2021-12-29 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income_calculator', '0005_delete_dailysalary_delete_test_delete_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pure_income', models.PositiveIntegerField(verbose_name='درآمد مربوط به سفر')),
                ('date', models.DateField(auto_now_add=True)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income_calculator.courier')),
            ],
        ),
    ]
