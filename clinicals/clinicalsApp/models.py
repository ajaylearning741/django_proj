from django.db import models
from datetime import date,timedelta


# Create your models here.
class Patient(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    dob = models.DateField(max_length=8)

    @property
    def age_count(self):
        today=date.today()
        age_gap=(today-self.dob)// timedelta(days=365.2425)
        return age_gap
    


class ClinicalData(models.Model):
    COMPONENT_NAMES=[('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient_id = models.IntegerField()

