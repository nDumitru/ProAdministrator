from django.contrib import admin
from management.models import Block, Apartment, Resident, Manager, Administrator


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'number_of_floors']
    search_fields = ['name', 'address', 'city']
    list_filter = ['city', 'number_of_floors']
    ordering = ['name']


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['number', 'floor', 'rooms', 'area', 'block', 'status']
    search_fields = ['number', 'block__name']
    list_filter = ['floor', 'status', 'block']
    ordering = ['block__name', 'number']


@admin.register(Resident)
class ManagementResidentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'apartment', 'active']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['active', 'apartment__block']
    ordering = ['last_name', 'first_name']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'block', 'is_active']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['is_active', 'block']
    ordering = ['last_name', 'first_name']


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'bloc', 'is_active', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'bloc']
    list_filter = ['is_active', 'bloc']
    date_hierarchy = 'created_at'
    ordering = ['last_name', 'first_name']