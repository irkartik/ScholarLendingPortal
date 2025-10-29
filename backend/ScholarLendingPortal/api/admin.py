from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Equipment

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin configuration for User model"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone_number')}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone_number', 'email', 'first_name', 'last_name')}),
    )

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """Admin configuration for Equipment model"""
    list_display = ['name', 'category', 'condition', 'quantity', 'available_quantity', 'is_available', 'created_at']
    list_filter = ['category', 'condition', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Status', {
            'fields': ('condition', 'quantity', 'available_quantity')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

