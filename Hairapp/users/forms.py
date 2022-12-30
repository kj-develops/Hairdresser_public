# Author Kjærsti L. Bergli, email: klb022@uit.no
from cProfile import label
from django import forms
from users.models import *
# imports djnago's own user registration form
from django.contrib.auth.forms import UserCreationForm 

# class to register a new user
class RegisterNewUserForm(UserCreationForm):
    # Attempt to translate form info to Norwegian. Future work
    #password1 = forms.CharField(label="Passord", help_text="Passordregler: Ikke likt personlig informasjon, minst 8 tegn, ikke et vanlig brukt passord, ikke bare tall")
    #password2 = forms.CharField(label="Bekreft passord")

    # connects to custom user model
    class Meta:
        model = User
        fields = ('email', 'username', 'name', 'password1', 'password2' )
       