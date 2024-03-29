from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=250 ,null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    