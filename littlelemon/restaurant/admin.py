from django.contrib import admin

# Register your models here.

from .models import Booking
from .models import Menu

admin.site.register(Menu)