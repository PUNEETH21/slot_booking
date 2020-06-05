# your django admin
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from slot_booking.models import User
from django.contrib.auth.admin import UserAdmin

# class UserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('name')})
#         )
        
admin.site.register(User, UserAdmin)
