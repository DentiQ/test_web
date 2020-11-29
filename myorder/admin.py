from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Order, Dish, Tableware, Dinner, Style

admin.site.register(Order)
admin.site.register(Dish)
admin.site.register(Tableware)
admin.site.register(Dinner)
admin.site.register(Style)