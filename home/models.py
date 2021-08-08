from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    description = models.CharField(max_length=256)


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


class Attendance(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    location = Location()
    attendance = Attendance()
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
