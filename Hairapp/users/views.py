# Author Kjærsti L. Bergli, email: klb022@uit.no
from django.shortcuts import render, redirect
from users.models import *
from .forms import RegisterNewUserForm
from django.contrib.auth import logout

# View that handles the form for registering a new user
def registerUserView(request):
    form = RegisterNewUserForm()

    if request.method == 'POST':
        form = RegisterNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    context = {'form':form}
    return render(request, 'registration/register.html', context)


# Sends a request to get the login.html
def login(request):
    return render(request, 'login.html')

