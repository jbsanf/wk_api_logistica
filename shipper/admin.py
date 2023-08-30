from django.contrib import admin

from .models import Shipment, Shipper


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    pass