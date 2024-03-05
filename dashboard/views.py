from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from models import *
from main.serializers import *


"""  CRUD Employee model  """
class GetAllEmployeeItems(ListAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer

class UpdateEmployeeItems(CreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer


class CreateEmployeeApiView(CreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer

class DeleteEmployeeApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer








# Create your views here.
