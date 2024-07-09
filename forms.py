from django import forms
from clinicaldataapp import models

class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields='__all__'

class ClinicaldataForm(forms.ModelForm):
    class Meta:
        model=models.Clinicaldata
        fields='__all__'