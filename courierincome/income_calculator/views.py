from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import models
from .serializer import CourierSerializer, ResponseSerializer


class GetWeeklySalary(GenericAPIView):

    def get(self, request):
        from_date = self.request.query_params.get("from_date")
        to_date = self.request.query_params.get("to_date")
        list_of_week_salaries = models.WeeklySalary.objects.filter(date__lte=to_date,
                                                                   date__gte=from_date).select_related('courier')
        week_salary = ResponseSerializer(list_of_week_salaries, many=True)


        return Response(
            data={
                "ok": True,
                "data": {
                    "list of week salary": week_salary.data
                },
                "status": status.HTTP_200_OK,
            },
            status=status.HTTP_200_OK,
        )
