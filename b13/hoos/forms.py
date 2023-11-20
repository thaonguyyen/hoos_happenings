from django import forms
from .models import EventSubmission

class EventSubmissionForm(forms.ModelForm):
    class Meta:
        model = EventSubmission
        fields = ['name', 'description', 'location', 'tag']