from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('appointments.html', views.home, name='home'),
    path('patient/', views.patient, name='patient'),
    path('patient.html', views.patient, name='patient'),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard.html', views.dashboard, name="dashboard"),

    path('Add_New_patient', views.Add_New_patient, name="Add_New_patient"),
    # path('Add_New_patient.html', views.Add_New_patient, name="Add_New_patient"),

    path('record/', views.patient_record, name="record"),
    path('record.html', views.patient_record, name="record"),
    path('assistants/', views.assistants, name='assistants'),
    path('assistants.html', views.assistants, name='assistants'),
  
    path('profile/', views.profile, name='profile'),
    path('profile.html', views.profile, name='profile'),

    path('getforview/', views.getforview, name='getforview'),
    path('editpatient/', views.edit_patient, name='editpatient'),
    path('getappinfo/', views.getappinfo, name='getappinfo'),

    path('Add_new_appointment', views.Add_new_appointment, name = 'Add_new_appointment'),

    path('assistants/', views.assistants, name='assistants'),
    




]