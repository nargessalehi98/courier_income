from datetime import timedelta

from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
import django.dispatch


class Courier(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Trip(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.CASCADE)
    pure_income = models.PositiveIntegerField(
        verbose_name=_("درآمد مربوط به سفر"))
    date = models.DateField()

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            signal = django.dispatch.Signal()
            signal.send(sender=self.__class__)
        except Exception as e:
            print('Exception:', e)

    def __str__(self):
        return str(self.courier) + " " + str(self.date)


class SalaryChange(models.Model):
    trip = models.OneToOneField("Trip", on_delete=models.CASCADE, verbose_name=_("اطلاعات سفر"))
    income_raise = models.PositiveIntegerField(
        verbose_name=_("افزایش درآمد"), default=0)
    income_reduce = models.PositiveIntegerField(
        verbose_name=_("کسر از درآمد"), default=0)

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            signal = django.dispatch.Signal()
            signal.send(sender=self.__class__)
        except Exception as e:
            print('Exception:', e)


    def __str__(self):
        return str(self.trip)


class DailySalary(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name=_("حقوق روز"), default=0)
    date = models.DateField(default=None, db_index=True)

    def __str__(self):
        return str(self.date) + " " + str(self.courier.name)


class WeeklySalary(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name=_("حقوق هفته"), default=0)
    date = models.DateField(default=None, db_index=True)

    def __str__(self):
        return str(self.date) + " " + str(self.courier.name)


