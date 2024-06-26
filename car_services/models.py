from django.db import models
from django.contrib.auth.admin import User

""" 
Service Models
"""
# Service Category Model
class ServiceCategory(models.Model):
  name = models.CharField(max_length=100)
  service_description = models.TextField(help_text='Description of the service type')

  def __str__(self):
    return self.name

# Service Choices Model
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
    CUSTOM = 'Custom', 'Custom (specify duration)'



"vehicles" (
  "vehicle_id",
  "make",
  "model",
  "year",
  "license_plate"
);


""" 
Appointment Model
"""
class Appointment (models.Model):
  class Status(models.TextChoices):
    CONFIRMED = 'Confirmed', 'Confirmed'
    PENDING = 'Pending', 'Pending'
    COMPLETED = 'Completed', 'Completed'
    CANCELLED = 'Cancelled', 'Cancelled'
    RESCHEDULED = 'Rescheduled', 'Rescheduled'


  appointment_id = models.AutoField(primary_key=True)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='appointments')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
  service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='appointtments')
  status = models.CharField(max_length=100, choices=Status.choices, default=Status.PENDING)
  service_type = models.CharField(max_length=100, choices=ServiceTypeChoices.choices)
  appointment_date = models.DateTimeField()
  service_duration = models.IntegerField(editable=False, null=True)
  custom_service_duration = models.IntegerField(blank=True, null=True, help_text='Duration in minutes for custom service')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
          if self.service_type != ServiceTypeChoices.CUSTOM:
              service_duration_mapping = {
                  ServiceTypeChoices.OIL_CHANGE: 60,
                  ServiceTypeChoices.TIRE_ROTATION: 45,
                  ServiceTypeChoices.BRAKE_INSPECTION: 90,
                  ServiceTypeChoices.ENGINE_REPAIR: 180,
                  ServiceTypeChoices.TRANSMISSION_REPAIR: 240,
                  ServiceTypeChoices.SAFETY_INSPECTION: 60,
                  ServiceTypeChoices.EMISSIONS_INSPECTION: 45,
                  ServiceTypeChoices.AUDIO_SYSTEM_INSTALLATION: 120,
                  ServiceTypeChoices.WINDOW_TINTING: 90,
              }
              self.service_duration = service_duration_mapping.get(self.service_type, 0)
              self.custom_service_type = None
              self.custom_service_duration = None
          else:
              self.service_duration = self.custom_service_duration

          super().save(*args, **kwargs)

  def __str__(self):
    return f"Appointment for {self.vehicle} on {self.appointment_date}"
