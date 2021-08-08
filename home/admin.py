from django.contrib import admin

from .models import Person, Education, Attendance, Location

admin.site.register(Attendance)
admin.site.register(Education)
admin.site.register(Location)
admin.site.register(Person)
