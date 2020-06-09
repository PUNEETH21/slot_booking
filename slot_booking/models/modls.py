from django.db import models
from django.contrib.auth.models import AbstractUser
from slot_booking.constants.constants import DAY_CHOICES

class User(AbstractUser):
    name = models.CharField(max_length=250 ,null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now=True)


class Washingmachine(models.Model):
    washing_machine_id = models.CharField(max_length=150, primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

class UserSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    washing_machine = models.ForeignKey(Washingmachine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class WashingmachineSlot(models.Model):
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    washing_machine = models.ForeignKey(Washingmachine, on_delete=models.CASCADE)

def 
