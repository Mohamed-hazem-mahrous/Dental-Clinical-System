from django.db import models


# Create your models here.

class Patient(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150, null=True)
    age = models.IntegerField()

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=250)


# class Assistants(models.Model):
#     name = models.CharField(max_length=150)
#     age = models.IntegerField()

#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

#     mobile = models.CharField(max_length=11)
#     address = models.CharField(max_length=250)


class Appointment(models.Model):
    
    fees = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    STATUS_CHOICES = (
        (0, 'DONE'),
        (1, 'COMING'),
    )

    TYPE_CHOICES = (
        (0, 'Cavity'),
        (1, 'Crown'),
        (2, 'Surgery'),
        (3, 'Regular Checkup'),
        (4, 'Cosmetic'),
        (5, 'Other'),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    app_type = models.IntegerField(choices=TYPE_CHOICES, default=3)

    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)

    description = models.CharField(max_length=1000, null=True)
    prescription = models.CharField(max_length=2000, null=True)

# class Report(models.Model):
#     description = models.CharField(max_length=1000, null=True)
#     prescription = models.CharField(max_length=2000, null=True)
#     # prescription (multivalued attr)
#     app_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)

#
# class ReportPrescription(models.Model):
#     Drug = models.CharField(max_length=200)
#     ReportID = models.ForeignKey(Report, on_delete=models.CASCADE)
