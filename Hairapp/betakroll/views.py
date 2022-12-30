from django.shortcuts import redirect, render
from django.http import HttpResponse
from users.models import User
from betakroll.models import Booking
from .forms import BookingForm
from datetime import date


import calendar, datetime
from calendar import HTMLCalendar

# Sends a request to get the homepage.html 
def home(request):
    return render(request, 'homepage.html')

# Sends a request to get the hairdressers.html
def hairdressers(request):
    def calculate_age(year, month, day):
        today = date.today()
        return today.year - year - ((today.month, today.day) < (month, day))
    
    jonas = f"Jonas Johnsen, {calculate_age(1969, 11, 23)}"
    janne = f"Janne Johnsen, {calculate_age(1974, 11, 8)}"
    guri = f"Guri Malla, {calculate_age(1986, 2, 17)}"
    endre = f"Endre Kjønn, {calculate_age(2000, 9, 19)}"

    return render(request, 'betakroll/hairdressers.html',{
        "jonas": jonas,
        "janne": janne,
        "guri": guri,
        "endre": endre,
    })

def booking(request):
    
    # Get the current date
    today = datetime.date.today()
    # Get the week number of the current date
    week_number = today.isocalendar()[1]
    dates = [today + datetime.timedelta(days=i) for i in range (0-today.weekday(), 7-today.weekday())]
    
    #When the user wants to make a new appointment this is triggerd
    if request.method == "POST":
        #from forms.py
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            #Taking the current users email address and adding it to the new appointment
            obj.email = User.objects.get(email=request.user.email)
            #Saves the data to db
            obj.save()
            return redirect("/")
        
    else:
        form = BookingForm()
        
    return render(request, 'betakroll/booking.html',{
        "today": today,
        "week_number": week_number,
        "dates": dates,
        "form": form,
    })
#Sends a request to get the appointments.html
def appointments(request):
    appointment = Booking.objects.all()
    return render(request, 'betakroll/appointments.html',
    {"appointment": appointment})
    
    

def myProfile(request):
    return render(request, 'betakroll/myprofile.html')

def contacts(request):
    return render(request, 'betakroll/contact.html')