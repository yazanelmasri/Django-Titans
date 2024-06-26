from django.db import models
from django.contrib.auth.admin import User

"appointments" (
  "appointment_id",
  "vehicle_id",
  "user_id",
  "service_id",
  "service_duration",
  "status",
  "created_at",
  "created_by"
);


"services" (
  "vehicle_id",
  "service_id",
  "service_name",
  "service_date",
  "description",
  "service_category"
);

"vehicles" (
  "vehicle_id",
  "make",
  "model",
  "year",
  "license_plate"
);