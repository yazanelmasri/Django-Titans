from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),#pass
    path('login/', auth_views.LoginView.as_view(), name='login'), #pass
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),#pass
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('signup/', views.SignupView.as_view(), name='signup'),#pass
    path('profile/', views.ProfileView.as_view(), name='profile'),#pass
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),#pass 
    
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),#pass
    path('vehicles/new/', views.VehicleCreateView.as_view(), name='vehicle_create'),#pass
    path('vehicles/<int:pk>/edit/', views.VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),

    path('appointments/', views.AppointmentListView.as_view(), name='appointment_list'),#pass
    path('appointments/new/', views.CreateAppointmentView.as_view(), name='create_appointment'),#pass
    path('appointments/<int:pk>/edit/', views.UpdateAppointmentView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.DeleteAppointmentView.as_view(), name='appointment_delete'),
    
    path('admin/appointments/', views.AllAppointmentsView.as_view(), name='all_appointments'),

    path('services/', views.service_list, name='services'),#pass
    path('services/new/', views.service_create, name='service_create'),#pass
    path('services/<int:pk>/edit/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

]
