from django.shortcuts import render,redirect
from clinicaldataapp import models
from clinicaldataapp import forms

def display(request):
    data=models.Patient.objects.all()
    return render(request,"clinicaldataapp/index.html",{'data':data})

def Create(request):
    form=forms.PatientForm()
    if(request.method=='POST'):
        form=forms.PatientForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect("/")
    return render(request,"clinicaldataapp/create.html",{'form':form})

def Delete(request,id):
    data=models.Patient.objects.get(id=id)
    data.delete()
    return redirect("/")

def Update(request,id):
    data=models.Patient.objects.get(id=id)
    form=forms.PatientForm(instance=data)
    if(request.method=='POST'):
        form=forms.PatientForm(request.POST,instance=data)
        if(form.is_valid()):
            form.save()
        return redirect("/")
    return render(request,"clinicaldataapp/update.html",{'form':form})

def Data(request,id):
    form=forms.ClinicaldataForm()
    data1=models.Patient.objects.get(id=id)
    if(request.method=='POST'):
        form=forms.ClinicaldataForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect("/")
    return render(request,"clinicaldataapp/data.html",{'form':form,'data1':data1})

def ReportData(request,id):
    data=models.Clinicaldata.objects.filter(patient_id=id)
    a=[]
    for d in data:
        if(d.ComponentName=='hw'):
            h_w=d.ComponentValue.split("/")
            if(len(h_w)>1):
                b=models.Clinicaldata()
                b.ComponentName='BMI'
                b.ComponentValue=float(h_w[1])/(float(h_w[0])*0.4563*0.4563*float(h_w[0]))
                a.append(b)
        a.append(d)
    return render(request,"clinicaldataapp/report.html",{'a':a})