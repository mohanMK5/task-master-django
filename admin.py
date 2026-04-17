"""
Admin Configuration - Register models in Django Admin

This file configures how the Task model appears in the Django admin interface.
"""

from django.contrib import admin
from .models import Task


# Register the Task model in the admin interface
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Task model
    
    This class customizes how tasks are displayed and managed
    in the Django admin panel.
    """
    
    # Fields to display in the list view
    list_display = ('title', 'completed', 'created_at')
    
    # Fields that can be searched
    search_fields = ('title', 'description')
    
    # Fields to filter by
    list_filter = ('completed', 'created_at')
    
    # Fields to show in the detail/edit view (organized in fieldsets)
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
    
    # Make created_at read-only (auto-set)
    readonly_fields = ('created_at',)
    
    # Default ordering (newest first)
    ordering = ('-created_at',)

