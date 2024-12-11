from django.shortcuts import render
from .models import Patient,ClinicalData
from .forms import *
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render

# Create your views here.
class PatientListView(ListView):
    model=Patient

class PatientCreateView(CreateView):
    model=Patient
    form_class = PatientForm
    success_url=reverse_lazy('index')


class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','dob')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')




def addData(request,**kwargs):
    form123 = ClinicalDataForm()
    patient123 = Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form123 = ClinicalDataForm(request.POST)
        if form123.is_valid():
            #print(form123)
            form123.instance.patient_id=patient123.id
            
            form123.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form123,'patient':patient123})


def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                feetToMetres = float(heightAndWeight[0]) * 0.4536
                BMI = (float(heightAndWeight[1]))/(feetToMetres*feetToMetres)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalsApp/generateReport.html',{'data':responseData})