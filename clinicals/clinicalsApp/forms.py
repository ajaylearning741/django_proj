from django import forms
from django.forms.fields import DateField
from .models import ClinicalData,Patient

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(forms.ModelForm):
      
      class Meta:
        model=Patient
        fields=['firstName','lastName','dob']
        widgets = {'dob': DateInput(),}

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model=ClinicalData
        exclude=['patient_id']