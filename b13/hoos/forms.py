from django import forms
from .models import EventSubmission

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

class EventSubmissionForm(forms.ModelForm):
    class Meta:
        tag = forms.MultipleChoiceField(
            choices=[('tag1', 'Tag 1'), ('tag2', 'Tag 2'), ('tag3', 'Tag 3')],
            widget=forms.CheckboxSelectMultiple
        )
        model = EventSubmission
        fields = ['name', 'description', 'location', 'date_time', 'tag']
        widgets = {
            'location': forms.TextInput(attrs={'id': 'autocomplete'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
