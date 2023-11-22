from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


class EventSubmission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_time = models.DateTimeField(default=None)
    approved = models.BooleanField(default=False)
    class Tags(models.TextChoices):
        CAREER = "career", _("Career")
        CLUB = "club", _("Club")
        COLLEGE = "arts & sciences", _("Arts and Sciences")
        CONCERT = "concert", _("Concert")
        CULTURE = "culture", _("Culture")
        EDU = "education", _("Education")
        ENG = "engineering", _("Engineering")
        FOOD = "food", _("Food")
        MCINTIRE = "mcintire", _("McIntire")
        RELIGIOUS = "religious", _("Religious")
        SOCIAL = "social", _("Social")
        SPORTS = "sports", _("Sports")
        THEATRE = "theatre", _("Theatre")
        __empty__ = _("No Tags")

    tag = models.CharField(max_length=200, choices=Tags.choices, null=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"

