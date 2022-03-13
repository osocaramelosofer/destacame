from django.contrib import admin
from .models import Driver, Passenger

# Register your models here.
admin.site.register(Passenger)
admin.site.register(Driver)
