from dataclasses import fields
from django import forms
from requests import post
from .models import *
from users.models import User




#class that handles booking appointment form for new appointments
class BookingForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        
        self.date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
        
    class Meta:
        model = Booking
        #Specifying the fields which the user needs to fill in
        fields = ['treatment', 'hairdresser', 'date', 'time']
        widgets={
            'treatment' : forms.Select(attrs={'class':'form-control'}),
            'hairdresser' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.TextInput(attrs={'class':'form-control'}),
            'time' : forms.Select(attrs={'class':'form-control'}),
        }






