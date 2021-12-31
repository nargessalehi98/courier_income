from datetime import timedelta

import django
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.test import TestCase
from . import models

signal = django.dispatch.Signal()


class ModelTestCase(TestCase):

    @receiver(post_save, sender=models.Trip)
    def update_daily_salary_by_trip(self, sender, instance, **kwargs):
        daily_salary = models.DailySalary.objects.filter(
            courier=instance.courier, date=instance.date).first()
        if not daily_salary:
            daily_salary = models.DailySalary.objects.create(
                courier=instance.courier, date=instance.date)
            daily_salary.salary = instance.pure_income
            try:
                with transaction.atomic():
                    daily_salary.save()
            except Exception as e:
                instance.delete()
        else:
            daily_salary.salary += instance.pure_income
            try:
                with transaction.atomic():
                    daily_salary.save()
                    daily_salary.salary -= instance.pure_income
            except Exception as e:
                instance.delete()

    @transaction.atomic
    @receiver(post_save, sender=models.SalaryChange)
    def update_daily_salary_by_salary_change(self, sender, instance, **kwargs):
        daily_salary = models.DailySalary.objects.filter(
            courier=instance.trip.courier, date=instance.trip.date).first()
        daily_salary.salary += instance.income_raise - instance.income_reduce
        try:
            with transaction.atomic():
                daily_salary.save()
        except Exception as e:
            instance.delete()

    def test_update_daily_salary_by_trip(self):
        courier = models.Courier.objects.create(name='Ali Salehi')
        trip = models.Trip.objects.create(courier=courier,
                                          pure_income=100,
                                          date='2021-12-06')

        signal.connect(self.update_daily_salary_by_trip, sender=models.Trip)
        signal.send(sender=models.Trip, instance=trip)

        daily_salary = models.DailySalary.objects.get(courier=courier,
                                                      salary=100,
                                                      date='2021-12-06')
        self.assertEqual(daily_salary.salary, 100)

        trip = models.Trip.objects.create(courier=courier,
                                          pure_income=80,
                                          date='2021-12-06')
        signal.connect(self.update_daily_salary_by_trip, sender=models.Trip)
        signal.send(sender=models.Trip, instance=trip)
        daily_salary = models.DailySalary.objects.get(courier=courier,
                                                      date='2021-12-06')
        self.assertEqual(daily_salary.salary, 180)

    def test_update_daily_salary_by_salary_change(self):
        courier = models.Courier.objects.create(name='Ali Salehi')
        trip = models.Trip.objects.create(courier=courier,
                                          pure_income=100,
                                          date='2021-12-06')
        daily_salary = models.DailySalary.objects.create(courier=courier,
                                                         salary=100,
                                                         date='2021-12-06')
        salary_change = models.SalaryChange.objects.create(trip=trip,
                                                           income_raise=10,
                                                           income_reduce=0)

        signal.connect(self.update_daily_salary_by_salary_change, sender=models.SalaryChange)
        signal.send(sender=models.SalaryChange, instance=salary_change)

        daily_salary = models.DailySalary.objects.get(courier=courier,
                                                      date='2021-12-06')
        self.assertEqual(daily_salary.salary, 110)

