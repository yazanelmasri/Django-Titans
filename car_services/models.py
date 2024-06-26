# models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

class ServiceCategoryChoices(models.TextChoices):
    MAINTENANCE = 'Maintenance', 'Maintenance'
    REPAIRS = 'Repairs', 'Repairs'
    INSPECTIONS = 'Inspections', 'Inspections'
    INSTALLATIONS = 'Installations', 'Installations'
    CUSTOM = 'Custom', 'Custom'

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

    def __str__(self):
        return f"{self.category} - {self.type}" + (f" ({self.duration} minutes)" if self.duration else "")

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('RESCHEDULED', 'Rescheduled'),
    ]

    appointment_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='appointments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    appointment_date = models.DateTimeField()
    description = models.TextField(blank=True, help_text="Enter service details")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.appointment_date}"

# Signal to validate custom services before saving
@receiver(pre_save, sender=Appointment)
def validate_custom_service(sender, instance, **kwargs):
    if instance.service.type == ServiceTypeChoices.CUSTOM and not instance.description:
        raise ValidationError('Custom service requires service details in description.')
