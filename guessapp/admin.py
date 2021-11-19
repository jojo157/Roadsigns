from django.contrib import admin
from .models import Roadsign

class RoadsignAdmin(admin.ModelAdmin):
    list_display = ("id","sign_name")

# Register your models here.
admin.site.register(Roadsign, RoadsignAdmin)