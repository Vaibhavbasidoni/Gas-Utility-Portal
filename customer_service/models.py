from django.db import models
from django.utils import timezone

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('CONNECTION', 'New Connection'),
        ('BILLING', 'Billing Issue'),
        ('MAINTENANCE', 'Maintenance'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    customer_name = models.CharField(max_length=100, default='Anonymous')
    customer_email = models.EmailField(default='customer@example.com')
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.customer_name}"

    def resolve(self):
        self.status = 'RESOLVED'
        self.resolved_at = timezone.now()
        self.save()

# Add this to your existing models.py

class RequestComment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='comments')
    staff_name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.staff_name} on Request #{self.service_request.id}"