from django.contrib import admin
from .models import ReportedIssue


@admin.register(ReportedIssue)
class ReportedIssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'resident_name', 'apartment_number', 'issue_type', 'status', 'created_at']
    list_filter = ['issue_type', 'status', 'created_at']
    search_fields = ['resident_name', 'apartment_number', 'description']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    fieldsets = [
        ('Informații Rezident', {
            'fields': ['resident_name', 'apartment_number']
        }),
        ('Detalii Problemă', {
            'fields': ['issue_type', 'description']
        }),
        ('Status', {
            'fields': ['status', 'reported_by', 'created_at', 'updated_at', 'resolved_at']
        }),
    ]
