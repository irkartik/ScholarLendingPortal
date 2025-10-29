from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    """Model representing equipment available for lending"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    quantity_available = models.IntegerField(default=0)
    quantity_total = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Equipment"
        ordering = ['-created_at']


class LendingRecord(models.Model):
    """Model representing lending transactions"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled'),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='lending_records')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lending_records')
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    borrow_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name}"

    class Meta:
        ordering = ['-created_at']

