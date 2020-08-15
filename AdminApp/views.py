from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from . import models


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        aut = authenticate(username=username,password=password)
        if aut is None:
            return redirect('login')
        else:
            login(request,aut)
            if aut.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('login')
    context = {}
    html = 'login.html'
    return render(request,html,context)


def LogoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def DashboardView(request):
    all_count = models.Appointment.objects.all().count()
    admin_count = models.AdminAppointment.objects.all().count()
    msg_count = models.Messanger.objects.all().count()

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        booking_message = request.POST.get('booking_message')
        date = datetime.today().date()
        obj_2 = models.AdminAppointment()
        obj_2.name = name
        obj_2.age = age
        obj_2.mobile = mobile
        obj_2.place = place
        obj_2.booking_message = booking_message
        obj_2.date = date
        if mobile == '':
            return redirect('dashboard')
        else:
            obj_2.save()
            return redirect('dashboard')
    context = {
        'all_count':all_count,
        'admin_count':admin_count,
        'msg_count':msg_count,
    }
    html = 'Dashboard.html'
    return render(request,html,context)


@login_required(login_url='login')
def AppointmentListView(request):
    data = models.Appointment.objects.all()
    context = {
        'data':data
    }
    html = 'AppointmentList.html'
    return render(request,html,context)


@login_required(login_url='login')
def AdminAppointmentListView(request):
    data = models.AdminAppointment.objects.all()
    context = {
        'data':data
    }
    html = 'AdminAppointmentList.html'
    return render(request,html,context)


@login_required(login_url='login')
def EditAppointmentListView(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        date = request.POST.get('date')
        obj = models.Appointment.objects.get(id=id)
        obj.name = name
        obj.age = age
        obj.mobile = mobile
        obj.place = place
        obj.date = date
        obj.save()
        return redirect('appointment_list')

    data = models.Appointment.objects.get(id=id)
    context = {
        'data':data
    }
    html = 'EditAppointmentList.html'
    return render(request,html,context)


@login_required(login_url='login')
def DeleteAppointmentListView(request,id):
    data = models.Appointment.objects.get(id=id)
    data.delete()
    return redirect('appointment_list')
    context = {}
    html = 'AppointmentList.html'
    return render(request,html,context)\


@login_required(login_url='login')
def MessagesView(request):
    data = models.Messanger.objects.all()
    context = {
        'data':data
    }
    html = 'Messages.html'
    return render(request,html,context)

@login_required(login_url='login')
def DeleteMessagesView(request,id):
    obj = models.Messanger.objects.get(id=id)
    obj.delete()
    return redirect('messages')
    context = {}
    html = 'Messages.html'
    return render(request,html,context)

