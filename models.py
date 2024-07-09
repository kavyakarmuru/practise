from django.db import models

class Patient(models.Model):
    FirstName=models.CharField(max_length=70)
    LastName=models.CharField(max_length=70)
    Age=models.IntegerField()

class Clinicaldata(models.Model):
    COMPONENT_NAMES=[('hw','Height/Weight'),('bp','Blood Pressure'),('hr','Heart Rate')]
    ComponentName=models.CharField(choices=COMPONENT_NAMES,max_length=20)
    ComponentValue=models.CharField(max_length=20)
    MeasuredDateTime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)