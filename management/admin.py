from django.contrib import admin
from management.models import Block, Apartment, Resident, Manager, Administrator


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'number_of_floors', 'manager']
    search_fields = ['name', 'address']
    list_filter = ['number_of_floors']


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['number', 'floor', 'block']
    search_fields = ['number']
    list_filter = ['floor', 'block']


@admin.register(Resident)
class ManagementResidentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'apartment']
    search_fields = ['name', 'email']
    list_filter = ['apartment']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'block']
    search_fields = ['user__username', 'phone']
    list_filter = ['block']


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bloc', 'active', 'created_at']
    search_fields = ['first_name', 'last_name', 'bloc']
    list_filter = ['active', 'bloc']
    date_hierarchy = 'created_at'
