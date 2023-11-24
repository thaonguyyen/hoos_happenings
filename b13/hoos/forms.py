from django import forms
from .models import EventSubmission

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

class EventSubmissionForm(forms.ModelForm):
    class Meta:
        model = EventSubmission
        fields = ['name', 'description', 'location', 'date_time', 'tag']
        widgets = {
            'location': forms.TextInput(attrs={'id': 'autocomplete'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        tag = forms.ChoiceField(
            choices=EventSubmission.Tags.choices,
            widget=forms.Select,
            required=False,
        )
