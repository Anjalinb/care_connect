from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer

class AppointmentListCreateView(APIView):
    def get(self,request):
        qs=Appointment.objects.all()
        serializer_instance=AppointmentSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
