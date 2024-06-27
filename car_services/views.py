# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_detail', pk=appointment.pk)  # Redirect to appointment detail view
    else:
        form = AppointmentForm()

    return render(request, 'create_appointment.html', {'form': form})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail', pk=pk)  # Redirect to appointment detail view
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'edit_appointment.html', {'form': form})

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

@login_required
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

@login_required
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()

    return render(request, 'create_vehicle.html', {'form': form})

@login_required
def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_detail', pk=pk)
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'edit_vehicle.html', {'form': form})


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})
