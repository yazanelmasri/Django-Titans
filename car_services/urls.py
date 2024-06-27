# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointment/create/', views.create_appointment, name='create_appointment'),
    path('appointment/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointment/<int:pk>/edit/', views.edit_appointment, name='edit_appointment'),

    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/create/', views.create_vehicle, name='create_vehicle'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:pk>/edit/', views.edit_vehicle, name='edit_vehicle'),

    path('services/', views.service_list, name='service_list'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
]
