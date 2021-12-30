from django.contrib import admin
from . import models

admin.site.register(models.Courier)
admin.site.register(models.Trip)
admin.site.register(models.DailySalary)
admin.site.register(models.SalaryChange)
admin.site.register(models.WeeklySalary)
