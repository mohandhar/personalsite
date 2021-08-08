from django.contrib import admin

from .models import Person, Education, Attendance, Location

admin.site.register(Person, Education, Attendance, Location)
