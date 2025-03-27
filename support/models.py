from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification 
 # Import Notification model
from django.db import models


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    request_type = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_type}"

# 🔹 Signal to insert a notification after a new service request
@receiver(post_save, sender=ServiceRequest)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title="New Service Request",
            message=f"A new request from {instance.customer_name} has been created.",
        )
