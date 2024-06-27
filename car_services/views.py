from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Appointment, Service, Vehicle, ServiceTypeChoices, ServiceCategoryChoices
from .forms import VehicleForm, AppointmentForm, SignupForm, ServiceForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from .models import Appointment, Service, Vehicle, ServiceTypeChoices, ServiceCategoryChoices
from .forms import VehicleForm, AppointmentForm, SignupForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Service
from .forms import ServiceForm

"""
Account Views
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
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

"""
General Views
"""

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

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
Vehicle Views
"""

@method_decorator(login_required, name='dispatch')
class VehicleListView(View):
    template_name = 'vehicle_list.html'

    def get(self, request):
        vehicles = request.user.vehicles.all()
        return render(request, self.template_name, {'vehicles': vehicles})

@method_decorator(login_required, name='dispatch')
class VehicleCreateView(View):
    template_name = 'vehicle_form.html'

    def get(self, request):
        form = VehicleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return redirect('vehicle_list')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class VehicleUpdateView(View):
    template_name = 'vehicle_form.html'

    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        if vehicle.user != request.user:
            return redirect('vehicle_list')
        form = VehicleForm(instance=vehicle)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        if vehicle.user != request.user:
            return redirect('vehicle_list')
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class VehicleDeleteView(View):
    def post(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        if vehicle.user == request.user:
            vehicle.delete()
        return redirect('vehicle_list')

"""
Appointment Views
"""

@method_decorator(login_required, name='dispatch')
class AppointmentListView(View):
    template_name = 'appointment_list.html'

    def get(self, request):
        appointments = request.user.appointments.all()
        return render(request, self.template_name, {'appointments': appointments})

@method_decorator(login_required, name='dispatch')
class CreateAppointmentView(View):
    template_name = 'appointment_form.html'

    def get(self, request):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class UpdateAppointmentView(View):
    template_name = 'appointment_form.html'

    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        if appointment.user != request.user:
            return redirect('appointment_list')
        form = AppointmentForm(instance=appointment)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        if appointment.user != request.user:
            return redirect('appointment_list')
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class DeleteAppointmentView(View):
    def post(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        if appointment.user == request.user:
            appointment.delete()
        return redirect('appointment_list')

@method_decorator(staff_member_required, name='dispatch')
class AllAppointmentsView(View):
    template_name = 'all_appointments.html'

    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, self.template_name, {'appointments': appointments})

"""
Service Views
"""

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

@staff_member_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_form.html', {'form': form})

@staff_member_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_form.html', {'form': form})

@staff_member_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_confirm_delete.html', {'service': service})
