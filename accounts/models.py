from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11, unique=True)
    national_id = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11 , unique=True)
    national_id = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name
