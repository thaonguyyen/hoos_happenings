from django import forms
from .models import EventSubmission, Tag
from django.core.exceptions import ValidationError
from django.utils import timezone

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

class EventSubmissionForm(forms.ModelForm):
    class Meta:
        model = EventSubmission
        fields = ['name', 'description', 'location', 'date_time', 'tags']
        widgets = {
            'location': forms.TextInput(attrs={'id': 'autocomplete'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def clean_date_time(self):
        date_time = self.cleaned_data.get('date_time')

        if date_time and date_time < timezone.now():
            raise ValidationError("Event cannot be in the past.")

        return date_time
