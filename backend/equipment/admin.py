from django.contrib import admin
from .models import Equipment, LendingRecord


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity_available', 'quantity_total', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['name', 'description', 'category']


@admin.register(LendingRecord)
class LendingRecordAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'user', 'quantity', 'status', 'borrow_date', 'due_date', 'return_date']
    list_filter = ['status', 'borrow_date', 'due_date']
    search_fields = ['equipment__name', 'user__username', 'notes']
    raw_id_fields = ['equipment', 'user']

