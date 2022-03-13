from django.shortcuts import render
from django.views.generic import ListView


from .models import Journey


class ListJourneys(ListView):
    model = Journey
    template_name = 'pages/journeys.html'
    context_object_name = 'journeys'
