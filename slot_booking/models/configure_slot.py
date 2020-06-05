from django.db import models

class ConfigureSlot(models.Model):
    book_days_after = models.IntegerField()
    cancel_days_before = models.IntegerField()
