"""Hairapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# We import the redirectview to be used to redirect to a specified URL
from django.views.generic import RedirectView

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # Adds the url pattern home to the website
    path('', include('betakroll.urls')),
    # Changes the url pattern to /home/ in the case of a blank url
    path('', RedirectView.as_view(url='home/', permanent=True)),
    #path to the 'users' app and it's features
        #Add Django site authentication urls (package of urls for login, logout, password management) 
        # if it does not find the loginfunctionality in this url-package
        # go to /home (They have to be executed in the right order)
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

