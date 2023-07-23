from django.shortcuts import render
from .models import *
from django.db.models import Count
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
import json
from login_app.models import User

from django.contrib import messages

# Create your views here.
def home(request):
    
    if request.method == "POST":
        if request.POST.get('reportedit'):
            # print(request.POST)
            """
            ID:
            1
            Appointment Description:
            Drug Selection:
            "appointmentDescription" "drugSelection"
            """
            id = request.POST['app_id_hidden']
            Appointment.objects.filter(id=id).update(description=request.POST["appointmentDescription"],
                                                     prescription=request.POST["drugSelection"])
        elif request.POST.get('datefilter'):
            
            date_query = request.POST['date']
        
            
            if date_query == "":
                records = Appointment.objects.all()
            else:
                # YYYY-MM-DD
                y, m, d = date_query.split('-')
                print(y, m, d)
                records = Appointment.objects.filter(date__day=d, date__month=m, date__year=y)
            context = {'appointments': records}
            return render(request, 'appointments.html', context)
        else:
            delete_id = request.POST.get('app_to_del')
            print(f"delete_id {delete_id}")
            if delete_id:
                appointment = Appointment.objects.get(id = delete_id)
                appointment.delete()
        
        
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'appointments.html', context)


def patient(request):
    if request.method == "POST":
        if request.POST.get('search_content'):
            search_content = request.POST['search_content']

            records = Patient.objects.filter(fname__icontains=search_content) | Patient.objects.filter(id__icontains=search_content) \
                      | Patient.objects.filter(lname__icontains=search_content)
        elif request.POST.get('id_to_del'):
            id_to_del = request.POST.get('id_to_del')
            p_to_del = Patient.objects.get(id=id_to_del)
            p_to_del.delete()

            records = Patient.objects.all()
        
        else:
            records = Patient.objects.all()
    else:
        records = Patient.objects.all()
    context = {
            'records': records
        }
    return render(request,  'patient.html', context)
# if( request.method == "POST" ):
#         if request.POST['search_content']:
#             search_content = request.POST['search_content']
#             records = Patient.objects.filter(name__icontains=search_content) | Patient.objects.filter(id__icontains=search_content)
#         else:
#             records = Patient.objects.all()
#     else:
#         records = Patient.objects.all()
#     context = {
#             'records': records
#         }
#     return render(request,  'patient.html', context)


    
    
# def one_appt(request):
#     appointment = request.GET['appointment']
#     patient = request.GET['patient']
#     appointment_record = Appointment.objects.get(id=appointment)
#     patient_record = Patient.objects.get(id=patient)

#     context = {
#             'patient_record':patient_record,
#             'appointment_record':appointment_record
#     }
#     return render(request, 'appointment_details.html',context)

def dashboard(request):

    def count_appointments_today():
        current_date = datetime.today()
        appointment_count = Appointment.objects.filter(date__year=current_date.year, date__month=current_date.month, date__day=current_date.day).count()
        return appointment_count
    
    def count_patients():
        patients_count = Patient.objects.count()
        return patients_count
    
    def count_patients_thismonth():
        current_date = datetime.today()
        
        patients_thismonth_count = Appointment.objects.filter(date__month=current_date.month, date__year=current_date.year).count()
 
        return patients_thismonth_count
   
    no_app = count_appointments_today() 
    patients_thismonth_count = count_patients_thismonth()
    
    patients_count=count_patients()
    
    
    context={
        'no_app':no_app,
        'patients_count':patients_count,
        'patients_thismonth_count':patients_thismonth_count
            }
    return render(request, 'dashboard.html', context)




def patient_record(request):
    id = request.GET['patient_id']
    kkk = request.GET['ss']
    patient_record = Patient.objects.get(id=id)

    return render(request, 'record.html', {'patient_record':patient_record})


def Add_New_patient(request):
   
    if request.method == "POST":
        
        fname = request.POST.get('patientFname')
       
        lname = request.POST.get('patientLname')
        
        mobile = int(request.POST.get('patientMob'))
       
        address = request.POST.get('RID')
        
        if request.POST.get('gender') == "female":
            gender = 'F'
            
        else:
            gender = 'M'
            
        age = request.POST.get('docAge')
        
        new_patient = Patient(fname=fname, lname=lname, age=age, gender=gender, mobile=mobile, address=address)

        new_patient.save()
        return redirect('patient')

    return render(request, 'Add_New_patient.html')

# A view called in the search page using an ajax request, to get data from the DB for the table of students
def getforview(request):
    # gets the search query
    id = request.GET['query']

    result = Patient.objects.filter(id=id)


    data = {'result': list(result.values())}
    return JsonResponse(data)

def edit_patient(request):
    patient = json.loads(request.GET['patient'])
    """
            let new_patient = {
                    'name': newName,
                    'id': patient_ID,
                    'age': newAge,
                    'gender': newGender,
                    'mobile': newMobile,
                    'address': newAddress
                }
    """
    Patient.objects.filter(pk=patient['id']).update(
        fname=patient['fname'],
        lname=patient['lname'],
        age=patient['age'],
        gender=patient['gender'],
        mobile=patient['mobile'],
        address=patient['address']
    )
    return HttpResponse('Successfully Edited')

def getappinfo(request):
    id = request.GET['query']
    result = Appointment.objects.filter(id=id)

    data = {'result': list(result.values())}
    return JsonResponse(data)

# Check if appointment with the chosen half hour already exists
        # if Appointment.objects.filter(time=appointmentTime).exists():
        #     # Handle the case when the chosen half hour is already taken
        #     error_message = f"The half hour '{appointmentTime}' is already booked. Please choose a different time."
        #     return render(request, 'appointment.html', {'error_message': error_message})
# def Add_new_appointment(request):
    if request.method == "POST":
        fees = request.POST.get('fees')
        date= request.POST.get('appointmentDate')
        time=request.POST.get('appointmentTime')
        status = int(request.POST.get('status'))

        app_type_str=request.POST.get('appointmentType')
        print(f"apptype: {app_type_str}")
        patientid=request.POST.get('pid')
        p = Patient.objects.get(id=patientid)

        if app_type_str == "Cavity":
            taipu=0
        elif app_type_str == "Crown":
            taipu=1
        elif app_type_str == "Surgery":
            taipu=2
        elif app_type_str == "Regular":
            taipu=3
        elif app_type_str == "Cosmetic":
            taipu=4
        else:
            taipu=5

        description=""
        prescription=""

        if_existing = Appointment.objects.filter(time=time) & Appointment.objects.filter(date=date)
        if if_existing.exists():
            # Handle the case when the chosen half hour is already taken
            error_message = f"The half hour '{time}' on {date}is already booked. Please choose a different time."
            return render(request, 'Add_new_appointment.html')

        new_appoint = Appointment(fees=fees, date=date, time=time,status=status, app_type=taipu,pid=p,description=description,prescription=prescription)
        new_appoint.save()
        return redirect('home')
    
  
    patients = Patient.objects.all()
    print(patients)
    context = {
        'patients':patients
    }
    return render(request, 'Add_new_appointment.html', context)
def Add_new_appointment(request):
    if request.method == "POST":
        fees = request.POST.get('fees')
        date= request.POST.get('appointmentDate')
        time=request.POST.get('appointmentTime')
        status = int(request.POST.get('status'))

        app_type_str=request.POST.get('appointmentType')
        print(f"apptype: {app_type_str}")
        patientid=request.POST.get('pid')
        p = Patient.objects.get(id=patientid)

        if app_type_str == "Cavity":
            taipu=0
        elif app_type_str == "Crown":
            taipu=1
        elif app_type_str == "Surgery":
            taipu=2
        elif app_type_str == "Regular":
            taipu=3
        elif app_type_str == "Cosmetic":
            taipu=4
        else:
            taipu=5

        description=""
        prescription=""

        if_existing = Appointment.objects.filter(time=time) & Appointment.objects.filter(date=date)
        if if_existing.exists():
            # Handle the case when the chosen half hour is already taken
            # error_message = f"The half hour '{time}' on {date}is already booked. Please choose a different time."
            messages.error(request, "Appointment time is taken", extra_tags='app-time-conflict')

            patients = Patient.objects.all()
            context = {
                'patients':patients
            }
            return render(request, 'Add_new_appointment.html',context)

        new_appoint = Appointment(fees=fees, date=date, time=time,status=status, app_type=taipu,pid=p,description=description,prescription=prescription)
        new_appoint.save()
        return redirect('home')
    
  
    patients = Patient.objects.all()
    print(patients)
    context = {
        'patients':patients
    }
    return render(request, 'Add_new_appointment.html', context)
# def assistants(request):

#     # assistants = User.objects.filter(type="")
#     context={
#         'assistants':assistants
#     }

#     return render(request, 'assistants.html', context)

def assistants(request):
    assistants = User.objects.filter(type="Assistance")
    print(f"assistants {assistants}")
    context = {
        'assistants':assistants
    }
    
    return render(request, 'assistants.html', context)

def profile(request):
    return render(request, "profile.html")



