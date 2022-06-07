from django.contrib import admin
from .models import Printer, Region, Address


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("address", "region")


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "ip_address", "address")
