from django.urls import path
from . import views

app_name = 'home123' 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
]

