from datetime import timedelta

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from . import models


@transaction.atomic
@receiver(post_save, sender=models.Trip)
def update_or_create_weekly_salary(sender, instance, created, **kwargs):
    if created:
        day = instance.date.weekday()
        if day == 5:
            weekly_salary = models.WeeklySalary.objects.filter(
                courier=instance.courier, date=instance.date).first()
        else:
            if day == 6:
                day = 1
            else:
                day = 7 - (5 - day)
            weekly_salary = models.WeeklySalary.objects.filter(
                courier=instance.courier, date=instance.date - timedelta(days=day)).first()
        if not weekly_salary:
            day = instance.date.weekday()
            if day == 5:
                weekly_salary = models.WeeklySalary.objects.create(
                    courier=instance.courier, date=instance.date)
            else:
                if day == 6:
                    day = 1
                else:
                    day = 7 - (5 - day)
                weekly_salary = models.WeeklySalary.objects.create(
                    courier=instance.courier, date=instance.date - timedelta(days=day))
            weekly_salary.salary = instance.pure_income
            try:
                with transaction.atomic():
                    weekly_salary.save()
            except Exception as e:
                instance.delete()
        else:
            weekly_salary.salary += instance.pure_income
            try:
                with transaction.atomic():
                    weekly_salary.save()
            except Exception as e:
                instance.delete()


@transaction.atomic
@receiver(post_save, sender=models.SalaryChange)
def update_or_create_weekly_salary(sender, instance, created, **kwargs):
    if created:
        day = instance.trip.date.weekday()
        if day == 5:
            weekly_salary = models.WeeklySalary.objects.filter(
                courier=instance.trip.courier, date=instance.trip.date).first()
        else:
            if day == 6:
                day = 1
            else:
                print(day)
                day = 7 - (5 - day)
                print(day)
            weekly_salary = models.WeeklySalary.objects.filter(
                courier=instance.trip.courier, date=instance.trip.date - timedelta(days=day)).first()
        weekly_salary.salary += instance.income_raise - instance.income_reduce
        if weekly_salary.salary < 0:
            weekly_salary.salary = 0
        try:
            with transaction.atomic():
                weekly_salary.save()
        except Exception as e:
            instance.delete()


@transaction.atomic
@receiver(post_save, sender=models.Trip)
def update_or_create_daily_salary(sender, instance, created, **kwargs):
    if created:
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
def update_or_create_daily_salary(sender, instance, created, **kwargs):
    if created:
        daily_salary = models.DailySalary.objects.filter(
            courier=instance.trip.courier, date=instance.trip.date).first()
        daily_salary.salary += instance.income_raise - instance.income_reduce
        if daily_salary.salary < 0:
            daily_salary.salary = 0
        try:
            with transaction.atomic():
                daily_salary.save()
        except Exception as e:
            instance.delete()
