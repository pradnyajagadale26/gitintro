from django.db import models

# Create your models here.

class doctor(models.Model):
    doctorName=models.CharField(max_length=50)
    contacts=models.IntegerField()
    special=models.CharField(max_length=50)
    is_deleted=models.CharField(max_length=5)

    def __str__(self):
        return self.doctorName


class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True)
    address=models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(doctor, on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()
    
    def __str__(self):
        return self.doctor.doctorName + "__"+self.Patient.name


 