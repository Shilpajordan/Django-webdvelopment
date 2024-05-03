from django.db import models

# Create your models here.
# models.py
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    appointment_datetime = models.DateTimeField()
    # Add other fields as needed
