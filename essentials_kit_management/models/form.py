from django.db import models

class Washingmachine(models.Model):
    washing_machine_id = models.CharField(max_length=150, primary_key=True)
    is_active = models.BooleanField(default=True)
