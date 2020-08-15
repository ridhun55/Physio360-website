from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=400,null=True,blank=True)
    age = models.CharField(max_length=400,null=True,blank=True)
    mobile = models.CharField(max_length=400,null=True,blank=True)
    place = models.CharField(max_length=400,null=True,blank=True)
    booking_message = models.CharField(max_length=1000,null=True,blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class AdminAppointment(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    age = models.CharField(max_length=400, null=True, blank=True)
    mobile = models.CharField(max_length=400, null=True, blank=True)
    place = models.CharField(max_length=400, null=True, blank=True)
    booking_message = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Messanger(models.Model):
    MessangerName = models.CharField(max_length=400, null=True, blank=True)
    MessangerMobile = models.CharField(max_length=400, null=True, blank=True)
    MessangerMessage = models.CharField(max_length=2000, null=True, blank=True)
    MessangerDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.MessangerName

