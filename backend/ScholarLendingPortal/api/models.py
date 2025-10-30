from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone


class User(AbstractUser):
    """Custom User model with role-based access"""
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Equipment(models.Model):
    """Equipment/Item model"""
    CONDITION_CHOICES = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    )

    CATEGORY_CHOICES = (
        ('sports', 'Sports Equipment'),
        ('lab', 'Lab Equipment'),
        ('camera', 'Camera & Photography'),
        ('musical', 'Musical Instruments'),
        ('project', 'Project Materials'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='good')
    quantity = models.IntegerField(default=1)
    available_quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.available_quantity}/{self.quantity} available)"

    def save(self, *args, **kwargs):
        # Ensure available quantity doesn't exceed total quantity
        if self.available_quantity > self.quantity:
            self.available_quantity = self.quantity
        super().save(*args, **kwargs)

    @property
    def is_available(self):
        return self.available_quantity > 0

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        ordering = ['-created_at']


class BorrowRequest(models.Model):
    """Borrowing request model"""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('issued', 'Issued'),
        ('returned', 'Returned'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_requests')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='borrow_requests')
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    request_date = models.DateTimeField(auto_now_add=True)
    borrow_from = models.DateField()
    borrow_to = models.DateField()

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_requests'
    )
    approved_date = models.DateTimeField(null=True, blank=True)

    issued_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)

    purpose = models.TextField(blank=True)
    rejection_reason = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name} ({self.status})"

    def clean(self):
        """Validate borrowing dates and check for overlapping bookings"""
        if self.borrow_from and self.borrow_to:
            if self.borrow_to < self.borrow_from:
                raise ValidationError("End date must be after start date")

            # Check for overlapping bookings only for approved/issued requests
            if self.status in ['approved', 'issued']:
                overlapping = BorrowRequest.objects.filter(
                    equipment=self.equipment,
                    status__in=['approved', 'issued'],
                    borrow_from__lte=self.borrow_to,
                    borrow_to__gte=self.borrow_from
                ).exclude(pk=self.pk)

                # Calculate total requested quantity in overlapping period
                total_requested = sum(req.quantity for req in overlapping)

                if total_requested + self.quantity > self.equipment.quantity:
                    raise ValidationError(
                        f"Equipment not available for the requested period. "
                        f"Only {self.equipment.quantity - total_requested} items available."
                    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Borrow Request'
        verbose_name_plural = 'Borrow Requests'
        ordering = ['-request_date']

