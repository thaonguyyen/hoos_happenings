from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class EventSubmission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, help_text="Enter exact address location.")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} by {self.user.username}"

