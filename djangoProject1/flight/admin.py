from django.contrib import admin

# Register your models here.
from flight.models import *
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
admin.site.register(Airports)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passengers,PassengerAdmin)