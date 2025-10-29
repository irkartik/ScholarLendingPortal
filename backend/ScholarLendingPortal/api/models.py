from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    """Custom user model extending AbstractUser with Role-Based Access"""
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    def clean(self):
        super().clean()
        if self.role not in dict(self.ROLE_CHOICES):
            raise ValidationError(f"Invalid role: {self.role}")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Equipment(models.Model):
    """Model representing equipment available for lending"""
    CONDITION_CHOICES = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    )
    CATEGORY_CHOICES = (
        ('sports', 'Sports Equipment'),
        ('lab', 'Lab Equipment'),
        ('other', 'Other')
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    available_quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_available(self):
        return self.available_quantity > 0

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        ordering = ['-created_at']

class BorrowRequest(models.Model):
    """Model representing a borrow request for equipment"""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('issued', 'Issued'),
        ('returned', 'Returned'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrow_requests")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    request_date = models.DateTimeField(auto_now_add=True)
    borrow_from = models.DateTimeField()
    borrow_to = models.DateTimeField()

    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_requests")
    approved_date = models.DateTimeField(null=True, blank=True)

    purpose = models.TextField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name} ({self.status})"

    class Meta:
        verbose_name = 'Borrow Request'
        verbose_name_plural = 'Borrow Requests'
        ordering = ['-request_date']