from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Courier(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Trip(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.CASCADE)
    pure_income = models.PositiveIntegerField(
        verbose_name=_("درآمد مربوط به سفر"))
    date = models.DateField()

    def __str__(self):
        return str(self.courier) + " " + str(self.date)


class SalaryChange(models.Model):
    trip = models.OneToOneField("Trip", on_delete=models.CASCADE, verbose_name=_("اطلاعات سفر"))
    income_raise = models.PositiveIntegerField(
        verbose_name=_("افزایش درآمد"), default=0)
    income_reduce = models.PositiveIntegerField(
        verbose_name=_("کسر از درآمد"), default=0)

    def __str__(self):
        return str(self.trip)


class DailySalary(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name=_("حقوق روز"), default=0)
    date = models.DateField(default=None, db_index=True)

    def __str__(self):
        return str(self.date)+" "+str(self.courier.name)


class WeeklySalary(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.CASCADE)
    saturday_date = models.DateField(default=None, db_index=True)
    salary = models.IntegerField(verbose_name=_("حقوق ماه"))

    def __str__(self):
        return str(self.saturday_date)


@receiver(post_save, sender=Trip)
def update_or_create_daily_salary(sender, instance, created, **kwargs):
    if created:
        daily_salary = DailySalary.objects.filter(
            courier=instance.courier, date=instance.date).first()
        if not daily_salary:
            daily_salary = DailySalary.objects.create(
                courier=instance.courier, date=instance.date)
            daily_salary.salary = instance.pure_income
            try:
                daily_salary.save()
            except Exception as e:
                instance.delete()
        else:
            daily_salary.salary += instance.pure_income
            try:
                daily_salary.save()
                daily_salary.salary -= instance.pure_income
            except Exception as e:
                instance.delete()


@receiver(post_save, sender=SalaryChange)
def update_or_create_daily_salary(sender, instance, created, **kwargs):
    if created:
        daily_salary = DailySalary.objects.filter(
            courier=instance.trip.courier, date=instance.trip.date).first()
        daily_salary.salary += instance.income_raise - instance.income_reduce
        daily_salary.save()



