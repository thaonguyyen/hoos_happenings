from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class EventSubmission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_time = models.DateTimeField(default=None)
    tags = models.ManyToManyField(Tag)
    date_time_created = models.DateTimeField(auto_now_add=True)

    APPROVAL_CHOICES = [
        ('pending', '⏰ Pending'),
        ('approved', '✅ Approved'),
        ('rejected', '❌ Rejected'),
    ]

    approval_status = models.CharField(
        max_length=20,
        choices=APPROVAL_CHOICES,
        default='pending',
    )

    def __str__(self):
        return f"{self.name} by {self.user.username}"

