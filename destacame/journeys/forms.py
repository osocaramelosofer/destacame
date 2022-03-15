from django import forms
from .models import Journey


class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = ['buss', 'route', 'passenger', 'driver', 'date', 'time']
