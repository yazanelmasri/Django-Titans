from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vehicle, Appointment, Service

class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
        )

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'year')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('vehicle', 'service', 'appointment_date', 'description')

# forms.py

from django import forms
from .models import Service, ServiceCategoryChoices, ServiceTypeChoices

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('category', 'type', 'duration')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set choices dynamically for category and type fields
        self.fields['category'].choices = ServiceCategoryChoices.choices
        self.fields['type'].choices = ServiceTypeChoices.choices
