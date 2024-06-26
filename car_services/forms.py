from django import forms
from .models import Appointment, Vehicle, Service

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'type']


class  AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['vehicle', 'service', 'status', 'appointment_date', 'custom_service_duration']