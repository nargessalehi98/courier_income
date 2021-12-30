from rest_framework import serializers
from . import models


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courier
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(read_only=True)

    class Meta:
        model = models.WeeklySalary
        fields = ['courier', 'salary', 'date']
