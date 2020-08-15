
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView, name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('appointment_list/', views.AppointmentListView, name='appointment_list'),
    path('admin_appointment_list/', views.AdminAppointmentListView, name='admin_appointment_list'),
    path('messages/', views.MessagesView, name='messages'),
    path('delete_message/<int:id>', views.DeleteMessagesView, name='delete_message'),
    path('edit_appointment_list/<int:id>', views.EditAppointmentListView, name='edit_appointment_list'),
    path('delete_appointment_list/<int:id>', views.DeleteAppointmentListView, name='delete_appointment_list'),
]
