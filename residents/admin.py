from django.contrib import admin
from residents.models import Apartment, Resident


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['number', 'floor', 'capacity']
    search_fields = ['number']
    list_filter = ['floor']


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'apartment', 'active', 'date_added']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['active', 'apartment', 'date_added']
    date_hierarchy = 'date_added'

