from django.db import models
from datetime import time
from slot_booking.constants.constants import DAY_CHOICES
from .washing_machine import Washingmachine

class WashingmachineSlot(models.Model):
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    washing_machine = models.ForeignKey(Washingmachine, on_delete=models.CASCADE)
