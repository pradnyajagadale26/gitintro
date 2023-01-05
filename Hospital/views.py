from django.shortcuts import render , HttpResponse, redirect
from Hospital.models import doctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import doctor, Patient, Appointment
from . import forms
from Hospital.forms import UserForm




def home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')
    
def Contact(request):
    return render(request, 'contact.html')
    

def dash(request):
    return render(request, 'dash.html')


def admin_login(request):

    if request.method=="POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            u=authenticate(username=uname, password=upass)
            if u:
                login(request, u) #this function starts session for that user
                return redirect('/')
    else:
        fm=AuthenticationForm
        return render(request, 'login.html', {'form':fm})


def admin_logout(request):
    logout(request) #this is used to distroy session 
    return redirect('/login')


def user_register(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/login")
            #return HttpResponse("User Register Sucessfully ")
        else:
            return HttpResponse("Failed to create User ")

    else:
        fm=UserForm()
        return render(request, 'register.html', {'form':fm})


def add_doctor(request):
    if request.method=='POST':
        n=request.POST['doctorName']
        c=request.POST['contacts']
        s=request.POST['special']
        
        n1=doctor.objects.create(doctorName=n, contacts=c, special=s, is_deleted='N')
        n1.save()
        return redirect("/dadd/")
    else:
        records=doctor.objects.all()
        content={'data': records}
    return render(request, 'add_dr.html', content)


def view_doctor(request):
    records=doctor.objects.all()
    content= {'data': records}
    return render(request, 'view_dr.html', content)

def remove(request, rid):
    t1=doctor.objects.get(id=rid)
    t1.delete()
    return redirect("/view_dr")

def edit(request, rid):
    if request.method=='POST':
        n=request.POST['doctorName']
        c=request.POST['contacts']
        s=request.POST['special']
        
        n1=doctor.objects.filter(id=rid)
        n1.update(doctorName=n, contacts=c, special=s)
        
        return redirect("/view_dr")
    rec=doctor.objects.filter(id=rid)
    content={}
    content['data']=rec
    return render(request, 'editform.html', content)





def add_patient(request):
    if request.method=='POST':
        N=request.POST['name']
        g=request.POST['gender']
        m=request.POST['mobile']
        a=request.POST['address']
        
        n1=Patient.objects.create(name=N, gender=g, mobile=m , address=a)
        n1.save()
        return redirect("/padd")
    else:
        record=Patient.objects.all()
        content={'data': record}
    return render(request, 'add_patient.html', content)


def view_patient(request):
    record=Patient.objects.all()
    content= {'data': record}
    return render(request, 'view_patient.html', content)

def delete(request, pid):
    t1=Patient.objects.get(id=pid)
    t1.delete()
    return redirect("/view_patient")

def add_appointment(request):
    if request.method == 'POST':
        n=request.POST['doctor']
        N=request.POST['Patient']
        d=request.POST['Date']
        t=request.POST['Time']
        Doctor=doctor.objects.filter(doctorName=n)
        patient=Patient.objects.filter(name=N)
        
        n1=Appointment.objects.create(doctor=n, Patient=N, Date=d, Time=t)
        n1.save()
        return redirect("/padd")
    else:
        record=Appointment.objects.all()
        content={'data': record}
    return render(request, 'add_appoint.html', content)

def view_appointment(request):
    record=Appointment.objects.all()
    content= {'data': record}
    return render(request, 'view_appoint.html', content)

def dels(request, aid):
    a1=Appointment.objects.get(id=aid)
    a1.delete()
    return redirect("/view_appoint")


def setsession(request):
    request.session['user']='itvedant'
    return render(request, 'setsession.html')

def getsession(request):
    data=request.session['user']
    return render(request, 'getsession.html',{'d': data} )