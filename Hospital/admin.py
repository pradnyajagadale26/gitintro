from django.contrib import admin

from.models import doctor, Patient, Appointment

# Register your models here.

admin.site.register(doctor)
admin.site.register(Patient)
admin.site.register(Appointment)