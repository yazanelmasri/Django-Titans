# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointment/create/', views.create_appointment, name='create_appointment'),
    path('appointment/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointment/<int:pk>/edit/', views.edit_appointment, name='edit_appointment'),

    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/create/', views.create_vehicle, name='create_vehicle'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:pk>/edit/', views.edit_vehicle, name='edit_vehicle'),

    path('services/', views.service_list, name='service_list'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
]
