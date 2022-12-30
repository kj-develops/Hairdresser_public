# Author Kjærsti L. Bergli, email: klb022@uit.no
from django.urls import path
from . import views
from .views import registerUserView

urlpatterns = [
    # With this url pattern we recieve login.html from views.py
    path('login/', views.login, name='login'),
    # With this url pattern we recieve register.html from views.py
    path('register/', registerUserView, name='register'),
]
