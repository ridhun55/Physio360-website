
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('make_appointment/', views.MakeAppointmentView, name='make_appointment'),
    path('success/', views.SuccessView, name='success'),
    path('error/', views.ErrorView, name='error'),
]
