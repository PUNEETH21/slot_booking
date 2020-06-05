from django.db import models
from datetime import date
from .user import User
from .washing_machine import Washingmachine


class UserSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    washing_machine = models.ForeignKey(Washingmachine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
