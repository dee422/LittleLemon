from django.contrib import admin
from .models import Menu, Booking

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
#admin.site.register(Users)  # Assuming User model is imported from django.contrib.auth.models
