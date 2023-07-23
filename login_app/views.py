# from django.shortcuts import render
# from django.shortcuts import HttpResponse
# import mysql.connector as sql
# from django.db import IntegrityError
# from django.core.exceptions import ValidationError
# import datetime


# from .models import User
# import datetime
# import mysql.connector

# from django.core.exceptions import ValidationError
# from django.db import IntegrityError
# from django.contrib import messages
# from django.shortcuts import render, HttpResponse
# from .models import User
# import datetime

# def index(request):
#     if 'signup' in request.GET:
#         # Retrieve the form data
#         fn = request.GET.get('first_name')
#         ln = request.GET.get('last_name')
#         em = request.GET.get('email')
#         pwd = request.GET.get('password')
#         dt = request.GET.get('birth')
#         mb = request.GET.get('mobile')
#         s = request.GET.get('sex')
#         tp = request.GET.get('type')

#         # Convert date to the correct format
#         dt = datetime.datetime.strptime(dt, '%Y-%m-%d').date() if dt else None

#         try:
#             # Check if the email already exists
#             if User.objects.filter(email=em).exists():
#                 raise ValidationError("Email already exists. Please sign up with a different email.")

#             # Insert the data into the database
#             user = User(first_name=fn, last_name=ln, sex=s, email=em, mobile=mb, birth=dt, password=pwd, type=tp)
#             user.save()

#             # # Redirect to the appropriate page
#             # if tp == 'Assistance':
#             #     return render(request, 'Nurse/dashboard - nurse.html')
#             # elif tp == 'Doctor':
#             #     return render(request, 'dashboard.html')
#             # else:
#             #     return HttpResponse("Invalid user type")

#         except ValidationError as e:
#             messages.error(request, str(e))

#         except IntegrityError:
#             messages.error(request, "An error occurred. Please try again.")

#     elif 'signin' in request.GET:
#         # Retrieve the form data
#         em = request.GET.get('email')
#         pwd = request.GET.get('password')

#         try:
#             # Query the database
#             user = User.objects.get(email=em, password=pwd)
#             user_type = user.type
#             if user_type == 'Assistance':
#                 return render(request, 'dashboard.html')
#             elif user_type == 'Doctor':
#                 return render(request, 'dashboard.html')
#             else:
#                 return HttpResponse("Invalid user type")

#         except User.DoesNotExist:

#             messages.error(request, "invalid email or password", extra_tags='email-pass-conflict')

#             # return HttpResponse("Error: Invalid email or password")

#     return render(request, 'login.html')



from django.shortcuts import render
from django.shortcuts import HttpResponse
import mysql.connector as sql
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import datetime


from .models import User
import datetime
import mysql.connector

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from .models import User
import datetime

def index(request):
    if 'signup' in request.GET:
        # Retrieve the form data
        fn = request.GET.get('first_name')
        ln = request.GET.get('last_name')
        em = request.GET.get('email')
        pwd = request.GET.get('password')
        dt = request.GET.get('birth')
        mb = request.GET.get('mobile')
        s = request.GET.get('sex')
        tp = request.GET.get('type')

        # Convert date to the correct format
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d').date() if dt else None

        try:
            # Check if the email already exists
            if User.objects.filter(email=em).exists():
                raise ValidationError("Email already exists. Please sign up with a different email.")

            # Insert the data into the database
            user = User(first_name=fn, last_name=ln, sex=s, email=em, mobile=mb, birth=dt, password=pwd, type=tp)
            user.save()

            # # Redirect to the appropriate page
            # if tp == 'Assistance':
            #     return render(request, 'Nurse/dashboard - nurse.html')
            # elif tp == 'Doctor':
            #     return render(request, 'dashboard.html')
            # else:
            #     return HttpResponse("Invalid user type")

        except ValidationError as e:
            messages.error(request, str(e))

        except IntegrityError:
            messages.error(request, "An error occurred. Please try again.")

    elif 'signin' in request.GET:
        # Retrieve the form data
        em = request.GET.get('email')
        pwd = request.GET.get('password')

        try:
            # Query the database
            user = User.objects.get(email=em, password=pwd)
            user_type = user.type
            if user_type == 'Assistance':
                return render(request, 'dashboard.html')
            elif user_type == 'Doctor':
                return render(request, 'dashboard.html')
            else:
                return HttpResponse("Invalid user type")

        except User.DoesNotExist:

            messages.error(request, "invalid email or password", extra_tags='email-pass-conflict')

            # return HttpResponse("Error: Invalid email or password")

    return render(request, 'login.html')