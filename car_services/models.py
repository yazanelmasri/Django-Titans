from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

"""
Service Models
"""
# Service Category Choices Model
class ServiceCategoryChoices(models.TextChoices):
    MAINTENANCE = 'Maintenance', 'Maintenance'
    REPAIRS = 'Repairs', 'Repairs'
    INSPECTIONS = 'Inspections', 'Inspections'
    INSTALLATIONS = 'Installations', 'Installations'
    CUSTOM = 'Custom', 'Custom (specify service details in description box!)'

# Service Type Choices Model
class ServiceTypeChoices(models.TextChoices):
    OIL_CHANGE = 'Oil Change', 'Oil Change (60 minutes)'
    TIRE_ROTATION = 'Tire Rotation', 'Tire Rotation (45 minutes)'
    BRAKE_INSPECTION = 'Brake Inspection', 'Brake Inspection (90 minutes)'
    ENGINE_REPAIR = 'Engine Repair', 'Engine Repair (180 minutes)'
    TRANSMISSION_REPAIR = 'Transmission Repair', 'Transmission Repair (240 minutes)'
    SAFETY_INSPECTION = 'Safety Inspection', 'Safety Inspection (60 minutes)'
    EMISSIONS_INSPECTION = 'Emissions Inspection', 'Emissions Inspection (45 minutes)'
    AUDIO_SYSTEM_INSTALLATION = 'Audio System Installation', 'Audio System Installation (120 minutes)'
    WINDOW_TINTING = 'Window Tinting', 'Window Tinting (90 minutes)'
    CUSTOM = 'Custom', 'Custom (specify service details in description box!)'

# Service model
class Service(models.Model):
    category = models.CharField(
        max_length=100,
        choices=ServiceCategoryChoices.choices,
        default=ServiceCategoryChoices.MAINTENANCE
    )
    
    type = models.CharField(
        max_length=100,
        choices=ServiceTypeChoices.choices,
        default=ServiceTypeChoices.OIL_CHANGE
    )

    duration = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text='Duration in minutes for custom service'
    )

    def save(self, *args, **kwargs):
        duration_map = {
            ServiceTypeChoices.OIL_CHANGE: 60,
            ServiceTypeChoices.TIRE_ROTATION: 45,
            ServiceTypeChoices.BRAKE_INSPECTION: 90,
            ServiceTypeChoices.ENGINE_REPAIR: 180,
            ServiceTypeChoices.TRANSMISSION_REPAIR: 240,
            ServiceTypeChoices.SAFETY_INSPECTION: 60,
            ServiceTypeChoices.EMISSIONS_INSPECTION: 45,
            ServiceTypeChoices.AUDIO_SYSTEM_INSTALLATION: 120,
            ServiceTypeChoices.WINDOW_TINTING: 90,
            ServiceTypeChoices.CUSTOM: 120,  # Default duration for Custom type
        }
        self.duration = duration_map.get(self.type, 60)  # Default duration based on type
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} - {self.type}" + (f" ({self.duration} minutes)" if self.duration else "")

"""
Vehicle Model
"""
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

"""
Appointment Model
"""
class Appointment(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = 'Confirmed', 'Confirmed'
        PENDING = 'Pending', 'Pending'
        COMPLETED = 'Completed', 'Completed'
        CANCELLED = 'Cancelled', 'Cancelled'
        RESCHEDULED = 'Rescheduled', 'Rescheduled'

    appointment_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='appointments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.PENDING)
    appointment_date = models.DateTimeField()
    custom_service_duration = models.PositiveIntegerField(blank=True, null=True, help_text='Duration in minutes for custom service')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.service.category == ServiceCategoryChoices.CUSTOM:
            if not self.custom_service_duration:
                raise ValidationError('Custom service category requires a custom duration to be specified.')
            self.service.duration = self.custom_service_duration
            self.service.type = ServiceTypeChoices.CUSTOM  # Set type to 'Custom'
        else:
            self.service.duration = self.service.duration or 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.appointment_date}"
