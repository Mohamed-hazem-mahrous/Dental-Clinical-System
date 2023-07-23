from django.db import models
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    birth = models.DateField()
    mobile = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    type = models.CharField(max_length=100)