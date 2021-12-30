from django.urls import path
from . import views


urlpatterns = [
    path('weeksalary/', views.GetWeeklySalary.as_view(), name='week salary')
    ]