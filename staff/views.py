from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from staff.models import Doctor


class DoctorListCreateView(APIView):

    def get(self,request):
        qs=Doctor.objects.all().values()
        doc_list=list(qs)
        return Response(data=doc_list)

    def post(self,request):
        form_data=request.data
        Doctor.objects.create(**form_data)
        return Response(data={"message":"created"})

class DoctorRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):
        qs=Doctor.objects.filter(id=pk).values()
        doc_list=list(qs)
        return Response(data=doc_list)

    def put(self,request,pk=None):
        form_data=request.data
        Doctor.objects.filter(id=pk).update(**form_data)
        return Response({"message":"updated"})

    def delete(self,request,pk=None):
        Doctor.objects.filter(id=pk).delete()
        return Response({"message":"deleted"})
    





