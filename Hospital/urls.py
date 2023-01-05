"""HospitalManagements URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views  as v 

urlpatterns = [
    path("", v.home),
    path("about/", v.About),
    path("contact/", v.Contact),
    path("dash", v.dash),
    path("padd", v.add_patient),
    path("dadd", v.add_doctor),
    path("Aadd", v.add_appointment),
    path('login', v.admin_login),
    path('logout', v.admin_logout),
    path("view_dr", v.view_doctor),
    path("view_patient", v.view_patient),
    path("view_appoint", v.view_appointment),
    path("delete/<int:rid>", v.remove),
    path("remove/<int:pid>",v.delete),
    path("dels/<aid>", v.dels),
    path("edit/<int:rid>", v.edit),
    path('set', v.setsession),
    path('get', v.getsession),
    path('register', v.user_register),
   
    
    
]
