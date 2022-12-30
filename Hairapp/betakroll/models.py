from django.db import models
from users.models import User


#Handels all the data involving booking appointments and viewing appointments
class Booking(models.Model):
      
   class Progress(models.IntegerChoices):
      ACTIVE = 1, "Active"
      COMPLETE = 2, "Complete"

   class Treatment_type(models.IntegerChoices):
      HAIRCUT = 1, "Hair cut"
      DYEHAIR = 2, "Dye hair"

   class Available_hours(models.IntegerChoices):
      ONE = 1, "13:00 - 14:00"
      TWO = 2, "14:00 - 15:00"
      THREE = 3, "15:00 - 16:00"
      FOUR = 4, "16:00 - 17:00"
      FIVE = 5, "17:00 - 18:00"

   email = models.EmailField("Email Address", max_length=100)
   hairdresser = models.CharField(max_length=100, blank=True)
   date = models.CharField("Date", max_length=50, blank=False)
   
   #Small Integer Fields takes the integer corresponding with the string chosen and saves it to the db
   treatment = models.SmallIntegerField(choices= Treatment_type.choices, blank=False)
   time = models.SmallIntegerField("Time", choices=Available_hours.choices, blank=False)
   complete = models.SmallIntegerField(choices=Progress.choices, default=Progress.ACTIVE)
   
   
