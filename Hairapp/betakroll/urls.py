from django.urls import path
from . import views


urlpatterns = [
    # With the url pattern home/ we will recieve the homepage.html page from views.py
    path('home/', views.home, name='home'),
    # Creating a path from the login, to book an appointment
    path('booking/', views.booking, name='booking'),
    # This url pattern access the hairdressers.html from views.py
    path('hairdressers/', views.hairdressers, name='hairdressers'),
    # This url pattern access the contact.html from views.py
    path('contact/', views.contacts, name='contact'),
    # this url pattern accesses the appointments html
    path('appointments/', views.appointments, name='appointments'),
    # With this url pattern we recieve myProfile.html from views.py
    path('myprofile/', views.myProfile, name='myprofile'),
]
