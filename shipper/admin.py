from django.contrib import admin

from .models import Shipper


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    pass