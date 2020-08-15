from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from AdminApp import models


def HomeView(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = datetime.today().date()
        obj = models.Appointment()
        obj.mobile = mobile
        obj.date = date
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
    context = {}
    html = 'index.html'
    return render(request,html,context)


def AboutView(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = datetime.today().date()
        obj = models.Appointment()
        obj.mobile = mobile
        obj.date = date
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
    context = {}
    html = 'About.html'
    return render(request,html,context)


def ContactView(request):
    if request.method == 'POST':
        MessangerName = request.POST.get('MessangerName')
        MessangerMobile = request.POST.get('MessangerMobile')
        MessangerMessage = request.POST.get('MessangerMessage')
        MessangerDate = datetime.today().date()
        msg = models.Messanger()
        msg.MessangerName = MessangerName
        msg.MessangerMobile = MessangerMobile
        msg.MessangerMessage = MessangerMessage
        msg.MessangerDate = MessangerDate
        if MessangerMessage == '':
            return redirect('error')
        else:
            msg.save()
            return redirect('success')

    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = datetime.today().date()
        obj = models.Appointment()
        obj.mobile = mobile
        obj.date = date
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
    context = {}
    html = 'Contact.html'
    return render(request,html,context)


def MakeAppointmentView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        booking_message = request.POST.get('booking_message')
        date = datetime.today().date()
        obj = models.Appointment()
        obj.name = name
        obj.age = age
        obj.mobile = mobile
        obj.place = place
        obj.booking_message = booking_message
        obj.date = date
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
    context = {}
    html = 'MakeAppointment.html'
    return render(request,html,context)


def SuccessView(request):
    context = {}
    html = 'success.html'
    return render(request,html,context)


def ErrorView(request):
    context = {}
    html = 'error.html'
    return render(request,html,context)


