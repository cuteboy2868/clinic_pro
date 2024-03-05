from django.urls import path
from .views import *

urlpatterns = [
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee/', CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployeeApiView.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployeeApiView.as_view()),



    path('get-patient-items', GetAllPatientItems.as_view)


]