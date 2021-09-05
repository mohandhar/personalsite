from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'state'], name='unique_location')
        ]

    def __str__(self):
        return f'{self.city}, {self.state}'


class Attendance(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['start_date', 'end_date'], name='unique_attendance')
        ]

    def __str__(self):
        return f'{self.start_date} - {self.end_date}'


class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None)
    attendance = models.ForeignKey(
        Attendance, on_delete=models.RESTRICT, default=None)
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.school_name}'


class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location, on_delete=models.RESTRICT, default=None)
    attendance = models.ForeignKey(
        Attendance, on_delete=models.RESTRICT, default=None)
    summary = models.CharField(max_length=600)

    class Meta:
        ordering = ['-attendance__start_date']

    def __str__(self):
        return f'{self.company}'


class Accomplishment(models.Model):
    detail = models.CharField(max_length=300)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.detail}'
