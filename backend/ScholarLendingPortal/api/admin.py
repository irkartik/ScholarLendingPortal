from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Equipment, BorrowRequest


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


@admin.register(BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):
    """Admin configuration for BorrowRequest model"""
    list_display = [
        'id', 'user', 'equipment', 'quantity', 'status',
        'borrow_from', 'borrow_to', 'request_date'
    ]
    list_filter = ['status', 'request_date', 'borrow_from']
    search_fields = ['user__username', 'equipment__name', 'purpose']
    readonly_fields = ['request_date', 'approved_date', 'issued_date', 'returned_date']

    fieldsets = (
        ('Request Information', {
            'fields': ('user', 'equipment', 'quantity', 'status')
        }),
        ('Dates', {
            'fields': ('request_date', 'borrow_from', 'borrow_to')
        }),
        ('Approval Information', {
            'fields': ('approved_by', 'approved_date', 'issued_date', 'returned_date')
        }),
        ('Additional Details', {
            'fields': ('purpose', 'rejection_reason', 'notes')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Make certain fields readonly after creation"""
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user', 'equipment')
        return self.readonly_fields

