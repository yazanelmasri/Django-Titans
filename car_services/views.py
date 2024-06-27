# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment, Service, Vehicle, ServiceTypeChoices, ServiceCategoryChoices
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Vehicle, Appointment
from .forms import VehicleForm, AppointmentForm, SignupForm

"""
Account Registration Views
"""

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class DeleteAccountView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return redirect('index')

class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            self._create_and_login_user(request, form)
            return redirect('appointment_list')
        return render(request, self.template_name, {'form': form})

    def _create_and_login_user(self, request, form):
        user = form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user is not None:
            login(request, user)

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('appointment_list')
        return render(request, self.template_name, {'error': 'Invalid username or password.'})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')

"""
Appointment views
"""

@login_required
def vehicle_list(request):
    vehicles = request.user.vehicles.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

@login_required
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

@login_required
def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if vehicle.user != request.user:
        return redirect('vehicle_list')  # Ensure user only updates their own vehicles
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_form.html', {'form': form})

@login_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if vehicle.user == request.user:
        vehicle.delete()
    return redirect('vehicle_list')

@login_required
def appointment_list(request):
    appointments = request.user.appointments.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.user != request.user:
        return redirect('appointment_list')  # Ensure user only updates their own appointments
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.user == request.user:
        appointment.delete()
    return redirect('appointment_list')

@staff_member_required
def all_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'all_appointments.html', {'appointments': appointments})
